from threading import Thread
from PySide.QtGui import QApplication,QCheckBox
import sys
import os
import subprocess
import time

from BasicDialogs import alert
from BiiDesigns.arduinoBlockWidget import arduinoBlockWidget
from BiiDesigns.cppBlockWidget import CppBlockWidget
from BiiDesigns.newHive import NewHiveForm
from BiiDesigns.pythonBlockWidget import pythonBlockWidget
from ErrorHandler.ErrorHandler import softError,error

os.chdir("C:/Jorge/biiTest")


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
        self.cancelButton.clicked.connect(self.close)
        self.okButton.clicked.connect(self.createHive)
        self.hiveNameEdit.textChanged.connect(self.checkOk)
        self.blockGroupBox.toggled.connect(self.checkOk)
        self.activeWidget=CppBlockWidget()
        self.activeWidget.setupUi()
        self.groupBlockLayout.addWidget(self.activeWidget)
        self.activeWidget.setCheckOkEventFunction(self.checkOk)
        self.checkOk()

    def checkOk(self):
        #todo check all text possibilities
        try:
            str(self.hiveNameEdit.text())
            if self.hiveNameEdit.text()=="" \
                    or (self.blockGroupBox.isChecked()
                        and not self.activeWidget.checkOk()):
                self.okButton.setEnabled(False)
            else:
                self.okButton.setEnabled(True)
        except:
            self.okButton.setEnabled(False)

    def langChanged(self,*args):
        if self.langCpp.isChecked():
            self.changeBlockWidget(CppBlockWidget())
        elif self.langArduino.isChecked():
            self.changeBlockWidget(arduinoBlockWidget())
        elif self.langFortran.isChecked():
            print "Fortran"
        elif self.langJava.isChecked():
            print "Java"
        elif self.langNode.isChecked():
            print "Node"
        elif self.langPython.isChecked():
            self.changeBlockWidget(pythonBlockWidget())
        self.checkOk()

    def changeBlockWidget(self, widget):
        widget.setupUi()
        self.activeWidget.close()
        self.groupBlockLayout.addWidget(widget)
        self.activeWidget=widget
        self.activeWidget.setCheckOkEventFunction(self.checkOk)

    def getArrayResponse(self):
        lang=""
        if self.langCpp.isChecked():
            lang="cpp"
        elif self.langArduino.isChecked():
            lang="arduino"
        elif self.langFortran.isChecked():
            lang="fortran"
        elif self.langJava.isChecked():
            lang="java"
        elif self.langNode.isChecked():
            lang="node"
        elif self.langPython.isChecked():
            lang="python"
        arrayResponse=[str(self.hiveNameEdit.text()),lang]
        arrayResponse.extend(self.activeWidget.getBlockResponse())
        return arrayResponse

    def createHive(self):
        global popenAnswer
        global popen
        arrayResponse=self.getArrayResponse()
        popenAnswer=""
        popen=None
        def createthread():
            global popen
            global popenAnswer
            popen=subprocess.Popen("bii new",shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            popenAnswer=popen.communicate("\n".join(arrayResponse))[0]
        try:
            thread=Thread(target=createthread)
            thread.start()
            thread.join(timeout=5)
            if thread.isAlive():
                raise Exception("Time out error, please check ")
                popen.kill()
                alert("BAD"+str(popenAnswer))
            else:
                alert(str(popenAnswer))
        except:
            error()





if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        main = NewHiveUI()
        sys.exit(app.exec_())
    except Exception as e:
        softError()