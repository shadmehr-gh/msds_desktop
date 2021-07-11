from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QAction, QFormLayout, QHBoxLayout, QVBoxLayout, \
    QSlider, QRadioButton, QTabWidget, QLabel, QDesktopWidget, QLineEdit, QTextEdit, \
    QCheckBox, QRadioButton, QScrollArea, QGridLayout, QListWidget, QListWidgetItem, \
    QTableWidget, QPushButton, QMessageBox, QGroupBox, QMainWindow, QProgressBar, QApplication, QFrame, QComboBox
import sys
import codecs


class Window_main_about(QMainWindow):

    screen_ratio = 1
    font_ratio = 1

    # strings_en:
    str_win_title_en = "About Us"
    str_about_en = "The MSDS Project:\n\nThis project has been implemented by the faculity of pharmacy of the Tehran University of Medical Sciences(TUMS) with the aim of translating material safety data sheets(MSDS) to persian and increasing access to these pages.\n\n\nHelp us improve our project by contacting to organic lab Email:\n\norgchemlab.pharm@gmail.com"
    # -----------
    # strings_fa:
    str_win_title_fa = "درباره ما"
    str_about_fa = "پروژه MSDS:\n\nاین پروژه با هدف فارسی سازی برگه های اطلاعات ایمنی(MSDS) و افزایش دسترسی به این صفحات طی یک پروژه گسترده توسط دانشکده داروسازی دانشگاه علوم پزشکی تهران اجرا شده است.\n\n\nبا ارتباط با ما به بهبود این پروژه کمک کنید:\n\norgchemlab.pharm@gmail.com"
    # -----------
    # strings_final:
    str_win_title = ""
    str_about = ""
    # -----------

    lang_main = ""

    def __init__(self):
        super(Window_main_about, self).__init__()
        self.initUI()

    def initUI(self):
        lang_main_get = codecs.open("data/lang.txt", encoding='utf-8', mode="r")
        self.lang_main = lang_main_get.read()
        lang_main_get.close()

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

        if self.lang_main == "en":
            self.str_win_title = self.str_win_title_en
            self.str_about = self.str_about_en
        elif self.lang_main == "fa":
            self.str_win_title = self.str_win_title_fa
            self.str_about = self.str_about_fa

        self.backgroundImage1 = QLabel(self)
        self.backgroundImage1.setPixmap(QPixmap("src/msds_title.png"))
        self.backgroundImage1.setScaledContents(True)
        self.backgroundImage1.resize(300 * self.screen_ratio, 40 * self.screen_ratio)
        self.backgroundImage1.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        self.titleLabel1 = QLabel('M', self)
        self.titleLabel1.setFont(QFont("Times New Roman", 17 * self.font_ratio, weight=QFont.Bold))
        self.titleLabel1.setAlignment(Qt.AlignCenter)
        self.titleLabel1.resize(75 * self.screen_ratio, 40 * self.screen_ratio)
        self.titleLabel1.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        self.titleLabel2 = QLabel('S', self)
        self.titleLabel2.setFont(QFont("Times New Roman", 17 * self.font_ratio, weight=QFont.Bold))
        self.titleLabel2.setAlignment(Qt.AlignCenter)
        self.titleLabel2.resize(75 * self.screen_ratio, 40 * self.screen_ratio)
        self.titleLabel2.move(75 * self.screen_ratio, 0 * self.screen_ratio)

        self.titleLabel3 = QLabel('D', self)
        self.titleLabel3.setFont(QFont("Times New Roman", 17 * self.font_ratio, weight=QFont.Bold))
        self.titleLabel3.setAlignment(Qt.AlignCenter)
        self.titleLabel3.resize(75 * self.screen_ratio, 40 * self.screen_ratio)
        self.titleLabel3.move(150 * self.screen_ratio, 0 * self.screen_ratio)

        self.titleLabel4 = QLabel('S', self)
        self.titleLabel4.setFont(QFont("Times New Roman", 17 * self.font_ratio, weight=QFont.Bold))
        self.titleLabel4.setAlignment(Qt.AlignCenter)
        self.titleLabel4.resize(75 * self.screen_ratio, 40 * self.screen_ratio)
        self.titleLabel4.move(225 * self.screen_ratio, 0 * self.screen_ratio)

        self.backgroundImage2 = QLabel(self)
        self.backgroundImage2.setPixmap(QPixmap("src/msds_about2.png"))
        self.backgroundImage2.setScaledContents(True)
        self.backgroundImage2.resize(300 * self.screen_ratio, 40 * self.screen_ratio)
        self.backgroundImage2.move(0 * self.screen_ratio, 40 * self.screen_ratio)

        self.backgroundImage3 = QLabel(self)
        self.backgroundImage3.setStyleSheet("background-color:#ffffff;")
        self.backgroundImage3.setScaledContents(True)
        self.backgroundImage3.resize(300 * self.screen_ratio, 360 * self.screen_ratio)
        self.backgroundImage3.move(0 * self.screen_ratio, 80 * self.screen_ratio)

        self.logoLabel1 = QLabel(self.str_about, self)
        if self.lang_main == "en":
            self.logoLabel1.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        elif self.lang_main == "fa":
            self.logoLabel1.setFont(QFont("B Nazanin", 10 * self.font_ratio))
        self.logoLabel1.setAlignment(Qt.AlignLeft)
        self.logoLabel1.setWordWrap(True)
        self.logoLabel1.setMargin(15)
        self.logoLabel1.resize(300 * self.screen_ratio, 250 * self.screen_ratio)
        self.logoLabel1.move(0 * self.screen_ratio, 100 * self.screen_ratio)

        self.LogoImage1 = QLabel(self)
        self.LogoImage1.setPixmap(QPixmap("src/google_translate.png"))
        self.LogoImage1.setScaledContents(True)
        self.LogoImage1.resize(80 * self.screen_ratio, 80 * self.screen_ratio)
        self.LogoImage1.move(20 * self.screen_ratio, 310 * self.screen_ratio)

        self.LogoImage2 = QLabel(self)
        self.LogoImage2.setPixmap(QPixmap("src/qt.png"))
        self.LogoImage2.setScaledContents(True)
        self.LogoImage2.resize(60 * self.screen_ratio, 40 * self.screen_ratio)
        self.LogoImage2.move(120 * self.screen_ratio, 330 * self.screen_ratio)

        self.LogoImage3 = QLabel(self)
        self.LogoImage3.setPixmap(QPixmap("src/tums.png"))
        self.LogoImage3.setScaledContents(True)
        self.LogoImage3.resize(80 * self.screen_ratio, 80 * self.screen_ratio)
        self.LogoImage3.move(200 * self.screen_ratio, 310 * self.screen_ratio)

        self.logoLabel2 = QLabel('All Rights Reserved By TUMS 2022 ©', self)
        self.logoLabel2.setAlignment(Qt.AlignCenter)
        self.logoLabel2.resize(300 * self.screen_ratio, 20 * self.screen_ratio)
        self.logoLabel2.move(0 * self.screen_ratio, 410 * self.screen_ratio)

        self.setFixedSize(300 * self.screen_ratio, 440 * self.screen_ratio)
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        self.setWindowIcon(QIcon('MSDS_titlebar_icon.png'))
        self.setWindowTitle('MSDS - ' + self.str_win_title)
