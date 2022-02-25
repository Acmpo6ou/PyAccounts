#  Copyright (c) 2021-2022. Bohdan Kolvakh
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
import glob
from pathlib import Path

from gi.repository import Gtk, Gdk, GdkPixbuf

import core
from core.database_utils import Database
from core.gtk_utils import GladeTemplate, abc_list_sort
from core.settings import Settings
from core.widgets import Window


class MainWindow(Gtk.ApplicationWindow, Window):
    # <editor-fold>
    parent_widget: Gtk.Box
    menubar_toolbar: Gtk.Box
    menubar: Gtk.MenuBar
    toolbar: Gtk.Toolbar
    separator: Gtk.Paned
    form_box: Gtk.Box
    db_list: Gtk.ListBox
    statusbar: Gtk.Statusbar
    # </editor-fold>

    def __init__(self, *args, **kwargs):
        Gtk.ApplicationWindow.__init__(self, *args, **kwargs)
        GladeTemplate.__init__(self, "main_window")
        Window.__init__(self)

        # we will copy password or notes here, because it's safer than using a regular clipboard
        self._safe_clipboard = ""

        self.main_window = self
        self.settings = Settings()
        self.load_css()

        self.databases = self.get_databases()
        self.load_databases()
        self.select_main_database()

        # TODO: test shortcuts
        # Ctrl+I to import database
        self.shortcuts.connect(
            Gdk.keyval_from_name("i"),
            Gdk.ModifierType.CONTROL_MASK,
            Gtk.AccelFlags.VISIBLE,
            self.on_import_database,
        )

        # Ctrl+E to export database
        self.shortcuts.connect(
            Gdk.keyval_from_name("e"),
            Gdk.ModifierType.CONTROL_MASK,
            Gtk.AccelFlags.VISIBLE,
            self.on_export_database,
        )

    @property
    def safe_clipboard(self) -> str:
        """
        Returns content from safe clipboard, then automatically clears the clipboard.
        This is done for safety.
        """

    @safe_clipboard.setter
    def safe_clipboard(self, value: str):
        """
        Puts `value` into safe clipboard and starts one minute timer to auto clear the clipboard.
        This is done for safety.
        """
        # TODO: use GObject.timeout_add() to add callback to clear safe clipboard

    @staticmethod
    def load_css():
        """
        Loads styles from global.css
        """
        # TODO: substitute font from settings.json
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("ui/global.css")
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_USER,
        )

    @staticmethod
    def get_databases() -> list[Database]:
        """
        Returns a sorted list of databases residing in SRC_DIR folder.
        """

        dbs = []
        for file in glob.glob(f"{core.SRC_DIR}/*.dba"):
            name = Path(file).stem
            dbs.append(Database(name))
        dbs.sort()
        return dbs

    def load_databases(self):
        """
        Populates db_list with items.
        """

        self.db_list.sort_func = abc_list_sort
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("img/icon.svg", 50, 50, True)

        for db in self.databases:
            icon = Gtk.Image.new_from_pixbuf(pixbuf)
            icon.xalign = 0
            icon.margin_start = 5

            label = Gtk.Label(db.name)
            label.xalign = 0
            label.margin_start = 5
            label.margin_end = 10

            hbox = Gtk.Box()
            hbox.homogeneous = False

            hbox.add(icon)
            hbox.add(label)
            self.db_list.add(hbox)

    def select_main_database(self):
        """
        If there is a database called `main` auto selects it.
        """
        # TODO: call on_database_selected or send 'select' event to db_list

    def on_database_selected(self, _, row: Gtk.ListBoxRow):
        """
        If selected database is closed – displays open database form.
        :param row: row containing selected database name.
        """
        # TODO: use show_form()

    def import_database(self, path: str):
        """
        Imports given database handling all errors.
        :param path: path to database file we're trying to import.
        """
        # TODO: show success and error messages
        # TODO: validate database file size, whether database already exists;
        #  update db_list and list widget

    def on_import_database(self, *args):
        """
        Displays import database dialog.
        """

        # see FileChooserDialog docs for more details
        # TODO: set dialog title to "Import database"
        # TODO: allow only .dba files
        # TODO: use Gtk.FileChooserAction.OPEN
        # TODO: add 2 buttons: Cancel and Import
        # TODO: import .dba file only if response is Gtk.ResponseType.ACCEPT
        # TODO: use `filename` property of dialog to access selected file path
        # TODO: call import_database

    def export_database(self, name: str, path: str):
        """
        Exports given database handling all errors.

        :param name: name of the database we're trying to export.
        :param path: where to export the database.
        """
        # TODO: show success and error messages; call export_database

    def on_export_database(self, *args):
        """
        Displays export database dialog.
        """

        # see FileChooserDialog docs for more details
        # TODO: set dialog title to "Export database"
        # TODO: set default file name to be <dbname>.dba
        # TODO: use Gtk.FileChooserAction.SAVE
        # TODO: add 2 buttons: Cancel and Export
        # TODO: export .dba file only if response is Gtk.ResponseType.ACCEPT
        # TODO: use `filename` property of dialog to access selected file path
        # TODO: call export_database

    def do_delete_event(self, event):
        """
        Called when user tries to close the window, propagates event to on_quit.
        NOTE: DO NOT move this method to Window superclass, or else it won't work.
        """
        return self.on_quit(event)

    def on_quit(self, _) -> bool:
        """
        Checks if all databases are closed, if they are – quits, if they aren't – displays
        confirmation dialog.
        :returns: True to prevent quiting and False to allow it.
        """

        # TODO: use any() to check if there is any opened database
        # TODO: call app.quit() to quit
        # TODO: return True if user doesn't want to quit and False otherwise

    def on_create_database(self, _):
        """
        Displays create database form.
        """

        # TODO: use show_form()

    def on_edit_database(self, _):
        """
        If selected database is opened – displays edit database form,
        otherwise – rename database form.
        """

        # TODO: show warning in statusbar if there is no database selected
        # TODO: use show_form()

    def delete_database(self, name: str):
        """
        Deletes given database from disk and database list handling all errors.
        :param name: name of the database to delete.
        """
        # TODO: show success message in statusbar if database is deleted successfully
        # TODO: show error message if there is an error
        # TODO: deselect any database and update database list (use ListBox.delete(name))

    def on_delete_database(self, _):
        """
        Displays confirmation dialog asking user if he really want's to delete selected database.
        """
        # TODO: show warning in statusbar if there is no database selected
