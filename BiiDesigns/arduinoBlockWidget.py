

from PySide.QtCore import *
from PySide.QtGui import *

class arduinoBlockWidget(QWidget):
    def setupUi(self):
        arduinoBlockWidget.setObjectName("arduinoBlockWidget")
        self.resize(346, 133)
        self.formLayout = QFormLayout(self)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QLabel(self)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)
        self.blockNameEdit_2 = QLineEdit(self)
        self.blockNameEdit_2.setObjectName("blockNameEdit_2")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.blockNameEdit_2)
        self.label_6 = QLabel(self)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)
        self.checkBox = QCheckBox(self)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.checkBox)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QApplication.translate("arduinoBlockWidget", "Form", None, QApplication.UnicodeUTF8))
        self.label_8.setText(QApplication.translate("arduinoBlockWidget", "Name", None, QApplication.UnicodeUTF8))
        self.label_6.setText(QApplication.translate("arduinoBlockWidget", "Firmware", None, QApplication.UnicodeUTF8))
        self.checkBox.setText(QApplication.translate("arduinoBlockWidget", "Generate a default frimware?", None, QApplication.UnicodeUTF8))

