#!/usr/bin/python3

import sys
from PyQt5 import QtWidgets
from hydradev.hydradev import HydraDev
from hydragui.voutgui import VoutGui
import threading

class HydraWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clicks = 0
        self.hydra = HydraDev()

    def initUI(self):
        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        vlayout1 = VoutGui(1)
        self.text = QtWidgets.QLabel("Hello")

        volt1 = QtWidgets.QGroupBox("V1")
        volt1.setLayout(vlayout1.layout)

        self.horizontalLayout.addStretch(1)
        self.horizontalLayout.addWidget(volt1)
        self.horizontalLayout.addStretch(1)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

    def set_voltage1(self):
        self.clicks += 1
        self.text.setText('Text{}'.format(self.clicks))
        v_set = self.v1_set_val.text()
        self.hydra.set_voltage(1, v_set)
        self.v1_set_val.clear()
        current_v = self.hydra.Vout[1].voltage
        self.text.setText('Voltage: {} V'.format(current_v))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = HydraWidget()

    sys.exit(app.exec_())
