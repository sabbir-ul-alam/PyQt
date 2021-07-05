import sys
from PyQt5 import  QtWidgets as qtw
from PyQt5 import  QtWidgets as qtw
from PyQt5 import  QtGui as qtg




class MainWindowUi(qtw.QWidget):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
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


        self.layout.addWidget(self.display_result,0,0,5,5)
        self.layout.addWidget(self.upload_file_button,0,6,1,2)
        self.layout.addWidget(self.search_text_input, 1, 6,)
        self.layout.addWidget(self.line_number_after_input ,1, 7)
        self.layout.addWidget(self.search_button ,2, 6)
        self.layout.addWidget(self.clear_button, 2, 7)
        self.setLayout(self.layout)

        self.upload_file_button.clicked.connect(self.open)

        self.showWindow()



    def showWindow(self):
        self.show()

    def open(self):
        path = qtw.QFileDialog.getOpenFileName(self, '', '',
                                           'Text files (*.txt *log*)')

        print(path[0])
        self.display_result.clear()
        with open(path[0],'r',encoding="utf8") as file:
            for line in file:
                self.display_result.appendPlainText(line)








if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    lol=MainWindowUi()
    sys.exit(app.exec_())

