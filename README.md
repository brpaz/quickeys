# Quickeys

> Linux application that provides an overlay window with the list of shortcuts for the current focused application. Inspired by Mac OS applications [CheatSheet](https://mediaatelier.com/CheatSheet/) and [pretzel](https://github.com/amiechen/pretzel).

![screenshot](screenshot.png)

This was tested on Ubuntu 18.04.

## System Requirements

* Python 3
* GTK > 3.14
* AppIndicator3

## Install

For now the only way to install this application is installing from source. I would like to provide flatpak, snap, deb support in the future. If you know how to package Python apps in these formats, PRs are welcome ;)

```
make install
```

## Supported Applications

Right now, this application supports displaying shortcuts for:

* Gedit
* Google Chrome
* Visual Studio Code
* JetBrains Applications
* Firefox
* Pinta

More applications will be added later. Contributions are always welcome.

---

## FAQ

### How do I add / change shortcuts?

Shortcuts are configured in YAML files in the data/shortcuts directory of the source code. The files in that directory are copied to ~/.config/quickkeys/shortcuts when starting the application for the first time.

As a user, you can change / add shortcuts directly to the .config directory as the application reads from it at runtime.

The filename should be the name of the executable of the application. In general you can get it from the command line like so:

* Get the pid of your application. (Ex: ```ps ax | grep firefox```)
* Run ```cat /proc/{pid}/comm```. The value displayed there should be the name of your shortcuts file.

Some applications like Java applications doesnt work like that and returns a generic "Java" from the previous command. In that case we need to modify the source code to be able to identify the application in other away. Workarounds for Jetbrains and Pinta are already implemented. Please see the function "get_active_application" in "quickeys/application.py" for details.

The yaml file should have the following structure (taken from Gedit shortcuts file):

```yml
Tabs:
  - Switch to the next tab to the left: <Control><Alt>Up
  - Switch to the next tab to the right:  <Control><Alt>Right
  - Close tab:  <Control>W
  - Save All tabs: <Control><Shift>L
  - Close All tabs: <Control><Shift>W
  - Reopen the most recently closed tab: <Control><Shift>T
  - Jump to nth tab: <Alt>N
  - New Tab Group: <Contol><Alt>N
  - Previous tab Group: <Shift><Ctrl><Alt>Up
  - Next tab group: <Shift><Control><Alt>Down
```

* This format is the same from [Pretzel](https://github.com/amiechen/pretzel).
* The shortcut combination should follow a pattern supported by "gtk_accelerator_parse" Ex: “<Control>a” or “<Shift><Alt>F1”.

### How do I start quickeys at start-up?

* Create a new startup application and use "quickeys" as command.

---

## Todo

* Build a proper installer (pip, deb, flatpak).
* Add more applications. (Contributors welcome)
* Is there any way in Linux to get an application registered shortcuts automatically??
* Improve docmentation on accelerators.

## Contributing

* All contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

MIT

