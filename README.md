# Command Select Contours

[English](#english) · [繁體中文](#繁體中文) · [简体中文](#简体中文)

## English

A persistent Python plug-in for Glyphs 3. Hold Command (⌘) and click a node or drag-select multiple nodes. When you release the mouse, all nodes on the corresponding contours are selected, including off-curve handles. Both open paths and closed contours are supported.

**[Download plug-in 1.0](https://github.com/Zonz-Ly/Glyphs-CommandSelectContours/releases/download/1.0/CommandSelectContours.zip)** · Unzip the download and double-click the plug-in bundle to install it.

### Installation

1. Install Python in Glyphs under **Window → Plugin Manager → Modules**, if it is not already installed.
2. Double-click `CommandSelectContours.glyphsPlugin` and follow the installation prompt in Glyphs.
3. Restart Glyphs. The plug-in is enabled by default. Toggle it under **Edit → Command 选择整个轮廓** (the menu item currently uses Simplified Chinese).

If double-clicking does not start installation, copy the entire plug-in bundle to `~/Library/Application Support/Glyphs 3/Plugins/` and restart Glyphs.

### Usage

- **⌘ + click a node:** expand the node selection made by Glyphs to the entire contour.
- **⌘ + drag-select nodes:** select all nodes on every contour involved.
- **⌘ + Shift:** retain Glyphs’ normal additive selection behavior, then expand the contours represented in the current selection.
- Ordinary mouse selection retains the normal Glyphs behavior.

Selection expands after mouse release; behavior during dragging is unchanged. Nodes already selected also participate in the expansion. Components and anchors do not trigger contour expansion. The plug-in changes only the selection, not node coordinates or path structure.

## 繁體中文

Glyphs 3 的常駐 Python 外掛。按住 Command（⌘）點選節點，或框選多個節點，放開滑鼠後便會選取這些節點所屬輪廓的全部節點，包括離曲線控制柄。支援開放路徑與閉合輪廓。

**[下載外掛 1.0](https://github.com/Zonz-Ly/Glyphs-CommandSelectContours/releases/download/1.0/CommandSelectContours.zip)** · 下載並解壓縮後，按兩下外掛套件即可安裝。

### 安裝

1. 若尚未安裝 Python，請在 Glyphs 的「視窗 → 外掛管理員 → 模組」中安裝。
2. 按兩下 `CommandSelectContours.glyphsPlugin`，依照 Glyphs 的提示安裝。
3. 重新啟動 Glyphs。外掛預設啟用，可透過「編輯 → Command 选择整个轮廓」暫時開關（選單項目目前使用簡體中文）。

若按兩下未啟動安裝，請將整個外掛套件複製到 `~/Library/Application Support/Glyphs 3/Plugins/`，再重新啟動 Glyphs。

### 使用

- **⌘ + 點選節點：** 將 Glyphs 選取的節點擴展為整個輪廓。
- **⌘ + 框選節點：** 選取所有涉及輪廓的全部節點。
- **⌘ + Shift：** 保留 Glyphs 原有的追加選取行為，再擴展目前選取範圍中的輪廓。
- 一般滑鼠選取維持 Glyphs 原有行為。

擴展發生在放開滑鼠之後；外掛不改變拖曳中的行為。原先已選取的節點也會參與擴展。組件與錨點不會觸發輪廓擴展。外掛只變更選取範圍，不修改節點座標或路徑結構。

## 简体中文

Glyphs 3 的常驻 Python 插件。按住 Command（⌘）点选节点，或框选多个节点，松开鼠标后会选中这些节点所属轮廓的全部节点，包含离曲线控制柄。支持开放路径和闭合轮廓。

**[下载插件 1.0](https://github.com/Zonz-Ly/Glyphs-CommandSelectContours/releases/download/1.0/CommandSelectContours.zip)** · 下载后解压，双击插件包安装。

### 安装

1. 在 Glyphs 的「窗口 → 插件管理器 → 模块」中安装 Python（如果尚未安装）。
2. 双击 `CommandSelectContours.glyphsPlugin`，按 Glyphs 的提示安装。
3. 重启 Glyphs。插件默认启用，可从「编辑 → Command 选择整个轮廓」临时开关。

如果双击没有触发安装，将整个插件包复制到 `~/Library/Application Support/Glyphs 3/Plugins/` 后重启。

### 使用

- ⌘ + 单击节点：将 Glyphs 得到的节点选区扩展为整个轮廓。
- ⌘ + 框选节点：扩展为所有涉及的完整轮廓。
- ⌘ + Shift：保留 Glyphs 原有的增选行为，再扩展当前选区中的轮廓。
- 普通鼠标选择保持 Glyphs 原有行为。

扩展发生在松开鼠标之后；插件不改变拖动中的行为。已有选区中的节点也会参与扩展。组件、锚点不作为轮廓扩展。插件只修改选择，不修改节点坐标或路径结构。
