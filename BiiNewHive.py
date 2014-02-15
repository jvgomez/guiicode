from PySide.QtGui import QApplication
import sys
from BiiDesigns.newHive import NewHiveForm
from ErrorHandler.ErrorHandler import softError

class NewHiveUI(NewHiveForm):

    def __init__(self):
        NewHiveForm.__init__(self)
        self.setupUi()
        self.show()
        self.langCpp.clicked.connect(self.langChanged)
        self.langArduino.clicked.connect(self.langChanged)
        self.langFortran.clicked.connect(self.langChanged)
        self.langJava.clicked.connect(self.langChanged)
        self.langNode.clicked.connect(self.langChanged)
        self.langPython.clicked.connect(self.langChanged)

    def langChanged(self,*args):
        if self.langCpp.isChecked():
            print "CPP"
        elif self.langArduino.isChecked():
            print "Arduino"
        elif self.langFortran.isChecked():
            print "Fortran"
        elif self.langJava.isChecked():
            print "Java"
        elif self.langNode.isChecked():
            print "Node"
        elif self.langPython.isChecked():
            print "Python"

    def changeWBlockWidget(self):
        self.groupBlockLayout.addWidget()
        pass

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        main = NewHiveUI()
        sys.exit(app.exec_())
    except Exception as e:
        softError()