"""
main_worker

Author: {{ cookiecutter.full_name }}
Date: {{ cookiecutter.creation_date }}

Main worker for handling processing and threaded communication for GUI
All processing to be done in threads using signal/slot

"""

import logging
import datetime

from PyQt4 import QtCore


class MainWorker(QtCore.QObject):
    """Class for Main Worker

    """

    def __init__(self, main_):
        super().__init__()

        self.main_ = main_

        # external worker modules with threads

        # signals/slots

        # button connection

        logging.debug('worker constructed')

    def init_worker(self):
        logging.debug('initialising worker')

    def close_worker(self):
        # close worker threads and objects
        logging.debug('close worker threads and objects')

    def clear_data(self):
        # clear data on start of tests
        logging.debug('Clearing data')
        # on successfull data clearing return True
        return True

    {% if cookiecutter.insert_statusbar == 'yes' -%}
    def display_status(self, msg, error=False):
        # display message and apply stylesheet based on message type
        if error:
            self.main_.status_bar.setStyleSheet(
                "QStatusBar{padding-left:8px;color:red;font-weight:bold;}")
        else:
            self.main_.status_bar.setStyleSheet(
                "QStatusBar{padding-left:8px;color:black;font-weight:bold;}")

        self.main_.status_bar.showMessage(msg)
    {%- endif %}
