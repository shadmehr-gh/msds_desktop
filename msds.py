from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QAction, QFormLayout, QHBoxLayout, QVBoxLayout, \
    QSlider, QRadioButton, QTabWidget, QLabel, QDesktopWidget, QLineEdit, QTextEdit, \
    QCheckBox, QRadioButton, QScrollArea, QGridLayout, QListWidget, QListWidgetItem, \
    QTableWidget, QPushButton, QMessageBox, QGroupBox, QMainWindow, QProgressBar, QApplication, QFrame, QComboBox
import sys
import codecs
import main1


class Window_splash(QMainWindow):

    screen_ratio = 1
    font_ratio = 1

    def __init__(self):
        super(Window_splash, self).__init__()
        self.initUI()

    def initUI(self):
        resolution = QDesktopWidget().screenGeometry()
        if resolution.height() <= 768 and resolution.width() <= 1024:
            self.screen_ratio = 1
            self.font_ratio = 1
        elif resolution.height() <= 768 and resolution.width() <= 1360:
            self.screen_ratio = 1.2
            self.font_ratio = 1.1
        elif resolution.height() <= 1080 and resolution.width() <= 1920:
            self.screen_ratio = 1.6
            self.font_ratio = 1.2
        else:
            self.screen_ratio = 2
            self.font_ratio = 1.4

        QFontDatabase.addApplicationFont("fonts/B Nazanin.TTF")
        QFontDatabase.addApplicationFont("fonts/times.ttf")
        QFontDatabase.addApplicationFont("fonts/Ubuntu-R.ttf")

        #self.backgroundImage1 = QLabel(self)
        #self.backgroundImage1.setStyleSheet("background-color:#ffffff;")
        #self.backgroundImage1.setScaledContents(True)
        #self.backgroundImage1.resize(300 * self.screen_ratio, 200 * self.screen_ratio)
        #self.backgroundImage1.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        self.logoImage1 = QLabel(self)
        self.logoImage1.setPixmap(QPixmap("src/msds_icon.png"))
        self.logoImage1.setScaledContents(True)
        self.logoImage1.resize(int(120 * self.screen_ratio), int(120 * self.screen_ratio))
        self.logoImage1.move(int(90 * self.screen_ratio), int(20 * self.screen_ratio))

        self.pbar = QProgressBar(self)
        self.pbar.setMinimum(0)
        self.pbar.setMaximum(0)
        self.pbar.setTextVisible(False)
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(1000, self)
        self.pbar.resize(int(120 * self.screen_ratio), int(15 * self.screen_ratio))
        self.pbar.move(int(90 * self.screen_ratio), int(150 * self.screen_ratio))

        self.logoImage2 = QLabel(self)
        self.logoImage2.setPixmap(QPixmap("src/tums.png"))
        self.logoImage2.setScaledContents(True)
        self.logoImage2.resize(int(60 * self.screen_ratio), int(58 * self.screen_ratio))
        self.logoImage2.move(int(230 * self.screen_ratio), int(136 * self.screen_ratio))

        self.logoLabel1 = QLabel('TUMS 2022 ©', self)
        self.logoLabel1.setAlignment(Qt.AlignCenter)
        self.logoLabel1.setStyleSheet('color:#ffffff')
        self.logoLabel1.resize(int(300 * self.screen_ratio), int(20 * self.screen_ratio))
        self.logoLabel1.move(int(0 * self.screen_ratio), int(170 * self.screen_ratio))

        self.setFixedSize(int(300 * self.screen_ratio), int(200 * self.screen_ratio))
        resolution = QDesktopWidget().screenGeometry()
        self.move(int((resolution.width() / 2) - (self.frameSize().width() / 2)),
                  int((resolution.height() / 2) - (self.frameSize().height() / 2)))
        self.setWindowIcon(QIcon('MSDS_titlebar_icon.png'))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle('MSDS')

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white, 0.0001, Qt.SolidLine))

        grad1 = QLinearGradient(0 * self.screen_ratio, 0 * self.screen_ratio, 300 * self.screen_ratio, 200 * self.screen_ratio)

        grad1.setColorAt(0.5, QColor("#365fd4"))
        grad1.setColorAt(1.0, QColor("#ec1f1f"))
        painter.setBrush(QBrush(grad1))

        painter.drawRect(int(0), int(0), int(300 * self.screen_ratio), int(200 * self.screen_ratio))

    def timerEvent(self, e):
        if self.step >= 4:
            self.timer.stop()
            self.win = main1.Window_main()
            self.win.show()
            self.hide()
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step * 25)


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    winSplash = Window_splash()
    winSplash.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
