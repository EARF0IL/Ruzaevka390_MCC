# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/gui/settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(520, 439)
        self.p_id = QtWidgets.QSpinBox(Dialog)
        self.p_id.setGeometry(QtCore.QRect(360, 160, 42, 21))
        self.p_id.setMinimum(1)
        self.p_id.setObjectName("p_id")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(280, 160, 71, 20))
        self.label.setObjectName("label")
        self.Imp_preset = QtWidgets.QPushButton(Dialog)
        self.Imp_preset.setGeometry(QtCore.QRect(410, 160, 93, 28))
        self.Imp_preset.setObjectName("Imp_preset")
        self.db_buttons = QtWidgets.QButtonGroup(Dialog)
        self.db_buttons.setObjectName("db_buttons")
        self.db_buttons.addButton(self.Imp_preset)
        self.com_select = QtWidgets.QComboBox(Dialog)
        self.com_select.setGeometry(QtCore.QRect(50, 160, 73, 22))
        self.com_select.setObjectName("com_select")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 55, 16))
        self.label_2.setObjectName("label_2")
        self.logo_imp = QtWidgets.QPushButton(Dialog)
        self.logo_imp.setGeometry(QtCore.QRect(10, 200, 121, 31))
        self.logo_imp.setObjectName("logo_imp")
        self.apply = QtWidgets.QPushButton(Dialog)
        self.apply.setGeometry(QtCore.QRect(190, 400, 93, 28))
        self.apply.setObjectName("apply")
        self.SaveButtons = QtWidgets.QButtonGroup(Dialog)
        self.SaveButtons.setObjectName("SaveButtons")
        self.SaveButtons.addButton(self.apply)
        self.ok_exit = QtWidgets.QPushButton(Dialog)
        self.ok_exit.setGeometry(QtCore.QRect(290, 400, 93, 28))
        self.ok_exit.setObjectName("ok_exit")
        self.SaveButtons.addButton(self.ok_exit)
        self.save_preset = QtWidgets.QPushButton(Dialog)
        self.save_preset.setGeometry(QtCore.QRect(390, 400, 121, 28))
        self.save_preset.setObjectName("save_preset")
        self.SaveButtons.addButton(self.save_preset)
        self.exp_db = QtWidgets.QPushButton(Dialog)
        self.exp_db.setGeometry(QtCore.QRect(10, 280, 121, 28))
        self.exp_db.setObjectName("exp_db")
        self.db_buttons.addButton(self.exp_db)
        self.clear_db = QtWidgets.QPushButton(Dialog)
        self.clear_db.setGeometry(QtCore.QRect(10, 320, 121, 28))
        self.clear_db.setObjectName("clear_db")
        self.db_buttons.addButton(self.clear_db)
        self.dataView = QtWidgets.QTableWidget(Dialog)
        self.dataView.setGeometry(QtCore.QRect(10, 10, 501, 141))
        self.dataView.setObjectName("dataView")
        self.dataView.setColumnCount(0)
        self.dataView.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 220, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.db_buttons.addButton(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 260, 231, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.db_buttons.addButton(self.pushButton_2)
        self.path2logo = QtWidgets.QLineEdit(Dialog)
        self.path2logo.setGeometry(QtCore.QRect(10, 240, 251, 31))
        self.path2logo.setObjectName("path2logo")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(260, 190, 281, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройки"))
        self.label.setText(_translate("Dialog", "ID пресета"))
        self.Imp_preset.setText(_translate("Dialog", "Загрузить"))
        self.label_2.setText(_translate("Dialog", "COM:"))
        self.logo_imp.setText(_translate("Dialog", "Загрузить лого"))
        self.apply.setText(_translate("Dialog", "Применить"))
        self.ok_exit.setText(_translate("Dialog", "Ок"))
        self.save_preset.setText(_translate("Dialog", "Сохранить пресет"))
        self.exp_db.setText(_translate("Dialog", "Экспорт БД"))
        self.clear_db.setText(_translate("Dialog", "Очистить БД"))
        self.pushButton.setText(_translate("Dialog", "Удалить"))
        self.pushButton_2.setText(_translate("Dialog", "Восстаноить настройки по умолчанию"))
        self.label_3.setText(_translate("Dialog", "Невозможно удалить записи по индексу 1"))
