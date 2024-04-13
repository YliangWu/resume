import sys
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QSizePolicy, QPushButton, QLineEdit , QGraphicsOpacityEffect
from PyQt5.QtGui import QPixmap, QColor, QPainter, QPen,QDesktopServices
from PyQt5.QtCore import Qt, QUrl
from PyQt5 import QtWebEngineWidgets, QtCore, QtWidgets

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = int(800*1.5)
        self.length = int(600*1.5)
        self.setWindowTitle("登录")
        self.setGeometry(100, 100, self.width, self.length) #初始位置
        self.set_background()

        self.username_label = QLabel("用户名:", self)
        self.username_label.move(self.width // 4+40, self.length // 4)

        self.name = QLineEdit(self)
        self.name.setText("吴宇亮")
        self.name.move(self.width // 4 + 60 + 40, self.length // 4)

        self.username_label = QLabel("学号:", self)
        self.username_label.move(self.width // 4 + 210, self.length // 4)

        self.password = QLineEdit(self)
        self.password.setText("21312121")
        self.password.move(self.width // 4 + 250, self.length // 4)

        self.login_button = QPushButton("登录", self)
        self.login_button.move(self.width // 4 + 100, self.length // 4 + 50)
        #self.login_button.clicked.connect(self.login)

        self.exit_button = QPushButton("退出", self)
        self.exit_button.move(self.width // 4 + 250, self.length // 4 + 50)
        self.exit_button.clicked.connect(self.close)

        self.textBrowser=QtWidgets.QTextBrowser(self)
        self.textBrowser.setText("请输入账号密码。(方便测试，此处默认给出用户密码。\n另外，网站已经挂载到github_page，因此不需要localhost激活。)")
        self.textBrowser.setGeometry(QtCore.QRect(self.width // 4 + 60, self.length // 4 + 150,256,101))
        self.login_button.clicked.connect(self.geturl)
        # 设置密码隐藏和回车效果，注意returnPressed是LineEdit的方法
        self.password.setEchoMode(QLineEdit.Password)
        self.password.returnPressed.connect(self.geturl)

    def geturl(self):
        # 如果是LineEdit控件获取内容是text() ；而TextEdit控件获取内容函数为toPlainText()
        if self.name.text()=='吴宇亮' and  self.password.text()=='21312121':
            self.textBrowser.setText("密码正确，登录成功")
            self.setWindowTitle("21312121吴宇亮 blog欢迎您")
            time.sleep(0.1)

            url = 'https://yliangwu.github.io/resume.io/'
            # 网页加载方法
            self.webview = QtWebEngineWidgets.QWebEngineView(self)
            # 设计视图大小尺寸
            self.webview.setGeometry(QtCore.QRect(10, 60, 800, 500))
            # 视图的拉伸效果
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)  # 水平拉伸因子为0，水平方向锁扩展以填充额外的空间
            sizePolicy.setVerticalStretch(4)
            # 竖直拉伸因子为8，这意味着如果布局中有额外的垂直空间，QWebEngineView 控件将在垂直方向上扩        展，并且其垂直扩展的优先级高于其他控件。
            sizePolicy.setHeightForWidth(self.webview.sizePolicy().hasHeightForWidth())  # 是否有一个为宽度设置的高度策略
            self.webview.setSizePolicy(sizePolicy)
            self.webview.setObjectName("webview")
            self.webview.load(QUrl(url))
            self.setCentralWidget(self.webview)
        else:
            self.textBrowser.setText("姓名或者密码错误，请重新输入。")

    def set_background(self):
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.width, self.length)
        pixmap = QPixmap("bg.png")
        self.image_label.setPixmap(pixmap)
        #缩放背景大小
        # if pixmap.width() > self.image_label.width() or pixmap.height() > self.image_label.height():
        #     scaled_pixmap = pixmap.scaled(self.image_label.size(), aspectRatioMode=Qt.KeepAspectRatio)
        #     self.image_label.setPixmap(scaled_pixmap)
        # else:
        #     self.image_label.setPixmap(pixmap)
        self.image_label.lower()

    def login(self):
        username = self.name.text()

        if username:
            self.main_window = BlogWindow(username)
            self.main_window.show()
            self.close()

class BlogWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.width = 800
        self.length = 600
        self.setWindowTitle("博客")
        self.setGeometry(100, 100, self.width, self.length)
        self.set_background()

        self.photo_label = QLabel(self)
        self.photo_label.setGeometry(self.width // 2 - 50, self.length // 4 - 50, 100, 100)
        self.photo_label.setPixmap(QPixmap("mypic.jpg"))
        self.photo_label.setScaledContents(True)

        self.username_label = QLabel(f"学号: 21312121", self)
        self.username_label.setAlignment(Qt.AlignCenter)
        self.username_label.setGeometry(self.width // 2 - 50, self.length // 2 + 10-100, 110, 20)

        self.name_label = QLabel("姓名: 吴宇亮", self)
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_label.setGeometry(self.width // 2 - 50, self.length // 2 + 40-100, 100, 20)

        self.text_label = QLabel("欢迎来到我的博客！", self)
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setGeometry(self.width // 2 - 50, self.length // 2 + 80- 100, 150, 20)

        self.goto_button = QPushButton("查看博客内容", self)
        self.goto_button.setGeometry(self.width // 2 - 50, self.length * 3 // 4-120, 120, 30)
        self.goto_button.clicked.connect(self.goto_blog)

        self.exit_button = QPushButton("退出", self)
        self.exit_button.setGeometry(self.width // 2 - 75, self.length * 3 // 4 - 80, 150, 30)
        self.exit_button.clicked.connect(self.close)

        self.draw_white_frame()

    def set_background(self):
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.width, self.length)
        pixmap = QPixmap("bg.png")
        self.image_label.setPixmap(pixmap)
        self.image_label.lower()

    def draw_white_frame(self):
        effect = QGraphicsOpacityEffect()
        effect.setOpacity(0.5)

        white_frame = QWidget(self)
        white_frame.setGeometry(self.width // 4+90, self.length // 4 -50, 220, 220)
        white_frame.setAutoFillBackground(True)
        white_frame.setStyleSheet("background-color: white;")
        white_frame.setGraphicsEffect(effect)

    def goto_blog(self):
        QDesktopServices.openUrl(QUrl("https://blog.csdn.net/m0_67441224?type=blog"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
