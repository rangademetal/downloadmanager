from PyQt5.QtWidgets import *
import sys
import urllib.request
from config import memory
from PyQt5.uic import loadUiType
import urllib.request
from datetime import date
import os


from config.database import db

cursor = db.cursor()

ui, _ = loadUiType('gui_test.ui')

class MainApp(QMainWindow , ui):
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUI()
        

    def InitUI(self):
        self.tabWidget.tabBar().setVisible(False)
        self.pushButton.clicked.connect(self.Open_Download)
        self.pushButton_2.clicked.connect(self.Open_Settings)
        self.pushButton_3.clicked.connect(self.Open_History)
        self.path_button.clicked.connect(self.Get_Path)
        self.download.clicked.connect(self.Get_Download)
    

    def Open_Download(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Settings(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_History(self):
        self.tabWidget.setCurrentIndex(2)
        self.tableWidget.setRowCount(0)
        self.View_Database()
        

    def View_Database(self):
        query = "SELECT * FROM  download_manager"
        cursor.execute(query)
        myresult = cursor.fetchall()
        for row_number, row_data in enumerate(myresult):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


    def Get_Path(self):        
        self.path = QFileDialog.getExistingDirectory(self, 'Select your folder:')
        print(str(self.path))
        self.path = memory.path(str(self.path))+'\\'
        self.pathField.setText(self.path)
        print(self.path)


    def Get_Download(self):
        sql = "insert into download_manager(file_name, link, file_size, date_download) values (%s, %s, %s, %s)"
        self.progressBar.setValue(0)
        arr = str(self.urlText.text()).split('/')
        for i in ['jpg','png', 'pdf','exe']:
            if i in str(self.urlText.text()):
                self.path = self.path + arr[-1]
                urllib.request.urlretrieve(str(self.urlText.text()), self.path)
                value = (arr[-1], str(self.urlText.text()), memory.convert(os.stat(self.path).st_size), date.today().strftime('%Y-%m-%d'))
                cursor.execute(sql, value)
                db.commit()
                break
        prgrs = os.stat(self.path).st_size
        for i in range(prgrs):
            self.progressBar.setValue(i)
       

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()