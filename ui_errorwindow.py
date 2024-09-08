# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_windowlJjamf.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Error(object):
    def setupUi(self, Error):
        if not Error.objectName():
            Error.setObjectName(u"Error")
        Error.resize(320, 150)
        Error.setMinimumSize(QSize(320, 150))
        Error.setMaximumSize(QSize(320, 150))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogError))
        Error.setWindowIcon(icon)
        Error.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.OKButton = QPushButton(Error)
        self.OKButton.setObjectName(u"OKButton")
        self.OKButton.setGeometry(QRect(116, 117, 91, 24))
        self.OKButton.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.ErrorMessage = QLabel(Error)
        self.ErrorMessage.setObjectName(u"ErrorMessage")
        self.ErrorMessage.setGeometry(QRect(0, 8, 321, 101))
        self.ErrorMessage.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.ErrorMessage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Error)

        QMetaObject.connectSlotsByName(Error)
    # setupUi

    def retranslateUi(self, Error):
        Error.setWindowTitle(QCoreApplication.translate("Error", u"Error", None))
        self.OKButton.setText(QCoreApplication.translate("Error", u"OK", None))
        self.ErrorMessage.setText(QCoreApplication.translate("Error", u"ErrorMessage", None))
    # retranslateUi

