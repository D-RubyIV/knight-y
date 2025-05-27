# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1236, 573)
        MainWindow.setStyleSheet(u"/*initial */\n"
"* {\n"
"    margin: 0;\n"
"    padding: 0;\n"
"}\n"
"QTableWidget {\n"
"    font-size: 12px\n"
"}\n"
"QTableWidget::indicator {\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"QTableWidget::indicator:checked {\n"
"    background-color: #0078d7;\n"
"    border: 1px solid #555;\n"
"}\n"
"QTableWidget::indicator:unchecked {\n"
"    background-color: white;\n"
"    border: 1px solid #555;\n"
"}\n"
"QTableWidget {\n"
"    border-radius: 10px;\n"
"    background-color: transparent\n"
"}\n"
"QTableWidget::item {\n"
"    border-radius: 3px;\n"
"    margin-bottom: 3px;\n"
"    margin-right: 3px;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgba(240, 240, 240, 50);\n"
"    border: 0px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSortingEnabled(True)

        self.verticalLayout_4.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.tab_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_browser_1 = QFrame(self.frame_5)
        self.frame_browser_1.setObjectName(u"frame_browser_1")
        self.frame_browser_1.setFrameShape(QFrame.StyledPanel)
        self.frame_browser_1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_browser_1)

        self.frame_browser_2 = QFrame(self.frame_5)
        self.frame_browser_2.setObjectName(u"frame_browser_2")
        self.frame_browser_2.setFrameShape(QFrame.StyledPanel)
        self.frame_browser_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_browser_2)

        self.frame_browser_3 = QFrame(self.frame_5)
        self.frame_browser_3.setObjectName(u"frame_browser_3")
        self.frame_browser_3.setFrameShape(QFrame.StyledPanel)
        self.frame_browser_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_browser_3)

        self.frame_browser_4 = QFrame(self.frame_5)
        self.frame_browser_4.setObjectName(u"frame_browser_4")
        self.frame_browser_4.setFrameShape(QFrame.StyledPanel)
        self.frame_browser_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_browser_4)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.start_scroll_page = QPushButton(self.frame_4)
        self.start_scroll_page.setObjectName(u"start_scroll_page")

        self.verticalLayout_2.addWidget(self.start_scroll_page)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"B\u1ea3ng d\u1eef li\u1ec7u", None))
        self.start_scroll_page.setText(QCoreApplication.translate("MainWindow", u"B\u1eaft \u0111\u1ea7u cu\u1ed9n trang", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"C\u1eeda s\u1ed5 nh\u00fang", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Ph\u00e2n t\u00edch", None))
    # retranslateUi

