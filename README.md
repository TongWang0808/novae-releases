# Novae

> **发现新声音** · 一个为 Windows 打造的多平台桌面音乐播放器

Novae 是一个用 **Wails（Go + WebView2）** 构建的桌面音乐客户端。它把华为音乐、QQ 音乐、网易云音乐、酷狗音乐、酷我音乐放在同一个界面里，支持多平台账号并存、随时切换；也可以不登录平台，只接一个自建或公开的云端音源。

**1.3.0 正式版** · Windows 10 / 11 x64

[GitHub 下载](https://github.com/TongWang0808/novae-releases/releases/latest) · [Gitee 下载](https://gitee.com/meiliwang0808/novae-releases/releases/latest) · [Gitee 仓库](https://gitee.com/meiliwang0808/novae-releases)

---

## 下载安装

| 来源 | 地址 |
| --- | --- |
| GitHub Release | https://github.com/TongWang0808/novae-releases/releases/latest |
| Gitee Release | https://gitee.com/meiliwang0808/novae-releases/releases/latest |

下载 `novae.exe` 后直接运行即可，不需要安装器。首次启动需要系统具备 WebView2 运行时（Windows 11 已内置，Windows 10 通常也已安装）。

> 内置更新支持 GitHub / Gitee 双源。设置页「关于」可以检查更新；检测到新版本会显示红点和更新说明，但不会自动下载，用户可以选择立即下载或继续使用当前版本。

---

## 界面预览

截图中的账号昵称、头像和个人信息均已打码。

| 首页 / 登录入口 | 搜索：歌手与专辑 |
| --- | --- |
| ![首页](https://gitee.com/meiliwang0808/novae-releases/releases/download/v1.3.0/01-home.png) | ![搜索](https://gitee.com/meiliwang0808/novae-releases/releases/download/v1.3.0/02-search.png) |

| 我喜欢的音乐 | 下载音乐 |
| --- | --- |
| ![我喜欢的音乐](https://gitee.com/meiliwang0808/novae-releases/releases/download/v1.3.0/03-favorites.png) | ![下载音乐](https://gitee.com/meiliwang0808/novae-releases/releases/download/v1.3.0/04-downloads.png) |

| 歌手页：专辑 | 歌手页：歌曲 |
| --- | --- |
| ![歌手页专辑](https://gitee.com/meiliwang0808/novae-releases/releases/download/v1.3.0/05-artist-albums.png) | ![歌手页歌曲](https://gitee.com/meiliwang0808/novae-releases/releases/download/v1.3.0/06-artist-songs.png) |

| 歌手页：简介展开 | 沉浸播放器 / 歌词页 |
| --- | --- |
| ![歌手页简介](https://gitee.com/meiliwang0808/novae-releases/releases/download/v1.3.0/07-artist-bio.png) | ![沉浸播放器](https://gitee.com/meiliwang0808/novae-releases/releases/download/v1.3.0/08-immersive-player.png) |

| 设置页：账号 | 最近播放 |
| --- | --- |
| ![设置页账号](https://gitee.com/meiliwang0808/novae-releases/releases/download/v1.3.0/09-settings-account.png) | ![最近播放](https://gitee.com/meiliwang0808/novae-releases/releases/download/v1.3.0/10-recent-play.png) |

| 搜索联想 | 账号详情 |
| --- | --- |
| ![搜索联想](https://gitee.com/meiliwang0808/novae-releases/releases/download/v1.3.0/11-search-suggest.png) | ![账号详情](https://gitee.com/meiliwang0808/novae-releases/releases/download/v1.3.0/12-account-detail.png) |

---

## 核心功能

### 多平台账号

- 华为音乐、QQ 音乐、网易云音乐、酷狗音乐、酷我音乐可以同时登录、随时切换。
- 平台账号、云端接口都可以设为默认音源；平台返回试听片段时，可用辅助音源补全。
- 登录态检查会实际向平台询问是否有效，失效时给出原因并支持重新授权。
- Cookie 使用 Windows DPAPI 加密保存在本机，不保存账号密码，也不模拟登录协议。

### 曲库与播放

- 我的歌单、收藏、自建歌单、榜单歌单自动整理，曲目渐进加载。
- 最近播放、下载音乐、本地音乐支持「播放全部」、单曲播放和批量管理。
- 播放队列支持顺序、列表循环、单曲循环、随机、拖动排序、清空。
- 播放过渡支持关闭、淡入淡出、交叉淡化、无缝播放；倍速 0.5×–2.0×；定时关闭。
- 歌曲右键菜单和「更多」支持歌曲详情、下一首播放、加入队列、下载、收藏。

### 搜索、歌手与专辑

- 按当前平台搜索，结果只显示该平台的数据，不混入其它平台条目。
- 搜索页包含歌手、专辑、歌曲三级结果；歌手 / 专辑卡片采用「外层背景板 + 独立卡片」结构。
- 歌手页提供歌曲、专辑、排序、批量管理和简介展开；简介支持点击或双击卡片展开 / 收起。
- 搜索页的歌手 / 专辑卡片和背景板均支持鼠标滑动光效。

### 歌词与音质

- 全屏沉浸歌词页：逐行高亮、点击歌词跳转、封面模糊背景。
- 支持平台翻译歌词、歌词对齐方式、字号、行距调整。
- 音质档位按平台真实档位列示，并在取流后实测容器头和码率，低于所选档位时如实降标。
- 播放失败会先降一档重试，仍失败再按「播放失败或无音源时自动下一首」处理。

### 外观与交互

- 12 套主题 + 跟随系统：午夜、曜石、极地、森语、深海、暮紫、余烬、白昼、纸张、薄荷、樱花、晴空。
- 界面字体、字号、字重、界面缩放独立设置；默认主题为「晴空」，默认字体为等线。
- 沉浸光感：侧栏、顶栏、主内容、播放器、播放队列、搜索页、设置浮层统一为玻璃质感表面。
- 鼠标滑动光效：按钮、卡片、列表行和页面大表面会出现跟随指针的前后双圈扫光。
- 统一按钮按压反馈：缩幅 96%，右下按钮向下形变；可在设置中整体关闭。
- 迷你播放器、托盘、关闭到托盘、原生标题栏明暗联动。

### 下载与云端

- 单曲下载、批量筛选下载（全部 / 仅 VIP / 仅免费），可选音质和目录。
- 试听片段拒绝下载，不会把 30 秒片段保存成完整歌曲。
- 云端音源支持多条接口、测试连接、设为默认音源，也可只作为平台无会员时的兜底。
- 接口地址、UID 保存在本机；远程 HTTP 携带 Cookie 会被拒绝。

### 应用更新

- 版本号位置提供检查更新入口，启动后也会自动检查。
- 新版本显示红点、版本号、更新说明和下载入口，不强制更新、不自动下载。
- 更新源支持 GitHub / Gitee 切换；GitHub 不稳定时可以改用 Gitee 检查和下载。

---

## 1.3.0 更新摘要

1. **界面材质统一**：迷你播放器半透明白玻璃 + 渐变；搜索页歌手 / 专辑卡片与背景板玻璃化；歌手页工具栏、歌词页展开面板、设置页账号 / 云端 / 接口 / 参考接口卡片统一；返回按钮、排序按钮、更新源按钮适配整体 UI；QQ 群卡片放入软件内。
2. **歌手页与搜索页**：歌手卡片滑动光效；歌手名悬停去掉下划线；歌手页搜索框改用主页样式并带放大镜；简介支持点击 / 双击展开收起；平台下拉框玻璃化；收起简介时高度收紧。
3. **设置页**：平台账号卡片「设为默认」改为玻璃按钮，与另外 4 个小按钮统一；接口新增区域改为半透明 `bg-input` 并轻模糊；排序菜单、歌曲更多菜单、批量管理底栏统一玻璃 / 渐变。
4. **按钮与浮层**：补齐所有按钮、卡片、歌曲条、队列条、菜单项、搜索历史删除和音量条的按压反馈；缩幅统一 96%；关闭按压反馈后全局取消缩放和位移；定位当前播放按钮玻璃化；队列批量按钮重做；所有临时浮层互斥并支持点外关闭。
5. **播放行为**：「播放失败时自动下一首」和「无音源时自动播放队列下一首」合并为「播放失败或无音源时自动下一首」；共用 700ms 延迟、最多连续跳过 5 首、成功播放后重置计数；覆盖 API 无歌曲、无播放地址、队列文件缺失等情况。
6. **数据保留**：WebView2 数据目录固定到 `%APPDATA%\novae.exe`，不同 exe 文件名共享同一份 localStorage；搜索历史、外观设置、续播记录可跨版本保留；后端最近播放仍在 `%APPDATA%\Novae\history.json`。

---

## 隐私与安全

- 不保存平台账号密码，不模拟登录接口；Cookie 只保存在本机，并用 Windows DPAPI 加密。
- 所有平台的 Cookie、昵称、头像与会员信息在 `%APPDATA%\Novae\accounts.json`；华为登录凭据单独加密。
- 截图中的账号昵称、头像和个人信息均已打码；README 不展示真实账号资料。
- 下载目录、播放记录和缓存都在本机；启用歌词翻译时，歌词文本会发送给第三方翻译服务（不含 Cookie）。
- 本项目不内置任何音源、账号或会员凭据；云端 / 本机 API 由使用者自行部署并承担相应责任。

---

## 系统要求

- Windows 10 / 11 x64
- WebView2 Runtime
- 建议 4GB 以上内存

## 说明

本项目为独立实现，与华为、腾讯、网易、酷狗、酷我及其关联公司没有隶属、合作或代理关系；各平台名称、会员名称与相关权利归对应公司所有。本项目不破解 DRM，也不会把试听片段当作完整歌曲下载。

---

## 致谢

界面组织与交互细节参考过：

- [听澜 · Tinglan](https://github.com/talongao/tinglan)
- [Melotopia](https://melotopia.chenlvin.cc/)

以及 [Wails](https://wails.io/)、[NeteaseCloudMusicApi](https://www.npmjs.com/package/NeteaseCloudMusicApi) 与各平台公开接口的社区整理。

## 许可

[MIT](https://github.com/TongWang0808/novae-releases/blob/main/LICENSE)
