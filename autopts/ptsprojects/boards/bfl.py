#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright (c) 2021, Nordic Semiconductor ASA.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
import logging
import os

supported_projects = ['zephyr']

board_type = 'bfl'


def reset_cmd(iutctl):
    """Return reset command for Reel_Board DUT

    Dependency: pyocd command line tools
    """
    return 'pyocd cmd -c reset'