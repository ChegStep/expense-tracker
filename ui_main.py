# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pgtram.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res_rc
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(818, 775)
        MainWindow.setStyleSheet(u"background-color: gray;\n"
"\n"
"font-family: Arial 14;\n"
"font-size: 14")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.BalanceFrame = QFrame(self.centralwidget)
        self.BalanceFrame.setObjectName(u"BalanceFrame")
        self.BalanceFrame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px")
        self.verticalLayout = QVBoxLayout(self.BalanceFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.lbl_balance = QLabel(self.BalanceFrame)
        self.lbl_balance.setObjectName(u"lbl_balance")
        font = QFont()
        font.setFamilies([u"Arial 14"])
        font.setPointSize(20)
        font.setBold(True)
        self.lbl_balance.setFont(font)
        self.lbl_balance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none\n"
"")

        self.verticalLayout.addWidget(self.lbl_balance)

        self.now_balance = QLabel(self.BalanceFrame)
        self.now_balance.setObjectName(u"now_balance")
        font1 = QFont()
        font1.setFamilies([u"Arial 14"])
        font1.setPointSize(30)
        font1.setBold(True)
        self.now_balance.setFont(font1)
        self.now_balance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none\n"
"")

        self.verticalLayout.addWidget(self.now_balance)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_income = QLabel(self.BalanceFrame)
        self.icon_income.setObjectName(u"icon_income")
        self.icon_income.setMaximumSize(QSize(24, 16777215))
        self.icon_income.setFont(font)
        self.icon_income.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px")
        self.icon_income.setPixmap(QPixmap(u":/icons/icon/north_west_white_24dp.svg"))

        self.horizontalLayout.addWidget(self.icon_income)

        self.lbl_income_zag = QLabel(self.BalanceFrame)
        self.lbl_income_zag.setObjectName(u"lbl_income_zag")
        font2 = QFont()
        font2.setFamilies([u"Arial 14"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.lbl_income_zag.setFont(font2)
        self.lbl_income_zag.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 18pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;\n"
"")
        self.lbl_income_zag.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lbl_income_zag)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.now_income = QLabel(self.BalanceFrame)
        self.now_income.setObjectName(u"now_income")
        font3 = QFont()
        font3.setFamilies([u"Arial 14"])
        font3.setPointSize(24)
        font3.setBold(True)
        self.now_income.setFont(font3)
        self.now_income.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 24pt;\n"
"background-color: none;\n"
"border: none\n"
"")

        self.verticalLayout.addWidget(self.now_income)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icon_outcome = QLabel(self.BalanceFrame)
        self.icon_outcome.setObjectName(u"icon_outcome")
        self.icon_outcome.setMaximumSize(QSize(24, 16777215))
        self.icon_outcome.setFont(font)
        self.icon_outcome.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px")
        self.icon_outcome.setPixmap(QPixmap(u":/icons/icon/call_received_white_24dp.svg"))

        self.horizontalLayout_2.addWidget(self.icon_outcome)

        self.lbl_outcome_zag = QLabel(self.BalanceFrame)
        self.lbl_outcome_zag.setObjectName(u"lbl_outcome_zag")
        self.lbl_outcome_zag.setFont(font2)
        self.lbl_outcome_zag.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 18pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px\n"
"")

        self.horizontalLayout_2.addWidget(self.lbl_outcome_zag)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.now_outcome = QLabel(self.BalanceFrame)
        self.now_outcome.setObjectName(u"now_outcome")
        self.now_outcome.setFont(font3)
        self.now_outcome.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 24pt;\n"
