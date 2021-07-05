import sys
from PyQt5 import  QtWidgets as qtw
from PyQt5 import  QtWidgets as qtw
from PyQt5 import  QtGui as qtg




class MainWindowUi(qtw.QWidget):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        layout=qtw.QGridLayout()
        upload_file_button=qtw.QPushButton("Upload")
        search_text_input=qtw.QLineEdit()
        search_text_input.setPlaceholderText("Insert your search word")
        line_number_after_input = qtw.QLineEdit()
        line_number_after_input.setPlaceholderText("Insert Line Number")
        line_number_after_input.setValidator(qtg.QIntValidator(1,1))
        search_button=qtw.QPushButton("Search")
        clear_button = qtw.QPushButton("Clear")
        display_result=qtw.QTextBrowser()

        layout.addWidget(display_result,0,0,5,5)
        layout.addWidget(upload_file_button,0,6,1,2)
        layout.addWidget(search_text_input, 1, 6,)
        layout.addWidget(line_number_after_input ,1, 7)
        layout.addWidget(search_button ,2, 6)
        layout.addWidget(clear_button, 2, 7)

        self.setLayout(layout)

        self.showWindow()



    def showWindow(self):
        self.show()






if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    lol=MainWindowUi()
    sys.exit(app.exec_())

