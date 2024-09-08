# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customization_windowXwPKeu.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGraphicsView, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_Customization(object):
    def setupUi(self, Customization):
        if not Customization.objectName():
            Customization.setObjectName(u"Customization")
        Customization.resize(660, 1000)
        Customization.setMinimumSize(QSize(660, 1000))
        Customization.setMaximumSize(QSize(660, 1000))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WeatherClear))
        Customization.setWindowIcon(icon)
        Customization.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.gridLayoutWidget = QWidget(Customization)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 10, 601, 974))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.departure_color_btn = QPushButton(self.gridLayoutWidget)
        self.departure_color_btn.setObjectName(u"departure_color_btn")

        self.gridLayout.addWidget(self.departure_color_btn, 12, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        font = QFont()
        font.setBold(True)
        self.label_13.setFont(font)

        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)

        self.label_21 = QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 27, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.arrival_size_slider = QSlider(self.gridLayoutWidget)
        self.arrival_size_slider.setObjectName(u"arrival_size_slider")
        self.arrival_size_slider.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.arrival_size_slider.setMaximum(200)
        self.arrival_size_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.arrival_size_slider)

        self.arrival_size_label = QLabel(self.gridLayoutWidget)
        self.arrival_size_label.setObjectName(u"arrival_size_label")
        self.arrival_size_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.arrival_size_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.arrival_size_label)


        self.gridLayout.addLayout(self.horizontalLayout, 23, 3, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)

        self.line_7 = QFrame(self.gridLayoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_7, 5, 0, 1, 4)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 23, 2, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 12, 2, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.font_size_slider = QSlider(self.gridLayoutWidget)
        self.font_size_slider.setObjectName(u"font_size_slider")
        self.font_size_slider.setMaximum(100)
        self.font_size_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_6.addWidget(self.font_size_slider)

        self.font_size_label = QLabel(self.gridLayoutWidget)
        self.font_size_label.setObjectName(u"font_size_label")
        self.font_size_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.font_size_label)


        self.gridLayout.addLayout(self.horizontalLayout_6, 27, 3, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.gridLayout.addWidget(self.label_20, 25, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 32, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 8, 2, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.gridLayout.addWidget(self.label_19, 29, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 23, 0, 1, 1)

        self.background_color_btn = QPushButton(self.gridLayoutWidget)
        self.background_color_btn.setObjectName(u"background_color_btn")

        self.gridLayout.addWidget(self.background_color_btn, 3, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.line_11 = QFrame(self.gridLayoutWidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_11, 30, 0, 1, 4)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 2, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 16, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout.addWidget(self.label_12, 21, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 4)

        self.line_12 = QFrame(self.gridLayoutWidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_12, 28, 0, 1, 4)

        self.title_line = QLineEdit(self.gridLayoutWidget)
        self.title_line.setObjectName(u"title_line")

        self.gridLayout.addWidget(self.title_line, 27, 1, 1, 1)

        self.line_8 = QFrame(self.gridLayoutWidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_8, 9, 0, 1, 4)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 12, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.alpha_route_slider = QSlider(self.gridLayoutWidget)
        self.alpha_route_slider.setObjectName(u"alpha_route_slider")
        self.alpha_route_slider.setMaximum(100)
        self.alpha_route_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_4.addWidget(self.alpha_route_slider)

        self.alpha_route_label = QLabel(self.gridLayoutWidget)
        self.alpha_route_label.setObjectName(u"alpha_route_label")
        self.alpha_route_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.alpha_route_label)


        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 3, 1, 1)

        self.line_3 = QFrame(self.gridLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 7, 0, 1, 4)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 27, 2, 1, 1)

        self.line_6 = QFrame(self.gridLayoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_6, 17, 0, 1, 4)

        self.line_14 = QFrame(self.gridLayoutWidget)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_14, 26, 0, 1, 4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.departure_size_slider = QSlider(self.gridLayoutWidget)
        self.departure_size_slider.setObjectName(u"departure_size_slider")
        self.departure_size_slider.setMaximum(200)
        self.departure_size_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_5.addWidget(self.departure_size_slider)

        self.departure_size_label = QLabel(self.gridLayoutWidget)
        self.departure_size_label.setObjectName(u"departure_size_label")
        self.departure_size_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.departure_size_label)


        self.gridLayout.addLayout(self.horizontalLayout_5, 12, 3, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 32, 2, 1, 1)

        self.intermediate_color_btn = QPushButton(self.gridLayoutWidget)
        self.intermediate_color_btn.setObjectName(u"intermediate_color_btn")

        self.gridLayout.addWidget(self.intermediate_color_btn, 18, 3, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 18, 0, 1, 1)

        self.line_13 = QFrame(self.gridLayoutWidget)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_13, 24, 0, 1, 4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.alpha_points_slider = QSlider(self.gridLayoutWidget)
        self.alpha_points_slider.setObjectName(u"alpha_points_slider")
        self.alpha_points_slider.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.alpha_points_slider.setMaximum(100)
        self.alpha_points_slider.setSingleStep(1)
        self.alpha_points_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.alpha_points_slider)

        self.alpha_points_label = QLabel(self.gridLayoutWidget)
        self.alpha_points_label.setObjectName(u"alpha_points_label")
        self.alpha_points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.alpha_points_label)


        self.gridLayout.addLayout(self.horizontalLayout_3, 32, 3, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.intermediate_size_slider = QSlider(self.gridLayoutWidget)
        self.intermediate_size_slider.setObjectName(u"intermediate_size_slider")
        self.intermediate_size_slider.setMaximum(200)
        self.intermediate_size_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_7.addWidget(self.intermediate_size_slider)

        self.intermediate_size_label = QLabel(self.gridLayoutWidget)
        self.intermediate_size_label.setObjectName(u"intermediate_size_label")
        self.intermediate_size_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.intermediate_size_label)


        self.gridLayout.addLayout(self.horizontalLayout_7, 19, 1, 1, 1)

        self.line_9 = QFrame(self.gridLayoutWidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_9, 22, 0, 1, 4)

        self.line_4 = QFrame(self.gridLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 15, 0, 1, 4)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 18, 2, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 19, 0, 1, 1)

        self.road_color_btn = QPushButton(self.gridLayoutWidget)
        self.road_color_btn.setObjectName(u"road_color_btn")

        self.gridLayout.addWidget(self.road_color_btn, 3, 3, 1, 1)

        self.intermediate_points_checkbox = QCheckBox(self.gridLayoutWidget)
        self.intermediate_points_checkbox.setObjectName(u"intermediate_points_checkbox")

        self.gridLayout.addWidget(self.intermediate_points_checkbox, 18, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.legend_checkbox = QCheckBox(self.gridLayoutWidget)
        self.legend_checkbox.setObjectName(u"legend_checkbox")

        self.gridLayout.addWidget(self.legend_checkbox, 32, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.line_5 = QFrame(self.gridLayoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_5, 34, 0, 1, 4)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 11, 0, 1, 4)

        self.line_10 = QFrame(self.gridLayoutWidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_10, 20, 0, 1, 4)

        self.arrival_color_btn = QPushButton(self.gridLayoutWidget)
        self.arrival_color_btn.setObjectName(u"arrival_color_btn")

        self.gridLayout.addWidget(self.arrival_color_btn, 23, 1, 1, 1)

        self.example_map_view = QGraphicsView(self.gridLayoutWidget)
        self.example_map_view.setObjectName(u"example_map_view")
        self.example_map_view.setMinimumSize(QSize(0, 390))

        self.gridLayout.addWidget(self.example_map_view, 35, 0, 2, 4)

        self.route_btns_layout = QGridLayout()
        self.route_btns_layout.setObjectName(u"route_btns_layout")
        self.route_color_btn = QPushButton(self.gridLayoutWidget)
        self.route_color_btn.setObjectName(u"route_color_btn")

        self.route_btns_layout.addWidget(self.route_color_btn, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.route_btns_layout, 8, 1, 1, 1)

        self.gridLayoutWidget_2 = QWidget(Customization)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(543, 898, 111, 86))
        self.verticalLayout = QVBoxLayout(self.gridLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.restore_defaults_btn = QPushButton(self.gridLayoutWidget_2)
        self.restore_defaults_btn.setObjectName(u"restore_defaults_btn")

        self.verticalLayout.addWidget(self.restore_defaults_btn)

        self.show_example_btn = QPushButton(self.gridLayoutWidget_2)
        self.show_example_btn.setObjectName(u"show_example_btn")

        self.verticalLayout.addWidget(self.show_example_btn)

        self.save_btn = QPushButton(self.gridLayoutWidget_2)
        self.save_btn.setObjectName(u"save_btn")

        self.verticalLayout.addWidget(self.save_btn)


        self.retranslateUi(Customization)

        QMetaObject.connectSlotsByName(Customization)
    # setupUi

    def retranslateUi(self, Customization):
        Customization.setWindowTitle(QCoreApplication.translate("Customization", u"Customization", None))
        self.departure_color_btn.setText("")
        self.label_13.setText(QCoreApplication.translate("Customization", u"Route", None))
        self.label_21.setText(QCoreApplication.translate("Customization", u"Title:", None))
        self.arrival_size_label.setText(QCoreApplication.translate("Customization", u"0", None))
        self.label_10.setText(QCoreApplication.translate("Customization", u"Departure point", None))
        self.label_18.setText(QCoreApplication.translate("Customization", u"Arrival point size:", None))
        self.label_8.setText(QCoreApplication.translate("Customization", u"Departure point size:", None))
        self.font_size_label.setText(QCoreApplication.translate("Customization", u"0", None))
        self.label_20.setText(QCoreApplication.translate("Customization", u"Title", None))
        self.label_6.setText(QCoreApplication.translate("Customization", u"Legend:", None))
        self.label_4.setText(QCoreApplication.translate("Customization", u"Alpha channel of the route: ", None))
        self.label_19.setText(QCoreApplication.translate("Customization", u"Other", None))
        self.label_17.setText(QCoreApplication.translate("Customization", u"Arrival point color:", None))
        self.background_color_btn.setText("")
        self.label_3.setText(QCoreApplication.translate("Customization", u"Route color:", None))
        self.label.setText(QCoreApplication.translate("Customization", u"Background color:", None))
        self.label_2.setText(QCoreApplication.translate("Customization", u"Road color:", None))
        self.label_11.setText(QCoreApplication.translate("Customization", u"Intermediate points", None))
        self.label_12.setText(QCoreApplication.translate("Customization", u"Arrival point", None))
        self.label_7.setText(QCoreApplication.translate("Customization", u"Departure point color:", None))
        self.alpha_route_label.setText(QCoreApplication.translate("Customization", u"0", None))
        self.label_22.setText(QCoreApplication.translate("Customization", u"Font size:", None))
        self.departure_size_label.setText(QCoreApplication.translate("Customization", u"0", None))
        self.label_5.setText(QCoreApplication.translate("Customization", u"Alpha channel of the points: ", None))
        self.intermediate_color_btn.setText("")
        self.label_15.setText(QCoreApplication.translate("Customization", u"Place intermediate points:", None))
        self.alpha_points_label.setText(QCoreApplication.translate("Customization", u"0", None))
        self.intermediate_size_label.setText(QCoreApplication.translate("Customization", u"0", None))
        self.label_16.setText(QCoreApplication.translate("Customization", u"Intermediate point color:", None))
        self.label_14.setText(QCoreApplication.translate("Customization", u"Intermediate point size:", None))
        self.road_color_btn.setText("")
        self.intermediate_points_checkbox.setText("")
        self.legend_checkbox.setText("")
        self.label_9.setText(QCoreApplication.translate("Customization", u"Map", None))
        self.arrival_color_btn.setText("")
        self.route_color_btn.setText("")
        self.restore_defaults_btn.setText(QCoreApplication.translate("Customization", u"Restore defaults", None))
        self.show_example_btn.setText(QCoreApplication.translate("Customization", u"Show example", None))
        self.save_btn.setText(QCoreApplication.translate("Customization", u"Save", None))
    # retranslateUi

