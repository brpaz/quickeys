
import gi
import os

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib, GObject, Gdk

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768


class ShortcutsOverlay(object):
    """Window that displays the shortcuts for the active application"""

    def __init__(self, application):
        """Window constructor"""

        self.Application = application
        self.shortcuts = {}

        self.win = Gtk.ShortcutsWindow()
        self.win.set_default_size(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.win.set_position(Gtk.WindowPosition.CENTER)
        self.win.set_modal(True)
        self.win.set_skip_taskbar_hint(True)
        self.win.connect("delete-event", self.on_close)

        self.win.set_application(application)

    def on_close(self, window, event, data=None):
        """
        This function is called when the user clicks on X key or press 'ESC' key to close the window.
        We want the application to keep running in the background so we just hide the window instead of destroying it
        """
        window.hide()
        return True  # dont close the window

    def show(self):
        """ Shows the Shortcuts Window to the user"""
        self.win.show_all()
        self.win.present()

    def destroy(self):
        self.win.destroy()

    def set_shortcuts(self, active_application, shortcuts):
        """
        This function is called after fetching the shortcuts for the current application.
        It will trigger a refresh of the window contents with the shortcuts for the new app
        """
        self.active_application = active_application
        self.shortcuts = shortcuts

        self.win.set_title("Shortcuts for %s" % active_application)
        self.build_widgets()

    def build_widgets(self):
        """ Constructs the widgets required by GtkShortcutsWindow to display the application shortcuts"""
        if len(self.win.get_children()) > 0:
            self.win.get_children()[0].destroy()

        section = Gtk.ShortcutsSection(max_height=10, section_name="General")
        section.show()
        for sectionName, items in self.shortcuts.iteritems():
            group = Gtk.ShortcutsGroup(
                title=sectionName)
            section.add(group)

            for shortcut in items:
                title = shortcut.keys()[0]

                # TODO proper parse accelerators
                accelerator = shortcut.values()[0]

                short = Gtk.ShortcutsShortcut(
                    title=title, accelerator=accelerator)
                short.show()
                group.add(short)

        self.win.add(section)
