"""
main_window

Author: {{ cookiecutter.full_name }}
Date: {{ cookiecutter.creation_date }}

Main window for {{ cookiecutter.package_name }}
All processing to be done in threads using signal/slot

"""

import os
import json
import logging
import configparser as cp

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt

from {{ cookiecutter.package_name }}.worker.main_worker import MainWorker
from {{ cookiecutter.package_name }}.ui.main_widget import MainWidget
from {{ cookiecutter.package_name }}.ui.dialogs import AboutDialog


class MainWindow(QtGui.QMainWindow):
    """Creates the main window that stores all of the widgets necessary for the application."""

    def __init__(self, ver, parent=None):
        """Initializes the window size and title and instantiates the menu bar and status bar
        if selected by the user."""
        super().__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)  # Prevents an error message about QtTimers.
        # settings: directory, mode etc
        self.setWindowTitle('{{ cookiecutter.application_title }}')
        self.gui_ver = ver

        self.widget = MainWidget(self)
        self.setCentralWidget(self.widget)

        self.worker = MainWorker(self)
        self.worker.init_worker()

        {% if cookiecutter.insert_menubar == 'yes' -%}
        self.menu_bar = self.menuBar()
        self.about_dialog = AboutDialog()

        self.file_menu()
        self.help_menu()
        {%- endif %}
        {% if cookiecutter.insert_statusbar == 'yes' -%}
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Ready', 5000)
        {%- endif %}
        {% if cookiecutter.insert_toolbar == 'yes' -%}
        self.tool_bar_items()
        {%- endif %}

    {% if cookiecutter.insert_toolbar == 'yes' -%}
    def tool_bar_items(self):
        self.tool_bar = QtGui.QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.tool_bar)
        self.tool_bar.setMovable(False)

        open_icon = pkg_resources.resource_filename('{{ cookiecutter.package_name }}.images',
                                                    'ic_open_in_new_black_48dp_1x.png')
        tool_bar_open_action = QtGui.QAction(QIcon(open_icon), 'Open File', self)
        tool_bar_open_action.triggered.connect(self.open_file)

        self.tool_bar.addAction(tool_bar_open_action)
    {%- endif %}

    {% if cookiecutter.insert_statusbar == 'yes' -%}
    def file_menu(self):
        """Create a file submenu with an Open File item that opens a file dialog."""
        self.file_sub_menu = self.menu_bar.addMenu('File')

        self.open_action = QtGui.QAction('Open File', self)
        self.open_action.setStatusTip('Open a file into {{ cookiecutter.application_title }}.')
        self.open_action.setShortcut('CTRL+O')
        self.open_action.triggered.connect(self.open_file)

        self.exit_action = QtGui.QAction('Exit Application', self)
        self.exit_action.setStatusTip('Exit the application.')
        self.exit_action.setShortcut('CTRL+Q')
        self.exit_action.triggered.connect(lambda: QtGui.QApplication.quit())

        self.file_sub_menu.addAction(self.open_action)
        self.file_sub_menu.addAction(self.exit_action)

    def help_menu(self):
        """Create a help submenu with an About item tha opens an about dialog."""
        self.help_sub_menu = self.menu_bar.addMenu('Help')

        self.about_action = QtGui.QAction('About', self)
        self.about_action.setStatusTip('About the application.')
        self.about_action.setShortcut('CTRL+H')
        self.about_action.triggered.connect(lambda: self.about_dialog.exec_())

        self.help_sub_menu.addAction(self.about_action)

    def open_file(self):
        """Open a QFileDialog to allow the user to open a file into the application."""

        file_select_out = QtGui.QFileDialog.getOpenFileName(self, 'Open File')

        # if file dialog used to select a file
        if file_select_out:
            filename, accepted = file_select_out

            if accepted:
                with open(filename) as file:
                    file.read()
    {%- endif %}
