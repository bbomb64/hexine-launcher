from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import *
import launcher as hexine
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.launcher = hexine.Launcher()
        
        self.ui = uic.loadUi("hexine.ui", self)
        self.initUI()

        self.selectedPlace = None
        self.username = ""


    def initUI(self):
        self.place = self.ui.hosting.findChildren(QtWidgets.QLabel, "placeLabel")[0]
        self.nameField = self.ui.hosting.findChildren(QtWidgets.QLineEdit, "usernameField")[0]
        self.title = self.ui.hosting.findChildren(QtWidgets.QLineEdit, "title")[0]
        self.selectPlace = self.ui.hosting.findChildren(QtWidgets.QPushButton, "placeButton")[0]
        self.ipField = self.ui.hosting.findChildren(QtWidgets.QLineEdit, "ipField")[0]
        self.portField = self.ui.hosting.findChildren(QtWidgets.QLineEdit, "portField")[0]
        self.ui.versionSelector.addItems(self.launcher.getVersions())
        self.place.setText("Place: [None]")

        self.ui.versionSelector.currentTextChanged.connect(self.updateVersion)
        self.ui.playButton.clicked.connect(self.playClicked)
        self.ui.hostButton.clicked.connect(self.hostClicked)
        self.selectPlace.clicked.connect(self.updatePlace)
        self.nameField.textChanged.connect(self.updateUsername)

        self.portField.setText(str(self.launcher.defualtPort))
        self.ipField.setText(self.launcher.defaultServer)

        self.ui.show()

    def playClicked(self):
        if self.username == "":
            QtWidgets.QMessageBox.about(self, "Error", "Please enter your Roblonuim username.")
        else: 
            print(f"Joining as {str(self.username)}")
            self.launcher.play(self.username, self.ipField.text(), self.portField.text())
    
    def hostClicked(self):
        if self.username == "":
            QtWidgets.QMessageBox.about(self, "Error", "Please enter your Roblonuim username.")
        elif self.title.text() == "":
             QtWidgets.QMessageBox.about(self, "Error", "The game needs a title.")
        else: 
            self.launcher.host(None, self.title.text(), self.portField.text(), True, self.username)

    def updatePlace(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        placePath, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Open Place File", "","ROBLOX Place Files (*.rbxl)", options=options)
        self.launcher.setPlace(placePath)
        url = QtCore.QUrl.fromLocalFile(placePath)
        self.place.setText(url.fileName())

    def updateUsername(self, value):
        print(value)
        self.username = value

    def updateVersion(self, value):
        self.launcher.setVersion(value)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()