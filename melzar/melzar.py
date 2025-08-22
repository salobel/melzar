#!/usr/bin/env python3
#
# Copyright (C) 2025, Matthew Polk.
#
# This file is part of melzar.
#
# Melzar is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Melzar is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# melzar. If not, see <https://www.gnu.org/licenses/>. 
#

import sys
import pathlib
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMenu,
    QFileDialog)

def QuitMelzar():
    exit(0)
    return None

def OpenFile():
    home = pathlib.Path.home()
    filename = QFileDialog.getOpenFileName(None,
                                           caption="Open",
                                           dir=str(home), filter="*.txt")

class EntryPoint(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Melzar")
        self.resize(800,600)
        self.mkmenubar()

        self.show()

    def mkmenubar(e):
        menu_bar = e.menuBar()

        file_menu = menu_bar.addMenu("&File")
        
        file_diag = QAction("&Open", e)
        file_diag.triggered.connect(OpenFile)

        quit_melzar = QAction("&Quit",e)
        quit_melzar.triggered.connect(QuitMelzar)

        file_menu.addAction(file_diag)
        file_menu.addAction(quit_melzar)
        

if __name__ == "__main__":
    App = QApplication(sys.argv)

    Window = EntryPoint()

    App.exec()

