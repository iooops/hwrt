#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Core Library modules
import os

# First party modules
import hwrt.create_model as create_model
import hwrt.utils as utils


def test_execution():
    small = os.path.join(utils.get_project_root(), "models/small-baseline")
    create_model.main(small)


def test_parser():
    create_model.get_parser()
