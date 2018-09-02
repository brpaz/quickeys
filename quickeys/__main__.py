import sys
import gi
import signal

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib
from quickeys import Application


def main():
    """
    The entry point for the application.
    It creates an instance of the application and run it.
    """
    app = Application()
    app.run(sys.argv)


if __name__ == "__main__":
    main()
