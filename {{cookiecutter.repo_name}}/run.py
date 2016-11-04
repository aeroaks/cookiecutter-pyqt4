#!/usr/bin/env python3

import os
import sys
import glob
import logging
import warnings

from PyQt4 import QtGui

from settings.setup_logging import setup_logging
from {{cookiecutter.package_name}}.main_window import MainWindow

warnings.simplefilter(action="ignore", category=RuntimeWarning)
warnings.simplefilter(action="ignore", category=UserWarning)


def init_logging():
    # setup logging throughout engine

    # setup logging - output to log tab, status message, dialogs
    setup_logging(os.path.join(os.path.abspath(os.path.curdir),
                               'settings\\logging.json'))
    _logger = logging.getLogger(__name__)
    return _logger


def get_version_number():
    # get version number from changelog.rst
    ver_num = ''
    with open('CHANGELOG.rst', 'r') as f:
        for f_line in f.readlines()[::-1]:
            if f_line.startswith('v'):
                ver_num = f_line[1:]
                break

    return ver_num.strip()

if __name__ == "__main__":

    # remove old log files
    for f in glob.glob(os.path.join(os.path.abspath(os.path.curdir), '*.log')):
        os.remove(f)

    _logger = init_logging()
    logging.debug('Starting {} GUI'.format('{{cookiecutter.application_title}}')

    ver_num = get_version_number()

    app = QtGui.QApplication(sys.argv)
    ex = MainWindow(ver_num)
    ex.showMaximized()
    sys.exit(app.exec_())
