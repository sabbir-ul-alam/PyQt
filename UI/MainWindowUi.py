import sys
from PyQt5 import  QtWidgets as qtw


from PyQt5 import  QtCore as qtc
from PyQt5 import  QtGui as qtg
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import pyqtBoundSignal






class MainWindowUi(qtw.QWidget):


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("Logger")
        self.resize(800,800)
        self.setMaximumWidth(800)
        self.setMinimumHeight(800)
        self.path=""
        self.file=None
        self.fileText=[]
        self.countWords=0
        self.layout=qtw.QGridLayout()
        self.upload_file_button=qtw.QPushButton("Upload")
        self.search_text_input=qtw.QLineEdit()
        self.search_text_input.setPlaceholderText("Insert your search word")
        self.line_number_after_input = qtw.QLineEdit()
        self.line_number_after_input.setPlaceholderText("Insert Line Number")
        #self.line_number_after_input.setValidator(qtg.QIntValidator(1,1))

        self.line_number_after_input.setValidator(qtg.QRegExpValidator(qtc.QRegExp("[0-9]"),self.line_number_after_input))
        self.search_button=qtw.QPushButton("Search")
        self.clear_button = qtw.QPushButton("Clear")
        self.display_result=qtw.QTextEdit()
        self.display_result.setReadOnly(True)
        self.display_result.setAcceptRichText(True)
        #self.display_result.ensureCursorVisible()
        self.font=qtg.QFont()
        self.font.setPointSize(14)
        self.display_result.setFont(self.font)
        self.warning_label=qtw.QLabel()
        self.warning_label.setFont(self.font)
        self.layout.setColumnMinimumWidth(0,500)

        self.layout.addWidget(self.display_result,0,0,0,3)
        self.layout.addWidget(self.upload_file_button,0,4,1,2)
        self.layout.addWidget(self.search_text_input, 1, 4,1,1)
        self.layout.addWidget(self.line_number_after_input ,1, 5,1,1)
        self.layout.addWidget(self.search_button ,2, 4,1,1)
        self.layout.addWidget(self.clear_button, 2, 5,1,1)
        self.layout.addWidget(self.warning_label, 3,4,1,2)

        self.scrollBar = qtw.QScrollBar()
        self.display_result.setVerticalScrollBar(self.scrollBar)

        self.setLayout(self.layout)
        self.search_text_input.returnPressed.connect(self.search_words)
        self.line_number_after_input.returnPressed.connect(self.search_words)
        self.upload_file_button.clicked.connect(self.open)
        self.search_button.clicked.connect(self.search_words)
        self.clear_button.clicked.connect(self.clear_all)

        self.scrollBar.sliderPressed.connect(self.sliderPressed)


        self.show()

    def sliderPressed(self):
        pass
        #self.scrollBar.sliderMoved.connect(self.sliderMoved)
        #self.scrollBar.sliderReleased.connect(self.sliderReleased)




    def disable_input(self):
        self.upload_file_button.setDisabled(True)
        self.search_text_input.setDisabled(True)
        self.line_number_after_input.setDisabled(True)
        self.search_button.setDisabled(True)

    def enable_input(self):
        self.upload_file_button.setDisabled(False)
        self.search_text_input.setDisabled(False)
        self.line_number_after_input.setDisabled(False)
        self.search_button.setDisabled(False)

    def clear_all(self,):

        try:
         qtc.QCoreApplication.processEvents()
         self.upload_file_button.blockSignals(True)
         self.display_result.blockSignals(True)
         self.display_result.blockSignals(False)
         self.upload_file_button.blockSignals(False)
         print("cear all")
         if self.file:
            self.file.close()
         self.search_text_input.clear()
         self.line_number_after_input.clear()
         self.display_result.clear()
         self.warning_label.clear()
         self.fileText=[]
         print("all cleared")
         self.enable_input()
        except Exception as e:
            print(e)
            self.enable_input()




    def show_warning(self,warning):
        print("show_warning")

        self.warning_label.clear()
        self.warning_label.setText(warning)
        self.warning_label.setWordWrap(True)
        self.warning_label.setStyleSheet('color: red')
        self.enable_input()
        #self.warning_label.setVisible(True)
    def search_words(self):
        print("search_words")
        self.warning_label.clear()
        try:
            keyword=self.search_text_input.text()
            line_number=int(self.line_number_after_input.text())

            if line_number >0 and len(keyword.strip())>0:
                self.match_words(keyword, line_number)
            else:
                self.show_warning("Line number cant be zero. And keyword cant be empty")

        except:
            self.show_warning("Insert both search word and line number please")




    def match_words(self,keyword,line_number):
       # self.clear_all(clear_display_only=True)

        print("match_words")
        list_of_block=[]
        len_of_file=len(self.fileText)
        if len_of_file<=0:
            self.show_warning("No file Found")
        else:
         cursor=0
         while(cursor<len_of_file):
             if self.fileText[cursor].find(keyword) !=-1:
                 try:
                     tmp_sliced_list=self.fileText[cursor:(cursor+line_number)]
                 except:
                     tmp_sliced_list = self.fileText[cursor:]
                 cursor=cursor+line_number
                 tmp_line="<br>".join(tmp_sliced_list)
                 #<p style="color:red;">I am red</p>
                 tmp_line=tmp_line.replace(keyword, '<b style="color:green;">{}</b>'.format(keyword))
                 print(tmp_line)
                 list_of_block.append(tmp_line)
             else:
                 cursor=cursor+1
        self.show_block(list_of_block)


    def show_block(self,block_list):
        try:
            self.disable_input()
            print("show_block")

            if len(block_list)<=0:
                self.show_warning("No match found")
                self.display_result.clear()
            else:
                self.display_result.clear()
                for i in block_list:
                   i=i+'<br>'+'<br>'+'<br>'
                   self.display_file(txt=i)
                self.enable_input()
        except :
            self.enable_input()




    def  display_file(self,txt=None):
        if len(txt)>0:
            self.display_result.append(txt)
            #self.display_result.moveCursor( qtg.QTextCursor.End)
            qtc.QCoreApplication.processEvents()
            #print(txt)

        else:
            self.show_warning("Nothing to show")




    def open(self):

        self.fileText=[]
        self.display_result.clear()
        path = qtw.QFileDialog.getOpenFileName(self, '', '',
                                           'Text files (*.txt *log*)')
        print(self.path)
        self.path=path[0]
        if path[0]:
            try:
                self.file=open(path[0],'r',encoding="utf8")
                self.disable_input()
                for line in self.file:
                    self.display_file(txt=line)
                    self.fileText.append(line)
                print("after clear")
                self.file.close()

                self.enable_input()
            except Exception as e:
                print(e)
                self.enable_input()



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    lol=MainWindowUi()
    sys.exit(app.exec_())

