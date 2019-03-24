"""Ejemplos para utilizar strftime con datetime."""
# -*- coding: utf-8 -*-

from datetime import datetime

date1 = datetime(2011, 4, 23, 12, 22, 3)

date2 = datetime(2015, 1, 2, 8, 20, 13)

print date1.strftime("%b %d %Y %H:%M:%S")

print date2.strftime("%d del %m del año %Y")
