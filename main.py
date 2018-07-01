#!/usr/bin/env python

import sys

from lib import Application


def main():
    """
    The entry point for the application.
    It creates an instance of the application and run it.
    """
    exit_status = Application().run(sys.argv)
    sys.exit(exit_status)


if __name__ == "__main__":
    main()
