from PyQt5 import QtWidgets
import pandas as pd
import matplotlib.pyplot as plt

class FileDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Grapher")
        self.title_label = QtWidgets.QLabel("Choose the CSV file with data you want to graph", self)
        self.data_format_label = QtWidgets.QLabel("Please ensure your CSV file has columns named 'Year' and 'Population'", self)
        self.open_button = QtWidgets.QPushButton("Open File", self)
        self.open_button.setMinimumSize(100, 50)  # Set minimum size of the button
        self.open_button.clicked.connect(self.open_file)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.data_format_label)
        self.layout.addWidget(self.open_button)
        self.file_path = ""

    def open_file(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","CSV Files (*.csv)", options=options)
        if fileName:
            self.file_path = fileName
            self.accept()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, file_dialog):
        super().__init__()
        self.file_dialog = file_dialog
        if self.file_dialog.exec() == QtWidgets.QDialog.Accepted:
            self.file_path = self.file_dialog.file_path
            self.setWindowTitle("Data Grapher")
            self.plot_button = QtWidgets.QPushButton("Plot", self)
            self.plot_button.setMinimumSize(100, 50)  # Set minimum size of the button
            self.plot_button.clicked.connect(self.plot)
            self.layout = QtWidgets.QGridLayout(self)
            self.layout.setRowStretch(1, 1)
            self.layout.setRowStretch(3, 1)
            self.layout.setColumnStretch(0, 1)
            self.layout.setColumnStretch(2, 1)
            self.layout.addWidget(self.plot_button, 2, 1)
        self.resize(800, 600)  # Set size of the window

    def check_data(self, df):
        required_columns = ['Year', 'Population']
        for column in required_columns:
            if column not in df.columns:
                return False, f"Column '{column}' not found in the CSV file"
            if not pd.api.types.is_numeric_dtype(df[column]):
                return False, f"Column '{column}' should be numeric"
        return True, ""

    def plot(self):
        try:
            df = pd.read_csv(self.file_path)
            is_valid, error_message = self.check_data(df)
            if not is_valid:
                raise ValueError(error_message)
            df.plot(x='Year', y='Population', kind='line')
            plt.show()
        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage(f'An error occurred: {str(e)}')
            error_dialog.exec_()



