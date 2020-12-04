import os
import shutil
import subprocess
import sys
import threading
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dialog_btn1Event = QDialog()  # 추가(신은철) - 임시파일제거
        self.dialog_btn3Event = QDialog()  # 추가(신은철) - 임시파일제거

    # 서비스 관리 이벤트
    def btn1Event(self):
        tb = QTextBrowser(self.dialog_btn1Event)
        self.dialog_btn1Event.setWindowTitle('서비스 관리')
        self.dialog_btn1Event.setWindowModality(Qt.ApplicationModal)
        self.dialog_btn1Event.resize(350, 200)
        self.dialog_btn1Event.show()

        try:
            file_path = 'C:/Users/' + os.getlogin()+ '/Desktop/makers/service.txt'
            subprocess.call('powershell Get-Service | Out-File -FilePath ' + file_path)

            file = open(file_path,"r")
            while(True):
                tb.append(file.readline())
                if file.readline() == ' ':
                    break






        except Exception as e:
            print(e)
            tb.append('Access Denied: %s')



    # 파일 정리 이벤트
    def btn2Event(self):
        msg = QMessageBox()
        msg.setWindowTitle("test")
        msg.setText("content")
        result = msg.exec_()

    # 임시파일 제거 이벤트
    def btn3Event(self):  #신은철 임시파일 제거

        tb = QTextBrowser(self.dialog_btn3Event)
        self.dialog_btn3Event.setWindowTitle('임시파일 정리')
        self.dialog_btn3Event.setWindowModality(Qt.ApplicationModal)
        self.dialog_btn3Event.resize(350, 200)
        self.dialog_btn3Event.show()



        folder = 'C:/Users/' + os.getlogin() + '/AppData/Local/Temp'

        deleteFileCount = 0
        deleteFolderCount = 0

        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)

            indexNo = file_path.find('\\')
            itemName = file_path[indexNo + 1:]
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    tb.append('%s file deleted' % itemName)
                    deleteFileCount = deleteFileCount + 1

                elif os.path.isdir(file_path):
                    if file_path.__contains__('chocolatey'):  continue
                    shutil.rmtree(file_path)
                    tb.append('%s file deleted' % itemName)
                    deleteFolderCount = deleteFolderCount + 1

            except Exception as e:
                tb.append('Access Denied: %s' % itemName)
            tb.append('%s file deleted' % deleteFileCount)

    # 시작 프로그램 관리 이벤트
    def btn4Event(self):
        msg = QMessageBox()
        msg.setWindowTitle("test")
        msg.setText("content")
        result = msg.exec_()

    # 프로세스 정리 이벤트
    def btn5Event(self):
        msg = QMessageBox()
        msg.setWindowTitle("test")
        msg.setText("content")
        result = msg.exec_()

    # 인터넷 속도 측정 이벤트
    def btn6Event(self):
        msg = QMessageBox()
        msg.setWindowTitle("test")
        msg.setText("content")
        result = msg.exec_()

    # 파일 정리 이벤트
    def btn7Event(self):
        msg = QMessageBox()
        msg.setWindowTitle("test")
        msg.setText("content")
        result = msg.exec_()

    # 멀웨어 탐색/제거 이벤트
    def btn8Event(self):
        msg = QMessageBox()
        msg.setWindowTitle("test")
        msg.setText("content")
        result = msg.exec_()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        btn1 = QPushButton('서비스 관리', self)
        btn2 = QPushButton('파일 정리', self)
        btn3 = QPushButton('임시파일 제거', self)
        btn4 = QPushButton('시작 프로그램 관리', self)
        btn5 = QPushButton('프로세스 정리', self)
        btn6 = QPushButton('인터넷 속도 측정', self)
        btn7 = QPushButton('부팅시 변경사항 초기화', self)
        btn8 = QPushButton('멀웨어 탐색/제거', self)

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 1, 0)
        grid.addWidget(btn3, 2, 0)
        grid.addWidget(btn4, 3, 0)
        grid.addWidget(btn5, 0, 1)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 2, 1)
        grid.addWidget(btn8, 3, 1)

        btn1.clicked.connect(self.btn1Event)
        btn2.clicked.connect(self.btn2Event)
        btn3.clicked.connect(self.btn3Event)
        btn4.clicked.connect(self.btn4Event)
        btn5.clicked.connect(self.btn5Event)
        btn6.clicked.connect(self.btn6Event)
        btn7.clicked.connect(self.btn7Event)
        btn8.clicked.connect(self.btn8Event)

        self.setWindowTitle('PC Cleaner')
        self.setWindowIcon(QIcon('Cleaner.png'))
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
