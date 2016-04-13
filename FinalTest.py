# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SecondTest.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from math import log, sqrt, exp,pow
from scipy.stats import norm
import random
import numpy
import sys

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(873, 686)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -231, 832, 850))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.EuropeanOption = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.EuropeanOption.setObjectName(_fromUtf8("EuropeanOption"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.EuropeanOption)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.EO_sigma = QtGui.QLineEdit(self.EuropeanOption)
        self.EO_sigma.setText(_fromUtf8(""))
        self.EO_sigma.setObjectName(_fromUtf8("EO_sigma"))
        self.gridLayout_2.addWidget(self.EO_sigma, 0, 3, 1, 1)
        self.EO_t = QtGui.QLineEdit(self.EuropeanOption)
        self.EO_t.setObjectName(_fromUtf8("EO_t"))
        self.gridLayout_2.addWidget(self.EO_t, 1, 3, 1, 1)
        self.EO_k = QtGui.QLineEdit(self.EuropeanOption)
        self.EO_k.setObjectName(_fromUtf8("EO_k"))
        self.gridLayout_2.addWidget(self.EO_k, 2, 1, 1, 1)
        self.EO_r = QtGui.QLineEdit(self.EuropeanOption)
        self.EO_r.setObjectName(_fromUtf8("EO_r"))
        self.gridLayout_2.addWidget(self.EO_r, 1, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.EuropeanOption)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 2, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.EuropeanOption)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.EuropeanOption)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 1, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.EuropeanOption)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        self.EO_s = QtGui.QLineEdit(self.EuropeanOption)
        self.EO_s.setText(_fromUtf8(""))
        self.EO_s.setObjectName(_fromUtf8("EO_s"))
        self.gridLayout_2.addWidget(self.EO_s, 0, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.EuropeanOption)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.EuropeanOption)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.EO_type = QtGui.QComboBox(self.EuropeanOption)
        self.EO_type.setFrame(True)
        self.EO_type.setObjectName(_fromUtf8("EO_type"))
        self.EO_type.addItem(_fromUtf8(""))
        self.EO_type.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.EO_type, 2, 3, 1, 1)
        self.EO_Method = QtGui.QComboBox(self.EuropeanOption)
        self.EO_Method.setObjectName(_fromUtf8("EO_Method"))
        self.EO_Method.addItem(_fromUtf8(""))
        self.EO_Method.addItem(_fromUtf8(""))
        self.EO_Method.addItem(_fromUtf8(""))
        self.EO_Method.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.EO_Method, 3, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.EuropeanOption)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 3, 2, 1, 1)
        self.label_16 = QtGui.QLabel(self.EuropeanOption)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1)
        self.EO_n = QtGui.QLineEdit(self.EuropeanOption)
        self.EO_n.setObjectName(_fromUtf8("EO_n"))
        self.gridLayout_2.addWidget(self.EO_n, 3, 3, 1, 1)
        self.label_18 = QtGui.QLabel(self.EuropeanOption)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 4, 0, 1, 1)
        self.EO_variate = QtGui.QLineEdit(self.EuropeanOption)
        self.EO_variate.setObjectName(_fromUtf8("EO_variate"))
        self.gridLayout_2.addWidget(self.EO_variate, 4, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.EuropeanOption)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_2.addWidget(self.label_26, 4, 2, 1, 1)
        self.EO_m = QtGui.QLineEdit(self.EuropeanOption)
        self.EO_m.setObjectName(_fromUtf8("EO_m"))
        self.gridLayout_2.addWidget(self.EO_m, 4, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.line = QtGui.QFrame(self.EuropeanOption)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.pushButton_5 = QtGui.QPushButton(self.EuropeanOption)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_6 = QtGui.QLabel(self.EuropeanOption)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_12 = QtGui.QLineEdit(self.EuropeanOption)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.horizontalLayout_2.addWidget(self.lineEdit_12)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.EuropeanOption)
        self.ImpliedVol = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.ImpliedVol.setObjectName(_fromUtf8("ImpliedVol"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.ImpliedVol)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_15 = QtGui.QLabel(self.ImpliedVol)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.ImpliedVol)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.Vol_pre = QtGui.QLineEdit(self.ImpliedVol)
        self.Vol_pre.setObjectName(_fromUtf8("Vol_pre"))
        self.gridLayout.addWidget(self.Vol_pre, 2, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.ImpliedVol)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.ImpliedVol)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.Vol_k = QtGui.QLineEdit(self.ImpliedVol)
        self.Vol_k.setObjectName(_fromUtf8("Vol_k"))
        self.gridLayout.addWidget(self.Vol_k, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.ImpliedVol)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.Vol_s = QtGui.QLineEdit(self.ImpliedVol)
        self.Vol_s.setObjectName(_fromUtf8("Vol_s"))
        self.gridLayout.addWidget(self.Vol_s, 0, 1, 1, 1)
        self.Vol_r = QtGui.QLineEdit(self.ImpliedVol)
        self.Vol_r.setObjectName(_fromUtf8("Vol_r"))
        self.gridLayout.addWidget(self.Vol_r, 0, 3, 1, 1)
        self.Vol_q = QtGui.QLineEdit(self.ImpliedVol)
        self.Vol_q.setObjectName(_fromUtf8("Vol_q"))
        self.gridLayout.addWidget(self.Vol_q, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.ImpliedVol)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.Vol_t = QtGui.QLineEdit(self.ImpliedVol)
        self.Vol_t.setObjectName(_fromUtf8("Vol_t"))
        self.gridLayout.addWidget(self.Vol_t, 1, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.ImpliedVol)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.Vol_type = QtGui.QComboBox(self.ImpliedVol)
        self.Vol_type.setObjectName(_fromUtf8("Vol_type"))
        self.Vol_type.addItem(_fromUtf8(""))
        self.Vol_type.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.Vol_type, 3, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.line_2 = QtGui.QFrame(self.ImpliedVol)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_4.addWidget(self.line_2)
        self.pushButton = QtGui.QPushButton(self.ImpliedVol)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_8 = QtGui.QLabel(self.ImpliedVol)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.Vol_ans = QtGui.QLineEdit(self.ImpliedVol)
        self.Vol_ans.setObjectName(_fromUtf8("Vol_ans"))
        self.horizontalLayout.addWidget(self.Vol_ans)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.ImpliedVol)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_23 = QtGui.QLabel(self.groupBox)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_3.addWidget(self.label_23, 2, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.groupBox)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_3.addWidget(self.label_21, 1, 0, 1, 1)
        self.BO_k = QtGui.QLineEdit(self.groupBox)
        self.BO_k.setObjectName(_fromUtf8("BO_k"))
        self.gridLayout_3.addWidget(self.BO_k, 1, 1, 1, 1)
        self.BO_m = QtGui.QLineEdit(self.groupBox)
        self.BO_m.setObjectName(_fromUtf8("BO_m"))
        self.gridLayout_3.addWidget(self.BO_m, 4, 3, 1, 1)
        self.label_25 = QtGui.QLabel(self.groupBox)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_3.addWidget(self.label_25, 3, 0, 1, 1)
        self.label_27 = QtGui.QLabel(self.groupBox)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_3.addWidget(self.label_27, 3, 2, 1, 1)
        self.label_29 = QtGui.QLabel(self.groupBox)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_3.addWidget(self.label_29, 4, 2, 1, 1)
        self.Vol_sigma1 = QtGui.QLineEdit(self.groupBox)
        self.Vol_sigma1.setObjectName(_fromUtf8("Vol_sigma1"))
        self.gridLayout_3.addWidget(self.Vol_sigma1, 1, 3, 1, 1)
        self.BO_sigma2 = QtGui.QLineEdit(self.groupBox)
        self.BO_sigma2.setObjectName(_fromUtf8("BO_sigma2"))
        self.gridLayout_3.addWidget(self.BO_sigma2, 2, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.groupBox)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_3.addWidget(self.label_24, 2, 2, 1, 1)
        self.BO_s2 = QtGui.QLineEdit(self.groupBox)
        self.BO_s2.setObjectName(_fromUtf8("BO_s2"))
        self.gridLayout_3.addWidget(self.BO_s2, 0, 3, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_3.addWidget(self.label_20, 0, 2, 1, 1)
        self.label_22 = QtGui.QLabel(self.groupBox)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_3.addWidget(self.label_22, 1, 2, 1, 1)
        self.BO_cor = QtGui.QLineEdit(self.groupBox)
        self.BO_cor.setObjectName(_fromUtf8("BO_cor"))
        self.gridLayout_3.addWidget(self.BO_cor, 2, 3, 1, 1)
        self.BO_r = QtGui.QLineEdit(self.groupBox)
        self.BO_r.setObjectName(_fromUtf8("BO_r"))
        self.gridLayout_3.addWidget(self.BO_r, 3, 1, 1, 1)
        self.label_28 = QtGui.QLabel(self.groupBox)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_3.addWidget(self.label_28, 4, 0, 1, 1)
        self.BO_t = QtGui.QLineEdit(self.groupBox)
        self.BO_t.setObjectName(_fromUtf8("BO_t"))
        self.gridLayout_3.addWidget(self.BO_t, 3, 3, 1, 1)
        self.BO_type = QtGui.QComboBox(self.groupBox)
        self.BO_type.setObjectName(_fromUtf8("BO_type"))
        self.BO_type.addItem(_fromUtf8(""))
        self.BO_type.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.BO_type, 4, 1, 1, 1)
        self.BO_s1 = QtGui.QLineEdit(self.groupBox)
        self.BO_s1.setObjectName(_fromUtf8("BO_s1"))
        self.gridLayout_3.addWidget(self.BO_s1, 0, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.groupBox)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_3.addWidget(self.label_19, 0, 0, 1, 1)
        self.label_31 = QtGui.QLabel(self.groupBox)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_3.addWidget(self.label_31, 5, 0, 1, 1)
        self.BO_method = QtGui.QComboBox(self.groupBox)
        self.BO_method.setObjectName(_fromUtf8("BO_method"))
        self.BO_method.addItem(_fromUtf8(""))
        self.BO_method.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.BO_method, 5, 1, 1, 1)
        self.label_32 = QtGui.QLabel(self.groupBox)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_3.addWidget(self.label_32, 5, 2, 1, 1)
        self.BO_ctr = QtGui.QLineEdit(self.groupBox)
        self.BO_ctr.setObjectName(_fromUtf8("BO_ctr"))
        self.gridLayout_3.addWidget(self.BO_ctr, 5, 3, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.line_3 = QtGui.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_5.addWidget(self.line_3)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_30 = QtGui.QLabel(self.groupBox)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.horizontalLayout_3.addWidget(self.label_30)
        self.lineEdit_14 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.horizontalLayout_3.addWidget(self.lineEdit_14)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOptionPricer = QtGui.QMenu(self.menubar)
        self.menuOptionPricer.setObjectName(_fromUtf8("menuOptionPricer"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionTest_1 = QtGui.QAction(MainWindow)
        self.actionTest_1.setObjectName(_fromUtf8("actionTest_1"))
        self.actionTest_2 = QtGui.QAction(MainWindow)
        self.actionTest_2.setObjectName(_fromUtf8("actionTest_2"))
        self.actionManual = QtGui.QAction(MainWindow)
        self.actionManual.setObjectName(_fromUtf8("actionManual"))
        self.menuOptionPricer.addSeparator()
        self.menuOptionPricer.addAction(self.actionTest_1)
        self.menuOptionPricer.addAction(self.actionTest_2)
        self.menuHelp.addAction(self.actionManual)
        self.menubar.addAction(self.menuOptionPricer.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QObject.connect(self.pushButton_5,QtCore.SIGNAL(_fromUtf8("clicked()")), self.EO_button_clicked)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL(_fromUtf8("clicked()")), self.Vol_button_clicked)
        QtCore.QObject.connect(self.pushButton_2,QtCore.SIGNAL(_fromUtf8("clicked()")), self.BO_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def EO_button_clicked(self):
        s = float(self.EO_s.text())
        k = float(self.EO_k.text())
        t = float(self.EO_t.text())
        sigma = float(self.EO_sigma.text())
        r = float(self.EO_r.text())

        if (self.EO_type.currentIndex() == 1 and self.EO_Method.currentIndex() == 0):
            self.lineEdit_12.setText( str(eurOptionBSformulas(s,k,t,sigma,r,"C")) )
        elif (self.EO_type.currentIndex() == 0 and self.EO_Method.currentIndex() == 0):
            self.lineEdit_12.setText( str(eurOptionBSformulas(s,k,t,sigma,r,"P")) )
        elif (self.EO_Method.currentIndex() == 1 and self.EO_type.currentIndex() == 1):
            self.lineEdit_12.setText( str(geoAsianCPCal(s,k,sigma,r,t, int(self.EO_n.text()), "C")))
        elif (self.EO_Method.currentIndex() == 1 and self.EO_type.currentIndex() == 0):
            self.lineEdit_12.setText( str(geoAsianCPCal(s,k,sigma,r,t, int(self.EO_n.text()), "P")))
        elif (self.EO_Method.currentIndex() == 2):
            n = int(self.EO_n.text())
            m = int(self.EO_m.text())
            ctl = bool(self.EO_variate.text())
            if (self.EO_type.currentIndex() == 0):
                type = "P"
            else:
                type = "C"
            self.lineEdit_12.setText(str( arithAsianCPCal(s,k,sigma,r,t,n,type,m,ctl) ))
        elif (self.EO_Method.currentIndex() == 3):
            if (self.EO_type.currentIndex() == 0):
                type = "P"
            else:
                type = "C"
            n = int(self.EO_n.text())
            ans = binominalTree(s,sigma,r,t,k,n,type)
            print (ans)
            self.lineEdit_12.setText(str( binominalTree(s,sigma,r,t,k,n,type)))

    def Vol_button_clicked(self):
        value = float(self.Vol_pre.text())
        s = float(self.Vol_s.text())
        k = float(self.Vol_k.text())
        r = float(self.Vol_r.text())
        q = float(self.Vol_q.text())
        t = float(self.Vol_t.text())
        if (self.Vol_type.currentIndex() == 0):
                type = "P"
        else:
                type = "C"
        self.Vol_ans.setText( str(impliedVolCal(type,value,s,k,0,t,r,q)) )

    def BO_button_clicked(self):
        if (self.BO_type.currentIndex() == 0):
                type = "P"
        else:
                type = "C"
        s1 = float(self.BO_s1.text())
        s2 = float(self.BO_s2.text())
        sigma1 = float(self.Vol_sigma1.text())
        sigma2 = float(self.BO_sigma2.text())
        k = float(self.BO_k.text())
        cor = float(self.BO_cor.text())
        r = float(self.BO_r.text())
        t = float(self.BO_t.text())
        if (self.BO_method.currentIndex() == 0):
            m = int(self.BO_m.text())
            ctl = int(self.BO_ctr.text())
            self.lineEdit_14.setText(str(arithAsianBasketCPCal(s1,s2,k,sigma1,sigma2,cor,r,t,m,type,ctl)))
        else:
            self.lineEdit_14.setText( str( geoAsianBasketCPCal(s1,s2,k,sigma1,sigma2,cor,r,t,type)))


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.EuropeanOption.setTitle(_translate("MainWindow", "Single Option Price", None))
        self.label_12.setText(_translate("MainWindow", "Option type:", None))
        self.label_14.setText(_translate("MainWindow", " Spot price of asset S(0):", None))
        self.label_11.setText(_translate("MainWindow", " Time to maturity (in years) T:", None))
        self.label_9.setText(_translate("MainWindow", " Volatility σ:", None))
        self.label_13.setText(_translate("MainWindow", " Strike K:", None))
        self.label_10.setText(_translate("MainWindow", " Risk-free interest rate r:", None))
        self.EO_type.setItemText(0, _translate("MainWindow", "Put Option", None))
        self.EO_type.setItemText(1, _translate("MainWindow", "Call Option", None))
        self.EO_Method.setItemText(0, _translate("MainWindow", "European Option", None))
        self.EO_Method.setItemText(1, _translate("MainWindow", "Geometric Asian Option", None))
        self.EO_Method.setItemText(2, _translate("MainWindow", "Arithmetic Asian Option", None))
        self.EO_Method.setItemText(3, _translate("MainWindow", "Binominal Tree", None))
        self.label_17.setText(_translate("MainWindow", "The number of steps N:", None))
        self.label_16.setText(_translate("MainWindow", "Option Method:", None))
        self.label_18.setText(_translate("MainWindow", "Control variate:", None))
        self.label_26.setText(_translate("MainWindow", "The number of paths M:", None))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton", None))
        self.label_6.setText(_translate("MainWindow", "Option Price:", None))
        self.ImpliedVol.setTitle(_translate("MainWindow", "Implied Volatility Calculator", None))
        self.label_15.setText(_translate("MainWindow", " Spot price of asset S(0):", None))
        self.label.setText(_translate("MainWindow", "Risk-free interest rate r:", None))
        self.label_5.setText(_translate("MainWindow", "Option premium:", None))
        self.label_4.setText(_translate("MainWindow", " Strike K:", None))
        self.label_2.setText(_translate("MainWindow", "Repo rate q:", None))
        self.label_3.setText(_translate("MainWindow", " Time to maturity (in years) T:", None))
        self.label_7.setText(_translate("MainWindow", "Option type:", None))
        self.Vol_type.setItemText(0, _translate("MainWindow", "Put option", None))
        self.Vol_type.setItemText(1, _translate("MainWindow", "Call option", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.label_8.setText(_translate("MainWindow", "Option Price:", None))
        self.groupBox.setTitle(_translate("MainWindow", "Basket Option Price", None))
        self.label_23.setText(_translate("MainWindow", " Volatility σ2:", None))
        self.label_21.setText(_translate("MainWindow", "Strike K:", None))
        self.label_25.setText(_translate("MainWindow", "Risk-free interest rate r:", None))
        self.label_27.setText(_translate("MainWindow", " Time to maturity (in years) T:", None))
        self.label_29.setText(_translate("MainWindow", "The number of paths M:", None))
        self.label_24.setText(_translate("MainWindow", "Correlation:", None))
        self.label_20.setText(_translate("MainWindow", "Spot price of asset S2(0):", None))
        self.label_22.setText(_translate("MainWindow", " Volatility σ1:", None))
        self.label_28.setText(_translate("MainWindow", "Option type:", None))
        self.BO_type.setItemText(0, _translate("MainWindow", "Put Option", None))
        self.BO_type.setItemText(1, _translate("MainWindow", "Call Option", None))
        self.label_19.setText(_translate("MainWindow", "Spot price of asset S1(0):", None))
        self.label_31.setText(_translate("MainWindow", "Option Method:", None))
        self.BO_method.setItemText(0, _translate("MainWindow", "Arithmatic Basket Option", None))
        self.BO_method.setItemText(1, _translate("MainWindow", "Geometric Basket Option", None))
        self.label_32.setText(_translate("MainWindow", "Control variate:", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.label_30.setText(_translate("MainWindow", "Option Price:", None))
        self.menuOptionPricer.setTitle(_translate("MainWindow", "OptionPricer", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionTest_1.setText(_translate("MainWindow", "test 1", None))
        self.actionTest_2.setText(_translate("MainWindow", "test 2", None))
        self.actionManual.setText(_translate("MainWindow", "manual", None))


#----------------------------------------------------------------------------------
"""European option"""
def eurOptionBSformulas(S,K,T,sigma,r,type):
    d1 = (log(S/K)+r*(T)) / (sigma*sqrt(T)) + 0.5*sigma*sqrt(T)
    d2 = (log(S/K)+r*(T)) / (sigma*sqrt(T)) - 0.5*sigma*sqrt(T)
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    Nd1n = norm.cdf(-d1)
    Nd2n = norm.cdf(-d2)
    C = S*Nd1 - K*exp(-r*(T))*Nd2
    P = K*exp(-r*(T))*Nd2n - S*Nd1n
    if type == 'C':
        return C
    if type == 'P':
        return P
"""Implied volatility calculation"""
def impliedVolCal(callput, value, S, K, t, T, r, q):
	sigma = sqrt(2 * abs((log(S/K) + (r-q)*(T-t)) / (T-t)))
	tol = 1e-5
	sigmadiff = 1
	for i in range(0,100):
		f = fx(callput, value, S, K, t, T, sigma, r, q)
		fprime = fxDe(S, K, t, T, sigma, r, q)
		sigmaNew = sigma - f/fprime
		sigmadiff = abs(sigmaNew - sigma)
		if sigmadiff < tol:
			return sigmaNew
		sigma = sigmaNew
	return 'NaN'
def fx(callput, value, S, K, t, T, sigma, r, q):
	d1 = (log(S/K)+(r-q)*(T-t)) / (sigma*sqrt(T-t)) + 0.5*sigma*sqrt(T-t)
	d2 = (log(S/K)+(r-q)*(T-t)) / (sigma*sqrt(T-t)) - 0.5*sigma*sqrt(T-t)
	Nd1 = norm.cdf(d1)
	Nd2 = norm.cdf(d2)
	Nd1n = norm.cdf(-d1)
	Nd2n = norm.cdf(-d2)
	C = S*exp(-q*(T-t))*Nd1 - K*exp(-r*(T-t))*Nd2
	P = K*exp(-r*(T-t))*Nd2n - S*exp(-q*(T-t))*Nd1n
	if callput == 'C':
		return C-value
	if callput == 'P':
		return P-value

def fxDe(S, K, t, T, sigma, r, q):
	d1 = (log(S/K)+(r-q)*(T-t)) / (sigma*sqrt(T-t)) + 0.5*sigma*sqrt(T-t)
	yprime = S*exp(-q*(T-t))*sqrt(T-t)*norm.pdf(d1)
	return yprime


"""Geometric Asian call/put option"""
def geoAsianCPCal(S, K, sigma, r, T, n, type):
    sigsqT = pow(sigma,2)*T*(n+1)*(2*n+1)/(6*n*n)
    muT = 0.5*sigsqT + (r-0.5*pow(sigma,2))*T*(n+1)/(2*n)
    d1 = (log(S/K) +(muT + 0.5*sigsqT))/sqrt(sigsqT)
    d2 = d1 - sqrt(sigsqT)
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    Nd1n = norm.cdf(-d1)
    Nd2n = norm.cdf(-d2)
    if type == 'C':
        geo = exp(-r*T)*(S*exp(muT)*Nd1 - K*Nd2)
    if type == 'P':
        geo = exp(-r*T)*(-S*exp(muT)*Nd1n + K*Nd2n)
    return geo

"""Geometric Asian basket call/put option"""
def geoAsianBasketCPCal(S1,S2,K, sigma1,sigma2,cor, r, T, type):
    S = sqrt((S1*S2))
    sigsqT = (pow(sigma1,2)+pow(sigma2,2)+2*sigma1*sigma2*cor)*T/(4)

    muT = 0.5*sigsqT + (r - 0.5 * (pow(sigma1,2)+pow(sigma2,2))/2)*T
    d1 = (log(S/K) +(muT + 0.5*sigsqT))/sqrt(sigsqT)
    d2 = d1 - sqrt(sigsqT)

    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    Nd1n = norm.cdf(-d1)
    Nd2n = norm.cdf(-d2)
    if type == 'C':
        geo = exp(-r*T)*(S*exp(muT)*Nd1 - K*Nd2)
    if type == 'P':
        geo = exp(-r*T)*(-S*exp(muT)*Nd1n + K*Nd2n)
    return geo

"""Control variates for Arithmetric Asian Option"""
def arithAsianCPCal(S, K, sigma, r, T, n, type,M,ctl):
    numpy.random.seed(1000)
    Dt = float(T)/n
    drift = exp((r-0.5*pow(sigma,2))*Dt)
    Spath = [None]*n
    arithPayoff =[None]*M
    geoPayoff = [None]*M
    for i in range(0,M):
        growthFactor =  drift * exp(sigma*sqrt(Dt)*numpy.random.randn())
        Spath[0] = S * growthFactor
        for j in range(1,n):
            growthFactor =  drift * exp(sigma*sqrt(Dt)*numpy.random.randn())
            Spath[j] = Spath[j-1] * growthFactor
        arithMean = numpy.mean(Spath)
        geoMean = exp(1.0/n*numpy.sum(numpy.log(Spath)))
        if type == 'C':
            arithPayoff[i] = exp(-r*T)*numpy.maximum(arithMean-K,0)
            geoPayoff[i] = exp(-r*T)*numpy.maximum(geoMean-K,0)

        if type == 'P':
            arithPayoff[i] = exp(-r*T)*numpy.maximum(K-arithMean,0)
            geoPayoff[i] = exp(-r*T)*numpy.maximum(K-geoMean,0)

    Pmean = numpy.mean(arithPayoff)
    Pstd = numpy.std(arithPayoff)
    confmlow, comfmup = Pmean-1.96*Pstd/sqrt(M), Pmean+1.96*Pstd/sqrt(M)
    if ctl == 0:
        return confmlow, comfmup

    """Control variate"""
    covXY = numpy.mean(numpy.multiply(arithPayoff,geoPayoff))- numpy.mean(arithPayoff)*numpy.mean(geoPayoff)
    theta = covXY/numpy.var(geoPayoff)
    geo = geoAsianCPCal(S, K, sigma, r, T, n, type)

    Z = numpy.add(arithPayoff, numpy.multiply(theta , (numpy.subtract(geo,geoPayoff))))
    Zmean = numpy.mean(Z)
    Zstd = numpy.std(Z)

    confcvlow,confcvup = Zmean - 1.96*Zstd/sqrt(M), Zmean + 1.96*Zstd/sqrt(M)

    if ctl == 1:
        return confcvlow, confcvup

"""Control variates for Arithmetric Asian Basket Option"""
def arithAsianBasketCPCal(S1,S2,K, sigma1,sigma2,cor, r, T, M, type, ctl):
    numpy.random.seed(1000)
    arithPayoff =[None]*M
    geoPayoff = [None]*M
    for i in range(0,M):
        rdn1 = numpy.random.randn()
        S1T = S1 * exp( (r-0.5*pow(sigma1, 2)) * T + sigma1 * sqrt(T) * rdn1 )
        rdn2 = cor * rdn1 + sqrt(1 - cor * cor) * numpy.random.randn()
        S2T = S2 * exp( (r-0.5*pow(sigma2, 2)) * T + sigma2 * sqrt(T) * rdn2 )

        arithMean = (S1T+S2T)/2
        geoMean = sqrt(S1T * S2T)
        if type == 'C':
            arithPayoff[i] = exp(-r*T)*numpy.maximum(arithMean-K,0)
            geoPayoff[i] = exp(-r*T)*numpy.maximum(geoMean-K,0)

        if type == 'P':
            arithPayoff[i] = exp(-r*T)*numpy.maximum(K-arithMean,0)
            geoPayoff[i] = exp(-r*T)*numpy.maximum(K-geoMean,0)

    Pmean = numpy.mean(arithPayoff)
    Pstd = numpy.std(arithPayoff)
    confmlow, comfmup = Pmean-1.96*Pstd/sqrt(M), Pmean+1.96*Pstd/sqrt(M)
    if ctl == 0:
        return confmlow, comfmup

    """Control variate"""
    covXY = numpy.mean(numpy.multiply(arithPayoff,geoPayoff))- numpy.mean(arithPayoff)*numpy.mean(geoPayoff)
    theta = covXY/numpy.var(geoPayoff)

    geo = geoAsianBasketCPCal(S1,S2,K,sigma1,sigma2,cor, r, T,  type)
    Z = numpy.add(arithPayoff, numpy.multiply(theta , (numpy.subtract(geo,geoPayoff))))
    Zmean = numpy.mean(Z)
    Zstd = numpy.std(Z)

    confcvlow,confcvup = Zmean - 1.96*Zstd/sqrt(M), Zmean + 1.96*Zstd/sqrt(M)

    if ctl == 1:
        return confcvlow, confcvup


def binominalTree(S, sigma, r, T, K, N, optionType):
	t = T/N
	u = exp(sigma*sqrt(t))
	d = exp(-sigma*sqrt(t))
	p = (exp(r*t)-d) / (u-d)
	StockPrice = {0: [S]}
	for n in range(N):
		StockPrice[n+1] = []
		for price in StockPrice[n]:
			StockPrice[n+1].append(price*u)
		StockPrice[n+1].append(StockPrice[n][-1] * d)

	OptionPrice = {N: []}
	if optionType == 'C':
		for price in StockPrice[N]:
			if price > K:
				OptionPrice[N].append(price-K)
			else:
				OptionPrice[N].append(0.0)
		for n in range(N)[::-1]:
			OptionPrice[n] = []
			for i in range(len(OptionPrice[n+1])-1):
				fu = OptionPrice[n+1][i]
				fd = OptionPrice[n+1][i+1]
				f = exp(-r*t) * (p*fu+(1-p)*fd)
				OptionPrice[n].append( max(f, StockPrice[n][i]-K) )
	if optionType == 'P':
		for price in StockPrice[N]:
			if price < K:
				OptionPrice[N].append(K-price)
			else:
				OptionPrice[N].append(0.0)
		for n in range(N)[::-1]:
			OptionPrice[n] = []
			for i in range(len(OptionPrice[n+1])-1):
				fu = OptionPrice[n+1][i]
				fd = OptionPrice[n+1][i+1]
				f = exp(-r*t) * (p*fu+(1-p)*fd)
				OptionPrice[n].append( max(f, K-StockPrice[n][i]) )
	return OptionPrice[0][0]


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = Ui_MainWindow()
    main_window.show()
    sys.exit(app.exec())
