#!/usr/bin/env python3
"""Merge GitHub / Gitee daily traffic into a lifetime visit ledger.

GitHub and Gitee only expose short rolling windows. This script keeps one
record per calendar day in stats/traffic-ledger.json, then writes the public
stats/visits.json snapshot used by the Novae client. Once a day is recorded it
is never dropped when it falls out of the remote rolling window.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER_PATH = ROOT / "stats" / "traffic-ledger.json"
SNAPSHOT_PATH = ROOT / "stats" / "visits.json"
GH_JSON_PATH = Path(os.environ.get("GH_TRAFFIC_JSON", "/tmp/novae-gh-traffic.json"))
GITEE_JSON_PATH = Path(os.environ.get("GITEE_TRAFFIC_JSON", "/tmp/novae-gitee-traffic.json"))
TZ = dt.timezone(dt.timedelta(hours=8))


def load_json(path: Path, default: dict) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else default
    except Exception:
        return default


def as_int(value, fallback: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return fallback


def github_day(raw: object) -> str:
    text = str(raw or "").strip()
    return text[:10] if len(text) >= 10 else ""


def gitee_day(raw: object) -> str:
    text = str(raw or "").strip()
    if text.isdigit():
        try:
            stamp = dt.datetime.fromtimestamp(int(text), tz=dt.timezone.utc)
            return stamp.astimezone(TZ).strftime("%Y-%m-%d")
        except Exception:
            return ""
    return text[:10] if len(text) >= 10 else ""


def empty_ledger() -> dict:
    return {
        "schema": 2,
        "startedAt": "",
        "updatedAt": "",
        "sources": {
            "github": {"days": {}},
            "gitee": {"days": {}},
        },
        "totals": {"github": 0, "gitee": 0, "total": 0},
    }


def merge_days(ledger: dict, source: str, incoming: dict[str, int]) -> None:
    days = ledger.setdefault("sources", {}).setdefault(source, {}).setdefault("days", {})
    for day, count in incoming.items():
        if not day:
            continue
        value = max(0, as_int(count))
        # 同一天可能因 API 延迟而补数；只升不降，避免累计被回退。
        days[day] = max(as_int(days.get(day) or 0, 0), value)


def main() -> int:
    ledger = load_json(LEDGER_PATH, empty_ledger())
    if not isinstance(ledger.get("sources"), dict):
        ledger = empty_ledger()

    gh = load_json(GH_JSON_PATH, {})
    gitee = load_json(GITEE_JSON_PATH, {})
    gh_error = str(gh.get("message") or "").strip()
    gitee_error = str(gitee.get("message") or "").strip()

    gh_days: dict[str, int] = {}
    for item in gh.get("views") or []:
        if not isinstance(item, dict):
            continue
        day = github_day(item.get("timestamp"))
        if day:
            gh_days[day] = as_int(item.get("count"))

    gitee_days: dict[str, int] = {}
    for item in gitee.get("counts") or []:
        if not isinstance(item, dict):
            continue
        day = gitee_day(item.get("bucket"))
        if day:
            gitee_days[day] = as_int(item.get("ip"))

    if gh_days:
        merge_days(ledger, "github", gh_days)
    if gitee_days:
        merge_days(ledger, "gitee", gitee_days)

    gh_total = sum(as_int(v) for v in ledger["sources"]["github"]["days"].values())
    gitee_total = sum(as_int(v) for v in ledger["sources"]["gitee"]["days"].values())
    all_days = [d for source in ledger["sources"].values() for d in (source.get("days") or {}) if d]
    nonzero_days = [
        d
        for source in ledger["sources"].values()
        for d, v in (source.get("days") or {}).items()
        if d and as_int(v) > 0
    ]
    if not ledger.get("startedAt"):
        ledger["startedAt"] = min(nonzero_days or all_days) if (nonzero_days or all_days) else ""

    now = dt.datetime.now(TZ).strftime("%Y-%m-%d %H:%M:%S")
    ledger["schema"] = 2
    ledger["updatedAt"] = now
    ledger["totals"] = {"github": gh_total, "gitee": gitee_total, "total": gh_total + gitee_total}

    snapshot = {
        "snapshot": 2,
        "updatedAt": now,
        "github": gh_total,
        "gitee": gitee_total,
        "total": gh_total + gitee_total,
        "trackingStartedAt": ledger.get("startedAt") or "",
        "githubWindow": f"自 {ledger.get('startedAt') or '开始记录'} 累计",
        "giteeWindow": f"自 {ledger.get('startedAt') or '开始记录'} 累计",
        "partial": bool(gh_error or gitee_error),
        "giteeAvailable": not bool(gitee_error),
        "note": "GitHub / Gitee 项目页累计访问（含仓库下各页面）",
    }
    if gh_error:
        snapshot["githubError"] = gh_error
    if gitee_error:
        snapshot["giteeError"] = gitee_error

    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    LEDGER_PATH.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    SNAPSHOT_PATH.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(SNAPSHOT_PATH.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
 
