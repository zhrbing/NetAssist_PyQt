# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(600, 500))
        Form.setMaximumSize(QtCore.QSize(2100, 1800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Icons/Network.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(18, 18, 18, 8)
        self.gridLayout.setHorizontalSpacing(22)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ProtocolTypeLabel = QtWidgets.QLabel(Form)
        self.ProtocolTypeLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ProtocolTypeLabel.setObjectName("ProtocolTypeLabel")
        self.verticalLayout.addWidget(self.ProtocolTypeLabel)
        self.ProtocolTypeComboBox = QtWidgets.QComboBox(Form)
        self.ProtocolTypeComboBox.setObjectName("ProtocolTypeComboBox")
        self.ProtocolTypeComboBox.addItem("")
        self.ProtocolTypeComboBox.addItem("")
        self.verticalLayout.addWidget(self.ProtocolTypeComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.MyHostAddrLabel = QtWidgets.QLabel(Form)
        self.MyHostAddrLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.MyHostAddrLabel.setObjectName("MyHostAddrLabel")
        self.verticalLayout.addWidget(self.MyHostAddrLabel)
        self.MyHostAddrLineEdit = QtWidgets.QLineEdit(Form)
        self.MyHostAddrLineEdit.setInputMask("")
        self.MyHostAddrLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MyHostAddrLineEdit.setReadOnly(True)
        self.MyHostAddrLineEdit.setObjectName("MyHostAddrLineEdit")
        self.verticalLayout.addWidget(self.MyHostAddrLineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.MyPortLabel = QtWidgets.QLabel(Form)
        self.MyPortLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.MyPortLabel.setObjectName("MyPortLabel")
        self.verticalLayout.addWidget(self.MyPortLabel)
        self.MyPortLineEdit = PortLineEdit(Form)
        self.MyPortLineEdit.setInputMask("")
        self.MyPortLineEdit.setMaxLength(5)
        self.MyPortLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MyPortLineEdit.setObjectName("MyPortLineEdit")
        self.verticalLayout.addWidget(self.MyPortLineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.TargetIPLineEdit = IPv4AddrLineEdit(Form)
        self.TargetIPLineEdit.setMaxLength(15)
        self.TargetIPLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TargetIPLineEdit.setObjectName("TargetIPLineEdit")
        self.verticalLayout.addWidget(self.TargetIPLineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.TargetPortLineEdit = PortLineEdit(Form)
        self.TargetPortLineEdit.setMaxLength(5)
        self.TargetPortLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TargetPortLineEdit.setObjectName("TargetPortLineEdit")
        self.verticalLayout.addWidget(self.TargetPortLineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.ConnectButton = ConnectButton(Form)
        self.ConnectButton.setMinimumSize(QtCore.QSize(0, 40))
        self.ConnectButton.setMaximumSize(QtCore.QSize(16777215, 40))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/Icons/broken_link_72px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/img/Icons/link_72px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ConnectButton.setIcon(icon1)
        self.ConnectButton.setCheckable(True)
        self.ConnectButton.setChecked(False)
        self.ConnectButton.setObjectName("ConnectButton")
        self.verticalLayout.addWidget(self.ConnectButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(5, 10, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ReceiveLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ReceiveLabel.sizePolicy().hasHeightForWidth())
        self.ReceiveLabel.setSizePolicy(sizePolicy)
        self.ReceiveLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ReceiveLabel.setWordWrap(False)
        self.ReceiveLabel.setObjectName("ReceiveLabel")
        self.verticalLayout_4.addWidget(self.ReceiveLabel)
        self.ReceivePlainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.ReceivePlainTextEdit.setReadOnly(True)
        self.ReceivePlainTextEdit.setObjectName("ReceivePlainTextEdit")
        self.verticalLayout_4.addWidget(self.ReceivePlainTextEdit)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.send_receive_setting = QtWidgets.QTabWidget(Form)
        self.send_receive_setting.setMinimumSize(QtCore.QSize(190, 0))
        self.send_receive_setting.setObjectName("send_receive_setting")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RSaveDataButton = QtWidgets.QPushButton(self.tab)
        self.RSaveDataButton.setObjectName("RSaveDataButton")
        self.horizontalLayout_2.addWidget(self.RSaveDataButton)
        self.RClearButton = QtWidgets.QPushButton(self.tab)
        self.RClearButton.setObjectName("RClearButton")
        self.horizontalLayout_2.addWidget(self.RClearButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.send_receive_setting.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_5.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_5.addWidget(self.checkBox_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QtCore.QSize(68, 0))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(9999999)
        self.spinBox.setSingleStep(100)
        self.spinBox.setProperty("value", 1000)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_6.addWidget(self.spinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.send_receive_setting.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.send_receive_setting, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SendPlainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.SendPlainTextEdit.setObjectName("SendPlainTextEdit")
        self.horizontalLayout.addWidget(self.SendPlainTextEdit)
        self.SendButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SendButton.sizePolicy().hasHeightForWidth())
        self.SendButton.setSizePolicy(sizePolicy)
        self.SendButton.setMinimumSize(QtCore.QSize(0, 45))
        self.SendButton.setMaximumSize(QtCore.QSize(80, 45))
        self.SendButton.setObjectName("SendButton")
        self.horizontalLayout.addWidget(self.SendButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.StateLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StateLabel.sizePolicy().hasHeightForWidth())
        self.StateLabel.setSizePolicy(sizePolicy)
        self.StateLabel.setMinimumSize(QtCore.QSize(120, 25))
        self.StateLabel.setMaximumSize(QtCore.QSize(120, 25))
        self.StateLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.StateLabel.setObjectName("StateLabel")
        self.horizontalLayout_3.addWidget(self.StateLabel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_3.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.SendCounterLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SendCounterLabel.sizePolicy().hasHeightForWidth())
        self.SendCounterLabel.setSizePolicy(sizePolicy)
        self.SendCounterLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.SendCounterLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.SendCounterLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.SendCounterLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.SendCounterLabel.setObjectName("SendCounterLabel")
        self.horizontalLayout_4.addWidget(self.SendCounterLabel)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.ReceiveCounterLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ReceiveCounterLabel.sizePolicy().hasHeightForWidth())
        self.ReceiveCounterLabel.setSizePolicy(sizePolicy)
        self.ReceiveCounterLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.ReceiveCounterLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ReceiveCounterLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ReceiveCounterLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.ReceiveCounterLabel.setObjectName("ReceiveCounterLabel")
        self.horizontalLayout_4.addWidget(self.ReceiveCounterLabel)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.CounterResetLabel = CounterResetLabel(Form)
        self.CounterResetLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.CounterResetLabel.setObjectName("CounterResetLabel")
        self.horizontalLayout_4.addWidget(self.CounterResetLabel)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.gridLayout.setRowMinimumHeight(0, 9)
        self.gridLayout.setRowMinimumHeight(1, 5)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)
        self.ProtocolTypeLabel.setBuddy(self.ProtocolTypeComboBox)
        self.MyHostAddrLabel.setBuddy(self.MyHostAddrLineEdit)
        self.MyPortLabel.setBuddy(self.MyPortLineEdit)
        self.label_4.setBuddy(self.TargetIPLineEdit)
        self.label_6.setBuddy(self.TargetPortLineEdit)

        self.retranslateUi(Form)
        self.send_receive_setting.setCurrentIndex(0)
        self.RClearButton.clicked.connect(self.ReceivePlainTextEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "网络调试助手"))
        self.ProtocolTypeLabel.setText(_translate("Form", "协议类型"))
        self.ProtocolTypeComboBox.setItemText(0, _translate("Form", "TCP"))
        self.ProtocolTypeComboBox.setItemText(1, _translate("Form", "UDP"))
        self.MyHostAddrLabel.setText(_translate("Form", "本机IP地址"))
        self.MyPortLabel.setText(_translate("Form", "本地端口"))
        self.label_4.setText(_translate("Form", "目标IP地址"))
        self.label_6.setText(_translate("Form", "目标端口"))
        self.ConnectButton.setText(_translate("Form", "连接网络"))
        self.ReceiveLabel.setText(_translate("Form", "数据接收区"))
        self.checkBox.setText(_translate("Form", "十六进制显示"))
        self.checkBox_3.setText(_translate("Form", "显示接收日期"))
        self.checkBox_2.setText(_translate("Form", "暂停接收显示"))
        self.RSaveDataButton.setText(_translate("Form", "保存数据"))
        self.RClearButton.setText(_translate("Form", "清空显示"))
        self.send_receive_setting.setTabText(self.send_receive_setting.indexOf(self.tab), _translate("Form", "接收设置"))
        self.checkBox_4.setText(_translate("Form", "十六进制发送"))
        self.checkBox_5.setText(_translate("Form", "循环发送"))
        self.label.setText(_translate("Form", "循环时间(ms)"))
        self.send_receive_setting.setTabText(self.send_receive_setting.indexOf(self.tab_2), _translate("Form", "发送设置"))
        self.SendPlainTextEdit.setPlainText(_translate("Form", "https://muzing.top"))
        self.SendPlainTextEdit.setPlaceholderText(_translate("Form", "输入要发送的数据"))
        self.SendButton.setText(_translate("Form", "发送"))
        self.label_7.setText(_translate("Form", "状态:"))
        self.StateLabel.setText(_translate("Form", "未连接"))
        self.label_9.setText(_translate("Form", "发送计数:"))
        self.SendCounterLabel.setText(_translate("Form", "0"))
        self.label_10.setText(_translate("Form", "接收计数:"))
        self.ReceiveCounterLabel.setText(_translate("Form", "0"))
        self.CounterResetLabel.setText(_translate("Form", "复位计数"))
from UI.MyWidgets import ConnectButton, CounterResetLabel, IPv4AddrLineEdit, PortLineEdit
import UI.resources_rc
