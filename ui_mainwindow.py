# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DrawRouteAppRCRGYX.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QDialog,
    QFormLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_DrawRouteApp(object):
    def setupUi(self, DrawRouteApp):
        if not DrawRouteApp.objectName():
            DrawRouteApp.setObjectName(u"DrawRouteApp")
        DrawRouteApp.resize(939, 510)
        DrawRouteApp.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.formLayoutWidget = QWidget(DrawRouteApp)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 70, 841, 344))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_2)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.label_5)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.label_7)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.label_8)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.label_3)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label)

        self.coordinates_text = QLineEdit(self.formLayoutWidget)
        self.coordinates_text.setObjectName(u"coordinates_text")
        self.coordinates_text.setClearButtonEnabled(True)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.coordinates_text)

        self.one_route_radio = QRadioButton(self.formLayoutWidget)
        self.one_route_radio.setObjectName(u"one_route_radio")
        self.one_route_radio.setEnabled(True)
        self.one_route_radio.setChecked(True)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.one_route_radio)

        self.multiple_routes_radio = QRadioButton(self.formLayoutWidget)
        self.multiple_routes_radio.setObjectName(u"multiple_routes_radio")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.multiple_routes_radio)

        self.submit_button = QPushButton(self.formLayoutWidget)
        self.submit_button.setObjectName(u"submit_button")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.submit_button)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.label_6)

        self.one_route_widget = QWidget(self.formLayoutWidget)
        self.one_route_widget.setObjectName(u"one_route_widget")
        self.one_route_layout = QVBoxLayout(self.one_route_widget)
        self.one_route_layout.setObjectName(u"one_route_layout")
        self.organizations_checkbox = QCheckBox(self.one_route_widget)
        self.organizations_checkbox.setObjectName(u"organizations_checkbox")

        self.one_route_layout.addWidget(self.organizations_checkbox)

        self.travel_time_checkbox = QCheckBox(self.one_route_widget)
        self.travel_time_checkbox.setObjectName(u"travel_time_checkbox")

        self.one_route_layout.addWidget(self.travel_time_checkbox)

        self.dateTimeEdit = QDateTimeEdit(self.one_route_widget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setEnabled(True)
        self.dateTimeEdit.setDate(QDate(2024, 1, 1))
        self.dateTimeEdit.setTime(QTime(12, 0, 0))
        self.dateTimeEdit.setCalendarPopup(True)

        self.one_route_layout.addWidget(self.dateTimeEdit)


        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.one_route_widget)


        self.retranslateUi(DrawRouteApp)

        QMetaObject.connectSlotsByName(DrawRouteApp)
    # setupUi

    def retranslateUi(self, DrawRouteApp):
        DrawRouteApp.setWindowTitle(QCoreApplication.translate("DrawRouteApp", u"DrawRouteApp-0.3.0", None))
        self.label_2.setText(QCoreApplication.translate("DrawRouteApp", u"<html><head/><body><p align=\"center\">Tooltip</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("DrawRouteApp", u"For one route: ", None))
        self.label_5.setText(QCoreApplication.translate("DrawRouteApp", u"1. Use [(lat_1, lon_1), (lat_2, lon_2)], where (lat_1, lon_1) are departure coordinates and (lat_2, lon_2) are arrival coordinates", None))
        self.label_7.setText(QCoreApplication.translate("DrawRouteApp", u"For multiple routes:", None))
        self.label_8.setText(QCoreApplication.translate("DrawRouteApp", u"1. ", None))
        self.label_3.setText(QCoreApplication.translate("DrawRouteApp", u"2. ", None))
        self.label.setText(QCoreApplication.translate("DrawRouteApp", u"Enter coordintes:", None))
        self.coordinates_text.setText("")
        self.one_route_radio.setText(QCoreApplication.translate("DrawRouteApp", u"One route", None))
        self.multiple_routes_radio.setText(QCoreApplication.translate("DrawRouteApp", u"Multiple routes", None))
        self.submit_button.setText(QCoreApplication.translate("DrawRouteApp", u"Submit", None))
        self.label_6.setText(QCoreApplication.translate("DrawRouteApp", u"2. Use [(lat_1, lon_1), (lat_2, lon_2), ..., (lat_n, lon_n)], where (lat_2, lon_2) to (lat_n-1, lon_n-1) are coordinates between departure and arrival", None))
        self.organizations_checkbox.setText(QCoreApplication.translate("DrawRouteApp", u"Get nearest organizations", None))
        self.travel_time_checkbox.setText(QCoreApplication.translate("DrawRouteApp", u"Predict travel time", None))
#if QT_CONFIG(whatsthis)
        self.dateTimeEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
    # retranslateUi

