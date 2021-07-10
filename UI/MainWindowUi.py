import sys
from PyQt5 import  QtWidgets as qtw

from PyQt5 import  QtCore as qtc
from PyQt5 import  QtGui as qtg
from PyQt5.QtGui import QTextCursor

import time


class MainWindowUi(qtw.QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fileText=""
        self.countWords=0
        self.layout=qtw.QGridLayout()
        self.upload_file_button=qtw.QPushButton("Upload")
        self.search_text_input=qtw.QLineEdit()
        self.search_text_input.setPlaceholderText("Insert your search word")
        self.line_number_after_input = qtw.QLineEdit()
        self.line_number_after_input.setPlaceholderText("Insert Line Number")
        self.line_number_after_input.setValidator(qtg.QIntValidator(1,1))
        self.search_button=qtw.QPushButton("Search")
        self.clear_button = qtw.QPushButton("Clear")
        self.display_result=qtw.QPlainTextEdit()
        self.display_result.setReadOnly(True)
        self.display_result.centerOnScroll()
        self.warning_label=qtw.QLabel()
        self.layout.addWidget(self.display_result,0,0,5,5)
        self.layout.addWidget(self.upload_file_button,0,6,1,2)
        self.layout.addWidget(self.search_text_input, 1, 6,)
        self.layout.addWidget(self.line_number_after_input ,1, 7)
        self.layout.addWidget(self.search_button ,2, 6)
        self.layout.addWidget(self.clear_button, 2, 7)
        self.layout.addWidget(self.warning_label, 3,6,2,2)


        self.setLayout(self.layout)

        self.upload_file_button.clicked.connect(self.open)
        self.search_button.clicked.connect(self.search_words)
        self.clear_button.clicked.connect(self.clear_all)

        self.showWindow()

    def clear_all(self,clear_display_only=None):
        if (clear_display_only):
            self.display_file(self.fileText)
        else:
            self.display_file(self.fileText)
            self.search_text_input.clear()
            self.line_number_after_input.clear()



    def show_warning(self,warning):
        self.warning_label.setText(warning)
        self.warning_label.setWordWrap(True)
        self.warning_label.setStyleSheet('color: red')
        #self.warning_label.setVisible(True)
    def search_words(self):
        keyword=self.search_text_input.text()
        line_number=self.search_text_input.text()
        if not keyword or not line_number:
           # pass
            self.show_warning("Insert both search word and line number please")
        else:
            self.match_words(keyword,line_number)

    def mergeFormatOnWordOrSelection(self, format):
        cursor = self.display_result.textCursor()
        if not cursor.hasSelection():
            cursor.select(qtg.QTextCursor.WordUnderCursor)
        cursor.mergeCharFormat(format)
        self.display_result.mergeCurrentCharFormat(format)

    def match_words(self,keyword,line_number):
        self.clear_all(clear_display_only=True)
        # indexArray=[i for i in range(len(self.fileText)) if self.fileText.startswith(keyword, i)]
        # self.display_file(listOfIndex=indexArray,keyword=len(keyword))
        fmt = qtg.QTextCharFormat()
        col=qtg.QBrush(qtg.QColor(qtc.Qt.green))
        fmt.setForeground(col)

        self.display_result.moveCursor(qtg.QTextCursor.Start)

        self.countWords = 0
        print('start',self.display_result.textCursor())
        while self.display_result.find(keyword):  # Find whole words
            print('2',self.display_result.textCursor())
            self.mergeFormatOnWordOrSelection(fmt)
            self.countWords += 1

        self.display_result.moveCursor(qtg.QTextCursor.End)
        print('End', self.display_result.textCursor())







    def showWindow(self):
        self.show()


    def  display_file(self,txt=None):
        if txt:
            self.display_result.clear()
            self.display_result.setPlainText(txt)
            self.display_result.moveCursor(qtg.QTextCursor.End)
        else:
            pass




    def open(self):
        path = qtw.QFileDialog.getOpenFileName(self, '', '',
                                           'Text files (*.txt *log*)')

        if path[0]:
             with open(path[0],'r',encoding="utf8") as file:
                #for line in file:
                    self.fileText=file.read()
                    self.display_file(txt=self.fileText)
                    #print(line)
                    #self.display_result.appendPlainText(line)








if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    lol=MainWindowUi()
    sys.exit(app.exec_())

