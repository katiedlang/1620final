import sys
from PyQt5 import QtWidgets
from gui import FileDialog, MainWindow

try:
    app = QtWidgets.QApplication(sys.argv)
    file_dialog = FileDialog()
    window = MainWindow(file_dialog)
    window.show()
    sys.exit(app.exec())
except Exception as e:
    print(f'An error occurred: {str(e)}')


