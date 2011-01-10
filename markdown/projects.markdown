# AT-SPI

AT-SPI (Assistive Technology Service Provider Interface) is a toolkit independent accessibility API for the [GNOME](http://www.gnome.org/) desktop, standardised by the [Linux Foundation](http://www.linuxfoundation.org/collaborate/workgroups/accessibility/atk/at-spi/at-spi_on_d-bus). AT-SPI was originally written as a CORBA API. This IPC mechanism has been deprecated in both GNOME and KDE environments and is no-longer useful. I have worked on replacing this with a compatible API based on [D-Bus](http://www.freedesktop.org/wiki/Software/dbus). The intention is to have an accessibility transport layer that works across the GNOME and KDE desktops. The project encompasses creating client and server libraries that are API compatible with their CORBA counterparts.

## Skills

C, Python, D-Bus, Acessibility, GNOME, Linux, Gtk+, X

## Site

[http://www.a11y.org/dbus](http://www.a11y.org/dbus)

## Code

 * [http://git.gnome.org/browse/pyatspi2/](http://git.gnome.org/browse/pyatspi2/)
 * [http://git.gnome.org/browse/at-spi2-core/](http://git.gnome.org/browse/at-spi2-core/)
 * [http://git.gnome.org/browse/at-spi2-atk/](http://git.gnome.org/browse/at-spi2-atk/)

# QSpiBridge

The QSpiBridge library bridges the QAccessible and AT-SPI API's enabling [Qt](http://qt.nokia.com/products/) applications to be accessible on a GNOME desktop. This is important to provide parity for users of accessible technologies. Qt applications are regularly used in Linux and in the past have not been accessible in either KDE or GNOME.

## Skills

C++, Qt, Accessibility, Linux

## Code

[http://gitorious.org/qt-at-spi](http://gitorious.org/qt-at-spi)

# dbuf

dbuf is an interface description language closely tied to [D-Bus](http://www.freedesktop.org/wiki/Software/dbus). The language has syntax for describing D-Bus interfaces, messages, errors, and replies. It can also combine basic D-Bus types in-to compound structures and enums that can be used in descriptions of the interfaces. I has a modules system and compiles down to D-Bus introspection XML. The compiler is written in Python, but uses the [Antlr](http://www.antlr.org/) to describe the syntax and generate lexers, parsers and output generators.

## Skills

Python, Antlr, Compilers, D-Bus

## Code

[http://github.com/doffm/dbuf](http://github.com/doffm/dbuf)