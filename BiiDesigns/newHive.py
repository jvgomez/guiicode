

from PySide.QtCore import *
from PySide.QtGui import *

class NewHiveForm(QWidget):
    def setupUi(self):
        self.setObjectName("NewHiveForm")
        self.resize(352, 331)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QGroupBox(self)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)
        self.hiveNameEdit = QLineEdit(self.groupBox)
        self.hiveNameEdit.setObjectName("hiveNameEdit")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.hiveNameEdit)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.langPython = QRadioButton(self.groupBox)
        self.langPython.setObjectName("langPython")
        self.gridLayout_2.addWidget(self.langPython, 0, 1, 1, 1)
        self.langJava = QRadioButton(self.groupBox)
        self.langJava.setEnabled(False)
        self.langJava.setObjectName("langJava")
        self.gridLayout_2.addWidget(self.langJava, 0, 0, 1, 1)
        self.langCpp = QRadioButton(self.groupBox)
        self.langCpp.setChecked(True)
        self.langCpp.setObjectName("langCpp")
        self.gridLayout_2.addWidget(self.langCpp, 1, 1, 1, 1)
        self.langNode = QRadioButton(self.groupBox)
        self.langNode.setEnabled(False)
        self.langNode.setObjectName("langNode")
        self.gridLayout_2.addWidget(self.langNode, 1, 0, 1, 1)
        self.langArduino = QRadioButton(self.groupBox)
        self.langArduino.setObjectName("langArduino")
        self.gridLayout_2.addWidget(self.langArduino, 0, 2, 1, 1)
        self.langFortran = QRadioButton(self.groupBox)
        self.langFortran.setEnabled(False)
        self.langFortran.setObjectName("langFortran")
        self.gridLayout_2.addWidget(self.langFortran, 1, 2, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.blockGroupBox = QGroupBox(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blockGroupBox.sizePolicy().hasHeightForWidth())
        self.blockGroupBox.setSizePolicy(sizePolicy)
        self.blockGroupBox.setFlat(True)
        self.blockGroupBox.setCheckable(True)
        self.blockGroupBox.setChecked(True)
        self.blockGroupBox.setObjectName("blockGroupBox")
        self.groupBlockLayout = QVBoxLayout(self.blockGroupBox)
        self.groupBlockLayout.setObjectName("groupBlockLayout")
        self.verticalLayout.addWidget(self.blockGroupBox)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QPushButton(self)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.okButton = QPushButton(self)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QApplication.translate("NewHiveForm", "New hive", None, QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QApplication.translate("NewHiveForm", "Hive", None, QApplication.UnicodeUTF8))
        self.label.setText(QApplication.translate("NewHiveForm", "Name", None, QApplication.UnicodeUTF8))
        self.label_2.setText(QApplication.translate("NewHiveForm", "Language", None, QApplication.UnicodeUTF8))
        self.langPython.setText(QApplication.translate("NewHiveForm", "python", None, QApplication.UnicodeUTF8))
        self.langJava.setText(QApplication.translate("NewHiveForm", "java", None, QApplication.UnicodeUTF8))
        self.langCpp.setText(QApplication.translate("NewHiveForm", "cpp", None, QApplication.UnicodeUTF8))
        self.langNode.setText(QApplication.translate("NewHiveForm", "node", None, QApplication.UnicodeUTF8))
        self.langArduino.setText(QApplication.translate("NewHiveForm", "arduino", None, QApplication.UnicodeUTF8))
        self.langFortran.setText(QApplication.translate("NewHiveForm", "fortran", None, QApplication.UnicodeUTF8))
        self.blockGroupBox.setTitle(QApplication.translate("NewHiveForm", "Block", None, QApplication.UnicodeUTF8))
        self.cancelButton.setText(QApplication.translate("NewHiveForm", "Cancel", None, QApplication.UnicodeUTF8))
        self.okButton.setText(QApplication.translate("NewHiveForm", "Ok", None, QApplication.UnicodeUTF8))

