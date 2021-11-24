import sys

from PyQt5.QtWidgets import QApplication

from release.main import Window


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def main():
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
