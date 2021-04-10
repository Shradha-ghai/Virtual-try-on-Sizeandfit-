#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""__init__ module for configs. Register your config file here by adding it's
entry in the CONFIG_MAP as shown.
"""
import sys
sys.path.append('.')

import camvid_resnet50
import human_parsing_resnet50


CONFIG_MAP = {
    'camvid_resnet50': camvid_resnet50.CONFIG,
    'human_parsing_resnet50': human_parsing_resnet50.CONFIG
}
