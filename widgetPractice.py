import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import QCoreApplication, Qt
from datetime import datetime


class Example(QWidget):
    now = datetime.now()
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        if self.now.strftime("%M") == "00":
            oClockMessage = QLabel("정각이에요. 잠시 환기 시켜보세요.",self)
            oClockMessage.move(40,60)

        label = QLabel(self.now.strftime("%Y/%m/%d, %H:%M:%S"), self)
        label.move(80,80)

        btn = QPushButton('알겠음', self)
        btn.resize(btn.sizeHint())
        btn.move(100,100)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("파이썬 비서")
        self.show()

    # def closeEvent(self, QCloseEvent):
    #     ans = QMessageBox.question(self, "종료 확인", "종료하시겠습니까?",
    #                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #     if ans == QMessageBox.Yes:
    #         QCloseEvent.accept()
    #     else:
    #         QCloseEvent.ignore()



app = QApplication(sys.argv)
w = Example()
sys.exit(app.exec_())
