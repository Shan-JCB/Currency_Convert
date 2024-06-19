# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CurrencyConvert.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CurrencyConvert(object):
    def setupUi(self, CurrencyConvert):
        CurrencyConvert.setObjectName("CurrencyConvert")
        CurrencyConvert.resize(324, 165)
        self.lbConvert = QtWidgets.QLabel(CurrencyConvert)
        self.lbConvert.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.lbConvert.setObjectName("lbConvert")
        self.lbTxtResult = QtWidgets.QLabel(CurrencyConvert)
        self.lbTxtResult.setGeometry(QtCore.QRect(190, 40, 47, 13))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lbTxtResult.setFont(font)
        self.lbTxtResult.setObjectName("lbTxtResult")
        self.lbResult = QtWidgets.QLabel(CurrencyConvert)
        self.lbResult.setGeometry(QtCore.QRect(190, 60, 121, 16))
        self.lbResult.setObjectName("lbResult")
        self.ltAmount = QtWidgets.QLineEdit(CurrencyConvert)
        self.ltAmount.setGeometry(QtCore.QRect(70, 10, 113, 20))
        self.ltAmount.setObjectName("ltAmount")
        self.gbFrom = QtWidgets.QGroupBox(CurrencyConvert)
        self.gbFrom.setGeometry(QtCore.QRect(10, 40, 71, 111))
        self.gbFrom.setObjectName("gbFrom")
        self.brFromUS = QtWidgets.QRadioButton(self.gbFrom)
        self.brFromUS.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.brFromUS.setChecked(True)
        self.brFromUS.setObjectName("brFromUS")
        self.brFromUK = QtWidgets.QRadioButton(self.gbFrom)
        self.brFromUK.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.brFromUK.setObjectName("brFromUK")
        self.brFromAUS = QtWidgets.QRadioButton(self.gbFrom)
        self.brFromAUS.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.brFromAUS.setObjectName("brFromAUS")
        self.gbTo = QtWidgets.QGroupBox(CurrencyConvert)
        self.gbTo.setGeometry(QtCore.QRect(100, 40, 71, 111))
        self.gbTo.setObjectName("gbTo")
        self.brToUS = QtWidgets.QRadioButton(self.gbTo)
        self.brToUS.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.brToUS.setChecked(True)
        self.brToUS.setObjectName("brToUS")
        self.brToUK = QtWidgets.QRadioButton(self.gbTo)
        self.brToUK.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.brToUK.setObjectName("brToUK")
        self.brToAUS = QtWidgets.QRadioButton(self.gbTo)
        self.brToAUS.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.brToAUS.setObjectName("brToAUS")
        self.pbConvert = QtWidgets.QPushButton(CurrencyConvert)
        self.pbConvert.setGeometry(QtCore.QRect(190, 100, 75, 23))
        self.pbConvert.setObjectName("pbConvert")
        self.pbExit = QtWidgets.QPushButton(CurrencyConvert)
        self.pbExit.setGeometry(QtCore.QRect(190, 130, 75, 23))
        self.pbExit.setObjectName("pbExit")

        self.retranslateUi(CurrencyConvert)
        QtCore.QMetaObject.connectSlotsByName(CurrencyConvert)

    def retranslateUi(self, CurrencyConvert):
        _translate = QtCore.QCoreApplication.translate
        CurrencyConvert.setWindowTitle(_translate("CurrencyConvert", "Currency Convert"))
        self.lbConvert.setText(_translate("CurrencyConvert", "Convert"))
        self.lbTxtResult.setText(_translate("CurrencyConvert", "Result"))
        self.lbResult.setText(_translate("CurrencyConvert", "0"))
        self.ltAmount.setText(_translate("CurrencyConvert", "0"))
        self.gbFrom.setTitle(_translate("CurrencyConvert", "From"))
        self.brFromUS.setText(_translate("CurrencyConvert", "US$"))
        self.brFromUK.setText(_translate("CurrencyConvert", "UK$"))
        self.brFromAUS.setText(_translate("CurrencyConvert", "AUS$"))
        self.gbTo.setTitle(_translate("CurrencyConvert", "To"))
        self.brToUS.setText(_translate("CurrencyConvert", "US$"))
        self.brToUK.setText(_translate("CurrencyConvert", "UK$"))
        self.brToAUS.setText(_translate("CurrencyConvert", "AUS$"))
        self.pbConvert.setText(_translate("CurrencyConvert", "Convert"))
        self.pbExit.setText(_translate("CurrencyConvert", "Exit"))
