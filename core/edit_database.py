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
import typing

from gi.repository import Gtk

from core.create_database import CreateDatabase
from core.database_utils import Database

if typing.TYPE_CHECKING:
    from core.main_window import MainWindow

EDIT_DB_TITLE = "Edit <i>{}</i> database"


class EditDatabase(CreateDatabase):
    # <editor-fold>
    parent_widget: Gtk.Box
    title: Gtk.Label
    name: Gtk.Entry
    password: Gtk.Entry
    repeat_password: Gtk.Entry
    apply: Gtk.Button
    name_error: Gtk.Label
    password_error: Gtk.Label
    passwords_diff_error: Gtk.Label
    # </editor-fold>

    APPLY_BUTTON_TEXT = "_Save"

    # TODO: implement `items` property (see RenameDatabase.items)

    def __init__(self, database: Database, main_window: "MainWindow"):
        super().__init__(main_window)
        self.database = database
        self.title.markup = EDIT_DB_TITLE.format(database.name)

        self.name.text = database.name
        self.password.text = database.password
        self.repeat_password.text = database.password

    def on_apply(self, _=None):
        """
        Applies changes to database using form data.
        """
        # TODO: save database, update list of databases
        # TODO: show success/error message
        # TODO: destroy form on success
