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

from core.create_account import CreateAccount
from core.database_utils import Account, Database
from core.widgets import AttachedFilesMixin

if typing.TYPE_CHECKING:
    from core.database_window import DatabaseWindow


class EditAccount(CreateAccount, AttachedFilesMixin):
    # <editor-fold>
    add: Gtk.Image
    remove: Gtk.Image
    parent_widget: Gtk.Box
    title: Gtk.Label
    apply: Gtk.Button
    username: Gtk.Entry
    email: Gtk.Entry
    copy_email: Gtk.RadioButton
    birth_box: Gtk.EventBox
    birth_date: Gtk.Label
    notes: Gtk.TextView
    attached_files: Gtk.ListBox
    accname: Gtk.Label
    name: Gtk.Entry
    name_error: Gtk.Label
    password: Gtk.Entry
    password_error: Gtk.Label
    repeat_password: Gtk.Entry
    passwords_diff_error: Gtk.Label
    # </editor-fold>

    APPLY_BUTTON_TEXT = "_Save"

    @property
    def items(self):
        accounts = list(self.database.accounts.keys())
        # it's OK if account name hasn't changed throughout editing
        accounts.remove(self.account.accountname)
        return accounts

    def __init__(self, database: Database, account: Account, database_window: "DatabaseWindow"):
        super().__init__(database, database_window)
        self.account = account
        # TODO: fill attached_paths with file names from account.attached_files;
        #  map file names to None (since they don't have any path)
        # load already attached files mapping them to None since they don't have any path
        self.attached_paths = ...
        self.load_account()
        # TODO: Create button should be changed to Save automatically, because load_account()
        #  will fill form fields with data

    def load_account(self):
        """
        Populates form fields with account data.
        """

        self.load_attached_files(self.account.attached_files)
        # TODO: change title to `Edit [account name] account`
        # TODO: make account name cursive

    def create_account(self) -> Account:
        """
        Creates account using form data.
        """
        account = super().create_account()
        # TODO: add already loaded attached files:
        """
        iterate over attached_paths keys:
            if key value is None:
                add attached file from self.account.attached_files to account.attached_files
        return account
        """

    def on_apply(self, _):
        """
        Saves changes done to account.
        """

        # TODO: remove old account from database and accounts list
        #  (use delete_list_item())
        super().on_apply()
