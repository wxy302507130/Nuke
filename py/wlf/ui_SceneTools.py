# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SceneTools.ui'
#
# Created: Mon Jul 03 14:12:22 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(488, 535)
        self.verticalLayout_7 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.serverEdit = QtGui.QLineEdit(Dialog)
        self.serverEdit.setDragEnabled(True)
        self.serverEdit.setObjectName("serverEdit")
        self.horizontalLayout_3.addWidget(self.serverEdit)
        self.serverButton = QtGui.QToolButton(Dialog)
        self.serverButton.setObjectName("serverButton")
        self.horizontalLayout_3.addWidget(self.serverButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.videoFolderEdit = QtGui.QLineEdit(Dialog)
        self.videoFolderEdit.setObjectName("videoFolderEdit")
        self.gridLayout.addWidget(self.videoFolderEdit, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.imageFolderEdit = QtGui.QLineEdit(Dialog)
        self.imageFolderEdit.setObjectName("imageFolderEdit")
        self.gridLayout.addWidget(self.imageFolderEdit, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nukeEdit = QtGui.QLineEdit(Dialog)
        self.nukeEdit.setDragEnabled(True)
        self.nukeEdit.setObjectName("nukeEdit")
        self.horizontalLayout_2.addWidget(self.nukeEdit)
        self.nukeButton = QtGui.QToolButton(Dialog)
        self.nukeButton.setObjectName("nukeButton")
        self.horizontalLayout_2.addWidget(self.nukeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_5 = QtGui.QFrame(Dialog)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.dirEdit = QtGui.QLineEdit(Dialog)
        self.dirEdit.setDragEnabled(True)
        self.dirEdit.setObjectName("dirEdit")
        self.horizontalLayout_5.addWidget(self.dirEdit)
        self.dirButton = QtGui.QToolButton(Dialog)
        self.dirButton.setObjectName("dirButton")
        self.horizontalLayout_5.addWidget(self.dirButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.projectEdit = QtGui.QLineEdit(Dialog)
        self.projectEdit.setObjectName("projectEdit")
        self.horizontalLayout_10.addWidget(self.projectEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.epEdit = QtGui.QLineEdit(Dialog)
        self.epEdit.setObjectName("epEdit")
        self.horizontalLayout.addWidget(self.epEdit)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.scEdit = QtGui.QLineEdit(Dialog)
        self.scEdit.setObjectName("scEdit")
        self.horizontalLayout.addWidget(self.scEdit)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_16)
        self.videoDestEdit = QtGui.QLineEdit(Dialog)
        self.videoDestEdit.setFrame(False)
        self.videoDestEdit.setReadOnly(True)
        self.videoDestEdit.setObjectName("videoDestEdit")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.videoDestEdit)
        self.imageDestEdit = QtGui.QLineEdit(Dialog)
        self.imageDestEdit.setFrame(False)
        self.imageDestEdit.setReadOnly(True)
        self.imageDestEdit.setObjectName("imageDestEdit")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.imageDestEdit)
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_17)
        self.csheetNameEdit = QtGui.QLineEdit(Dialog)
        self.csheetNameEdit.setFrame(False)
        self.csheetNameEdit.setReadOnly(True)
        self.csheetNameEdit.setObjectName("csheetNameEdit")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.csheetNameEdit)
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setObjectName("label_18")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_18)
        self.label_20 = QtGui.QLabel(Dialog)
        self.label_20.setObjectName("label_20")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_20)
        self.csheetDestEdit = QtGui.QLineEdit(Dialog)
        self.csheetDestEdit.setFrame(False)
        self.csheetDestEdit.setReadOnly(True)
        self.csheetDestEdit.setObjectName("csheetDestEdit")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.csheetDestEdit)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_11)
        self.csheetFFNameEdit = QtGui.QLineEdit(Dialog)
        self.csheetFFNameEdit.setObjectName("csheetFFNameEdit")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.csheetFFNameEdit)
        self.label_19 = QtGui.QLabel(Dialog)
        self.label_19.setObjectName("label_19")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_19)
        self.csheetPrefixEdit = QtGui.QLineEdit(Dialog)
        self.csheetPrefixEdit.setObjectName("csheetPrefixEdit")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.csheetPrefixEdit)
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_12)
        self.backDropBox = QtGui.QComboBox(Dialog)
        self.backDropBox.setObjectName("backDropBox")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.backDropBox)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.csheetUpCheck = QtGui.QCheckBox(Dialog)
        self.csheetUpCheck.setObjectName("csheetUpCheck")
        self.verticalLayout_2.addWidget(self.csheetUpCheck)
        self.csheetOpenCheck = QtGui.QCheckBox(Dialog)
        self.csheetOpenCheck.setObjectName("csheetOpenCheck")
        self.verticalLayout_2.addWidget(self.csheetOpenCheck)
        self.sheetButton = QtGui.QPushButton(Dialog)
        self.sheetButton.setMinimumSize(QtCore.QSize(0, 50))
        self.sheetButton.setObjectName("sheetButton")
        self.verticalLayout_2.addWidget(self.sheetButton)
        self.openCSheetButton = QtGui.QPushButton(Dialog)
        self.openCSheetButton.setEnabled(True)
        self.openCSheetButton.setObjectName("openCSheetButton")
        self.verticalLayout_2.addWidget(self.openCSheetButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_5.addWidget(self.line_4)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.imageFNameEdit = QtGui.QLineEdit(Dialog)
        self.imageFNameEdit.setObjectName("imageFNameEdit")
        self.gridLayout_2.addWidget(self.imageFNameEdit, 1, 1, 1, 1)
        self.videoFNameEdit = QtGui.QLineEdit(Dialog)
        self.videoFNameEdit.setObjectName("videoFNameEdit")
        self.gridLayout_2.addWidget(self.videoFNameEdit, 1, 0, 1, 1)
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.videoUpCheck = QtGui.QCheckBox(Dialog)
        self.videoUpCheck.setObjectName("videoUpCheck")
        self.horizontalLayout_6.addWidget(self.videoUpCheck)
        self.imageUpCheck = QtGui.QCheckBox(Dialog)
        self.imageUpCheck.setObjectName("imageUpCheck")
        self.horizontalLayout_6.addWidget(self.imageUpCheck)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.videoDownCheck = QtGui.QCheckBox(Dialog)
        self.videoDownCheck.setEnabled(False)
        self.videoDownCheck.setCheckable(True)
        self.videoDownCheck.setObjectName("videoDownCheck")
        self.horizontalLayout_8.addWidget(self.videoDownCheck)
        self.imageDownCheck = QtGui.QCheckBox(Dialog)
        self.imageDownCheck.setObjectName("imageDownCheck")
        self.horizontalLayout_8.addWidget(self.imageDownCheck)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.syncButton = QtGui.QPushButton(Dialog)
        self.syncButton.setMinimumSize(QtCore.QSize(0, 50))
        self.syncButton.setObjectName("syncButton")
        self.verticalLayout_4.addWidget(self.syncButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_7.addWidget(self.listWidget)
        self.version_label = QtGui.QLabel(Dialog)
        self.version_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version_label.setObjectName("version_label")
        self.verticalLayout_7.addWidget(self.version_label)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "场集工具", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "服务器路径", None, QtGui.QApplication.UnicodeUTF8))
        self.serverButton.setText(QtGui.QApplication.translate("Dialog", "浏览", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "服务器视频路径", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "服务器单帧文件夹", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Nuke路径", None, QtGui.QApplication.UnicodeUTF8))
        self.nukeButton.setText(QtGui.QApplication.translate("Dialog", "浏览", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "工作目录", None, QtGui.QApplication.UnicodeUTF8))
        self.dirButton.setText(QtGui.QApplication.translate("Dialog", "浏览", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "工程名", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "集", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "场", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Dialog", "视频上传至", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Dialog", "单帧上传至", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Dialog", "色板名称", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Dialog", "色板上传至", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "色板素材文件夹", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Dialog", "色板名称前缀", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "色板底板", None, QtGui.QApplication.UnicodeUTF8))
        self.csheetUpCheck.setText(QtGui.QApplication.translate("Dialog", "创建后上传色板", None, QtGui.QApplication.UnicodeUTF8))
        self.csheetOpenCheck.setText(QtGui.QApplication.translate("Dialog", "创建后打开色板", None, QtGui.QApplication.UnicodeUTF8))
        self.sheetButton.setText(QtGui.QApplication.translate("Dialog", "创建色板", None, QtGui.QApplication.UnicodeUTF8))
        self.openCSheetButton.setText(QtGui.QApplication.translate("Dialog", "打开色板", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog", "视频文件夹名称", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Dialog", "单帧文件夹名称", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "上传", None, QtGui.QApplication.UnicodeUTF8))
        self.videoUpCheck.setText(QtGui.QApplication.translate("Dialog", "视频", None, QtGui.QApplication.UnicodeUTF8))
        self.imageUpCheck.setText(QtGui.QApplication.translate("Dialog", "单帧", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "下载", None, QtGui.QApplication.UnicodeUTF8))
        self.videoDownCheck.setText(QtGui.QApplication.translate("Dialog", "视频", None, QtGui.QApplication.UnicodeUTF8))
        self.imageDownCheck.setText(QtGui.QApplication.translate("Dialog", "单帧", None, QtGui.QApplication.UnicodeUTF8))
        self.syncButton.setText(QtGui.QApplication.translate("Dialog", "上传及下载", None, QtGui.QApplication.UnicodeUTF8))
        self.version_label.setText(QtGui.QApplication.translate("Dialog", "version", None, QtGui.QApplication.UnicodeUTF8))
