from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QDialog,
    QFormLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QWidget)
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Slot
import sys
import ast

from ui_mainwindow import Ui_DrawRouteApp


def convert_string_array(string_array, mode):
    try:
        array = ast.literal_eval(string_array)
        
        if (type(array) is not list) and (type(array) is not tuple):
            raise SyntaxError()
        
        if mode == "one_route":
            for element in array:
                if (type(element) is not list) and (type(element) is not tuple):
                    raise SyntaxError()
                if len(element) != 2:
                    raise ValueError()
                for value in element:
                    if (type(value) is not int) and (type(value) is not float):
                        raise SyntaxError()
        
        if mode == "multiple_routes":
            for item in array:
                if (type(item) is not list) and (type(item) is not tuple):
                        raise SyntaxError()
                for element in item:
                    if (type(element) is not list) and (type(element) is not tuple):
                        raise SyntaxError()
                    if len(element) != 2:
                        raise ValueError()
                    for value in element:
                        if (type(value) is not int) and (type(value) is not float):
                            raise SyntaxError()
        return array
    
    except:
        print("Invalid syntax")
        return None

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_DrawRouteApp()
        self.ui.setupUi(self)
        
        self.ui.dateTimeEdit.hide()
        self.ui.coordinates_text.setText("[(), ()]")
        
        self.ui.submit_button.clicked.connect(self.submit)
        self.ui.one_route_radio.clicked.connect(self.show_additional_one) 
        self.ui.multiple_routes_radio.clicked.connect(self.hide_additional_multiple)
        self.ui.travel_time_checkbox.clicked.connect(self.hide_show_datetime)

    @Slot()
    def hide_show_datetime(self):
        if self.ui.travel_time_checkbox.isChecked():
            self.ui.dateTimeEdit.show()
        else: 
            self.ui.dateTimeEdit.hide()
    
    @Slot()
    def hide_additional_multiple(self):
        coordinates = self.ui.coordinates_text.text()
        if coordinates.strip() == "[(), ()]"\
            or (coordinates.strip() == ""):
            self.ui.coordinates_text.setText("[[(), ()], [(), ()]]")
        self.ui.one_route_widget.hide()
    
    @Slot()
    def show_additional_one(self):
        coordinates = self.ui.coordinates_text.text()
        if (coordinates.strip() == "[[(), ()], [(), ()]]")\
            or (coordinates.strip() == ""):
            self.ui.coordinates_text.setText("[(), ()]")
        self.ui.one_route_widget.show()

    @Slot()
    def submit(self):
        self.ui.submit_button.setEnabled(False)
        coordinates = self.ui.coordinates_text.text()
        
        if self.ui.one_route_radio.isChecked():
            mode = "one_route"
        if self.ui.multiple_routes_radio.isChecked():
            mode = "multiple_routes"
        
        search_organizations = self.ui.organizations_checkbox.isChecked()
        predict_travel_time = self.ui.travel_time_checkbox.isChecked()
        date_time = None
        if predict_travel_time:
            date_time = self.ui.dateTimeEdit.dateTime().toPython()
        
        coordinates = convert_string_array(coordinates.strip(), mode)
        
        print(coordinates, mode, search_organizations, predict_travel_time, date_time)
        
        self.ui.submit_button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())