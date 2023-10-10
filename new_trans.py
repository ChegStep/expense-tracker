# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_trans.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res_new_window

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(409, 300)
        Dialog.setStyleSheet(u"background-color: gray;\n"
"\n"
"font-family: Arial 14;\n"
"font-size: 14")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_new_tr = QLabel(self.frame)
        self.lbl_new_tr.setObjectName(u"lbl_new_tr")
        self.lbl_new_tr.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none\n"
"")
        self.lbl_new_tr.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_new_tr)

        self.combo_category = QComboBox(self.frame)
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.setObjectName(u"cmb_category")
        self.combo_category.setStyleSheet(u"QComboBox {\n"
"font-size: 16px;\n"
"color: white;\n"
"}\n"
"QComboBox:item {\n"
"color: white;\n"
"}")
        self.combo_category.setPlaceholderText(u"\u0412\u044b\u0431\u043e\u0440 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438")

        self.verticalLayout.addWidget(self.combo_category)

        self.date = QDateEdit(self.frame)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")
        self.date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))

        self.verticalLayout.addWidget(self.date)

        self.le_descr = QLineEdit(self.frame)
        self.le_descr.setObjectName(u"le_descr")
        self.le_descr.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 10px")

        self.verticalLayout.addWidget(self.le_descr)

        self.le_balance = QLineEdit(self.frame)
        self.le_balance.setObjectName(u"le_balance")
        self.le_balance.setStyleSheet(u"font-size: 16px;\n"
"color: white;\n"
"padding-left: 10px")

        self.verticalLayout.addWidget(self.le_balance)

        self.combo_income = QComboBox(self.frame)
        self.combo_income.addItem("")
        self.combo_income.addItem("")
        self.combo_income.setObjectName(u"combo_income")
        self.combo_income.setStyleSheet(u"QComboBox {\n"
"font-size: 16px;\n"
"color: white;\n"
"}\n"
"QComboBox:item {\n"
"color: white;\n"
"}")

        self.verticalLayout.addWidget(self.combo_income)

        self.btn_new_tr = QPushButton(self.frame)
        self.btn_new_tr.setObjectName(u"btn_new_tr")
        font = QFont()
        font.setFamilies([u"Arial 14"])
        font.setPointSize(11)
        self.btn_new_tr.setFont(font)
        self.btn_new_tr.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rbga(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 40px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icon/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_tr.setIcon(icon)
        self.btn_new_tr.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_new_tr)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.combo_category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_new_tr.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u0422\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f", None))
        self.combo_category.setItemText(0, QCoreApplication.translate("Dialog", u"\u041f\u043e\u043a\u0443\u043f\u043a\u0438", None))
        self.combo_category.setItemText(1, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0431\u043e\u0442\u0430", None))
        self.combo_category.setItemText(2, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.combo_category.setItemText(3, QCoreApplication.translate("Dialog", u"\u0410\u0432\u0442\u043e", None))
        self.combo_category.setItemText(4, QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0447\u0435\u0435", None))

        self.le_descr.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.le_balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0411\u0430\u043b\u0430\u043d\u0441", None))
        self.combo_income.setItemText(0, QCoreApplication.translate("Dialog", u"\u0414\u043e\u0445\u043e\u0434", None))
        self.combo_income.setItemText(1, QCoreApplication.translate("Dialog", u"\u0417\u0430\u0442\u0440\u0430\u0442\u044b", None))

        self.btn_new_tr.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

