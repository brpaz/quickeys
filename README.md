# Shortcuts overlay

> Linux application that provides an easy way to access the shortcuts of the current focused application.

## System Requirements

* Python 2.7
* GTK > 3.14

## Build

```
python main.py
```

## Configure shortcuts

This application provides a set of default shortcuts for some common applications like Chrome, Firefox and Visual Studio code.
These shortcuts are configured in YAML files in the data/shortcuts directory of the application. The files in that directory are copied to ~/.config/shortcuter/shortcuts when starting the application for the first time.
You add your own by adding a new file to the config directory.

The filename should be the name of the executable of the application. You can get it from the command line like so:

* Get the pid of your application. (Ex: ```ps ax | grep firefox```)
* Run ```cat /proc/{pid}/comm```. The value displayed there should be the name of your shortcuts file.

The yaml file should have the following structure:

```yml
Section Name:
  - Description1: Shortcut combination
  - Description2: Shortcut combination
```

This format is the same from [Pretzel](https://github.com/amiechen/pretzel).
The shortcut combination should follow a pattern supported by "gtk_accelerator_parse" Ex: “<Control>a” or “<Shift><Alt>F1”.


## Todo

* Build a proper installer (pip, deb, flatpak).

## Contributing

* All contributions are welcome, mostly adding shortcuts for new applications. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

MIT

