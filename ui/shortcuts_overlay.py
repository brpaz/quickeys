
import gi
import os

import logging

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib, GObject, Gdk

logger = logging.getLogger("main")

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768


class ShortcutsOverlay(Gtk.ShortcutsWindow):
    """Window that displays the shortcuts for the active application"""

    def __init__(self, application, active_application, shortcuts=[]):
        """Window constructor"""

        Gtk.ShortcutsWindow.__init__(self)
        self.Application = application

        self.active_application = active_application
        self.shortcuts = shortcuts

        self.set_default_size(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_modal(True)
        self.set_skip_taskbar_hint(True)

        self.set_application(application)
        self.build_widgets()
        self.set_property("section-name", "app")

    def build_widgets(self):
        """ Constructs the widgets required by GtkShortcutsWindow to display the application shortcuts"""

        section = Gtk.ShortcutsSection(
            max_height=10, title=self.active_application, section_name="app")
        section.show()
        for sectionName, items in self.shortcuts.iteritems():
            group = Gtk.ShortcutsGroup(
                title=sectionName)
            section.add(group)

            if items is None:
                continue

            for shortcut in items:
                title = shortcut.keys()[0]
                accelerator = shortcut.values()[0]

                short = Gtk.ShortcutsShortcut(
                    title=title, accelerator=accelerator)
                short.show()
                group.add(short)

        self.add(section)
