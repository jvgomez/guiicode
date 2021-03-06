

from PySide.QtCore import *
from PySide.QtGui import *

class CppBlockWidget(QWidget):
    def setupUi(self):
        self.setObjectName("CppBlockWidget")
        self.resize(344, 162)
        self.formLayout = QFormLayout(self)
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
        self.langConbo_4 = QComboBox(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.langConbo_4.sizePolicy().hasHeightForWidth())
        self.langConbo_4.setSizePolicy(sizePolicy)
        self.langConbo_4.setObjectName("langConbo_4")
        self.langConbo_4.addItem("")
        self.langConbo_4.addItem("")
        self.langConbo_4.addItem("")
        self.langConbo_4.addItem("")
        self.langConbo_4.addItem("")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.langConbo_4)
        self.label_7 = QLabel(self)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)
        self.langConbo_3 = QComboBox(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.langConbo_3.sizePolicy().hasHeightForWidth())
        self.langConbo_3.setSizePolicy(sizePolicy)
        self.langConbo_3.setObjectName("langConbo_3")
        self.langConbo_3.addItem("")
        self.langConbo_3.addItem("")
        self.langConbo_3.addItem("")
        self.langConbo_3.addItem("")
        self.langConbo_3.addItem("")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.langConbo_3)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QApplication.translate("CppBlockWidget", "Form", None, QApplication.UnicodeUTF8))
        self.label_8.setText(QApplication.translate("CppBlockWidget", "Name", None, QApplication.UnicodeUTF8))
        self.label_6.setText(QApplication.translate("CppBlockWidget", "IDE ", None, QApplication.UnicodeUTF8))
        self.langConbo_4.setItemText(0, QApplication.translate("CppBlockWidget", "None", None, QApplication.UnicodeUTF8))
        self.langConbo_4.setItemText(1, QApplication.translate("CppBlockWidget", "Visual", None, QApplication.UnicodeUTF8))
        self.langConbo_4.setItemText(2, QApplication.translate("CppBlockWidget", "CodeBlocks", None, QApplication.UnicodeUTF8))
        self.langConbo_4.setItemText(3, QApplication.translate("CppBlockWidget", "Eclipse", None, QApplication.UnicodeUTF8))
        self.langConbo_4.setItemText(4, QApplication.translate("CppBlockWidget", "Netbeans", None, QApplication.UnicodeUTF8))
        self.label_7.setText(QApplication.translate("CppBlockWidget", "Bild type", None, QApplication.UnicodeUTF8))
        self.langConbo_3.setItemText(0, QApplication.translate("CppBlockWidget", "None", None, QApplication.UnicodeUTF8))
        self.langConbo_3.setItemText(1, QApplication.translate("CppBlockWidget", "Debug", None, QApplication.UnicodeUTF8))
        self.langConbo_3.setItemText(2, QApplication.translate("CppBlockWidget", "Release", None, QApplication.UnicodeUTF8))
        self.langConbo_3.setItemText(3, QApplication.translate("CppBlockWidget", "RelWithDebInfo", None, QApplication.UnicodeUTF8))
        self.langConbo_3.setItemText(4, QApplication.translate("CppBlockWidget", "MinSizeRel", None, QApplication.UnicodeUTF8))

    def checkOk(self):
        #todo check all possibilities
        return self.blockNameEdit.text()!=""

    def setCheckOkEventFunction(self, function):
        self.blockNameEdit.textChanged.connect(function)

    def getBlockResponse(self):
        try:
            return [str(self.blockNameEdit.text())]
        except:
            return False