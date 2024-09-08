# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowqmMtbq.ui'
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
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_DrawRouteApp(object):
    def setupUi(self, DrawRouteApp):
        if not DrawRouteApp.objectName():
            DrawRouteApp.setObjectName(u"DrawRouteApp")
        DrawRouteApp.resize(750, 225)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DrawRouteApp.sizePolicy().hasHeightForWidth())
        DrawRouteApp.setSizePolicy(sizePolicy)
        DrawRouteApp.setMinimumSize(QSize(750, 225))
        DrawRouteApp.setMaximumSize(QSize(750, 225))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WeatherClear))
        DrawRouteApp.setWindowIcon(icon)
        DrawRouteApp.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.formLayoutWidget = QWidget(DrawRouteApp)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 20, 722, 151))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.coordinates_text = QLineEdit(self.formLayoutWidget)
        self.coordinates_text.setObjectName(u"coordinates_text")
        self.coordinates_text.setMinimumSize(QSize(625, 0))
        self.coordinates_text.setMaximumSize(QSize(600, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.coordinates_text)

        self.one_route_radio = QRadioButton(self.formLayoutWidget)
        self.one_route_radio.setObjectName(u"one_route_radio")
        self.one_route_radio.setEnabled(True)
        self.one_route_radio.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.one_route_radio)

        self.multiple_routes_radio = QRadioButton(self.formLayoutWidget)
        self.multiple_routes_radio.setObjectName(u"multiple_routes_radio")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.multiple_routes_radio)

        self.one_route_widget = QWidget(self.formLayoutWidget)
        self.one_route_widget.setObjectName(u"one_route_widget")
        font = QFont()
        font.setKerning(True)
        self.one_route_widget.setFont(font)
        self.one_route_layout = QVBoxLayout(self.one_route_widget)
        self.one_route_layout.setObjectName(u"one_route_layout")
        self.one_route_layout.setContentsMargins(-1, 0, -1, -1)
        self.organizations_checkbox = QCheckBox(self.one_route_widget)
        self.organizations_checkbox.setObjectName(u"organizations_checkbox")

        self.one_route_layout.addWidget(self.organizations_checkbox)

        self.travel_time_checkbox = QCheckBox(self.one_route_widget)
        self.travel_time_checkbox.setObjectName(u"travel_time_checkbox")

        self.one_route_layout.addWidget(self.travel_time_checkbox)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.dateTimeEdit = QDateTimeEdit(self.one_route_widget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setEnabled(True)
        self.dateTimeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dateTimeEdit.setDate(QDate(2024, 1, 1))
        self.dateTimeEdit.setTime(QTime(12, 0, 0))
        self.dateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dateTimeEdit)

        self.horizontalSpacer = QSpacerItem(535, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.one_route_layout.addLayout(self.horizontalLayout_4)


        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.one_route_widget)

        self.verticalSpacer = QSpacerItem(0, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.verticalSpacer)

        self.layoutWidget = QWidget(DrawRouteApp)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(611, 120, 131, 92))
        self.formLayout_3 = QFormLayout(self.layoutWidget)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.submit_button = QPushButton(self.layoutWidget)
        self.submit_button.setObjectName(u"submit_button")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.submit_button)

        self.tooltip_button = QPushButton(self.layoutWidget)
        self.tooltip_button.setObjectName(u"tooltip_button")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.tooltip_button)

        self.customize_button = QPushButton(self.layoutWidget)
        self.customize_button.setObjectName(u"customize_button")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.customize_button)


        self.retranslateUi(DrawRouteApp)

        QMetaObject.connectSlotsByName(DrawRouteApp)
    # setupUi

    def retranslateUi(self, DrawRouteApp):
        DrawRouteApp.setWindowTitle(QCoreApplication.translate("DrawRouteApp", u"DrawRouteApp-1.0.0", None))
        self.label.setText(QCoreApplication.translate("DrawRouteApp", u"Enter coordintes:", None))
        self.one_route_radio.setText(QCoreApplication.translate("DrawRouteApp", u"One route", None))
        self.multiple_routes_radio.setText(QCoreApplication.translate("DrawRouteApp", u"Multiple routes", None))
        self.organizations_checkbox.setText(QCoreApplication.translate("DrawRouteApp", u"Get nearest organizations", None))
        self.travel_time_checkbox.setText(QCoreApplication.translate("DrawRouteApp", u"Predict travel time", None))
#if QT_CONFIG(whatsthis)
        self.dateTimeEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.submit_button.setText(QCoreApplication.translate("DrawRouteApp", u"Submit", None))
        self.tooltip_button.setText(QCoreApplication.translate("DrawRouteApp", u"Tooltip", None))
        self.customize_button.setText(QCoreApplication.translate("DrawRouteApp", u"Customize map", None))
    # retranslateUi

