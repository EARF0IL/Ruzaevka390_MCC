# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\gui\ReqstWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(524, 325)
        self.begin = QtWidgets.QPushButton(Dialog)
        self.begin.setGeometry(QtCore.QRect(10, 280, 241, 41))
        self.begin.setObjectName("begin")
        self.data = QtWidgets.QTextEdit(Dialog)
        self.data.setGeometry(QtCore.QRect(10, 10, 501, 231))
        self.data.setReadOnly(True)
        self.data.setObjectName("data")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 250, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.save2csv = QtWidgets.QPushButton(Dialog)
        self.save2csv.setGeometry(QtCore.QRect(270, 280, 211, 41))
        self.save2csv.setObjectName("save2csv")
        self.delim = QtWidgets.QLineEdit(Dialog)
        self.delim.setGeometry(QtCore.QRect(490, 280, 21, 22))
        self.delim.setObjectName("delim")
        self.info = QtWidgets.QLineEdit(Dialog)
        self.info.setGeometry(QtCore.QRect(10, 250, 281, 22))
        self.info.setFrame(False)
        self.info.setReadOnly(True)
        self.info.setObjectName("info")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Запрос данных"))
        self.begin.setText(_translate("Dialog", "Начать"))
        self.save2csv.setText(_translate("Dialog", "Сохранить в csv"))
        self.delim.setText(_translate("Dialog", ";"))
