from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, \
    QLabel, QPushButton


class Dialogs(QDialog):
    def dialog_update_add(
        self, id='0', name='Кофе', roasting='little',
        type='ground', description='Пока ничего', price='0', volume='100'
    ):
        dialog = QDialog()
        main_layout = QVBoxLayout(dialog)
        elem_layout_1 = QHBoxLayout()
        elem_layout_2 = QHBoxLayout()
        elem_layout_3 = QHBoxLayout()
        elem_layout_4 = QHBoxLayout()
        elem_layout_5 = QHBoxLayout()
        elem_layout_6 = QHBoxLayout()
        elem_layout_7 = QHBoxLayout()

        id_input = QLineEdit()
        id_input.setText(id)
        id_label = QLabel('id')

        name_input = QLineEdit()
        name_input.setText(name)
        name_label = QLabel('name')

        roasting_input = QLineEdit()
        roasting_input.setText(roasting)
        roasting_label = QLabel('roasting')

        type_input = QLineEdit()
        type_input.setText(type)
        type_label = QLabel('type')

        description_input = QLineEdit()
        description_input.setText(description)
        description_label = QLabel('description')

        price_input = QLineEdit()
        price_input.setText(price)
        price_label = QLabel('price')

        volume_input = QLineEdit()
        volume_input.setText(volume)
        volume_label = QLabel('volume')

        button_exit = QPushButton('Сохранить')
        button_exit.clicked.connect(dialog.accept)

        elem_layout_1.addWidget(id_label)
        elem_layout_1.addWidget(id_input)

        elem_layout_2.addWidget(name_label)
        elem_layout_2.addWidget(name_input)

        elem_layout_3.addWidget(roasting_label)
        elem_layout_3.addWidget(roasting_input)

        elem_layout_4.addWidget(type_label)
        elem_layout_4.addWidget(type_input)

        elem_layout_5.addWidget(description_label)
        elem_layout_5.addWidget(description_input)

        elem_layout_6.addWidget(price_label)
        elem_layout_6.addWidget(price_input)

        elem_layout_7.addWidget(volume_label)
        elem_layout_7.addWidget(volume_input)

        main_layout.addLayout(elem_layout_1)
        main_layout.addLayout(elem_layout_2)
        main_layout.addLayout(elem_layout_3)
        main_layout.addLayout(elem_layout_4)
        main_layout.addLayout(elem_layout_5)
        main_layout.addLayout(elem_layout_6)
        main_layout.addLayout(elem_layout_7)
        main_layout.addWidget(button_exit)

        if dialog.exec_():
            return id_input.text(),\
                   name_input.text(),\
                   roasting_input.text(),\
                   type_input.text(), \
                   description_input.text(),\
                   price_input.text(),\
                   volume_input.text()
        else:
            return None
