import os
import yaml
import logging

logger = logging.getLogger("main")


class ShortcutsReader:
    """This class is responsible for opening and parse the shortcuts files."""

    def __init__(self, shortcuts_path):
        self.shortcuts_path = shortcuts_path

    def find(self, application):
        """Returns a list of shortcuts for the specified application"""

        filename = os.path.join(self.shortcuts_path, "%s.yml" % application)
        shortcuts = {}

        try:
            with open(filename, 'r') as stream:
                shortcuts = yaml.load(stream)
        except IOError as e:
            logger.info("Cannot find shortcuts for application %s" %
                        application)
        except yaml.YAMLError as exc:
            logger.error("Cannot parse shortcuts file %s" %
                         filename)
        finally:
            return shortcuts