"background-color: none;\n"
"border: none\n"
"")

        self.verticalLayout.addWidget(self.now_outcome)


        self.horizontalLayout_7.addWidget(self.BalanceFrame)

        self.CategoriesFrame2 = QFrame(self.centralwidget)
        self.CategoriesFrame2.setObjectName(u"CategoriesFrame2")
        self.CategoriesFrame2.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px")
        self.CategoriesFrame = QVBoxLayout(self.CategoriesFrame2)
        self.CategoriesFrame.setObjectName(u"CategoriesFrame")
        self.lbl_category_zag = QLabel(self.CategoriesFrame2)
        self.lbl_category_zag.setObjectName(u"lbl_category_zag")
        self.lbl_category_zag.setFont(font)
        self.lbl_category_zag.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none\n"
"")

        self.CategoriesFrame.addWidget(self.lbl_category_zag)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_10 = QLabel(self.CategoriesFrame2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(24, 16777215))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.label_10.setPixmap(QPixmap(u":/icons/icon/local_grocery_store_white_24dp.svg"))

        self.horizontalLayout_3.addWidget(self.label_10)

        self.lbl_pokupki = QLabel(self.CategoriesFrame2)
        self.lbl_pokupki.setObjectName(u"lbl_pokupki")
        font4 = QFont()
        font4.setFamilies([u"Arial 14"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.lbl_pokupki.setFont(font4)
        self.lbl_pokupki.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.lbl_pokupki)

        self.summ_pokupki = QLabel(self.CategoriesFrame2)
        self.summ_pokupki.setObjectName(u"summ_pokupki")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(20)
        font5.setBold(False)
        font5.setItalic(False)
        self.summ_pokupki.setFont(font5)
        self.summ_pokupki.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-family: Segoe UI")

        self.horizontalLayout_3.addWidget(self.summ_pokupki)


        self.CategoriesFrame.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_15 = QLabel(self.CategoriesFrame2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(24, 16777215))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.label_15.setPixmap(QPixmap(u":/icons/icon/sports_esports_white_24dp.svg"))

        self.horizontalLayout_4.addWidget(self.label_15)

        self.lbl_razvl = QLabel(self.CategoriesFrame2)
        self.lbl_razvl.setObjectName(u"lbl_razvl")
        self.lbl_razvl.setFont(font4)
        self.lbl_razvl.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.lbl_razvl)

        self.summ_razvl = QLabel(self.CategoriesFrame2)
        self.summ_razvl.setObjectName(u"summ_razvl")
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(20)
        font6.setBold(False)
        self.summ_razvl.setFont(font6)
        self.summ_razvl.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-family: Segoe UI")

        self.horizontalLayout_4.addWidget(self.summ_razvl)


        self.CategoriesFrame.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_18 = QLabel(self.CategoriesFrame2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(24, 16777215))
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.label_18.setPixmap(QPixmap(u":/icons/icon/directions_car_white_24dp.svg"))

        self.horizontalLayout_5.addWidget(self.label_18)

        self.lbl_auto = QLabel(self.CategoriesFrame2)
        self.lbl_auto.setObjectName(u"lbl_auto")
        self.lbl_auto.setFont(font4)
        self.lbl_auto.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.lbl_auto)

        self.summ_auto = QLabel(self.CategoriesFrame2)
        self.summ_auto.setObjectName(u"summ_auto")
        self.summ_auto.setFont(font6)
        self.summ_auto.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-family: Segoe UI")

        self.horizontalLayout_5.addWidget(self.summ_auto)


        self.CategoriesFrame.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_21 = QLabel(self.CategoriesFrame2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(24, 16777215))
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.label_21.setPixmap(QPixmap(u":/icons/icon/list_white_24dp.svg"))

        self.horizontalLayout_6.addWidget(self.label_21)

        self.lbl_other = QLabel(self.CategoriesFrame2)
        self.lbl_other.setObjectName(u"lbl_other")
        self.lbl_other.setFont(font4)
        self.lbl_other.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.lbl_other)

        self.summ_other = QLabel(self.CategoriesFrame2)
        self.summ_other.setObjectName(u"summ_other")
        self.summ_other.setFont(font6)
        self.summ_other.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-family: Segoe UI")

        self.horizontalLayout_6.addWidget(self.summ_other)


        self.CategoriesFrame.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addWidget(self.CategoriesFrame2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_add_tr = QPushButton(self.centralwidget)
        self.btn_add_tr.setObjectName(u"btn_add_tr")
        font7 = QFont()
        font7.setFamilies([u"Arial 14"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.btn_add_tr.setFont(font7)
        self.btn_add_tr.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/icons/icon/sports_esports_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_tr.setIcon(icon)
        self.btn_add_tr.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_add_tr)

        self.btn_edit_tr = QPushButton(self.centralwidget)
        self.btn_edit_tr.setObjectName(u"btn_edit_tr")
        self.btn_edit_tr.setFont(font7)
        self.btn_edit_tr.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/edit_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_tr.setIcon(icon1)
        self.btn_edit_tr.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_edit_tr)

        self.btn_del_tr = QPushButton(self.centralwidget)
        self.btn_del_tr.setObjectName(u"btn_del_tr")
        self.btn_del_tr.setFont(font7)
        self.btn_del_tr.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_del_tr.setIcon(icon2)
        self.btn_del_tr.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_del_tr)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFont(font4)
        self.tableView.setStyleSheet(u"QTableView {\n"
                                     "background-color: rgba(255, 255, 255, 30); \n"
                                     "border: 1px solid rgba(255,255,255,40);\n"
                                     "border-bottom-right-radius: 7px; \n"
                                     "border-bottom-left-radius: 7px; \n"
                                     "color: white;\n"
                                     "}\n"
                                     "\n"
                                     "QHeaderView::section {\n"
                                     "background-color: rgb(53, 53, 53);\n"
                                     "color: white;\n"
                                     "border: none;\n"
                                     "height: 50px;\n"
                                     "font-size: 16pt;\n"
                                     "}\n"
                                     "\n"
                                     "QTableView::item {\n"
                                     "    border-style: none;\n"
                                     "    border-bottom: 1px solid rgba(255,255,255,50);\n"
                                     "}\n"
                                     "\n"
                                     "QTableView::item:selected{\n"
                                     "	border: none;\n"
                                     "	color: rgb(255, 255, 255);\n"
                                     "    background-color: rgba(255, 255, 255, 50);\n"
                                     "}\n"
                                     "")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Трекер расходов", None))
        self.lbl_balance.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0411\u0430\u043b\u0430\u043d\u0441", None))
        self.now_balance.setText(QCoreApplication.translate("MainWindow", u"120₽", None))
        self.icon_income.setText("")
        self.lbl_income_zag.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434:", None))
        self.now_income.setText(QCoreApplication.translate("MainWindow", u"120₽", None))
        self.icon_outcome.setText("")
        self.lbl_outcome_zag.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434:", None))
        self.now_outcome.setText(QCoreApplication.translate("MainWindow", u"120₽", None))
        self.lbl_category_zag.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_10.setText("")
        self.lbl_pokupki.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0443\u043f\u043a\u0438", None))
        self.summ_pokupki.setText(QCoreApplication.translate("MainWindow", u"100₽", None))
        self.label_15.setText("")
        self.lbl_razvl.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.summ_razvl.setText(QCoreApplication.translate("MainWindow", u"100₽", None))
        self.label_18.setText("")
        self.lbl_auto.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e", None))
        self.summ_auto.setText(QCoreApplication.translate("MainWindow", u"100₽", None))
        self.label_21.setText("")
        self.lbl_other.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0447\u0435\u0435", None))
        self.summ_other.setText(QCoreApplication.translate("MainWindow", u"100₽", None))
        self.btn_add_tr.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0442\u0440\u0430\u043d\u0437.", None))
        self.btn_edit_tr.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u0440\u0430\u043d\u0437.", None))
        self.btn_del_tr.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u0440\u0430\u043d\u0437.", None))
    # retranslateUi

