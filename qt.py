import sys


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from blog import LoginWindow as Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('加载外部网页的例子')
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi()
        self.__ui.login_button.clicked.connect(self.geturl)
        # 设置密码隐藏和回车效果，注意returnPressed是LineEdit的方法
        self.__ui.password.setEchoMode(QLineEdit.Password)
        self.__ui.password.returnPressed.connect(self.geturl)

    def geturl(self):
        # 如果是LineEdit控件获取内容是text() ；而TextEdit控件获取内容函数为toPlainText()
        if  self.__ui.name.text()=='吴宇亮' and  self.__ui.password.text()=='21312121':
            self.__ui.signin.setText("密码正确，登录成功")
            url = 'https://yliangwu.github.io/resume.io/'
            # 网页加载方法
            self.__ui.webview.load(QUrl(url))
        else:
            self.__ui.signin.setText("姓名或者密码错误，请重新输入。")
# ... 其他代码 ...

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())