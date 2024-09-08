# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tooltip_windowFBhODn.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Tooltip(object):
    def setupUi(self, Tooltip):
        if not Tooltip.objectName():
            Tooltip.setObjectName(u"Tooltip")
        Tooltip.resize(850, 430)
        Tooltip.setMinimumSize(QSize(850, 430))
        Tooltip.setMaximumSize(QSize(850, 430))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WeatherClear))
        Tooltip.setWindowIcon(icon)
        Tooltip.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.verticalLayoutWidget = QWidget(Tooltip)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 14, 809, 402))
        self.verticalLayoutWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.verticalLayout.addWidget(self.label_4)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.verticalLayout.addWidget(self.label_6)

        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.verticalLayout.addWidget(self.label_8)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.verticalLayout.addWidget(self.label_7)

        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_13)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.verticalLayout.addWidget(self.label_5)

        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout.addWidget(self.label_12)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.line_3 = QFrame(self.verticalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.onre_route_line = QLineEdit(self.verticalLayoutWidget)
        self.onre_route_line.setObjectName(u"onre_route_line")
        self.onre_route_line.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.onre_route_line)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.multiple_routes_line = QLineEdit(self.verticalLayoutWidget)
        self.multiple_routes_line.setObjectName(u"multiple_routes_line")
        self.multiple_routes_line.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.multiple_routes_line)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.line_4 = QFrame(self.verticalLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)


        self.retranslateUi(Tooltip)

        QMetaObject.connectSlotsByName(Tooltip)
    # setupUi

    def retranslateUi(self, Tooltip):
        Tooltip.setWindowTitle(QCoreApplication.translate("Tooltip", u"Tooltip", None))
        self.label.setText(QCoreApplication.translate("Tooltip", u"Hints", None))
        self.label_3.setText(QCoreApplication.translate("Tooltip", u"One route logic:", None))
        self.label_4.setText(QCoreApplication.translate("Tooltip", u"1. Use [(lat_1, lon_1), (lat_2, lon_2)], where (lat_1, lon_1) are departure coordinates and (lat_2, lon_2) are arrival coordinates", None))
        self.label_2.setText(QCoreApplication.translate("Tooltip", u"OR", None))
        self.label_6.setText(QCoreApplication.translate("Tooltip", u"2. Use [(lat_1, lon_1), (lat_2, lon_2), ..., (lat_n, lon_n)], where (lat_2, lon_2) to (lat_n-1, lon_n-1) are coordinates between departure and arrival\n"
"", None))
        self.label_14.setText(QCoreApplication.translate("Tooltip", u"A single one route list must contain at least two points. Every two points must be connected to a road.\n"
"", None))
        self.label_8.setText(QCoreApplication.translate("Tooltip", u"Multiple route logic:", None))
        self.label_7.setText(QCoreApplication.translate("Tooltip", u"1. Use [[(lat_1, lon_1), (lat_2, lon_2)], ..., [(lat_1, lon_1), (lat_2, lon_2)]", None))
        self.label_13.setText(QCoreApplication.translate("Tooltip", u"OR", None))
        self.label_5.setText(QCoreApplication.translate("Tooltip", u"2. Use [[(lat_1, lon_1), (lat_2, lon_2), ..., (lat_n, lon_n)], ...,  [(lat_1, lon_1), (lat_2, lon_2), ..., (lat_n, lon_n)]]\n"
"", None))
        self.label_12.setText(QCoreApplication.translate("Tooltip", u"A single multiple routes list can contain more than one route, but no more than nine.", None))
        self.label_11.setText(QCoreApplication.translate("Tooltip", u"Examples", None))
        self.label_9.setText(QCoreApplication.translate("Tooltip", u"One route:", None))
        self.onre_route_line.setText(QCoreApplication.translate("Tooltip", u"[(1.363714644767422, 103.86646826804811), (1.3524767116325576, 103.87666028388607 ), (1.3482262503868399, 103.88993287181567)]", None))
        self.label_10.setText(QCoreApplication.translate("Tooltip", u"Multiple routes:", None))
        self.multiple_routes_line.setText(QCoreApplication.translate("Tooltip", u"[[(52.04970320507061, 4.2504818042421375), (52.05755637723045, 4.262599976185987)], [(52.06116524906595, 4.283010325267095), (52.04854027311392, 4.284284934257416), (52.05558196178574, 4.299873221750225)]]", None))
    # retranslateUi

