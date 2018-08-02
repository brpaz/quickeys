#!/usr/bin/env python

import sys
import gi
import signal

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib

from lib import Application


def main():
    """
    The entry point for the application.
    It creates an instance of the application and run it.
    """
    app = Application()

    exit_status = app.run(sys.argv)
    sys.exit(exit_status)


if __name__ == "__main__":
    main()
