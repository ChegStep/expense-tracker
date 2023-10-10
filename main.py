import sys
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QDate
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel
from ui_main import Ui_MainWindow
from new_trans import Ui_Dialog
from connection import Data
import datetime

class ExpeenseTracker(QMainWindow):
    def __init__(self):
        super(ExpeenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()
        self.reload_data()
        self.setWindowIcon(QIcon('icon/logo.png'))
        self.ui.btn_add_tr.clicked.connect(self.open_new_trans_window)
        self.ui.btn_edit_tr.clicked.connect(self.open_new_trans_window)
        self.ui.btn_del_tr.clicked.connect(self.del_current_trans)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('expenses')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def reload_data(self):
        self.ui.now_balance.setText(self.conn.total_balance())
        self.ui.now_income.setText(self.conn.total_income())
        self.ui.now_outcome.setText(self.conn.total_outcome())
        self.ui.summ_pokupki.setText(self.conn.total_pokipki())
        self.ui.summ_razvl.setText(self.conn.total_razvl())
        self.ui.summ_auto.setText(self.conn.total_auto())
        self.ui.summ_other.setText(self.conn.total_other())

    def open_new_trans_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == 'Новая транз.':
            self.ui_window.date.setDate(datetime.datetime.now())
            self.ui_window.btn_new_tr.clicked.connect(self.add_new_trans)
        else:
            model = self.ui.tableView.model()
            data = []
            rows = sorted(set(index1.row() for index1 in
                              self.ui.tableView.selectedIndexes()))
            for column in range(model.columnCount()):
                index1 = model.index(rows[0], column)
                data.append(str(model.data(index1)))
            dt = list(map(int, data[1].split('.')))
            self.ui_window.date.setDate(QDate(dt[2], dt[1], dt[0]))
            self.ui_window.combo_category.setCurrentIndex(self.ui_window.combo_category.findText(data[2]))
            self.ui_window.le_descr.setText(data[3])
            self.ui_window.le_balance.setText(data[4])
            self.ui_window.combo_income.setCurrentIndex(self.ui_window.combo_income.findText(data[5]))
            self.ui_window.btn_new_tr.clicked.connect(self.edit_current_trans)

    def add_new_trans(self):
        date = self.ui_window.date.text()
        category = self.ui_window.combo_category.currentText()
        description = self.ui_window.le_descr.text()
        balance = self.ui_window.le_balance.text()
        status = self.ui_window.combo_income.currentText()

        self.conn.add_new_trans_query(date, category, description, balance, status)

        self.view_data()
        self.reload_data()
        self.new_window.close()

    def edit_current_trans(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        date = self.ui_window.date.text()
        category = self.ui_window.combo_category.currentText()
        description = self.ui_window.le_descr.text()
        balance = self.ui_window.le_balance.text()
        status = self.ui_window.combo_income.currentText()

        self.conn.update_trans_query(date, category, description, balance, status, id)

        self.view_data()
        self.reload_data()
        self.new_window.close()

    def del_current_trans(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        self.conn.del_trans_query(id)
        self.view_data()
        self.reload_data()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpeenseTracker()
    window.show()
    sys.exit(app.exec())
