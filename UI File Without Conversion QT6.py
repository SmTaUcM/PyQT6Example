#--------------------------------------------------------------------------------------------------
# Name:        UI File Without Conversion QT6.py
# Purpose:     PyQT6 Example of using a .ui file to create a mmain window application.
#
# Author:      Stuart Macintosh
#
# Created:     24/07/2023
# Copyright:   (c) Stuart Macintosh 2023
# Licence:     Open Source
#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
#                                            Imports
#--------------------------------------------------------------------------------------------------
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
#                                            Classes
#--------------------------------------------------------------------------------------------------
class TestApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('UI_pyqt_tutorial.ui')
        self.ui.show()

        self.ui.doubleSpinBox.valueChanged.connect(spinFn)
        self.ui.comboBox.currentIndexChanged.connect(comboFn)
        self.ui.pushButton.clicked.connect(buttonFn)
    #----------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
#                                          Functions
#--------------------------------------------------------------------------------------------------
def spinFn(value):
    win.ui.doubleSpinBoxLabel.setText('doubleSpinBox is set to ' + str(value))
    #----------------------------------------------------------------------------------------------

def buttonFn():
    win.ui.setWindowTitle(win.ui.lineEdit.text())
    #----------------------------------------------------------------------------------------------

def comboFn(value):
    win.ui.comboBoxLabel.setText(str(value) + ' is selected')
    #----------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
#                                        Main Program
#--------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TestApp()
    sys.exit(app.exec())
#--------------------------------------------------------------------------------------------------