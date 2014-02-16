

from PySide.QtCore import *
from PySide.QtGui import *

class arduinoBlockWidget(QWidget):
    def setupUi(self):
        self.setObjectName("arduinoBlockWidget")
        self.resize(346, 133)
        self.formLayout = QFormLayout(self)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QLabel(self)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)
        self.blockNameEdit = QLineEdit(self)
        self.blockNameEdit.setObjectName("blockNameEdit_2")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.blockNameEdit)
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

    def checkOk(self):
        #todo check all possibilities
        try:
            return str(self.blockNameEdit.text())!=""
        except:
            return False

    def setCheckOkEventFunction(self, function):
        self.blockNameEdit.textChanged.connect(function)

    def getBlockResponse(self):
        return [str(self.blockNameEdit.text())]