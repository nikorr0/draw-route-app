# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'result_windowhCkHTn.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGraphicsView, QHBoxLayout,
    QHeaderView, QLayout, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class CustomGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._zoom = 1

        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def wheelEvent(self, event):
        # Zoom in/out based on mouse wheel
        factor = 1.2

        if event.angleDelta().y() < 0:
            factor = 1 / factor
        
        self._zoom *= factor
        if (self._zoom >= 0.4) and (self._zoom <= 15):
            self.scale(factor, factor)
        
        if self._zoom < 0.4:
            self._zoom = 0.4
        
        if self._zoom > 15:
            self._zoom = 15

class Ui_Result(object):
    def setupUi(self, Result):
        if not Result.objectName():
            Result.setObjectName(u"Result")
        Result.resize(745, 825)
        Result.setMinimumSize(QSize(745, 825))
        Result.setMaximumSize(QSize(745, 825))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WeatherClear))
        Result.setWindowIcon(icon)
        Result.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.verticalLayoutWidget = QWidget(Result)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 721, 808))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MapImage = CustomGraphicsView(self.verticalLayoutWidget)
        self.MapImage.setObjectName(u"MapImage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MapImage.sizePolicy().hasHeightForWidth())
        self.MapImage.setSizePolicy(sizePolicy)
        self.MapImage.setMinimumSize(QSize(400, 400))
        self.MapImage.setMaximumSize(QSize(700, 600))
        self.MapImage.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.MapImage.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.MapImage.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.MapImage, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.map_information_table = QTableWidget(self.verticalLayoutWidget)
        if (self.map_information_table.columnCount() < 1):
            self.map_information_table.setColumnCount(1)
        if (self.map_information_table.rowCount() < 1):
            self.map_information_table.setRowCount(1)
        self.map_information_table.setObjectName(u"map_information_table")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.map_information_table.sizePolicy().hasHeightForWidth())
        self.map_information_table.setSizePolicy(sizePolicy1)
        self.map_information_table.setMinimumSize(QSize(329, 272))
        self.map_information_table.setMaximumSize(QSize(329, 272))
#if QT_CONFIG(accessibility)
        self.map_information_table.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.map_information_table.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.map_information_table.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed)
        self.map_information_table.setTabKeyNavigation(False)
        self.map_information_table.setProperty("showDropIndicator", False)
        self.map_information_table.setDragDropOverwriteMode(False)
        self.map_information_table.setSortingEnabled(False)
        self.map_information_table.setCornerButtonEnabled(False)
        self.map_information_table.setRowCount(1)
        self.map_information_table.setColumnCount(1)
        self.map_information_table.horizontalHeader().setVisible(False)
        self.map_information_table.horizontalHeader().setCascadingSectionResizes(False)
        self.map_information_table.horizontalHeader().setMinimumSectionSize(150)
        self.map_information_table.horizontalHeader().setDefaultSectionSize(150)
        self.map_information_table.horizontalHeader().setHighlightSections(False)
        self.map_information_table.verticalHeader().setVisible(True)
        self.map_information_table.verticalHeader().setCascadingSectionResizes(False)
        self.map_information_table.verticalHeader().setMinimumSectionSize(30)
        self.map_information_table.verticalHeader().setHighlightSections(True)

        self.horizontalLayout.addWidget(self.map_information_table)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Result)

        QMetaObject.connectSlotsByName(Result)
    # setupUi

    def retranslateUi(self, Result):
        Result.setWindowTitle(QCoreApplication.translate("Result", u"Result", None))
    # retranslateUi

