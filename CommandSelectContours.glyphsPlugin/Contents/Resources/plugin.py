# encoding: utf-8
"""Expand a Command mouse selection to complete paths in Glyphs Edit View."""
import traceback
import objc
from AppKit import NSApp, NSEventModifierFlagCommand, NSEventModifierFlagControl
from AppKit import NSEventModifierFlagOption, NSMenuItem
from GlyphsApp import Glyphs, GSNode, EDIT_MENU, MOUSEDOWN, MOUSEUP
from GlyphsApp.plugins import GeneralPlugin


class CommandSelectContours(GeneralPlugin):
    @objc.python_method
    def settings(self):
        self.name = "Command Select Contours"
        self._gesture = None
        self._pending = None
        self._enabled = True

    @objc.python_method
    def start(self):
        self._item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            "Command 选择整个轮廓", self.toggle_, "")
        self._item.setTarget_(self)
        self._item.setState_(1)
        Glyphs.menu[EDIT_MENU].append(self._item)
        Glyphs.addCallback(self.mouseDown, MOUSEDOWN)
        Glyphs.addCallback(self.mouseUp, MOUSEUP)

    def toggle_(self, sender):
        self._enabled = not self._enabled
        self._item.setState_(int(self._enabled))
        self._gesture = self._pending = None

    @objc.python_method
    def editView(self, event):
        window = event.window()
        if window is None:
            return None
        root = window.contentView()
        point = root.convertPoint_fromView_(event.locationInWindow(), None)
        view = root.hitTest_(point)
        graphicClass = objc.lookUpClass("GSGraphicView")
        while view is not None:
            if view.isKindOfClass_(graphicClass):
                return view
            view = view.superview()
        return None

    @objc.python_method
    def mouseDown(self, notification):
        self._gesture = None
        self._pending = None
        if not self._enabled:
            return
        try:
            event = NSApp.currentEvent()
            if event is None or event.buttonNumber() != 0:
                return
            flags = event.modifierFlags()
            if not flags & NSEventModifierFlagCommand:
                return
            # Leave Command-Option and Command-Control gestures to Glyphs.
            if flags & (NSEventModifierFlagOption | NSEventModifierFlagControl):
                return
            view = self.editView(event)
            if view is not None:
                self._gesture = (view, event.window())
        except Exception:
            self.logError(traceback.format_exc())

    @objc.python_method
    def mouseUp(self, notification):
        gesture = self._gesture
        self._gesture = None
        if not self._enabled or gesture is None:
            return
        self._pending = gesture
        # Mouse notifications may precede the tool's selection update.
        # Run on the next main-loop iteration, after Glyphs finishes selecting.
        self.performSelector_withObject_afterDelay_("expandSelection:", None, 0.0)

    def expandSelection_(self, unused):
        pending = self._pending
        self._pending = None
        if not self._enabled or pending is None:
            return
        try:
            view, window = pending
            if view.window() != window or NSApp.keyWindow() != window:
                return
            layer = view.activeLayer()
            if layer is None:
                return
            # Snapshot first: adding nodes must not mutate an iterated selection.
            paths = []
            for item in list(layer.selection):
                if isinstance(item, GSNode) and item.parent is not None:
                    if item.parent not in paths:
                        paths.append(item.parent)
            for path in paths:
                for node in path.nodes:
                    node.selected = True
            if paths:
                view.setNeedsDisplay_(True)
        except Exception:
            self.logError(traceback.format_exc())

    @objc.python_method
    def __file__(self):
        return __file__
