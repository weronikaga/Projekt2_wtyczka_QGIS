# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wtyczka_projekt_2_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wtyczka_QGISDialogBase(object):
    def setupUi(self, wtyczka_QGISDialogBase):
        wtyczka_QGISDialogBase.setObjectName("wtyczka_QGISDialogBase")
        wtyczka_QGISDialogBase.resize(743, 529)
        self.button_box = QtWidgets.QDialogButtonBox(wtyczka_QGISDialogBase)
        self.button_box.setGeometry(QtCore.QRect(510, 480, 211, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.Wybierz_warstwe = QtWidgets.QLabel(wtyczka_QGISDialogBase)
        self.Wybierz_warstwe.setGeometry(QtCore.QRect(80, 40, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Wybierz_warstwe.setFont(font)
        self.Wybierz_warstwe.setMouseTracking(False)
        self.Wybierz_warstwe.setObjectName("Wybierz_warstwe")
        self.mMapLayerComboBox = QgsMapLayerComboBox(wtyczka_QGISDialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(400, 40, 261, 31))
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.licz_przewyzszenie = QtWidgets.QPushButton(wtyczka_QGISDialogBase)
        self.licz_przewyzszenie.setGeometry(QtCore.QRect(90, 140, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.licz_przewyzszenie.setFont(font)
        self.licz_przewyzszenie.setObjectName("licz_przewyzszenie")
        self.licz_powierzchnie = QtWidgets.QPushButton(wtyczka_QGISDialogBase)
        self.licz_powierzchnie.setGeometry(QtCore.QRect(90, 200, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.licz_powierzchnie.setFont(font)
        self.licz_powierzchnie.setObjectName("licz_powierzchnie")
        self.wynik = QtWidgets.QTextEdit(wtyczka_QGISDialogBase)
        self.wynik.setGeometry(QtCore.QRect(390, 400, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wynik.setFont(font)
        self.wynik.setObjectName("wynik")
        self.line = QtWidgets.QFrame(wtyczka_QGISDialogBase)
        self.line.setGeometry(QtCore.QRect(0, 120, 741, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(wtyczka_QGISDialogBase)
        self.line_2.setGeometry(QtCore.QRect(360, 130, 20, 181))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.rysuj_poligon = QtWidgets.QPushButton(wtyczka_QGISDialogBase)
        self.rysuj_poligon.setGeometry(QtCore.QRect(90, 260, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rysuj_poligon.setFont(font)
        self.rysuj_poligon.setObjectName("rysuj_poligon")
        self.wyczysc_wyniki = QtWidgets.QPushButton(wtyczka_QGISDialogBase)
        self.wyczysc_wyniki.setGeometry(QtCore.QRect(90, 320, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.wyczysc_wyniki.setFont(font)
        self.wyczysc_wyniki.setObjectName("wyczysc_wyniki")
        self.odznacz_wszystko = QtWidgets.QPushButton(wtyczka_QGISDialogBase)
        self.odznacz_wszystko.setGeometry(QtCore.QRect(90, 380, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.odznacz_wszystko.setFont(font)
        self.odznacz_wszystko.setObjectName("odznacz_wszystko")
        self.wynik_m = QtWidgets.QRadioButton(wtyczka_QGISDialogBase)
        self.wynik_m.setGeometry(QtCore.QRect(550, 210, 95, 20))
        self.wynik_m.setObjectName("wynik_m")
        self.wynik_m2 = QtWidgets.QRadioButton(wtyczka_QGISDialogBase)
        self.wynik_m2.setGeometry(QtCore.QRect(550, 270, 141, 20))
        self.wynik_m2.setObjectName("wynik_m2")
        self.wynik_ha = QtWidgets.QRadioButton(wtyczka_QGISDialogBase)
        self.wynik_ha.setGeometry(QtCore.QRect(550, 330, 141, 20))
        self.wynik_ha.setObjectName("wynik_ha")
        self.wynik_a = QtWidgets.QRadioButton(wtyczka_QGISDialogBase)
        self.wynik_a.setGeometry(QtCore.QRect(550, 300, 141, 20))
        self.wynik_a.setObjectName("wynik_a")
        self.Wybierz_warstwe_2 = QtWidgets.QLabel(wtyczka_QGISDialogBase)
        self.Wybierz_warstwe_2.setGeometry(QtCore.QRect(390, 350, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Wybierz_warstwe_2.setFont(font)
        self.Wybierz_warstwe_2.setObjectName("Wybierz_warstwe_2")
        self.wczytaj_plik = QtWidgets.QPushButton(wtyczka_QGISDialogBase)
        self.wczytaj_plik.setGeometry(QtCore.QRect(20, 460, 201, 51))
        self.wczytaj_plik.setObjectName("wczytaj_plik")
        self.Wybierz_warstwe_3 = QtWidgets.QLabel(wtyczka_QGISDialogBase)
        self.Wybierz_warstwe_3.setGeometry(QtCore.QRect(400, 150, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Wybierz_warstwe_3.setFont(font)
        self.Wybierz_warstwe_3.setObjectName("Wybierz_warstwe_3")
        self.Wybierz_warstwe_4 = QtWidgets.QLabel(wtyczka_QGISDialogBase)
        self.Wybierz_warstwe_4.setGeometry(QtCore.QRect(400, 180, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Wybierz_warstwe_4.setFont(font)
        self.Wybierz_warstwe_4.setObjectName("Wybierz_warstwe_4")
        self.Wybierz_warstwe_5 = QtWidgets.QLabel(wtyczka_QGISDialogBase)
        self.Wybierz_warstwe_5.setGeometry(QtCore.QRect(400, 240, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Wybierz_warstwe_5.setFont(font)
        self.Wybierz_warstwe_5.setObjectName("Wybierz_warstwe_5")
        self.wybierz_pkt = QtWidgets.QPushButton(wtyczka_QGISDialogBase)
        self.wybierz_pkt.setGeometry(QtCore.QRect(400, 80, 261, 31))
        self.wybierz_pkt.setObjectName("wybierz_pkt")

        self.retranslateUi(wtyczka_QGISDialogBase)
        self.button_box.accepted.connect(wtyczka_QGISDialogBase.accept) # type: ignore
        self.button_box.rejected.connect(wtyczka_QGISDialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(wtyczka_QGISDialogBase)

    def retranslateUi(self, wtyczka_QGISDialogBase):
        _translate = QtCore.QCoreApplication.translate
        wtyczka_QGISDialogBase.setWindowTitle(_translate("wtyczka_QGISDialogBase", "projekt_2"))
        self.Wybierz_warstwe.setText(_translate("wtyczka_QGISDialogBase", "Wybierz warstwę "))
        self.licz_przewyzszenie.setText(_translate("wtyczka_QGISDialogBase", "Licz przewyższenie [m]"))
        self.licz_powierzchnie.setText(_translate("wtyczka_QGISDialogBase", "Licz powierzchnię [m^2]"))
        self.rysuj_poligon.setText(_translate("wtyczka_QGISDialogBase", "Rysuj poligon"))
        self.wyczysc_wyniki.setText(_translate("wtyczka_QGISDialogBase", "Wyczyść wyniki "))
        self.odznacz_wszystko.setText(_translate("wtyczka_QGISDialogBase", "Odznacz wszystko"))
        self.wynik_m.setText(_translate("wtyczka_QGISDialogBase", "Wynik w [m]"))
        self.wynik_m2.setText(_translate("wtyczka_QGISDialogBase", "Wynik w [m^2]"))
        self.wynik_ha.setText(_translate("wtyczka_QGISDialogBase", "Wynik w [ha]"))
        self.wynik_a.setText(_translate("wtyczka_QGISDialogBase", "Wynik w [a]"))
        self.Wybierz_warstwe_2.setText(_translate("wtyczka_QGISDialogBase", "Wynik"))
        self.wczytaj_plik.setText(_translate("wtyczka_QGISDialogBase", "Wczytaj plik"))
        self.Wybierz_warstwe_3.setText(_translate("wtyczka_QGISDialogBase", "Wybierz jednostkę wyniku:"))
        self.Wybierz_warstwe_4.setText(_translate("wtyczka_QGISDialogBase", "Przewyższenie:"))
        self.Wybierz_warstwe_5.setText(_translate("wtyczka_QGISDialogBase", "Pole powierzchni:"))
        self.wybierz_pkt.setText(_translate("wtyczka_QGISDialogBase", "Wybierz nowe punkty"))
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wtyczka_QGISDialogBase = QtWidgets.QDialog()
    ui = Ui_wtyczka_QGISDialogBase()
    ui.setupUi(wtyczka_QGISDialogBase)
    wtyczka_QGISDialogBase.show()
    sys.exit(app.exec_())
