# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'red_wine.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1093, 1087)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 0, 441, 51))
        self.label.setStyleSheet("color:rgb(255, 0, 0);\n"
"font: 75 italic 20pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 60, 181, 51))
        self.label_2.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 italic 20pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 130, 231, 51))
        self.label_3.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 italic 20pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(160, 200, 181, 51))
        self.label_4.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 italic 20pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 260, 251, 51))
        self.label_5.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 italic 20pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(160, 330, 181, 51))
        self.label_6.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 italic 20pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 400, 311, 51))
        self.label_7.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 italic 20pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 470, 301, 51))
        self.label_8.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 italic 20pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(170, 540, 131, 51))
        self.label_9.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 italic 20pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(130, 680, 161, 51))
        self.label_10.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 italic 20pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(160, 750, 121, 51))
        self.label_11.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 italic 20pt \"Arial\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(150, 610, 161, 51))
        self.label_12.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 italic 20pt \"Arial\";")
        self.label_12.setObjectName("label_12")
        self.lineEdit_fa = QtWidgets.QLineEdit(Form)
        self.lineEdit_fa.setGeometry(QtCore.QRect(340, 70, 431, 41))
        self.lineEdit_fa.setObjectName("lineEdit_fa")
        self.lineEdit_va = QtWidgets.QLineEdit(Form)
        self.lineEdit_va.setGeometry(QtCore.QRect(340, 140, 431, 41))
        self.lineEdit_va.setObjectName("lineEdit_va")
        self.lineEdit_ca = QtWidgets.QLineEdit(Form)
        self.lineEdit_ca.setGeometry(QtCore.QRect(340, 200, 431, 41))
        self.lineEdit_ca.setObjectName("lineEdit_ca")
        self.lineEdit_rs = QtWidgets.QLineEdit(Form)
        self.lineEdit_rs.setGeometry(QtCore.QRect(340, 260, 431, 41))
        self.lineEdit_rs.setObjectName("lineEdit_rs")
        self.lineEdit_c = QtWidgets.QLineEdit(Form)
        self.lineEdit_c.setGeometry(QtCore.QRect(340, 330, 431, 41))
        self.lineEdit_c.setObjectName("lineEdit_c")
        self.lineEdit_fsd = QtWidgets.QLineEdit(Form)
        self.lineEdit_fsd.setGeometry(QtCore.QRect(340, 410, 431, 41))
        self.lineEdit_fsd.setObjectName("lineEdit_fsd")
        self.lineEdit_tsd = QtWidgets.QLineEdit(Form)
        self.lineEdit_tsd.setGeometry(QtCore.QRect(340, 480, 431, 41))
        self.lineEdit_tsd.setObjectName("lineEdit_tsd")
        self.lineEdit_d = QtWidgets.QLineEdit(Form)
        self.lineEdit_d.setGeometry(QtCore.QRect(340, 550, 431, 41))
        self.lineEdit_d.setObjectName("lineEdit_d")
        self.lineEdit_ph = QtWidgets.QLineEdit(Form)
        self.lineEdit_ph.setGeometry(QtCore.QRect(340, 610, 431, 41))
        self.lineEdit_ph.setObjectName("lineEdit_ph")
        self.lineEdit_s = QtWidgets.QLineEdit(Form)
        self.lineEdit_s.setGeometry(QtCore.QRect(340, 690, 431, 41))
        self.lineEdit_s.setObjectName("lineEdit_s")
        self.lineEdit_a = QtWidgets.QLineEdit(Form)
        self.lineEdit_a.setGeometry(QtCore.QRect(340, 760, 431, 41))
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(870, 230, 191, 51))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(85, 255, 0);\n"
"font: 75 italic 18pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.qul = QtWidgets.QLabel(Form)
        self.qul.setGeometry(QtCore.QRect(850, 430, 231, 51))
        self.qul.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 18pt \"Arial\";")
        self.qul.setObjectName("qul")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Predict red wine quality types"))
        self.label_2.setText(_translate("Form", "Fixed Acid:"))
        self.label_3.setText(_translate("Form", "volatile acidity:"))
        self.label_4.setText(_translate("Form", "Citric Acid:"))
        self.label_5.setText(_translate("Form", "Residual Sugar:"))
        self.label_6.setText(_translate("Form", "Chlorides:"))
        self.label_7.setText(_translate("Form", "Free Sulfur dioxide:"))
        self.label_8.setText(_translate("Form", "Total sulfur dioxide:"))
        self.label_9.setText(_translate("Form", "Density:"))
        self.label_10.setText(_translate("Form", "Sulphates:"))
        self.label_11.setText(_translate("Form", "Alcohol:"))
        self.label_12.setText(_translate("Form", "pH Value:"))
        self.pushButton.setText(_translate("Form", "Predict"))
        self.qul.setText(_translate("Form", "Quality"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
