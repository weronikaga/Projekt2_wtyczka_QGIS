# -*- coding: utf-8 -*-
"""
/***************************************************************************
 wtyczka_QGISDialog
                                 A QGIS plugin
 Wtyczka do obliczeń na wybranej warstwie
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-04
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Weronika_Garbacz/Emilia_Bartnik
        email                : 01179134@pw.edu.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import Qgis, QgsProject, QgsWkbTypes, QgsPointXY
from qgis.utils import iface

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'wtyczka_projekt_2_dialog_base.ui'))


class wtyczka_QGISDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(wtyczka_QGISDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.licz_przewyzszenie.clicked.connect(self.calculate_dh)
        self.licz_powierzchnie.clicked.connect(self.pole)

        
    def calculate_dh(self):
        selected_layer = self.mMapLayerComboBox.selectedLayer()
        if not selected_layer:
            iface.message().pushMessageBar('Błąd - Nie wybrano warstwy', level=Qgis.Warning)
            return
        features = selected_layer.selectedFeatures()
        if len(features) != 2:
            iface.message().pushMessageBar('Błąd - Należy wybrać dokładnie dwa punkty', level=Qgis.Warning)
            return
        try:
            h_1 = float(features[0]['wysokosc'])
            h_2 = float(features[1]['wysokosc'])
        except KeyError:
            iface.message().pushMessageBar('Bład - Brak atrybuty "wysokosc" przy wybranych punktach', level=Qgis.Warning)
            return
        
        dh = round(h_2 - h_1, 3)
        self.wynik.setText(f'{dh} m')
        iface.messageBar().pushMessage("Różnica wysokoci", f"Różnica wysokoci między wybranymi punktami wynosi:{dh}")
        
        
        
    # def calculate_area(self):
    #     selected_layer = self.mMapLayerComboBox.currentLayer()
    #     features = selected_layer.selectedFeatures()
    #     x = float(features[0]['wysokosc'])
    #     y = float(features[1]['wysokosc'])
        
        
    def punkty(self):
        self.label_error.clear()
        selected_features = self.mMapLayerComboBox.selectedLayer().selectedFeatures()
        pkt = []
        for feature in selected_features:
            feature_geometry = feature.geometry().asPoint()
            x = feature_geometry[0]
            y = feature_geometry[1]
            pkt.append([float(x), float(y)])
        
        pkt = self.sortuj_punkty(pkt)
        return pkt
        
    def pole(self):
        selected_layer = self.mMapLayerComboBox.currentLayer()
        if not selected_layer:
            iface.message().pushMessageBar('Błąd - Nie wybrano warstwy', level=Qgis.Warning)
            return
        features = selected_layer.selectedFeatures()
        if len(features) < 3:
            iface.message().pushMessageBar('Błąd - Należy wybrać dokładnie 3 punkty', level=Qgis.Warning)
            return
        selected_features = self.mMapLayerComboBox.currentLayer().selectedFeatures()
        
        pkt = []
        id_pkt = []
        for feature in selected_features:
            feature_geometry = feature.geometry()
            if feature_geometry.isEmpty() or QgsWkbTypes.geometryType(feature_geometry.wkbType()) != QgsWkbTypes.PointGeometry:
                iface.messageBar().pushMessage("Błąd - Wybrany obiekt nie jest punktem", level=Qgis.Warning)
                return
            punkt = feature_geometry.asPoint()
            pkt.append(QgsPointXY(punkt.x(), punkt.y()))
            id_pkt.append(feature.id())
        pole = self.gauss(pkt)
        iface.messageBar().pushMessage("Wynik", f"Powierzchnia wielokąta o wierzchołkach w punktach wynosi: {pole}", level=Qgis.Success)
        self.wynik.setText("{:.3f} m^2".format(pole))
        
    def gauss(self, pkt):
        n = len(pkt)
        pole = 0.0
        
        for i in range(n):
            x1, y1 = pkt[i].x(), pkt[i].y()
            x2, y2 = pkt[(i + 1) % n].x(), pkt[(i + 1) % n].y()
            pole += x1 * y2 - x2 * y1
        return abs(pole) / 2