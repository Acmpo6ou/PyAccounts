#!/usr/bin/python3

#  Copyright (c) 2022. Bohdan Kolvakh
#  This file is part of PyAccounts.
#
#  PyAccounts is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  PyAccounts is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with PyAccounts.  If not, see <https://www.gnu.org/licenses/>.

"""
Contains various utilities to simplify development with GTK.
"""

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GObject, Gtk


# noinspection PyUnresolvedReferences
def _getattr(self, item):
    """
    A fluent API to get GTK object's attributes.

    Instead of writing:
    >>> label.get_text()
    >>> label.props.angle
    This method allows us to write:
    >>> label.text
    >>> label.angle
    Which is a more pythonic API.
    """
    try:
        return object.__getattribute__(self.props, item)
    except AttributeError:
        return object.__getattribute__(self, f"get_{item}")()


# noinspection PyUnresolvedReferences
def _setattr(self, item, value):
    """
    A fluent API to set GTK object's attributes.

    Instead of writing:
    >>> label.set_text("test")
    >>> label.props.angle = 90
    This method allows us to write:
    >>> label.text = "test"
    >>> label.angle = 90
    Which is a more pythonic API.
    """
    try:
        return setattr(self.props, item, value)
    except AttributeError:
        pass

    try:
        getattr(self, f"set_{item}")(value)
    except AttributeError:
        original_setattr(self, item, value)


# save original __setattr__
original_setattr = GObject.Object.__setattr__

# replace __getattr__ and __setattr__ with our methods that provide fluent API
GObject.Object.__getattr__ = _getattr
GObject.Object.__setattr__ = _setattr


class GladeTemplate(Gtk.Bin):
    """
    Simplifies loading of glade ui files.
    This class should be subclassed to automatically load needed ui file.
    """

    def __init__(self, template: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.builder = Gtk.Builder.new_from_file(f"ui/{template}.glade")
        self.parent_widget = self.builder.get_object(template)
        self.add(self.parent_widget)
        self.builder.connect_signals(self)

    # noinspection PyUnresolvedReferences
    def __getattr__(self, item):
        """
        Simplifies widget access, instead of making builder.get_object() calls we can
        access widgets directly as attributes.

        Instead of writing this:
        >>> form.builder.get_object("mywidget")
        We can do this:
        >>> form.mywidget

        :param item: id of the widget.
        """
        # try to get widget from builder
        builder = object.__getattribute__(self, "builder")
        widget = builder.get_object(item)

        # if worked, return the widget
        if widget:
            attrs = object.__getattribute__(self, "__dict__")
            attrs[item] = widget  # cache it
            return widget

        # else, attribute we're trying to get is not a widget, so we return it the normal way
        return object.__getattribute__(self, item)


def load_icon(icon_name, size):
    """
    Returns icon from default theme.
    """
    icon_theme = Gtk.IconTheme.get_default()
    icon = icon_theme.load_icon(icon_name, size, Gtk.IconLookupFlags.FORCE_SVG)
    return Gtk.Image.new_from_pixbuf(icon)


def get_mime_icon(path) -> Gtk.Image:
    """
    Returns mime icon associated with file given in `path`.
    :param path: path to file icon of which we want to get.
    """

    # TODO: see StackOverflow bookmark:
    #  https://stackoverflow.com/questions/1629172/how-do-you-get-the-icon-mime-type-and-application-associated-with-a-file-in-th

    # TODO: use load_icon()
    # TODO: possibly test this function; it returns Image, so test it's properties
