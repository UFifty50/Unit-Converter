from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
import ctypes
import sys
from plugins import *
  
myappid = 'company.product.none.number'
  
class Window(QMainWindow): 
  
    def __init__(self): 
        super().__init__() 
  
        self.setWindowTitle("Python")
        self.setWindowIcon(QIcon("Icons\windowIcon1.png"))
        self.setGeometry(100, 200, 800, 600) 
        self.Uicomponents() 
        self.show()
  
    def Uicomponents(self):
        def backButton(self):
            self.backButton = QPushButton(self)
            self.backButton.setGeometry(50, 50, 100, 30)
            self.backButton.setText("Back")
        def computeButton(self):
            self.computeButton = QPushButton(self)
            self.computeButton.setGeometry(330, 320, 125, 30)
            self.computeButton.setText("Compute")
        def select_button(self):
            self.select_button = QPushButton(self)
            self.select_button.setGeometry(330, 220, 125, 30)
            self.select_button.setText("Select")
        def combo_box(self):
            self.combo_box = QComboBox(self) 
            self.combo_box.setGeometry(330, 115, 125, 30) 
            list = ["Please select an item", "°C to °F", "°F to °C", "Test for leap years"] 
            self.combo_box.setEditable(False)
            self.combo_box.addItems(list)
        def CtoF(self):
            self.CtoFNumBox = QSpinBox(self)
            self.CtoFNumBox.setGeometry(350, 220, 70, 30)
            self.CtoFNumBox.setMinimum(-2147483648)
        def FtoC(self):
            self.FtoCNumBox = QSpinBox(self)
            self.FtoCNumBox.setGeometry(350, 220, 70, 30)
            self.FtoCNumBox.setMinimum(-2147483648)
        def leapYears(self):
            self.leapYearNumBox = QSpinBox(self)
            self.leapYearNumBox.setGeometry(350, 220, 70, 30)

        combo_box(self)
        select_button(self)
        CtoF(self)
        FtoC(self)
        leapYears(self)
        computeButton(self)
        backButton(self)

    def hide_backButton(self):
        self.backButton.hide()

    def show_backButton(self):
        self.backButton.show()

    def hide_computeButton(self):
        self.computeButton.hide()

    def show_computeButton(self):
        self.computeButton.show()
        
    def hide_leapYearNumBox(self):
        self.leapYearNumBox.hide()

    def show_leapYearNumBox(self):
        self.leapYearNumBox.show()

    def hide_CtoFNumBox(self):
        self.CtoFNumBox.hide()

    def show_CtoFNumBox(self):
        self.CtoFNumBox.show()

    def hide_FtoCNumBox(self):
        self.FtoCNumBox.hide()

    def show_FtoCNumBox(self):
        self.FtoCNumBox.show()

    def hide_select_button(self): 
        self.select_button.hide()

    def show_select_button(self):
        self.select_button.show()

    def hide_combo_box(self): 
        self.combo_box.hide()

    def show_combo_box(self):
        self.combo_box.show()

    def handleComputePress(self, currentIndex):
        if currentIndex == 1:
            print()
        if currentIndex == 2:
            print()
        if currentIndex == 3:
            calc1 = CtoFNumBox.Value()
            try:
                leapYears()
            except Exception:
                pass

    def handleBackButtonPress(self):
         self.show_combo_box()
         self.show_select_button()
         self.hide_CtoFNumBox()
         self.hide_computeButton()
         self.hide_FtoCNumBox()
         self.hide_leapYearNumBox()
         self.hide_backButton()
    
    def handleComboSelect(self):
        self.show_select_button()

    def handleButtonPress(self):
        self.hide_select_button()
        self.hide_combo_box()
        self.show_backButton()
        currentIndex = self.combo_box.currentIndex()
        if currentIndex == 1:
            self.show_CtoFNumBox()
            self.show_computeButton()
        elif currentIndex == 2:
            self.show_FtoCNumBox()
            self.show_computeButton()
        elif currentIndex == 3:
            self.show_leapYearNumBox()
            self.show_computeButton()

def main():
    App = QApplication(sys.argv) 
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    window = Window()
    window.hide_backButton()
    window.hide_computeButton()
    window.hide_leapYearNumBox()
    window.hide_FtoCNumBox()
    window.hide_CtoFNumBox()
    window.hide_select_button()
    window.show_combo_box()
    while True:
        window.backButton.clicked.connect(window.handleBackButtonPress)
        window.combo_box.view().pressed.connect(window.handleComboSelect)
        window.select_button.clicked.connect(window.handleButtonPress)
        window.computeButton.clicked.connect(window.handleComputePress)
        sys.exit(App.exec())

if __name__ == '__main__':
    main()