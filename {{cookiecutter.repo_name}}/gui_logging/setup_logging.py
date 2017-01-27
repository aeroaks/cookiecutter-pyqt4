#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup logging for the Module

Read configs from json file
"""

import os
import json
import logging.config


def setup_logging(default_path='settings/logging.json',
                  default_level=logging.DEBUG,
                  env_key='LOG_CFG'):
    """Setup logging configuration
    """
    path = default_path

    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
