from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator, QValidator
from PyQt5.QtWidgets import QLineEdit, QPushButton


class PortLineEdit(QLineEdit):
    class PortValidator(QIntValidator):
        def fixup(self, inputs: str) -> str:
            if len(inputs) == 0:
                return ''
            elif int(inputs) > 65535:
                return '7777'
            return inputs

    def __init__(self, parent):
        super().__init__(parent)
        validator = self.PortValidator(0, 65535, parent)
        self.setValidator(validator)


class IPv4AddrLineEdit(QLineEdit):
    class IPValidator(QRegExpValidator):
        def validate(self, inputs: str, pos: int) -> [QValidator.State, str, int]:
            inputs = inputs.replace('。', '.')
            return super().validate(inputs, pos)

    reg_ex = QRegExp("((2[0-4]\\d|25[0-5]|[01]?\\d\\d?)\\.){3}(2[0-4]\\d|25[0-5]|[01]?\\d\\d?)")

    def __init__(self, parent):
        super().__init__(parent)
        ip_input_validator = self.IPValidator(self.reg_ex, parent)
        self.setValidator(ip_input_validator)


class ConnectButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setCheckable(True)
        self.toggled.connect(self.toggled_slot)

    def toggled_slot(self):
        """
        连接按钮状态切换时的额外操作
        """
        if not self.isChecked():
            self.setText("连接网络")
        else:
            self.setText("断开连接")