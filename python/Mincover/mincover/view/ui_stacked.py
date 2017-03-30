# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'revised_stacked_interface.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 501)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Page1 = QtWidgets.QWidget()
        self.Page1.setObjectName("Page1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Page1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.fdText = QtWidgets.QListView(self.Page1)
        self.fdText.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fdText.setObjectName("fdText")
        self.gridLayout_4.addWidget(self.fdText, 4, 0, 1, 1)
        self.mincoverText = QtWidgets.QListView(self.Page1)
        self.mincoverText.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.mincoverText.setObjectName("mincoverText")
        self.gridLayout_4.addWidget(self.mincoverText, 6, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mincoverLabel = QtWidgets.QLabel(self.Page1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.mincoverLabel.setFont(font)
        self.mincoverLabel.setStyleSheet("")
        self.mincoverLabel.setObjectName("mincoverLabel")
        self.horizontalLayout_3.addWidget(self.mincoverLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.genCoverBtn = QtWidgets.QPushButton(self.Page1)
        self.genCoverBtn.setStyleSheet("")
        self.genCoverBtn.setObjectName("genCoverBtn")
        self.horizontalLayout_3.addWidget(self.genCoverBtn)
        self.saveCoverBtn = QtWidgets.QPushButton(self.Page1)
        self.saveCoverBtn.setObjectName("saveCoverBtn")
        self.horizontalLayout_3.addWidget(self.saveCoverBtn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 5, 0, 1, 1)
        self.schemaLine = QtWidgets.QLineEdit(self.Page1)
        self.schemaLine.setAcceptDrops(False)
        self.schemaLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.schemaLine.setReadOnly(True)
        self.schemaLine.setObjectName("schemaLine")
        self.gridLayout_4.addWidget(self.schemaLine, 2, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.fdLabel = QtWidgets.QLabel(self.Page1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.fdLabel.setFont(font)
        self.fdLabel.setStyleSheet("")
        self.fdLabel.setObjectName("fdLabel")
        self.horizontalLayout_8.addWidget(self.fdLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.editFDBtn = QtWidgets.QPushButton(self.Page1)
        self.editFDBtn.setObjectName("editFDBtn")
        self.horizontalLayout_8.addWidget(self.editFDBtn)
        self.splitFDBtn = QtWidgets.QPushButton(self.Page1)
        self.splitFDBtn.setObjectName("splitFDBtn")
        self.horizontalLayout_8.addWidget(self.splitFDBtn)
        self.clearFDBtn = QtWidgets.QPushButton(self.Page1)
        self.clearFDBtn.setObjectName("clearFDBtn")
        self.horizontalLayout_8.addWidget(self.clearFDBtn)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.schemaLabel = QtWidgets.QLabel(self.Page1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.schemaLabel.setFont(font)
        self.schemaLabel.setStyleSheet("")
        self.schemaLabel.setObjectName("schemaLabel")
        self.horizontalLayout_7.addWidget(self.schemaLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.editSchemaBtn = QtWidgets.QPushButton(self.Page1)
        self.editSchemaBtn.setObjectName("editSchemaBtn")
        self.horizontalLayout_7.addWidget(self.editSchemaBtn)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.Page1)
        self.Page2 = QtWidgets.QWidget()
        self.Page2.setObjectName("Page2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Page2)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mincoverLabel_2 = QtWidgets.QLabel(self.Page2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.mincoverLabel_2.setFont(font)
        self.mincoverLabel_2.setStyleSheet("")
        self.mincoverLabel_2.setObjectName("mincoverLabel_2")
        self.horizontalLayout_2.addWidget(self.mincoverLabel_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.editCoverBtn = QtWidgets.QPushButton(self.Page2)
        self.editCoverBtn.setObjectName("editCoverBtn")
        self.horizontalLayout_2.addWidget(self.editCoverBtn)
        self.clearCoverBtn = QtWidgets.QPushButton(self.Page2)
        self.clearCoverBtn.setStyleSheet("")
        self.clearCoverBtn.setObjectName("clearCoverBtn")
        self.horizontalLayout_2.addWidget(self.clearCoverBtn)
        self.testCoverBtn = QtWidgets.QPushButton(self.Page2)
        self.testCoverBtn.setObjectName("testCoverBtn")
        self.horizontalLayout_2.addWidget(self.testCoverBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 5, 0, 1, 1)
        self.fdText_2 = QtWidgets.QListView(self.Page2)
        self.fdText_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fdText_2.setObjectName("fdText_2")
        self.gridLayout_2.addWidget(self.fdText_2, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fdLabel_2 = QtWidgets.QLabel(self.Page2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.fdLabel_2.setFont(font)
        self.fdLabel_2.setStyleSheet("")
        self.fdLabel_2.setObjectName("fdLabel_2")
        self.horizontalLayout_6.addWidget(self.fdLabel_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.editFDBtn_2 = QtWidgets.QPushButton(self.Page2)
        self.editFDBtn_2.setObjectName("editFDBtn_2")
        self.horizontalLayout_6.addWidget(self.editFDBtn_2)
        self.clearFDBtn_2 = QtWidgets.QPushButton(self.Page2)
        self.clearFDBtn_2.setObjectName("clearFDBtn_2")
        self.horizontalLayout_6.addWidget(self.clearFDBtn_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.schemaLine_2 = QtWidgets.QLineEdit(self.Page2)
        self.schemaLine_2.setAcceptDrops(False)
        self.schemaLine_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.schemaLine_2.setReadOnly(True)
        self.schemaLine_2.setObjectName("schemaLine_2")
        self.gridLayout_2.addWidget(self.schemaLine_2, 2, 0, 1, 1)
        self.mincoverText_2 = QtWidgets.QListView(self.Page2)
        self.mincoverText_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.mincoverText_2.setObjectName("mincoverText_2")
        self.gridLayout_2.addWidget(self.mincoverText_2, 6, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.schemaLabel_2 = QtWidgets.QLabel(self.Page2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.schemaLabel_2.setFont(font)
        self.schemaLabel_2.setStyleSheet("")
        self.schemaLabel_2.setObjectName("schemaLabel_2")
        self.horizontalLayout_5.addWidget(self.schemaLabel_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.editSchemaBtn_2 = QtWidgets.QPushButton(self.Page2)
        self.editSchemaBtn_2.setObjectName("editSchemaBtn_2")
        self.horizontalLayout_5.addWidget(self.editSchemaBtn_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.Page2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mincoverLabel.setText(_translate("MainWindow", "Minimal Cover"))
        self.genCoverBtn.setToolTip(_translate("MainWindow", "Generate"))
        self.genCoverBtn.setStatusTip(_translate("MainWindow", "Generate a minimal cover from the FDs"))
        self.genCoverBtn.setText(_translate("MainWindow", "Generate Cover"))
        self.saveCoverBtn.setToolTip(_translate("MainWindow", "Export"))
        self.saveCoverBtn.setStatusTip(_translate("MainWindow", "Export minimal cover to file in comma-separated format"))
        self.saveCoverBtn.setText(_translate("MainWindow", "Export..."))
        self.fdLabel.setText(_translate("MainWindow", "Functional Dependencies"))
        self.editFDBtn.setToolTip(_translate("MainWindow", "Edit FDs"))
        self.editFDBtn.setStatusTip(_translate("MainWindow", "Add/Remove functional dependencies"))
        self.editFDBtn.setText(_translate("MainWindow", "Edit"))
        self.splitFDBtn.setToolTip(_translate("MainWindow", "Split RHS"))
        self.splitFDBtn.setStatusTip(_translate("MainWindow", "Simplify FDs by splitting RHS"))
        self.splitFDBtn.setText(_translate("MainWindow", "Split RHS"))
        self.clearFDBtn.setToolTip(_translate("MainWindow", "Clear FDs"))
        self.clearFDBtn.setStatusTip(_translate("MainWindow", "Clear all functional dependencies"))
        self.clearFDBtn.setText(_translate("MainWindow", "Clear"))
        self.schemaLabel.setText(_translate("MainWindow", "Schema"))
        self.editSchemaBtn.setToolTip(_translate("MainWindow", "Edit Schema"))
        self.editSchemaBtn.setStatusTip(_translate("MainWindow", "Add/Remove attributes from schema"))
        self.editSchemaBtn.setText(_translate("MainWindow", "Edit"))
        self.mincoverLabel_2.setText(_translate("MainWindow", "Minimal Cover"))
        self.editCoverBtn.setToolTip(_translate("MainWindow", "Edit cover"))
        self.editCoverBtn.setStatusTip(_translate("MainWindow", "Edit the minimal cover"))
        self.editCoverBtn.setText(_translate("MainWindow", "Edit"))
        self.clearCoverBtn.setToolTip(_translate("MainWindow", "Clear cover"))
        self.clearCoverBtn.setStatusTip(_translate("MainWindow", "Clear FDs from the minimal cover"))
        self.clearCoverBtn.setText(_translate("MainWindow", "Clear"))
        self.testCoverBtn.setToolTip(_translate("MainWindow", "Test cover"))
        self.testCoverBtn.setStatusTip(_translate("MainWindow", "Test the proposed minimal cover"))
        self.testCoverBtn.setText(_translate("MainWindow", "Test"))
        self.fdLabel_2.setText(_translate("MainWindow", "Functional Dependencies"))
        self.editFDBtn_2.setToolTip(_translate("MainWindow", "Edit FDs"))
        self.editFDBtn_2.setStatusTip(_translate("MainWindow", "Add/Remove functional dependencies"))
        self.editFDBtn_2.setText(_translate("MainWindow", "Edit"))
        self.clearFDBtn_2.setToolTip(_translate("MainWindow", "Clear FDs"))
        self.clearFDBtn_2.setStatusTip(_translate("MainWindow", "Clear all functional dependencies"))
        self.clearFDBtn_2.setText(_translate("MainWindow", "Clear"))
        self.schemaLabel_2.setText(_translate("MainWindow", "Schema"))
        self.editSchemaBtn_2.setToolTip(_translate("MainWindow", "Edit Schema"))
        self.editSchemaBtn_2.setStatusTip(_translate("MainWindow", "Add/Remove attributes from schema"))
        self.editSchemaBtn_2.setText(_translate("MainWindow", "Edit"))

