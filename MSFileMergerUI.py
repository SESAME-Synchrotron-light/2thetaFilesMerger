"""
Version 0.1

Version 0.2:
- Adding minimize button. 
- Open destanation folder issue
- 

"""
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MSFileMerger.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
import subprocess
from SEDSupplements import UIMessage
from PyQt5 import Qt, QtCore, QtGui, QtWidgets



class fileMergerUI(object):
    def setupUi(self, Dialog):
        """
        this is a standard method created by QC
        """
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 316)
        Dialog.setFixedSize(578, 316)
        self.flags = QtCore.Qt.WindowFlags(
            QtCore.Qt.Window |
            #QtCore.Qt.CustomizeWindowHint |
            #QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint |
            QtCore.Qt.WindowMinimizeButtonHint
            #QtCore.Qt.WindowStaysOnTopHint
            )
        Dialog.setWindowFlags(self.flags)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(440, 270, 131, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.cleanAndMerge)
        self.pushButton.setEnabled(False)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(325, 270, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 541, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(7, 30, 561, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 80, 561, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setGeometry(91, 4, 150, 21)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(250, 4, 150, 20)
        self.label_5.setStyleSheet("background-color: yellow;")
        self.vlaidateOutputFN()
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(10, 140, 561, 126))
        self.listView.setObjectName("listView")
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(10, 110, 416, 32))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.listFiles)
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.clicked.connect(self.selectAll)
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.clicked.connect(self.deselectAll)
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 50, 561, 33))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.inputFolderDialog)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        """
        this is a standard method created by QC
        """
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SED | 2theta file merger"))
        self.pushButton.setText(_translate("Dialog", "Clean and Merge"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "SED | MS Beamline | 2theta files merger "))
        self.label_3.setText(_translate("Dialog", "Output file name:"))
        self.label_5.setText(_translate("Dialog", "Allowed: [A-Z][a-z][0-9][_-]"))
        self.label_4.setText(_translate("Dialog", "Files to be merged:"))
        self.label_2.setText(_translate("Dialog", "Source files path:"))
        self.pushButton_3.setText(_translate("Dialog", "..."))
        self.pushButton_5.setText(_translate("Dialog", "Show"))
        self.pushButton_6.setText(_translate("Dialog", "Select all"))
        self.pushButton_7.setText(_translate("Dialog", "Deselect all"))

    def inputFolderDialog(self):
        """
        a method being used to open choose directory window
        """
        self.pushButton.setEnabled(False)
        self.startOver()
        self.inputDirectory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit.setText('{}'.format(self.inputDirectory))
        if self.lineEdit.text() != "": 
            self.pushButton.setEnabled(True)

    def listFiles(self):
        """
        a method used to scan and then list all 
        files in a path 
        """
        pathChoosen = False

        try: 
            entries = os.listdir(self.inputDirectory)
            pathChoosen = True
        except: 
            UIMessage("Path is not defined!!","Source files path:"\
                ,"Please provide the source file location (folder path)").showCritical()

        if pathChoosen: 
            self.model = QtGui.QStandardItemModel()
            self.listView.setModel(self.model)
            for i in entries:
                item = QtGui.QStandardItem(i)
                item.setCheckable(True)
                self.model.appendRow(item)
            self.pushButton_6.setEnabled(True)
            self.pushButton_7.setEnabled(True)

    def selectAll(self):
        """
        a method used to select all items in the QListView 
        """
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Checked)

    def deselectAll(self):
        """
        a method used to deselect all items in the QListView 
        """
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Unchecked)
    
    def startOver(self): 
        """
        a method used to setup some parameters before start 
        proccessing the files..
        """
        try:
            self.model = QtGui.QStandardItemModel()
            self.listView.setModel(self.model)
            self.inputDirectory=""
            self.pushButton_6.setEnabled(False)
            self.pushButton_7.setEnabled(False)
            self.pushButton.setEnabled(False)
            self.lineEdit.setText("")
            self.lineEdit_3.setText("")
        except: 
            pass

    def vlaidateOutputFN(self):
        """
        This method validates the output file name 
        The follwoing RegExp just accepts characters A-Z, a-z and _
        Also, numbers 0-9  
        """ 
        regexp = QtCore.QRegExp('^[A-Z0-9a-z_-]{0,30}$')
        validator = QtGui.QRegExpValidator(regexp)
        self.lineEdit_3.setValidator(validator)

    def isLineEmpty(self, line):
        """
        a method used to check if the line blank or not 
        """
        #print (len(line.strip()))
        return len(line.strip()) == 0

    def cleanAndMerge(self): 
        """
        This method goes through the files and does the follwoing: 
        - Read the files
        - Proccess the files 
            - merge all the files in one temp file 
            - go the lines of the temp file, line by line 
            - ignore any line starts with #
            - ignore any blank lines 
            - save the lines in a list 
            - sort the lines 
            - write them back in a .dat file 
        """
        fileNames = []
        rawData = list()
        
        outputFileName = self.lineEdit_3.text()
        if not self.lineEdit_3.text():
            UIMessage("Output file name","Output file name:","Please enter the output file name").showCritical()
            """
            get file names from QListView object 
            """
        else:

            for i in range(self.model.rowCount()): 
                item = self.model.item(i)
                if item.checkState() == QtCore.Qt.Checked:
                    fileNames.append(item.text())
            if not fileNames: 
                UIMessage("No files to be merged have been selected!!","No files have been selected"\
                    ,"Please click on Show then select the files that you want to merge").showCritical()
            else: 

                with open(self.inputDirectory+"/"+"output_file.txt", "w") as outfile:
                    for filename in fileNames:
                        with open(self.inputDirectory+"/"+filename) as infile:
                            contents = infile.read()
                            outfile.write(contents)

                with open (self.inputDirectory+"/"+"output_file.txt", "r") as fin: 
                    for line in fin:
                        ignoreLine = line.strip()
                        if not ignoreLine.startswith('#'): 
                            if not self.isLineEmpty(line):
                                rawData.append(line)
                        
                rawData.sort()
                with open (self.inputDirectory+"/"+self.lineEdit_3.text()+".dat", "w") as fOut:
                    for line in rawData: 
                        fOut.write(line)

                outfile.close()
                fin.close()
                fOut.close()

                UIMessage("Done", "The file: {} has been successfully created".format(self.lineEdit_3.text()), "The file "\
                    "can be found at this path {}".format(self.inputDirectory)).showInformation()
                os.remove(self.inputDirectory+"/"+"output_file.txt")
                self.openDestinationFolder()
                self.startOver()

    def openDestinationFolder(self):
        """
        This method is used to open Windows window, which is the window 
        that contains the output file. 
        """
        FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe') # path to explorer.exe 
        path = os.path.normpath(self.inputDirectory)
        print("DestinationFolder: ", path)
        if os.path.isdir(path):
            subprocess.run([FILEBROWSER_PATH, path])
        elif os.path.isfile(path):
            subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TestQFileDialog = QtWidgets.QDialog()
    ui = fileMergerUI()
    ui.setupUi(TestQFileDialog)
    TestQFileDialog.show()
    sys.exit(app.exec_())
