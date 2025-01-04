# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(951, 711)
        MainWindow.setMinimumSize(QSize(951, 711))
        MainWindow.setMaximumSize(QSize(951, 711))
        MainWindow.setStyleSheet(u"border: none;\n"
"background-color: rgb(62, 62, 62);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_header = QFrame(self.frame)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMaximumSize(QSize(16777215, 100))
        self.frame_header.setStyleSheet(u"QFrame {\n"
"    border: 1px solid black;\n"
"	background-color: rgb(202, 202, 202);\n"
"}\n"
"\n"
"QFrame QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_header)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 55))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_header)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Pages = QStackedWidget(self.frame_3)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"QStackedWidget {\n"
"    border: 1px solid black;\n"
"    padding: 5px;\n"
"	background-color: rgb(202, 202, 202);\n"
"}\n"
"\n"
"QStackedWidget QLabel, \n"
"QStackedWidget QPushButton,\n"
"QStackedWidget QTabWidget,\n"
"QStackedWidget QLineEdit {\n"
"    border: none;\n"
"}\n"
"")
        self.pg_data = QWidget()
        self.pg_data.setObjectName(u"pg_data")
        self.pg_data.setStyleSheet(u"background-color: transparent;;")
        self.cbx_option = QComboBox(self.pg_data)
        self.cbx_option.addItem("")
        self.cbx_option.addItem("")
        self.cbx_option.addItem("")
        self.cbx_option.addItem("")
        self.cbx_option.setObjectName(u"cbx_option")
        self.cbx_option.setGeometry(QRect(380, 30, 121, 41))
        self.cbx_option.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 2px solid black;")
        self.label_8 = QLabel(self.pg_data)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(200, 20, 171, 61))
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.frame_6 = QFrame(self.pg_data)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(30, 90, 341, 231))
        self.frame_6.setMinimumSize(QSize(150, 100))
        self.frame_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_files_name = QLabel(self.frame_6)
        self.lbl_files_name.setObjectName(u"lbl_files_name")
        self.lbl_files_name.setStyleSheet(u"background-image: url(:/saving/assets/images/domain-name.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"\n"
"")

        self.verticalLayout_6.addWidget(self.lbl_files_name)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setStyleSheet(u"border: 1px solid black;\n"
"padding: 1px;\n"
"border-radius: 3px;")

        self.verticalLayout_6.addWidget(self.label_4)

        self.frame_7 = QFrame(self.pg_data)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(410, 90, 351, 231))
        self.frame_7.setMinimumSize(QSize(150, 100))
        self.frame_7.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lbl_links_in_file = QLabel(self.frame_7)
        self.lbl_links_in_file.setObjectName(u"lbl_links_in_file")
        self.lbl_links_in_file.setStyleSheet(u"background-image: url(:/saving/assets/images/link-creation.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.lbl_links_in_file)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))
        self.label_12.setStyleSheet(u"border: 1px solid black;\n"
"padding: 1px;\n"
"border-radius: 3px;")

        self.verticalLayout_7.addWidget(self.label_12)

        self.frame_8 = QFrame(self.pg_data)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(30, 330, 341, 221))
        self.frame_8.setMinimumSize(QSize(150, 100))
        self.frame_8.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lbl_sample_rank = QLabel(self.frame_8)
        self.lbl_sample_rank.setObjectName(u"lbl_sample_rank")
        self.lbl_sample_rank.setStyleSheet(u"background-image: url(:/saving/assets/images/hierarchy.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"\n"
"")

        self.verticalLayout_8.addWidget(self.lbl_sample_rank)

        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 20))
        self.label_13.setStyleSheet(u"border: 1px solid black;\n"
"padding: 1px;\n"
"border-radius: 3px;")

        self.verticalLayout_8.addWidget(self.label_13)

        self.frame_9 = QFrame(self.pg_data)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(410, 330, 351, 221))
        self.frame_9.setMinimumSize(QSize(150, 100))
        self.frame_9.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lbl_iterate_page_rank = QLabel(self.frame_9)
        self.lbl_iterate_page_rank.setObjectName(u"lbl_iterate_page_rank")
        self.lbl_iterate_page_rank.setStyleSheet(u"background-image: url(:/saving/assets/images/schema.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.lbl_iterate_page_rank)

        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 20))
        self.label_14.setStyleSheet(u"border: 1px solid black;\n"
"padding: 1px;\n"
"border-radius: 3px;")

        self.verticalLayout_9.addWidget(self.label_14)

        self.Pages.addWidget(self.pg_data)
        self.pg_graphics = QWidget()
        self.pg_graphics.setObjectName(u"pg_graphics")
        self.pg_graphics.setStyleSheet(u"background-color: transparent;;")
        self.verticalLayout_4 = QVBoxLayout(self.pg_graphics)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.pg_graphics)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"border: none;")
        self.tab_sample_page_rank = QWidget()
        self.tab_sample_page_rank.setObjectName(u"tab_sample_page_rank")
        self.tab_sample_page_rank.setStyleSheet(u"border: none;\n"
"background-image: url(:/saving/assets/images/python-logo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.tabWidget.addTab(self.tab_sample_page_rank, "")
        self.tab_iterate_page_rank = QWidget()
        self.tab_iterate_page_rank.setObjectName(u"tab_iterate_page_rank")
        self.tab_iterate_page_rank.setStyleSheet(u"border: none;\n"
"background-image: url(:/saving/assets/images/python-logo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.tabWidget.addTab(self.tab_iterate_page_rank, "")
        self.tab_links_quantity_page_rank = QWidget()
        self.tab_links_quantity_page_rank.setObjectName(u"tab_links_quantity_page_rank")
        self.tab_links_quantity_page_rank.setStyleSheet(u"border: none;\n"
"background-image: url(:/saving/assets/images/python-logo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.tabWidget.addTab(self.tab_links_quantity_page_rank, "")
        self.tab_comparison_results_professor = QWidget()
        self.tab_comparison_results_professor.setObjectName(u"tab_comparison_results_professor")
        self.tab_comparison_results_professor.setStyleSheet(u"border: none;\n"
"background-image: url(:/saving/assets/images/python-logo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.tabWidget.addTab(self.tab_comparison_results_professor, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_graphics)
        self.pg_about = QWidget()
        self.pg_about.setObjectName(u"pg_about")
        self.pg_about.setStyleSheet(u"background-color: transparent;;")
        self.verticalLayout_5 = QVBoxLayout(self.pg_about)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.pg_about)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(107, 107, 107);")

        self.verticalLayout_5.addWidget(self.label_5)

        self.frame_5 = QFrame(self.pg_about)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame {\n"
" border: 1px solid black;\n"
"}\n"
"\n"
"QFrame QLabel{\n"
"	border: none;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(20, 20))
        self.label_7.setStyleSheet(u"background-image: url(:/saving/assets/images/rank-page-img.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(300, 16777215))
        self.label_6.setStyleSheet(u"background-color: rgb(149, 149, 149);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_3.addWidget(self.label_6)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.Pages.addWidget(self.pg_about)

        self.horizontalLayout_2.addWidget(self.Pages)

        self.frame_right = QFrame(self.frame_3)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setMinimumSize(QSize(100, 0))
        self.frame_right.setStyleSheet(u"QFrame {\n"
"    border: 1px solid black;\n"
"	background-color: rgb(202, 202, 202);\n"
"}\n"
"\n"
"QFrame QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 137, 206);\n"
"	color: #fff;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 113, 170);\n"
"}")
        self.frame_right.setFrameShape(QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_right)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.btn_data = QPushButton(self.frame_right)
        self.btn_data.setObjectName(u"btn_data")
        self.btn_data.setMinimumSize(QSize(64, 64))
        self.btn_data.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/saving/assets/images/data.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_data.setIcon(icon)
        self.btn_data.setIconSize(QSize(64, 64))

        self.verticalLayout_3.addWidget(self.btn_data)

        self.btn_graphics = QPushButton(self.frame_right)
        self.btn_graphics.setObjectName(u"btn_graphics")
        self.btn_graphics.setMinimumSize(QSize(64, 64))
        self.btn_graphics.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/saving/assets/images/predictive-chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_graphics.setIcon(icon1)
        self.btn_graphics.setIconSize(QSize(64, 64))

        self.verticalLayout_3.addWidget(self.btn_graphics)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_about = QPushButton(self.frame_right)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMinimumSize(QSize(40, 40))
        self.btn_about.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/saving/assets/images/about.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_about.setIcon(icon2)
        self.btn_about.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.btn_about)


        self.horizontalLayout_2.addWidget(self.frame_right)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">PAGE RANK APP VISUALIZATION</span></p></body></html>", None))
        self.cbx_option.setItemText(0, QCoreApplication.translate("MainWindow", u"Choice...", None))
        self.cbx_option.setItemText(1, QCoreApplication.translate("MainWindow", u"corpus0", None))
        self.cbx_option.setItemText(2, QCoreApplication.translate("MainWindow", u"corpus1", None))
        self.cbx_option.setItemText(3, QCoreApplication.translate("MainWindow", u"corpus2", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Choose your option:</span></p></body></html>", None))
        self.lbl_files_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Site names</p></body></html>", None))
        self.lbl_links_in_file.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Links on the websites</p></body></html>", None))
        self.lbl_sample_rank.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Sample PageRank</p></body></html>", None))
        self.lbl_iterate_page_rank.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Iterate PageRank</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sample_page_rank), QCoreApplication.translate("MainWindow", u"Sample PageRank", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_iterate_page_rank), QCoreApplication.translate("MainWindow", u"Iterate PageRank", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_links_quantity_page_rank), QCoreApplication.translate("MainWindow", u"Links Quantity", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_comparison_results_professor), QCoreApplication.translate("MainWindow", u"Comparison Results", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">ABOUT</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_data.setText("")
        self.btn_graphics.setText("")
        self.btn_about.setText("")
    # retranslateUi

