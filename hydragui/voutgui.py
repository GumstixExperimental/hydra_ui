from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

class VoutGui(object):
    def __init__(self, Vout_n):
        self.index = Vout_n
        self.layout = QVBoxLayout()

        volt_align = QHBoxLayout()
        volt_align.addWidget(QLabel('Vout:'))
        volt_align.addStretch(1)
        self.voltage = QLineEdit('Vout')
        volt_align.addWidget(self.voltage)
        self.voltage.setDisabled(True)

        amp_align = QHBoxLayout()
        amp_align.addWidget(QLabel('Aout:'))
        amp_align.addStretch(1)
        self.current = QLineEdit('Aout')
        amp_align.addWidget(self.current)
        self.current.setDisabled(True)

        maxA_align = QHBoxLayout()
        maxA_align.addWidget(QLabel('Amax:'))
        maxA_align.addStretch(1)
        self.maxCurrent = QLineEdit('Amax')
        maxA_align.addWidget(self.maxCurrent)
        self.maxCurrent.setDisabled(True)

        self.enabled = QLabel('Enabled')
        self.enabled.setFixedWidth(80)
        self.enabled.setFixedHeight(28)
        self.enabled.setAlignment(Qt.AlignCenter)
        self.enabled.setAutoFillBackground(True)
        self.enabled.setBackgroundRole(QPalette.Base)
        p = self.enabled.palette()
        p.setColor(self.enabled.backgroundRole(), Qt.red)
        self.enabled.setPalette(p)

        setV_align = QHBoxLayout()
        setV_align.addStretch(1)
        setV_align.addWidget(QLabel('Set Voltage:'))
        setV_align.addStretch(1)
        self.setVoltage = QLineEdit()
        self.setVoltage.setFixedWidth(30)
        setV_align.addWidget(self.setVoltage)
        setV_align.addWidget(QLabel('V'))
        setV_align.addStretch(1)

        self.voltageButton = QPushButton('Update Voltage')
        self.voltageButton.setFixedWidth(90)

        self.enableButton = QPushButton('Power')
        self.enableButton.setFixedHeight(40)
        self.enableButton.setFixedWidth(60)

        self.layout.addLayout(volt_align)
        self.layout.addLayout(amp_align)
        self.layout.addLayout(maxA_align)
        self.layout.addWidget(self.enabled, alignment=Qt.AlignCenter)
        self.layout.addStretch(1)
        self.layout.addLayout(setV_align)
        self.layout.addWidget(self.voltageButton, alignment=Qt.AlignCenter)
        self.layout.addStretch(1)
        self.layout.addWidget(self.enableButton, alignment=Qt.AlignCenter)
        self.layout.addStretch(1)
