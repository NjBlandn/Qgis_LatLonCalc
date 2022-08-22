# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LatLonCalc
                                 A QGIS plugin
 Conversion de coordenadas en DMS a DD
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-08-21
        copyright            : (C) 2022 by Navir Blandon
        email                : navir.blandn@unah.hn
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LatLonCalc class from file LatLonCalc.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .latloncalc import LatLonCalc
    return LatLonCalc(iface)
