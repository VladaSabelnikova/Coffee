import sqlite3

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow

from UI.addEditCoffeeForm import Dialogs
from UI.main_ui import Ui_MainWindow


class Window(QMainWindow, Dialogs, Ui_MainWindow):
    def __init__(
        self
    ):
        super().__init__()
        self.setupUi(self)
        self.display_db()

    def display_db(self):
        self.button_1.clicked.connect(self.add_base)
        self.button_2.clicked.connect(self.update_base)
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('../data/coffee.sqlite')
        self.db.open()

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('coffee')
        self.model.select()

        self.data_base.setModel(self.model)

        self.main_layout = QHBoxLayout(self)

        self.main_layout.addWidget(self.data_base)

    def add_base(self):
        data = self.dialog_update_add()
        if not data:
            return
        id, name, roasting, type, description, price, volume = data
        con = sqlite3.connect('../data/coffee.sqlite')
        cur = con.cursor()
        insert_into = f'INSERT INTO ' \
                      f'coffee(id, name, roasting, type, description, ' \
                      f'price, volume' \
                      f') ' \
                      f'VALUES(' \
                      f'{id},' \
                      f'"{name}",' \
                      f' "{roasting}", ' \
                      f'"{type}", ' \
                      f'"{description}", ' \
                      f'{price}, ' \
                      f'{volume})'

        self.db.close()
        cur.execute(insert_into)
        con.commit()
        con.close()
        self.display_db()

    def update_base(self):
        row = self.data_base.currentIndex().row()
        col = self.data_base.currentIndex().column()
        if row >= 0 and col >= 0:
            id = str(self.model.index(row, 0).data())
            name = self.model.index(row, 1).data()
            roasting = self.model.index(row, 2).data()
            type = self.model.index(row, 3).data()
            description = self.model.index(row, 4).data()
            price = str(self.model.index(row, 5).data())
            volume = str(self.model.index(row, 6).data())

            data = self.dialog_update_add(id, name, roasting, type,
                                          description, price, volume)
            id, name, roasting, type, description, price, volume = data

            con = sqlite3.connect('../data/coffee.sqlite')
            cur = con.cursor()

            update_1 = f'UPDATE coffee SET id = {id} WHERE id = {id}'
            self.db.close()
            cur.execute(update_1)
            con.commit()

            update_2 = f'UPDATE coffee SET name = "{name}" WHERE id = {id}'
            cur.execute(update_2)
            con.commit()

            update_3 = f'UPDATE coffee ' \
                       f'SET roasting = "{roasting}" ' \
                       f'WHERE id = {id}'
            cur.execute(update_3)
            con.commit()

            update_4 = f'UPDATE coffee ' \
                       f'SET type = "{type}" ' \
                       f'WHERE id = {id}'
            cur.execute(update_4)
            con.commit()

            update_5 = f'UPDATE coffee ' \
                       f'SET description = "{description}" ' \
                       f'WHERE id = {id}'
            cur.execute(update_5)
            con.commit()

            update_6 = f'UPDATE coffee SET price = {price} WHERE id =' \
                       f' {id}'
            cur.execute(update_6)
            con.commit()

            update_7 = f'UPDATE coffee SET volume = {volume} WHERE id =' \
                       f' {id}'
            cur.execute(update_7)
            con.commit()
            con.close()
            self.display_db()
