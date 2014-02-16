

from PySide.QtCore import *
from PySide.QtGui import *

class pythonBlockWidget(QWidget):
    def setupUi(self):
        self.setObjectName("pythonBlockWidget")
        self.resize(346, 115)
        self.formLayout = QFormLayout(self)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QLabel(self)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)
        self.blockNameEdit = QLineEdit(self)
        self.blockNameEdit.setObjectName("blockNameEdit_2")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.blockNameEdit)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QApplication.translate("pythonBlockWidget", "Form", None, QApplication.UnicodeUTF8))
        self.label_8.setText(QApplication.translate("pythonBlockWidget", "Name", None, QApplication.UnicodeUTF8))

    def checkOk(self):
        #todo check all possibilities
        return self.blockNameEdit.text()!=""

    def setCheckOkEventFunction(self, function):
        self.blockNameEdit.textChanged.connect(function)

    def getBlockResponse(self):
        try:
            return [str(self.blockNameEdit.text())]
        except:
            pass
