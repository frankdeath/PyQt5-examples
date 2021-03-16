#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def main():
  app = QApplication([])
  
  window = QWidget()
  
  layout = QVBoxLayout()
  
  title = QLabel("Title of the App")
  title.setFont(QFont("Times", 18, QFont.Bold))
  title.setAlignment(Qt.AlignCenter)
  
  layout.addWidget(title)
  
  tableWidget = QTableWidget()
  tableWidget.setRowCount(10)
  tableWidget.setColumnCount(5)
  tableWidget.horizontalHeader().setVisible(False)
  tableWidget.verticalHeader().setVisible(False)
  tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
  tableWidget.setSelectionMode(QTableWidget.NoSelection)
  
  tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
  tableWidget.resizeColumnsToContents()
  
  layout.addWidget(tableWidget)
  
  buttons = QWidget()
  
  bLayout = QHBoxLayout()
  
  button1 = QPushButton('Click')
  button1.clicked.connect(on_button_clicked)
  
  button2 = QPushButton('Me')
  button2.clicked.connect(on_button_clicked)
  
  bLayout.addWidget(button1)
  bLayout.addWidget(button2)
  
  buttons.setLayout(bLayout)
  
  layout.addWidget(buttons)
  
  window.setLayout(layout)
  
  window.show()
  
  app.exec()

def on_button_clicked():
  alert = QMessageBox()
  alert.setText('You clicked the button!')
  alert.exec()



if __name__ == '__main__':
  main()
