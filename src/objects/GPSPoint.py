# -*- coding: utf-8 -*-
"""
__source__ : 
__author__ : Michele Trevisiol @trevi
"""

import sys

class GPSPoint:

    def __init__(self, coo, pointType='WGS84'):
        self.type = pointType
        self.lat = float(coo[0])
        self.lng = float(coo[1])

    """ Convert WGS84 in meters
    """
    def getMeters(self, val, field):
        return -1