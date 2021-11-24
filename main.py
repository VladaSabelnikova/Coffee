import sys

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QHBoxLayout, QApplication, \
    QMainWindow


class Window(QMainWindow):
    def __init__(
        self
    ):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('coffee.sqlite')
        self.db.open()

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('coffee')
        self.model.select()

        self.data_base.setModel(self.model)

        self.main_layout = QHBoxLayout(self)

        self.main_layout.addWidget(self.data_base)


def main():
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
