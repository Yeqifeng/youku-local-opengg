# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      weiyc
#
# Created:     16/01/2013
# Copyright:   (c) weiyc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#run cmd python setup.py build
import sys

from cx_Freeze import setup, Executable

base = None
#if sys.platform == "win32":
#    base = "Win32GUI"

setup(
        name = "weiyc",
        version = "0.1",
        description = "local youku",
        executables = [Executable("youkuv.py", base = base)])
