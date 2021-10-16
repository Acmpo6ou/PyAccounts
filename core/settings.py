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

import gi

gi.require_version("Gtk", "3.0")
from core.gtk_utils import GladeTemplate


class SettingsDialog(GladeTemplate):
    def __init__(self):
        super().__init__("settings")
        self.load_fonts()

    def run(self):
        self.parent_widget.run()

    def on_cancel(self, _):
        self.parent_widget.hide()

    def load_fonts(self):
        """
        Loads font settings from settings.json
        """

    def on_save(self):
        """
        Saves fonts to settings.json and applies changes.
        """
        # TODO: call main_window.load_css() to apply changes.