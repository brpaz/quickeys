
import gi
import os

import logging

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib, GObject, Gdk

logger = logging.getLogger("main")

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768


class ShortcutsOverlay(Gtk.ShortcutsWindow):
    """ Window that displays the shortcuts for the active application """

    def __init__(self, application, active_application,
                 app_shortcuts=[], system_shortcuts=[]):
        """Window constructor"""

        Gtk.ShortcutsWindow.__init__(self)
        self.Application = application

        self.set_default_size(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_modal(True)
        self.set_skip_taskbar_hint(True)

        self.set_application(application)
        self.add_shortcuts_section("app", active_application, app_shortcuts)
        self.add_shortcuts_section("system", "System", system_shortcuts)

        # always sets the default section to the "focused" app
        self.set_property("section-name", "app")

    def add_shortcuts_section(self, name, title, shortcuts=[]):
        """ Constructs the widgets required by GtkShortcutsWindow to display the application shortcuts"""

        section = Gtk.ShortcutsSection(
            max_height=10, title=title, section_name=name)
        section.show()

        for category, items in shortcuts.items():
            group = Gtk.ShortcutsGroup(
                title=category)
            section.add(group)

            if items is None:
                continue

            for shortcut in items:
                title = list(shortcut.keys())[0]
                accelerator = list(shortcut.values())[0]

                short = Gtk.ShortcutsShortcut(
                    title=title, accelerator=accelerator)
                short.show()
                group.add(short)

        self.add(section)
