# Command Select Contours

Glyphs 3 的常驻 Python 插件。按住 Command（⌘）点选节点，或框选多个节点，松开鼠标后会选中这些节点所属轮廓的全部节点，包含离曲线控制柄。支持开放路径和闭合轮廓。

**[下载插件 1.0](https://github.com/Zonz-Ly/Glyphs-CommandSelectContours/releases/download/1.0/CommandSelectContours.zip)** · 下载后解压，双击插件包安装。

A Glyphs 3 plug-in that expands a Command-click or Command-drag node selection to complete contours, including off-curve handles. Selection expands on mouse release. Toggle it in the Edit menu.

## 安装

1. 在 Glyphs 的「窗口 → 插件管理器 → 模块」中安装 Python（如果尚未安装）。
2. 双击 `CommandSelectContours.glyphsPlugin`，按 Glyphs 的提示安装。
3. 重启 Glyphs。插件默认启用，可从「编辑 → Command 选择整个轮廓」临时开关。

如果双击没有触发安装，将整个插件包复制到 `~/Library/Application Support/Glyphs 3/Plugins/` 后重启。

## 使用

- ⌘ + 单击节点：将 Glyphs 得到的节点选区扩展为整个轮廓。
- ⌘ + 框选节点：扩展为所有涉及的完整轮廓。
- ⌘ + Shift：保留 Glyphs 原有的增选行为，再扩展当前选区中的轮廓。
- 普通鼠标选择保持 Glyphs 原有行为。
- ⌘ + Option / Control 不触发插件，以保留组合手势。

扩展发生在松开鼠标之后；插件不改变拖动中的行为。已有选区中的节点也会参与扩展。组件、锚点不作为轮廓扩展。插件只修改选择，不修改节点坐标或路径结构。

## 验证状态

1.0.1 已在本机 Glyphs 3 中验证 Command 点选：一个节点所属轮廓的 28 个节点全部选中。修复了错误的画布类名以及带有视图变换时的命中检测。已检查 Python 语法、plist 和官方 SDK 启动文件。框选、背景层和 Glyphs 4 兼容性尚未实测。

建议在测试字体中确认：单击一个节点、跨两个轮廓框选、Shift 增选、控制柄、开放路径、背景层、普通选择以及菜单开关。

## 来源

插件启动二进制来自 [Glyphs 官方 SDK](https://github.com/schriftgestalt/GlyphsSDK)，原许可见 `LICENSE-SDK.txt`。插件逻辑位于 `Contents/Resources/plugin.py`。
