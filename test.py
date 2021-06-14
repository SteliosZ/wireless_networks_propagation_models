from PyQt5 import QtCore, QtGui, QtWidgets, QtWebKitWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import numpy as np
import math
import traceback
import webbrowser
import matplotlib.pyplot as plt
from pyqtgraph import PlotWidget, plot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from functools import partial
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import warnings

warnings.filterwarnings("ignore")

pathLoss = 0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 624)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("antenna1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.OutdoorTab = QtWidgets.QWidget()
        self.OutdoorTab.setObjectName("OutdoorTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.OutdoorTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.OutdoorTab)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.FreeSpaceTab = QtWidgets.QWidget()
        self.FreeSpaceTab.setObjectName("FreeSpaceTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.FreeSpaceTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.freeSpaceWidget = QtWidgets.QWidget(self.FreeSpaceTab)
        self.freeSpaceWidget.setObjectName("freeSpaceWidget")
        self.gridLayout_3.addWidget(self.freeSpaceWidget, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.FreeSpaceTab)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.frequencyLabel = QtWidgets.QLabel(self.groupBox)
        self.frequencyLabel.setObjectName("frequencyLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frequencyLabel)
        self.freeSpaceFrequency = QtWidgets.QSpinBox(self.groupBox)
        self.freeSpaceFrequency.setMouseTracking(True)
        self.freeSpaceFrequency.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.freeSpaceFrequency.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.freeSpaceFrequency.setMinimum(0)
        self.freeSpaceFrequency.setMaximum(100000000)
        self.freeSpaceFrequency.setObjectName("freeSpaceFrequency")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.freeSpaceFrequency)
        self.distanceLabel = QtWidgets.QLabel(self.groupBox)
        self.distanceLabel.setObjectName("distanceLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.distanceLabel)
        self.freeSpaceDistance = QtWidgets.QSpinBox(self.groupBox)
        self.freeSpaceDistance.setMaximum(9999999)
        self.freeSpaceDistance.setObjectName("freeSpaceDistance")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.freeSpaceDistance)
        self.baseLabel_4 = QtWidgets.QLabel(self.groupBox)
        self.baseLabel_4.setObjectName("baseLabel_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.baseLabel_4)
        self.freeSpaceBase = QtWidgets.QSpinBox(self.groupBox)
        self.freeSpaceBase.setEnabled(False)
        self.freeSpaceBase.setReadOnly(True)
        self.freeSpaceBase.setMinimum(30)
        self.freeSpaceBase.setMaximum(30)
        self.freeSpaceBase.setObjectName("freeSpaceBase")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.freeSpaceBase)
        self.mobileLabel_4 = QtWidgets.QLabel(self.groupBox)
        self.mobileLabel_4.setObjectName("mobileLabel_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.mobileLabel_4)
        self.freeSpaceMobile = QtWidgets.QSpinBox(self.groupBox)
        self.freeSpaceMobile.setEnabled(False)
        self.freeSpaceMobile.setReadOnly(True)
        self.freeSpaceMobile.setMinimum(1)
        self.freeSpaceMobile.setMaximum(1)
        self.freeSpaceMobile.setObjectName("freeSpaceMobile")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.freeSpaceMobile)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.FreeSpaceBtn = QtWidgets.QPushButton(self.groupBox)
        self.FreeSpaceBtn.setObjectName("FreeSpaceBtn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.FreeSpaceBtn)
        self.gridLayout_23.addLayout(self.formLayout, 0, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.freeSpaceReport = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freeSpaceReport.sizePolicy().hasHeightForWidth())
        self.freeSpaceReport.setSizePolicy(sizePolicy)
        self.freeSpaceReport.setReadOnly(True)
        self.freeSpaceReport.setObjectName("freeSpaceReport")
        self.gridLayout_5.addWidget(self.freeSpaceReport, 0, 0, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_5, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.tabWidget_2.addTab(self.FreeSpaceTab, "")
        self.HataUrbanTab = QtWidgets.QWidget()
        self.HataUrbanTab.setObjectName("HataUrbanTab")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.HataUrbanTab)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.hataUrbanWidget = QtWidgets.QWidget(self.HataUrbanTab)
        self.hataUrbanWidget.setObjectName("hataUrbanWidget")
        self.gridLayout_13.addWidget(self.hataUrbanWidget, 0, 0, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.groupBox_3 = QtWidgets.QGroupBox(self.HataUrbanTab)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.frequencyLabel_5 = QtWidgets.QLabel(self.groupBox_3)
        self.frequencyLabel_5.setObjectName("frequencyLabel_5")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frequencyLabel_5)
        self.hataUrbanFrequency = QtWidgets.QSpinBox(self.groupBox_3)
        self.hataUrbanFrequency.setMouseTracking(True)
        self.hataUrbanFrequency.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hataUrbanFrequency.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.hataUrbanFrequency.setMinimum(150)
        self.hataUrbanFrequency.setMaximum(1500)
        self.hataUrbanFrequency.setObjectName("hataUrbanFrequency")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hataUrbanFrequency)
        self.distanceLabel_5 = QtWidgets.QLabel(self.groupBox_3)
        self.distanceLabel_5.setObjectName("distanceLabel_5")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.distanceLabel_5)
        self.hataUrbanDistance = QtWidgets.QSpinBox(self.groupBox_3)
        self.hataUrbanDistance.setMinimum(1)
        self.hataUrbanDistance.setMaximum(20)
        self.hataUrbanDistance.setObjectName("hataUrbanDistance")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.hataUrbanDistance)
        self.baseLabel_8 = QtWidgets.QLabel(self.groupBox_3)
        self.baseLabel_8.setObjectName("baseLabel_8")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.baseLabel_8)
        self.hataUrbanBase = QtWidgets.QSpinBox(self.groupBox_3)
        self.hataUrbanBase.setReadOnly(True)
        self.hataUrbanBase.setMinimum(30)
        self.hataUrbanBase.setMaximum(200)
        self.hataUrbanBase.setObjectName("hataUrbanBase")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.hataUrbanBase)
        self.mobileLabel_8 = QtWidgets.QLabel(self.groupBox_3)
        self.mobileLabel_8.setObjectName("mobileLabel_8")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.mobileLabel_8)
        self.hataUrbanMobile = QtWidgets.QSpinBox(self.groupBox_3)
        self.hataUrbanMobile.setReadOnly(True)
        self.hataUrbanMobile.setMinimum(1)
        self.hataUrbanMobile.setMaximum(10)
        self.hataUrbanMobile.setObjectName("hataUrbanMobile")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.hataUrbanMobile)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_5.setLayout(4, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_5)
        self.HataUrbanBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.HataUrbanBtn.setObjectName("HataUrbanBtn")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.HataUrbanBtn)
        self.gridLayout_27.addLayout(self.formLayout_5, 0, 0, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.hataUrbanReport = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hataUrbanReport.sizePolicy().hasHeightForWidth())
        self.hataUrbanReport.setSizePolicy(sizePolicy)
        self.hataUrbanReport.setReadOnly(True)
        self.hataUrbanReport.setObjectName("hataUrbanReport")
        self.gridLayout_15.addWidget(self.hataUrbanReport, 0, 0, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_15, 1, 0, 1, 1)
        self.gridLayout_14.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_14, 0, 1, 1, 1)
        self.tabWidget_2.addTab(self.HataUrbanTab, "")
        self.HataSuburbanTab = QtWidgets.QWidget()
        self.HataSuburbanTab.setObjectName("HataSuburbanTab")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.HataSuburbanTab)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.hataSuburbanWidget = QtWidgets.QWidget(self.HataSuburbanTab)
        self.hataSuburbanWidget.setObjectName("hataSuburbanWidget")
        self.gridLayout_16.addWidget(self.hataSuburbanWidget, 0, 0, 1, 1)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.groupBox_4 = QtWidgets.QGroupBox(self.HataSuburbanTab)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.frequencyLabel_6 = QtWidgets.QLabel(self.groupBox_4)
        self.frequencyLabel_6.setObjectName("frequencyLabel_6")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frequencyLabel_6)
        self.hataSuburbanFrequency = QtWidgets.QSpinBox(self.groupBox_4)
        self.hataSuburbanFrequency.setMinimum(150)
        self.hataSuburbanFrequency.setMaximum(1500)
        self.hataSuburbanFrequency.setObjectName("hataSuburbanFrequency")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hataSuburbanFrequency)
        self.distanceLabel_6 = QtWidgets.QLabel(self.groupBox_4)
        self.distanceLabel_6.setObjectName("distanceLabel_6")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.distanceLabel_6)
        self.hataSuburbanDistance = QtWidgets.QSpinBox(self.groupBox_4)
        self.hataSuburbanDistance.setMinimum(1)
        self.hataSuburbanDistance.setMaximum(20)
        self.hataSuburbanDistance.setObjectName("hataSuburbanDistance")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.hataSuburbanDistance)
        self.baseLabel = QtWidgets.QLabel(self.groupBox_4)
        self.baseLabel.setObjectName("baseLabel")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.baseLabel)
        self.hataSuburbanBase = QtWidgets.QSpinBox(self.groupBox_4)
        self.hataSuburbanBase.setMinimum(30)
        self.hataSuburbanBase.setMaximum(200)
        self.hataSuburbanBase.setObjectName("hataSuburbanBase")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.hataSuburbanBase)
        self.mobileLabel = QtWidgets.QLabel(self.groupBox_4)
        self.mobileLabel.setObjectName("mobileLabel")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.mobileLabel)
        self.hataSuburbanMobile = QtWidgets.QSpinBox(self.groupBox_4)
        self.hataSuburbanMobile.setMinimum(1)
        self.hataSuburbanMobile.setMaximum(10)
        self.hataSuburbanMobile.setObjectName("hataSuburbanMobile")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.hataSuburbanMobile)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.formLayout_6.setLayout(4, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_6)
        self.HataSuburbanBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.HataSuburbanBtn.setObjectName("HataSuburbanBtn")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.HataSuburbanBtn)
        self.gridLayout_21.addLayout(self.formLayout_6, 0, 0, 1, 1)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.hataSuburbanReport = QtWidgets.QLineEdit(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hataSuburbanReport.sizePolicy().hasHeightForWidth())
        self.hataSuburbanReport.setSizePolicy(sizePolicy)
        self.hataSuburbanReport.setReadOnly(True)
        self.hataSuburbanReport.setObjectName("hataSuburbanReport")
        self.gridLayout_18.addWidget(self.hataSuburbanReport, 0, 0, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_18, 1, 0, 1, 1)
        self.gridLayout_17.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_17, 0, 1, 1, 1)
        self.tabWidget_2.addTab(self.HataSuburbanTab, "")
        self.Cost231Tab = QtWidgets.QWidget()
        self.Cost231Tab.setObjectName("Cost231Tab")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.Cost231Tab)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.cost231Widget = QtWidgets.QWidget(self.Cost231Tab)
        self.cost231Widget.setObjectName("cost231Widget")
        self.gridLayout_19.addWidget(self.cost231Widget, 0, 0, 1, 1)
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.groupBox_5 = QtWidgets.QGroupBox(self.Cost231Tab)
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.frequencyLabel_7 = QtWidgets.QLabel(self.groupBox_5)
        self.frequencyLabel_7.setObjectName("frequencyLabel_7")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frequencyLabel_7)
        self.cost231Frequency = QtWidgets.QSpinBox(self.groupBox_5)
        self.cost231Frequency.setMinimum(1500)
        self.cost231Frequency.setMaximum(2000)
        self.cost231Frequency.setObjectName("cost231Frequency")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cost231Frequency)
        self.distanceLabel_7 = QtWidgets.QLabel(self.groupBox_5)
        self.distanceLabel_7.setObjectName("distanceLabel_7")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.distanceLabel_7)
        self.cost231Distance = QtWidgets.QSpinBox(self.groupBox_5)
        self.cost231Distance.setMinimum(1)
        self.cost231Distance.setMaximum(20)
        self.cost231Distance.setObjectName("cost231Distance")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cost231Distance)
        self.baseLabel_2 = QtWidgets.QLabel(self.groupBox_5)
        self.baseLabel_2.setObjectName("baseLabel_2")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.baseLabel_2)
        self.cost231Base = QtWidgets.QSpinBox(self.groupBox_5)
        self.cost231Base.setMinimum(30)
        self.cost231Base.setMaximum(200)
        self.cost231Base.setObjectName("cost231Base")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cost231Base)
        self.mobileLabel_2 = QtWidgets.QLabel(self.groupBox_5)
        self.mobileLabel_2.setObjectName("mobileLabel_2")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.mobileLabel_2)
        self.cost231Mobile = QtWidgets.QSpinBox(self.groupBox_5)
        self.cost231Mobile.setMinimum(1)
        self.cost231Mobile.setMaximum(10)
        self.cost231Mobile.setObjectName("cost231Mobile")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cost231Mobile)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.formLayout_7.setLayout(4, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_7)
        self.Cost231Btn = QtWidgets.QPushButton(self.groupBox_5)
        self.Cost231Btn.setObjectName("Cost231Btn")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Cost231Btn)
        self.gridLayout_33.addLayout(self.formLayout_7, 0, 0, 1, 1)
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.cost231Report = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cost231Report.sizePolicy().hasHeightForWidth())
        self.cost231Report.setSizePolicy(sizePolicy)
        self.cost231Report.setReadOnly(True)
        self.cost231Report.setObjectName("cost231Report")
        self.gridLayout_22.addWidget(self.cost231Report, 0, 0, 1, 1)
        self.gridLayout_33.addLayout(self.gridLayout_22, 1, 0, 1, 1)
        self.gridLayout_20.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_20, 0, 1, 1, 1)
        self.tabWidget_2.addTab(self.Cost231Tab, "")
        self.gridLayout_2.addWidget(self.tabWidget_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.OutdoorTab, "")
        self.IndoorTab = QtWidgets.QWidget()
        self.IndoorTab.setObjectName("IndoorTab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.IndoorTab)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.IndoorTab)
        self.tabWidget_3.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.ITUTab = QtWidgets.QWidget()
        self.ITUTab.setObjectName("ITUTab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.ITUTab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ITUWidget = QtWidgets.QWidget(self.ITUTab)
        self.ITUWidget.setObjectName("ITUWidget")
        self.gridLayout_7.addWidget(self.ITUWidget, 0, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_2 = QtWidgets.QGroupBox(self.ITUTab)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.frequencyLabel_3 = QtWidgets.QLabel(self.groupBox_2)
        self.frequencyLabel_3.setObjectName("frequencyLabel_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frequencyLabel_3)
        self.ITUFrequency = QtWidgets.QSpinBox(self.groupBox_2)
        self.ITUFrequency.setMouseTracking(True)
        self.ITUFrequency.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ITUFrequency.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITUFrequency.setMinimum(900)
        self.ITUFrequency.setMaximum(5200)
        self.ITUFrequency.setObjectName("ITUFrequency")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ITUFrequency)
        self.distanceLabel_3 = QtWidgets.QLabel(self.groupBox_2)
        self.distanceLabel_3.setObjectName("distanceLabel_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.distanceLabel_3)
        self.ITUDistance = QtWidgets.QSpinBox(self.groupBox_2)
        self.ITUDistance.setMinimum(1)
        self.ITUDistance.setMaximum(30)
        self.ITUDistance.setObjectName("ITUDistance")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ITUDistance)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_3.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_3)
        self.ITUBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.ITUBtn.setObjectName("ITUBtn")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ITUBtn)
        self.gridLayout_25.addLayout(self.formLayout_3, 0, 1, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.ITUReport = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ITUReport.sizePolicy().hasHeightForWidth())
        self.ITUReport.setSizePolicy(sizePolicy)
        self.ITUReport.setReadOnly(True)
        self.ITUReport.setObjectName("ITUReport")
        self.gridLayout_10.addWidget(self.ITUReport, 0, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_10, 1, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_9, 0, 1, 1, 1)
        self.tabWidget_3.addTab(self.ITUTab, "")
        self.LongDistanceTab = QtWidgets.QWidget()
        self.LongDistanceTab.setObjectName("LongDistanceTab")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.LongDistanceTab)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.LongDistanceWidget = QtWidgets.QWidget(self.LongDistanceTab)
        self.LongDistanceWidget.setObjectName("LongDistanceWidget")
        self.gridLayout_28.addWidget(self.LongDistanceWidget, 0, 0, 1, 1)
        self.gridLayout_29 = QtWidgets.QGridLayout()
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.groupBox_6 = QtWidgets.QGroupBox(self.LongDistanceTab)
        self.groupBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_49 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.frequencyLabel_8 = QtWidgets.QLabel(self.groupBox_6)
        self.frequencyLabel_8.setObjectName("frequencyLabel_8")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frequencyLabel_8)
        self.LongDistanceFrequency = QtWidgets.QSpinBox(self.groupBox_6)
        self.LongDistanceFrequency.setMinimum(0)
        self.LongDistanceFrequency.setMaximum(999999999)
        self.LongDistanceFrequency.setObjectName("LongDistanceFrequency")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LongDistanceFrequency)
        self.distanceLabel_8 = QtWidgets.QLabel(self.groupBox_6)
        self.distanceLabel_8.setObjectName("distanceLabel_8")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.distanceLabel_8)
        self.LongDistanceDistance = QtWidgets.QSpinBox(self.groupBox_6)
        self.LongDistanceDistance.setMinimum(1)
        self.LongDistanceDistance.setMaximum(30)
        self.LongDistanceDistance.setObjectName("LongDistanceDistance")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LongDistanceDistance)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.formLayout_8.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_8)
        self.LongDistanceBtn = QtWidgets.QPushButton(self.groupBox_6)
        self.LongDistanceBtn.setObjectName("LongDistanceBtn")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.LongDistanceBtn)
        self.gridLayout_49.addLayout(self.formLayout_8, 0, 0, 1, 1)
        self.gridLayout_30 = QtWidgets.QGridLayout()
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.LongDistanceReport = QtWidgets.QLineEdit(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LongDistanceReport.sizePolicy().hasHeightForWidth())
        self.LongDistanceReport.setSizePolicy(sizePolicy)
        self.LongDistanceReport.setReadOnly(True)
        self.LongDistanceReport.setObjectName("LongDistanceReport")
        self.gridLayout_30.addWidget(self.LongDistanceReport, 0, 0, 1, 1)
        self.gridLayout_49.addLayout(self.gridLayout_30, 1, 0, 1, 1)
        self.gridLayout_29.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.gridLayout_28.addLayout(self.gridLayout_29, 0, 1, 1, 1)
        self.tabWidget_3.addTab(self.LongDistanceTab, "")
        self.gridLayout_11.addWidget(self.tabWidget_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.IndoorTab, "")
        self.HelpTab = QtWidgets.QWidget()
        self.HelpTab.setObjectName("HelpTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.HelpTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.textEdit = QtWidgets.QTextEdit(self.HelpTab)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_12.addWidget(self.textEdit, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_24 = QtWidgets.QGridLayout()
        self.gridLayout_24.setObjectName("gridLayout_24")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_24.addItem(spacerItem, 0, 0, 1, 1)
        self.OpenPDFBtn = QtWidgets.QPushButton(self.HelpTab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pdf1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.OpenPDFBtn.setIcon(icon1)
        self.OpenPDFBtn.setObjectName("OpenPDFBtn")
        self.gridLayout_24.addWidget(self.OpenPDFBtn, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_24.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_24, 1, 0, 1, 1)
        self.tabWidget.addTab(self.HelpTab, "")
        self.AboutTab = QtWidgets.QWidget()
        self.AboutTab.setObjectName("AboutTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.AboutTab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label = QtWidgets.QLabel(self.AboutTab)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(0)
        self.label.setMidLineWidth(0)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("report2.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.AboutTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(3)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Events
        self.FreeSpaceBtn.clicked.connect(partial(self.freespacePathLoss, MainWindow))
        self.HataUrbanBtn.clicked.connect(partial(self.hataurbanPathLoss, MainWindow))
        self.HataSuburbanBtn.clicked.connect(partial(self.hatasuburbanPathLoss, MainWindow))
        self.Cost231Btn.clicked.connect(partial(self.cost231PathLoss, MainWindow))
        self.ITUBtn.clicked.connect(partial(self.ITUPathLoss, MainWindow))
        self.LongDistanceBtn.clicked.connect(partial(self.LongDistancePathLoss, MainWindow))
        self.OpenPDFBtn.clicked.connect(self.open_pdf)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(3)
        self.tabWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Radio Waves Propagation Models"))
        self.groupBox.setTitle(_translate("MainWindow", "Propagation Outdoor Parameters"))
        self.frequencyLabel.setText(_translate("MainWindow", "Frequency (MHz)                                "))
        self.distanceLabel.setText(_translate("MainWindow", "Distance (Km)"))
        self.baseLabel_4.setText(_translate("MainWindow", "Base Station Height (m)"))
        self.mobileLabel_4.setText(_translate("MainWindow", "Mobile Station Height (m)"))
        self.FreeSpaceBtn.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.FreeSpaceTab), _translate("MainWindow", "Free Space"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Propagation Outdoor Parameters"))
        self.frequencyLabel_5.setText(_translate("MainWindow", "Frequency (MHz)                                "))
        self.distanceLabel_5.setText(_translate("MainWindow", "Distance (Km)"))
        self.baseLabel_8.setText(_translate("MainWindow", "Base Station Height (m)"))
        self.mobileLabel_8.setText(_translate("MainWindow", "Mobile Station Height (m)"))
        self.HataUrbanBtn.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.HataUrbanTab), _translate("MainWindow", "Hata Urban"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Propagation Outdoor Parameters"))
        self.frequencyLabel_6.setText(_translate("MainWindow", "Frequency (MHz)                                "))
        self.distanceLabel_6.setText(_translate("MainWindow", "Distance (Km)"))
        self.baseLabel.setText(_translate("MainWindow", "Base Station Height (m)"))
        self.mobileLabel.setText(_translate("MainWindow", "Mobile Station Height (m)"))
        self.HataSuburbanBtn.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.HataSuburbanTab),
                                    _translate("MainWindow", "Hata Suburban"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Propagation Outdoor Parameters"))
        self.frequencyLabel_7.setText(_translate("MainWindow", "Frequency (MHz)                                "))
        self.distanceLabel_7.setText(_translate("MainWindow", "Distance (Km)"))
        self.baseLabel_2.setText(_translate("MainWindow", "Base Station Height (m)"))
        self.mobileLabel_2.setText(_translate("MainWindow", "Mobile Station Height (m)"))
        self.Cost231Btn.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Cost231Tab), _translate("MainWindow", "Cost 231"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OutdoorTab), _translate("MainWindow", "Outdoor"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Propagation Indoor Parameters"))
        self.frequencyLabel_3.setText(_translate("MainWindow", "Frequency (MHz)                                "))
        self.distanceLabel_3.setText(_translate("MainWindow", "Distance (Km)"))
        self.ITUBtn.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.ITUTab), _translate("MainWindow", "ITU"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Propagation Indoor Parameters"))
        self.frequencyLabel_8.setText(_translate("MainWindow", "Frequency (MHz)                                "))
        self.distanceLabel_8.setText(_translate("MainWindow", "Distance (Km)"))
        self.LongDistanceBtn.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.LongDistanceTab),
                                    _translate("MainWindow", "Long-Distance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.IndoorTab), _translate("MainWindow", "Indoor"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#588bc1;\">Radio Waves</span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#588bc1;\">Propagation Models</span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline; color:#588bc1;\">                                                                                                                             </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ca0000;\">Advanced Topics in Antennas, Propagation of EMF fields, and Wireless Networks</span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#588bc1;\">Term Project - June 15, 2020</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#588bc1;\"><br /></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#588bc1;\">Χάρης Σάββα ΜΠ218</span><span style=\" font-size:12pt; color:#588bc1;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#588bc1;\">Αριστέα Τερεζάκη ΜΠ233</span><span style=\" font-size:12pt; color:#588bc1;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#588bc1;\">Ιωάννης Γεώργιος Κεφαλούκος ΜΠ224</span><span style=\" font-size:12pt; color:#588bc1;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline; color:#588bc1;\">                                                        </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ca0000;\">Hellenic Mediterranean University</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; color:#ca0000;\"><br /></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; color:#ca0000;\"><br /></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; color:#ca0000;\"><br /></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; color:#ca0000;\"><br /></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; color:#ca0000;\"><br /></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"OP\"></a><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">O</span><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">utdoor Propagation Models</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"OP1\"></a><span style=\" font-size:16pt; font-weight:600;\">1</span><span style=\" font-size:16pt; font-weight:600;\">.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><a href=\"#OP11\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#0000ff;\">Cost Hata Model</span></a><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"OP2\"></a><span style=\" font-size:16pt; font-weight:600;\">2</span><span style=\" font-size:16pt; font-weight:600;\">.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><a href=\"#OP22\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#0000ff;\">Free Space path loss</span></a><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"OP3\"></a><span style=\" font-size:16pt; font-weight:600; color:#202122;\">3</span><span style=\" font-size:16pt; font-weight:600; color:#202122;\">.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#202122;\">    </span><a href=\"#OP33\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#0000ff; background-color:#ffffff;\">Hata model for Urban areas</span></a><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"OP4\"></a><span style=\" font-size:16pt; font-weight:600; color:#202122;\">4</span><span style=\" font-size:16pt; font-weight:600; color:#202122;\">.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#202122;\">    </span><a href=\"#OP44\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#0000ff; background-color:#ffffff;\">Hata model for Suburban areas</span></a><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#202122; background-color:#ffffff;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Indoor Propagation Models</span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"IP1\"></a><span style=\" font-size:16pt; font-weight:600;\">1</span><span style=\" font-size:16pt; font-weight:600;\">.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><a href=\"#IP11\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#0000ff;\">ITU model for indoor attenuation</span></a><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"IP2\"></a><span style=\" font-size:16pt; font-weight:600; color:#202122;\">2</span><span style=\" font-size:16pt; font-weight:600; color:#202122;\">.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#202122;\">    </span><a href=\"#IP22\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#0000ff; background-color:#ffffff;\">Log- distance path loss model</span></a><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"OP11\"></a><a href=\"#OP1\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#0000ff;\">C</span></a><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#0000ff;\">ost Hata Model</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:12pt; color:#202122;\">The </span><span style=\" font-size:12pt; font-weight:600; color:#202122;\">COST Hata model</span><span style=\" font-size:12pt; color:#202122;\"> is </span><span style=\" font-size:12pt; color:#000000;\">a radio propagation model </span><span style=\" font-size:12pt; color:#202122;\">(i.e. path loss) that extends the urban </span><span style=\" font-size:12pt; color:#000000;\">Hata model </span><span style=\" font-size:12pt; color:#202122;\">(which in turn is based on the </span><span style=\" font-size:12pt; color:#000000;\">Okumura model</span><span style=\" font-size:12pt; color:#202122;\">) to cover a more elaborated range of frequencies (up to 2 GHz). It is the most often cited of the COST 231 models (EU funded research project ca. April 1986 – April 1996), also called the </span><span style=\" font-size:12pt; font-style:italic; color:#202122;\">Hata Model PCS Extension</span><span style=\" font-size:12pt; color:#202122;\">. </span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:12pt; color:#000000;\">COST</span><span style=\" font-size:12pt; color:#202122;\"> (COopération européenne dans le domaine de la recherche Scientifique et Technique) is a European Union Forum for cooperative scientific research which has developed this model based on experimental measurements in multiple cities across Europe.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">Applicable to:</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\">This model is applicable to macro cells in urban areas. To further evaluate Path Loss in suburban or rural (quasi-)open areas, this path loss has to be substituted into </span><span style=\" font-size:12pt; font-style:italic; color:#202122; background-color:#ffffff;\">Urban to Rural</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> / </span><span style=\" font-size:12pt; font-style:italic; color:#202122; background-color:#ffffff;\">Urban to Suburban</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> Conversions. (Ray GAO, 09 Sep 2007)</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10.5pt; font-style:italic; text-decoration: underline; color:#202122;\">Coverage:</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Symbol\'; font-size:10pt; color:#202122;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#202122;\">         </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10.5pt; color:#202122;\">Frequency: 1500–2000 MHz</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Symbol\'; font-size:10pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">         </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10.5pt; color:#000000;\">Mobile station antenna height: 1–10 m</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Symbol\'; font-size:10pt; color:#202122;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#202122;\">         </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10.5pt; color:#000000;\">Base station antenna </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10.5pt; color:#202122;\">height: 30–200 m</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Symbol\'; font-size:10pt; color:#202122;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#202122;\">         </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10.5pt; color:#202122;\">Link distance: 1–20 km</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"OP22\"></a><a href=\"#OP2\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#0000ff;\">F</span></a><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#0000ff;\">ree Space path loss</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\">The </span><span style=\" font-size:12pt; font-weight:600; color:#202122; background-color:#ffffff;\">free-space path loss</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> (</span><span style=\" font-size:12pt; font-weight:600; color:#202122; background-color:#ffffff;\">FSPL</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\">) is the </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">attenuation</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> of radio energy between the feed points of two antennas that results from the combination of the receiving antenna\'s capture area plus the obstacle free, </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">line-of-sight</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> path through free space (usually air). The &quot;Standard Definitions of Terms for Antennas&quot;, IEEE Std 145-1993, defines &quot;free-space loss&quot; as &quot;The loss between two isotropic radiators in free space, expressed as a power ratio.&quot; It does not include any power loss in the antennas themselves due to imperfections such as resistance. Free space loss increases with the square of distance between the antennas because the radio waves spread out due the </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">inverse square law</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> and decreases with the square of the </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">wavelength</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> of the radio waves. The FSPL is rarely used standalone, but rather as a part of the </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">Friis transmission formula</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\">, which includes the gain of antennas. It is a factor that must be included in the power </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">link budget</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> of a radio communication system, to ensure that sufficient radio power reaches the receiver that the transmitted signal is received intelligibly.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The radio waves from the transmitting antenna spread out in a spherical wavefront. The amount of power passing through any sphere centered on the transmitting antenna is equal. The surface area of a sphere of radius d is 4πd</span><span style=\" font-size:12pt; vertical-align:super;\">2</span><span style=\" font-size:12pt;\">. Thus the intensity or power density of the radiation in any particular direction from the antenna is inversely proportional to the square of distance</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"OP33\"></a><a href=\"#OP3\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#0000ff; background-color:#ffffff;\">H</span></a><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#0000ff; background-color:#ffffff;\">ata model for urbun areas</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\">The </span><span style=\" font-size:12pt; font-weight:600; color:#202122; background-color:#ffffff;\">Hata model</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> is a </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">radio propagation model</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> for predicting the </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">path loss</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> of cellular transmissions in exterior environments, valid for </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">microwave</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> frequencies from 150 to 1500 MHz. It is an empirical formulation based on the data from the </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">Okumura Model</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\">, and is thus also commonly referred to as the </span><span style=\" font-size:12pt; font-weight:600; color:#202122; background-color:#ffffff;\">Okumura–Hata model</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\">. The model incorporates the graphical information from Okumura model and develops it further to realize the effects of diffraction, reflection and scattering caused by city structures. Additionally, the Hata Model applies corrections for applications in suburban and rural environments.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; text-decoration: underline; color:#202122; background-color:#ffffff;\">Model description</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\">Though based on the Okumura model, the Hata model does not provide coverage to the whole range of frequencies covered by Okumura model. Hata model does not go beyond 1500 MHz while Okumura provides support for up to 1920 MHz. The model is suited for both </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">point-to-point</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> and </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">broadcast</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> communications, and covers mobile station antenna heights of 1–10 m, base station antenna heights of 30–200 m, and link distances from 1–10 km.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"OP44\"></a><a href=\"#OP4\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#0000ff; background-color:#ffffff;\">H</span></a><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#0000ff; background-color:#ffffff;\">ata model for Suburban areas</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\">The Hata model for suburban environments is applicable to the transmissions just out of the cities and on rural areas where man-made structures are there but not so high and dense as in the cities. To be more precise, this model is suitable where buildings exist, but the mobile station does not have a significant variation of its height. </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#202122;\"><br /></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"IP11\"></a><a href=\"#IP1\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#0000ff;\">I</span></a><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#0000ff;\">TU model for indoor attenuation</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\">The </span><span style=\" font-size:12pt; font-weight:600; color:#202122; background-color:#ffffff;\">ITU indoor propagation model</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\">, also known as </span><span style=\" font-size:12pt; font-style:italic; color:#202122; background-color:#ffffff;\">ITU model for indoor attenuation</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\">, is a </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">radio propagation model</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> that estimates the </span><span style=\" font-size:12pt; color:#000000; background-color:#ffffff;\">path loss</span><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> inside a room or a closed area inside a building delimited by walls of any form. Suitable for appliances designed for indoor use, this model approximates the total path loss an indoor link may experience.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"IP22\"></a><a href=\"#IP2\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#0000ff; background-color:#ffffff;\">L</span></a><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#0000ff; background-color:#ffffff;\">og- distance path loss model</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\">The log- distance path loss model is a radio propagation model that predicts the path loss a signal encounters inside a building or densely populated areas over dostance.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#202122; background-color:#ffffff;\"> </span><span style=\" font-size:8pt;\"> </span></p></body></html>"))
        self.OpenPDFBtn.setText(_translate("MainWindow", "Open PDF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HelpTab), _translate("MainWindow", "Help"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AboutTab), _translate("MainWindow", "About"))

        # Initial Canvas

        # Creating Canvas Object

        # freeSpace
        canvas = Canvas(MainWindow, width=5, height=8, dpi=60, x=[], y=[])
        toolbar = NavigationToolbar(canvas, self.freeSpaceWidget)
        self.gridLayout_3.addWidget(canvas, 0, 0)
        self.gridLayout_3.addWidget(toolbar, 1, 0)

        # hataUrban
        canvas = Canvas(MainWindow, width=5, height=8, dpi=60, x=[], y=[])
        toolbar = NavigationToolbar(canvas, parent=None)
        self.gridLayout_13.addWidget(canvas, 0, 0)
        self.gridLayout_13.addWidget(toolbar, 1, 0)

        # hataSuburban
        canvas = Canvas(MainWindow, width=5, height=8, dpi=60, x=[], y=[])
        toolbar = NavigationToolbar(canvas, parent=None)
        self.gridLayout_16.addWidget(canvas, 0, 0)  # hataSuburban
        self.gridLayout_16.addWidget(toolbar, 1, 0)

        # Cost231
        canvas = Canvas(MainWindow, width=5, height=8, dpi=60, x=[], y=[])
        toolbar = NavigationToolbar(canvas, parent=None)
        self.gridLayout_19.addWidget(canvas, 0, 0)
        self.gridLayout_19.addWidget(toolbar, 1, 0)

        # ITU
        canvas = Canvas(MainWindow, width=5, height=8, dpi=60, x=[], y=[])
        toolbar = NavigationToolbar(canvas, parent=None)
        self.gridLayout_7.addWidget(canvas, 0, 0)
        self.gridLayout_7.addWidget(toolbar, 1, 0)

        # LongDistance
        canvas = Canvas(MainWindow, width=5, height=8, dpi=60, x=[], y=[])
        toolbar = NavigationToolbar(canvas, parent=None)
        self.gridLayout_28.addWidget(canvas, 0, 0)
        self.gridLayout_28.addWidget(toolbar, 1, 0)

        canvas.show()  # for showing the plot to application window

    def freespacePathLoss(self, MainWindow):
        frequencyValue = self.freeSpaceFrequency.text()
        distanceValue = self.freeSpaceDistance.value()

        # creating distance_array from distance_value (required for plotting)
        distance_array = np.arange(1, int(distanceValue) + 1)

        # Using numpy instead of math module for generating pathLoss array (required for plotting)
        pathLoss = 20 * (np.log10(distance_array)) + 20 * (np.log10(int(frequencyValue))) + 32.44

        pathLoss_Str = str(round(pathLoss[-1], 2))

        self.freeSpaceReport.setText("The calculated path loss is: " + str(pathLoss_Str) + " dB")

        distance_array *= 1000

        # Creating Canvas Object
        canvas = Canvas(MainWindow, width=5, height=10, dpi=60, x=distance_array, y=pathLoss)
        self.gridLayout_3.addWidget(canvas, 0, 0)
        # set toolbar after doing the calculations
        toolbar = NavigationToolbar(canvas, self.freeSpaceWidget)
        self.gridLayout_3.addWidget(toolbar, 1, 0)

        canvas.show()  # for showing the plot to application window

    def hataurbanPathLoss(self, MainWindow):
        frequencyValue = self.hataUrbanFrequency.text()
        distanceValue = self.hataUrbanDistance.value()

        # creating distance_array from distance_value (required for plotting)
        distance_array = np.arange(1, int(distanceValue) + 1)

        baseValue = self.hataUrbanBase.text()
        mobileValue = self.hataUrbanMobile.text()

        CH = 0.8 + (1.1 * ((np.log10(int(frequencyValue))) - 0.7)) * (int(mobileValue)) - (
                1.56 * (np.log10(int(frequencyValue))))
        pathLoss = 69.55 + 26.16 * (np.log10(int(frequencyValue))) - 13.82 * (np.log10(int(baseValue))) - CH + (
                44.9 - 6.55 * (np.log10(int(baseValue)))) * (np.log10(distance_array))

        pathLoss_Str = str(round(pathLoss[-1], 2))

        self.hataUrbanReport.setText("The calculated path loss is: " + str(pathLoss_Str) + " dB")

        distance_array *= 1000

        # Creating Canvas Object
        canvas = Canvas(MainWindow, width=5, height=10, dpi=60, x=distance_array, y=pathLoss)
        self.gridLayout_13.addWidget(canvas, 0, 0)
        # set toolbar after doing the calculations
        toolbar = NavigationToolbar(canvas, parent=None)
        self.gridLayout_13.addWidget(toolbar, 1, 0)

        canvas.show()  # for showing the plot to application window

    def hatasuburbanPathLoss(self, MainWindow):
        frequencyValue = self.hataSuburbanFrequency.text()
        distanceValue = self.hataSuburbanDistance.value()

        # creating distance_array from distance_value (required for plotting)
        distance_array = np.arange(1, int(distanceValue) + 1)

        baseValue = self.hataSuburbanBase.text()
        mobileValue = self.hataSuburbanMobile.text()

        CH = 0.8 + (1.1 * ((np.log10(int(frequencyValue))) - 0.7)) * (int(mobileValue)) - (
                1.56 * (np.log10(int(frequencyValue))))
        LSU = 2 * (((np.log10(int(frequencyValue))) / 28) ** 2) - 5.4
        pathLoss = 69.55 + 26.16 * (np.log10(int(frequencyValue))) - 13.82 * (np.log10(int(baseValue))) - CH + (
                44.9 - 6.55 * (np.log10(int(baseValue)))) * (np.log10(distance_array)) - LSU

        pathLoss_Str = str(round(pathLoss[-1], 2))
        self.hataSuburbanReport.setText("The calculated path loss is: " + str(pathLoss_Str) + " dB")

        distance_array *= 1000

        # Creating Canvas Object
        canvas = Canvas(MainWindow, width=5, height=10, dpi=60, x=distance_array, y=pathLoss)
        self.gridLayout_16.addWidget(canvas, 0, 0)
        # set toolbar after doing the calculations
        toolbar = NavigationToolbar(canvas, parent=None)
        self.gridLayout_16.addWidget(toolbar, 1, 0)

        canvas.show()  # for showing the plot to application window

    def cost231PathLoss(self, MainWindow):
        frequencyValue = self.cost231Frequency.text()
        distanceValue = self.cost231Distance.value()

        # creating distance_array from distance_value (required for plotting)
        distance_array = np.arange(1, int(distanceValue) + 1)

        baseValue = self.cost231Base.text()
        mobileValue = self.cost231Mobile.text()

        a = (1.1 * ((np.log10(int(frequencyValue))) - 0.7)) * (int(mobileValue)) - (
                1.56 * (np.log10(int(frequencyValue))) - 0.8)
        pathLoss = 46.3 + 33.9 * (np.log10(int(frequencyValue))) - 13.82 * (np.log10(int(baseValue))) - a + (
                44.9 - 6.55 * (np.log10(int(baseValue)))) * (np.log10(distance_array))

        pathLoss_Str = str(round(pathLoss[-1], 2))
        self.cost231Report.setText("The calculated path loss is: " + str(pathLoss_Str) + " dB")

        distance_array *= 1000

        # Creating Canvas Object
        canvas = Canvas(MainWindow, width=5, height=10, dpi=60, x=distance_array, y=pathLoss)
        self.gridLayout_19.addWidget(canvas, 0, 0)
        # set toolbar after doing the calculations
        toolbar = NavigationToolbar(canvas, parent=None)
        self.gridLayout_19.addWidget(toolbar, 1, 0)

        canvas.show()  # for showing the plot to application window

    def ITUPathLoss(self, MainWindow):
        frequencyValue = self.ITUFrequency.text()
        distanceValue = self.ITUDistance.value()

        # creating distance_array from distance_value (required for plotting)
        distance_array = np.arange(1, int(distanceValue) + 1)

        pathLoss = 20 * (np.log10(int(frequencyValue))) - 30 * (np.log10(distance_array)) + 27 - 28

        pathLoss_Str = str(round(pathLoss[-1], 2))
        self.ITUReport.setText("The calculated path loss is: " + str(pathLoss_Str) + " dB")

        distance_array *= 1000

        # Creating Canvas Object
        canvas = Canvas(MainWindow, width=5, height=10, dpi=60, x=distance_array, y=pathLoss)
        self.gridLayout_7.addWidget(canvas, 0, 0)
        # set toolbar after doing the calculations
        toolbar = NavigationToolbar(canvas, parent=None)
        self.gridLayout_7.addWidget(toolbar, 1, 0)

        canvas.show()  # for showing the plot to application window

    def LongDistancePathLoss(self, MainWindow):
        frequencyValue = self.LongDistanceFrequency.text()
        distanceValue = self.LongDistanceDistance.value()

        # creating distance_array from distance_value (required for plotting)
        distance_array = np.arange(1, int(distanceValue) + 1)

        # Free Space Path Loss Equation
        # {d_{0}} is the reference distance, usually 1 km (or 1 mile) for large cell and 1 m to 10 m for microcell
        d0 = 10
        PL = 20 * d0 + 20 * (np.log10(int(frequencyValue))) - 27.55

        pathLoss = PL + 10 * 2.6 * (np.log10((distance_array / d0))) + 14.6

        pathLoss_Str = str(round(pathLoss[-1], 2))
        self.LongDistanceReport.setText("The calculated path loss is: " + str(pathLoss_Str) + " dB")

        distance_array *= 1000

        # Creating Canvas Object
        canvas = Canvas(MainWindow, width=5, height=10, dpi=60, x=distance_array, y=pathLoss)
        self.gridLayout_28.addWidget(canvas, 0, 0)
        # set toolbar after doing the calculations
        toolbar = NavigationToolbar(canvas, parent=None)
        self.gridLayout_28.addWidget(toolbar, 1, 0)

        canvas.show()  # for showing the plot to application window

    def open_pdf(self):
        webbrowser.open_new("Project.pdf")


class Canvas(FigureCanvas):
    """Class inherits FigureCanvasQTAgg Class of Matplotlib.Backends"""

    """
    FigureCanvasQTAgg is the class of matplotlib.backends which is used
    to embed canvases (e.g. plots and figures) inside QT applications
    including PyQT5 library of Python.
    """

    def __init__(self, parent=None, width=5, height=5, dpi=60, x=None, y=None):
        """Function initializes the variables"""
        # For setting width, height and dpi of figure
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)  # for adding plots to figure

        FigureCanvas.__init__(self, fig)
        # Setting MainWindow as parent of Canvas class in order to show canvas on MainWindow
        self.setParent(parent)

        # Calling plot function to define and show the plot at MainWindow
        self.plot(x, y)

    def plot(self, x, y):
        """Function implements plot function"""
        ax = self.figure.add_subplot(111)  # creating axes object to call plot function

        ax.plot(x, y)  # Defines line plot
        ax.grid()  # Shows grids inside plot
        ax.set_xlabel('Distance in Meters', fontsize=14)  # label for x-axis
        ax.set_ylabel('Path Loss in dB', fontsize=14)  # label for y-axis


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
