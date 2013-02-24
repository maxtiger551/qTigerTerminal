#!/usr/bin/python
# -*- coding: utf-8 -*-
  
import sys
from PySide.QtCore import *
from PySide.QtGui import *
  
class Form(QDialog):
    
    def __init__(self, parent=None):
	super(Form, self).__init__(parent)
	# Create widgets
	self.sendEdit = QLineEdit("")
	self.sendButton = QPushButton("Send")   
	self.recText = QTextEdit("")
	# Create layout and add widgets
	vlayout = QVBoxLayout()
	vlayout.addWidget(self.recText)
	
	
	hlayout = QHBoxLayout()
	hlayout.addWidget(self.sendEdit)
	hlayout.addWidget(self.sendButton)
	# Set dialog layout
	vlayout.addLayout(hlayout)
	self.setLayout(vlayout)
	
	
	self.sendButton.clicked.connect(self.send_clicked)
	
    # When "Send button prossed
    def send_clicked(self):
	#this is only for test
	self.recText.append(self.sendEdit.text())   
  
  
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
