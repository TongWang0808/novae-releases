# Novae 第三方开源声明

更新日期：2026-11-25

适用版本：Novae 1.4.2（Windows x64）

Novae 本体采用 MIT License，见仓库根目录 `LICENSE`。本文件列出 Novae 在产品中实际使用、参考或分发的第三方项目及许可证信息。

除明确标注「内置分发」的项目外，其余项目仅以界面参考、HTTP 服务调用、协议参考或数据核对的方式使用；Novae 仓库不包含其源代码。



***

## 1. 内置分发

### 1.1 KuGouMusicApi 1.6.3



* 来源：[https://github.com/MakcRe/KuGouMusicApi](https://github.com/MakcRe/KuGouMusicApi)

* 版本：1.6.3

* 许可证：MIT

* 分发方式：`assets/kugou-api.exe` 内嵌到 Novae，运行时释放到用户缓存目录并启动

* 默认地址：`http://127.0.0.1:3200`

* 用途：酷狗扫码登录、搜索、歌单、喜欢、最近播放等本机 API 能力

KuGouMusicApi 的 MIT 许可证原文：



```
MIT License

Copyright (c) 2023 MakcRe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### 1.2 KuGouMusicApi 内置运行时依赖

`kugou-api.exe` 由 KuGouMusicApi 官方打包流程生成，内部包含 Node.js 14.20.0 运行时及其依赖。KuGouMusicApi 1.6.3 的 `package.json` 声明了以下运行时依赖：



| npm 包                     | 许可证（npm registry）       |
| ------------------------- | ----------------------- |
| axios                     | MIT                     |
| big-integer               | Unlicense               |
| crypto-js                 | MIT                     |
| dotenv                    | BSD-2-Clause            |
| express                   | MIT                     |
| form-data                 | MIT                     |
| node-forge                | BSD-3-Clause OR GPL-2.0 |
| pako                      | MIT AND Zlib            |
| qrcode                    | MIT                     |
| safe-decode-uri-component | MIT                     |
| url                       | MIT                     |

说明：实际打包进二进制的精确版本由 KuGouMusicApi 上游的 `pnpm-lock.yaml` 决定；上表按包名列出许可证表达式。各包的完整许可证文本见 npm 包页面或上游仓库。

Node.js 本身采用 MIT 许可证；其完整许可证与第三方声明见 Node.js 官方发行包。



***

## 2. 界面与视觉参考

以下项目用于界面组织、交互或视觉效果参考，Novae 未复制其源代码。



| 项目         | 许可证       | 参考内容                               | 链接                                                                                       |
| ---------- | --------- | ---------------------------------- | ---------------------------------------------------------------------------------------- |
| 听澜 Tinglan | AGPL-3.0  | 华为音乐客户端的界面组织与交互细节                  | [https://github.com/talongao/tinglan](https://github.com/talongao/tinglan)               |
| Melotopia  | 未标注（公开源码） | 界面组织与交互细节                          | [https://github.com/Chenlvin/Melotopia-HMOS](https://github.com/Chenlvin/Melotopia-HMOS) |
| 沐语 2.0.0   | 非开源（闭源产品） | 沉浸光感、液态材质的视觉参考                     | [https://wutuapp.com/](https://wutuapp.com/)                                             |
| MyGo       | MIT（框架）   | 液态材质 shader 的技术参考：边缘折射、跟随指针光斑、按压形变 | [https://github.com/egoist/mygo](https://github.com/egoist/mygo)                         |

补充：`frontend/dist/premium.css` 的「沉浸光感」注释明确写了「沐语 2.0.0 液态材质的前端重建」，并注明「参考实现是 MyGo 原生 shader」。MyGo 框架为 MIT；MyGo 生态中的 MyGo Music 应用为 AGPL-3.0，两者不是同一个许可证。



***

## 3. 接口、协议、数据与外部服务



| 项目                              | 许可证                                   | 使用方式                                                              | 是否随 Novae 分发 | 链接                                                                                                                               |
| ------------------------------- | ------------------------------------- | ----------------------------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| NeteaseCloudMusicApi            | npm 包 MIT；GitHub 仓库已归档、当前无 LICENSE 文件 | 网易云云端 API 模式的接口约定                                                 | 否，用户自行部署     | [https://github.com/Binaryify/NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)                           |
| api-enhanced                    | MIT                                   | `/song/url/match` 解灰 / 换源；上游音源 `pyncmd,kuwo,qq,kugou,migu,bodian` | 否，用户自行部署     | [https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced)     |
| KuGouMusicApi                   | MIT                                   | 内置酷狗 API sidecar                                                  | 是，见第 1 节     | [https://github.com/MakcRe/KuGouMusicApi](https://github.com/MakcRe/KuGouMusicApi)                                               |
| QQMusicApi                      | GPL-3.0                               | 可选的本机 QQ API，补歌单、喜欢、最近播放等                                         | 否，用户自行运行     | [https://github.com/jsososo/QQMusicApi](https://github.com/jsososo/QQMusicApi)                                                   |
| qqmusic-dl                      | MIT                                   | QQ CDN 文件前缀表交叉核对                                                  | 否，仅数据参考      | [https://github.com/menghuanshiguang/qqmusic-dl](https://github.com/menghuanshiguang/qqmusic-dl)                                 |
| QQ\_music\_direct\_link\_export | GPL-3.0                               | QQ CDN 文件前缀表交叉核对                                                  | 否，仅数据参考      | [https://github.com/DreamWalkerXZ/QQ\_music\_direct\_link\_export](https://github.com/DreamWalkerXZ/QQ_music_direct_link_export) |
| Supabase                        | Apache-2.0（开源部分）；托管服务按 Supabase 条款    | 匿名使用人数计数（PostgreSQL + PostgREST RPC），客户端仅通过 HTTPS 调用                  | 否，托管服务       | [https://supabase.com](https://supabase.com)                                                                                     |
| SodaM                           | AGPL-3.0                              | 汽水音乐扫码、二次验证与 PC 签名流程参考；仅阅读公开实现，未复制代码                                     | 否，仅协议参考      | [https://github.com/sodahub-org/sodam](https://github.com/sodahub-org/sodam)                                                     |
| mygo-music-qishui               | 未标注（公开源码）                         | 汽水音乐登录与播放链路参考；仅阅读公开实现，未复制代码                                          | 否，仅协议参考      | [https://github.com/DaviRain-Su/mygo-music-qishui](https://github.com/DaviRain-Su/mygo-music-qishui)                             |
| bowen_music                     | 未标注（公开源码）                         | 波点音乐会员到期与最近播放协议参考；仅阅读公开实现，未复制代码                                      | 否，仅协议参考      | [https://github.com/ldm0715/bowen_music](https://github.com/ldm0715/bowen_music)                                                 |

QQ CDN 前缀表用于以下档位映射：



```
m4a    C400/C600 .m4a   128k AAC
mp3    M500 .mp3         128k CBR
mp3    M800 .mp3         320k CBR
ogg    O400/O600/O800 .ogg
flac   F000 .flac        无损
hires  RS01 .flac        Hi-Res 无损（48kHz/24bit）
```



***

## 4. 基础依赖

正式 Windows x64 构建实际链接以下 Go 模块：



| 模块                                                                                          | 许可证          | 用途                            |
| ------------------------------------------------------------------------------------------- | ------------ | ----------------------------- |
| [github.com/wailsapp/wails/v2](https://github.com/wailsapp/wails/v2) v2.17.1                | MIT          | Go + WebView2 桌面框架            |
| [github.com/wailsapp/go-webview2](https://github.com/wailsapp/go-webview2) v1.0.22          | MIT          | Wails 的 WebView2 绑定           |
| [github.com/gorilla/websocket](https://github.com/gorilla/websocket) v1.5.3                 | BSD-2-Clause | Chrome DevTools Protocol 登录窗口 |
| [github.com/skip2/go-qrcode](https://github.com/skip2/go-qrcode) v0.0.0-20200617195104-da1b6568686e | MIT          | 汽水 / 波点原生扫码二维码生成            |
| [golang.org/x/crypto](https://golang.org/x/crypto) v0.57.0                                  | BSD-3-Clause | 汽水 CENC MP4 解密、密码学原语           |
| [golang.org/x/image](https://golang.org/x/image) v0.41.0                                    | BSD-3-Clause | WebP 封面解码、取色                  |
| [golang.org/x/sys](https://golang.org/x/sys) v0.48.0                                        | BSD-3-Clause | Windows 注册表、DPAPI、音频会话、托盘     |
| [golang.org/x/text](https://golang.org/x/text) v0.42.0                                      | BSD-3-Clause | GBK 歌词解码                      |
| [golang.org/x/net](https://golang.org/x/net) v0.60.0                                        | BSD-3-Clause | 网络相关依赖                        |
| git.sr.ht/\~jackmordaunt/go-toast/v2 v2.0.3                                                 | 仓库未显示许可证文件   | Windows Toast 通知              |
| [github.com/bep/debounce](https://github.com/bep/debounce) v1.2.1                           | MIT          | 防抖                            |
| [github.com/gabriel-vasile/mimetype](https://github.com/gabriel-vasile/mimetype) v1.4.16    | MIT          | MIME 类型识别                     |
| [github.com/go-ole/go-ole](https://github.com/go-ole/go-ole) v1.3.0                         | MIT          | Windows OLE                   |
| [github.com/google/uuid](https://github.com/google/uuid) v1.6.0                             | BSD-3-Clause | UUID                          |
| [github.com/pkg/browser](https://github.com/pkg/browser) v0.0.0-20240102092130-5ac0b6a4141c | BSD-2-Clause | 打开浏览器                         |
| [github.com/pkg/errors](https://github.com/pkg/errors) v0.9.1                               | BSD-2-Clause | 错误处理                          |
| [github.com/leaanthony/go-ansi-parser](https://github.com/leaanthony/go-ansi-parser) v1.6.1 | MIT          | ANSI 解析                       |
| [github.com/leaanthony/slicer](https://github.com/leaanthony/slicer) v1.6.0                 | MIT          | 切片工具                          |
| [github.com/leaanthony/u](https://github.com/leaanthony/u) v1.1.1                           | MIT          | 可空类型                          |
| [github.com/leaanthony/gosod](https://github.com/leaanthony/gosod) v1.0.4                   | MIT          | 模板渲染                          |
| [github.com/godbus/dbus/v5](https://github.com/godbus/dbus/v5) v5.1.0                       | BSD-2-Clause | Linux / 桌面总线兼容                |
| [github.com/jchv/go-winloader](https://github.com/jchv/go-winloader) v0.0.0-20210711035445-715c2860da7e | MIT          | Windows 原生库加载                   |
| [github.com/labstack/echo/v4](https://github.com/labstack/echo/v4) v4.16.1                  | MIT          | Wails 内部 HTTP 服务                |
| [github.com/labstack/gommon](https://github.com/labstack/gommon) v0.5.0                     | MIT          | Echo 通用工具                       |
| [github.com/mattn/go-colorable](https://github.com/mattn/go-colorable) v0.1.15              | MIT          | 终端颜色输出                        |
| [github.com/mattn/go-isatty](https://github.com/mattn/go-isatty) v0.0.22                    | MIT          | 终端检测                          |
| [github.com/valyala/bytebufferpool](https://github.com/valyala/bytebufferpool) v1.0.0       | MIT          | 字节缓冲池                          |
| [github.com/valyala/fasttemplate](https://github.com/valyala/fasttemplate) v1.2.2           | MIT          | 快速模板渲染                        |
| [github.com/rivo/uniseg](https://github.com/rivo/uniseg) v0.4.7                             | MIT          | Unicode 文本分段                  |
| [github.com/samber/lo](https://github.com/samber/lo) v1.49.1                                | MIT          | 泛型工具集                         |
| [github.com/tkrajina/go-reflector](https://github.com/tkrajina/go-reflector) v0.5.8         | Apache-2.0   | 反射工具                          |

Wails 的 MIT 许可证原文：



```
MIT License

Copyright (c) 2018-Present Lea Anthony

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

其他许可证全文：



* BSD-2-Clause：[https://opensource.org/license/bsd-2-clause](https://opensource.org/license/bsd-2-clause)

* BSD-3-Clause：[https://opensource.org/license/bsd-3-clause](https://opensource.org/license/bsd-3-clause)

* Apache-2.0：[https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)

* Unlicense：[https://unlicense.org/](https://unlicense.org/)

* Zlib：[https://opensource.org/license/zlib](https://opensource.org/license/zlib)

GitHub Actions 同步模板仅使用 `actions/checkout`（MIT），不属于应用运行时依赖。



***

## 5. 未具名参考

以下内容在源码或文档中被标注为「公开实现」「参考实现」「社区整理」，但没有记录具体仓库名或作者，无法在本文件中给出精确链接：



* 华为音乐 `client_id = 101444301`、`loginex` 音乐会话兑换、Digest 鉴权与字段名：`README.md` 与 `docs/API.md` 标注来自公开实现 / 公开接口行为。

* 华为歌单分页逻辑：`internal/hwmusic/library.go` 标注「按参考实现翻页」。

* 各平台公开接口的社区整理与讨论：`README.md` 致谢段仅写类别，没有具体链接。

* NCM 接口状态站：软件内「参考接口」指向 `https://status.beta-next.icu/status/ncm`，属于社区状态页。

* 腾讯交互翻译、MyMemory、Google gtx：外部翻译服务，不是开源项目，未计入本文件的开源清单。



***

## 6. 许可证说明



* **听澜 Tinglan（AGPL-3.0）**：仅作为界面与交互参考；未复制其代码。若后续引入其代码或样式文件，需要按 AGPL-3.0 处理。

* **Melotopia（未标注许可证）**：公开源码但未声明许可证，严格说不能按开源项目复用代码；当前仅作为公开界面参考。

* **沐语（闭源）**：仅作为视觉参考，不使用其代码。

* **MyGo（MIT）**：仅参考 shader 效果，Novae 用 CSS 语义参数重建；MyGo Music 为 AGPL-3.0，未使用其代码。

* **QQMusicApi（GPL-3.0）**：可选外部服务，不随 Novae 分发；如自行部署，请遵守其许可证。

* **QQ\_music\_direct\_link\_export（GPL-3.0）**：仅用于 CDN 前缀表交叉核对，未复制其代码。

* **NeteaseCloudMusicApi**：GitHub 仓库已归档且当前无 LICENSE 文件；npm 包标注 MIT。后续维护优先使用 `api-enhanced`（MIT）。

* **SodaM（AGPL-3.0）**：仅阅读其公开实现以核对汽水扫码、二次验证与 PC 签名流程，未复制其代码。SodaM 作为可选本机 signer 由用户自行安装，不随 Novae 分发；如后续引入其代码，需要按 AGPL-3.0 处理。

* **mygo-music-qishui / bowen_music（未标注许可证）**：仅作为公开协议与交互参考，未复制代码，也未随包分发；许可证以各自仓库为准。

* **Supabase**：匿名使用人数计数托管服务（PostgreSQL + PostgREST）；开源部分采用 Apache-2.0，托管服务按其服务条款使用。Novae 仅通过 HTTPS 调用部署在本项目的 REST RPC，不随包分发其代码。

* **go-toast**：Wails 运行时依赖，上游仓库未显示许可证文件；建议在正式分发前向上游确认。

从仓库可见源码静态检查看，未发现带 GPL/AGPL 版权头的复制代码；本文件不是法律意见。



***

## 7. 维护约定

新增、移除或升级第三方组件时，需要同步更新：



1. 本文件；

2. 软件内「设置 → 关于 → 致谢与开源许可」；

3. 如涉及随包分发的组件，保留其许可证与版权声明。