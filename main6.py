from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QAction, QFormLayout, QHBoxLayout, QVBoxLayout, \
    QSlider, QRadioButton, QTabWidget, QLabel, QDesktopWidget, QLineEdit, QTextEdit, \
    QCheckBox, QRadioButton, QScrollArea, QGridLayout, QListWidget, QListWidgetItem, \
    QTableWidget, QPushButton, QMessageBox, QGroupBox, QMainWindow, QProgressBar, QApplication, QFrame, QComboBox
import sys
import codecs
import main7
import main8


class Window_main6(QMainWindow):

    screen_ratio = 1
    font_ratio = 1

    # strings_en:
    str_win_title_en = "Material Safety Data Sheet(MSDS) signs"
    str_sign_help_en = "MSDS Sign Help"
    str_sign_health_en = "4 Deadly\n3 Extreme danger\n2 Hazardous\n1 Slightly hazardous\n0 Normal material"
    str_sign_fire_en = "Flash points:\n4 Below 73°F(22.8°C)\n3 Below 100°F(37.8°C)\n2 Above 100°F(37.8°C)\n1 Above 200°F(93.3°C)\n0 Will not burn"
    str_sign_reactivity_en = "4 May detonate\n3 Shock and heat\nmay dedonate\n2 Violent chemical\nchange\n1 Unstable if heated\n0 Stable"
    str_sign_specific_en = "OX\u0009Oxidizer\nACID\u0009Acid\nALK\u0009Alali\nCOR\u0009Corrosive\n\uFFE6\u0009Use no water\n\u2622\u0009Radioactive"
    str_button_health_en = "Health hazard"
    str_button_fire_en = "Fire hazard"
    str_button_reactivity_en = "Reactivity"
    str_button_specific_en = "HMIS guide"
    # -----------
    # strings_fa:
    str_win_title_fa = "(MSDS)علائم برگه های اطلاعات ایمنی"
    str_sign_help_fa = "MSDS راهنمای علامت"
    str_sign_health_fa = "4 مرگ آور\n3 خطر شدید\n2 خطرناک\n1 کمی خطرناک\n0 ماده عادی"
    str_sign_fire_fa = "نقاط اشتعال:\n4 زیر (22.8°C)\n3 زیر (37.8°C)\n2 بالای (37.8°C)\n1 بالای (93.3°C)\n0 غیر قابل اشتعال"
    str_sign_reactivity_fa = "4 ممکن است منفجر شود\n3 شوک و گرما ممکن است\nباعث انفجار شود\n2 تغییر شیمیایی شدید\n1 ناپایدار در صورت\nحرارت دهی\n0 پایدار"
    str_sign_specific_fa = "اکسید کننده OX\nاسید ACID\n قلیا ALK\nخورنده COR\nآب استفاده نشود \uFFE6\nرادیواکتیو \u2622"
    str_button_health_fa = "خطر سلامت"
    str_button_fire_fa = "خطر اشتعال"
    str_button_reactivity_fa = "واکنش پزیری"
    str_button_specific_fa = "HMIS راهنمای"
    # -----------
    # strings_final:
    str_win_title = ""
    str_sign_help = ""
    str_sign_health = ""
    str_sign_fire = ""
    str_sign_reactivity = ""
    str_sign_specific = ""
    str_button_health = ""
    str_button_fire = ""
    str_button_reactivity = ""
    str_button_specific = ""
    # -----------

    lang_main = ""

    def __init__(self):
        super(Window_main6, self).__init__()
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
            self.str_sign_help = self.str_sign_help_en
            self.str_sign_health = self.str_sign_health_en
            self.str_sign_fire = self.str_sign_fire_en
            self.str_sign_reactivity = self.str_sign_reactivity_en
            self.str_sign_specific = self.str_sign_specific_en
            self.str_button_health = self.str_button_health_en
            self.str_button_fire = self.str_button_fire_en
            self.str_button_reactivity = self.str_button_reactivity_en
            self.str_button_specific = self.str_button_specific_en
        elif self.lang_main == "fa":
            self.str_win_title = self.str_win_title_fa
            self.str_sign_help = self.str_sign_help_fa
            self.str_sign_health = self.str_sign_health_fa
            self.str_sign_fire = self.str_sign_fire_fa
            self.str_sign_reactivity = self.str_sign_reactivity_fa
            self.str_sign_specific = self.str_sign_specific_fa
            self.str_button_health = self.str_button_health_fa
            self.str_button_fire = self.str_button_fire_fa
            self.str_button_reactivity = self.str_button_reactivity_fa
            self.str_button_specific = self.str_button_specific_fa

        self.backgroundImage1 = QLabel(self)
        self.backgroundImage1.setStyleSheet("background-color:#ffffff;")
        self.backgroundImage1.setScaledContents(True)
        self.backgroundImage1.resize(460 * self.screen_ratio, 410 * self.screen_ratio)
        self.backgroundImage1.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        self.advancedSearchTitleLabel = QLabel(self.str_sign_help, self)
        if self.lang_main == "en":
            self.advancedSearchTitleLabel.setFont(QFont("Times New Roman", 17 * self.font_ratio, weight=QFont.Bold))
        elif self.lang_main == "fa":
            self.advancedSearchTitleLabel.setFont(QFont("B Nazanin", 17 * self.font_ratio, weight=QFont.Bold))
        self.advancedSearchTitleLabel.setAlignment(Qt.AlignCenter)
        self.advancedSearchTitleLabel.resize(440 * self.screen_ratio, 30 * self.screen_ratio)
        self.advancedSearchTitleLabel.move(10 * self.screen_ratio, 10 * self.screen_ratio)

        self.msdsSignImage = QLabel(self)
        self.msdsSignImage.setPixmap(QPixmap("src/msds_sign.png"))
        self.msdsSignImage.setScaledContents(True)
        self.msdsSignImage.resize(120 * self.screen_ratio, 120 * self.screen_ratio)
        self.msdsSignImage.move(170 * self.screen_ratio, 160 * self.screen_ratio)

        self.msdsSignLabel_m = QLabel("3", self)
        self.msdsSignLabel_m.setFont(QFont("Ubuntu Regular", 14 * self.font_ratio))
        self.msdsSignLabel_m.setStyleSheet("color:#ffffff;")
        self.msdsSignLabel_m.setAlignment(Qt.AlignCenter)
        self.msdsSignLabel_m.resize(20 * self.screen_ratio, 20 * self.screen_ratio)
        self.msdsSignLabel_m.move(190 * self.screen_ratio, 210 * self.screen_ratio)

        self.msdsSignLabel_s1 = QLabel("4", self)
        self.msdsSignLabel_s1.setFont(QFont("Ubuntu Regular", 14 * self.font_ratio))
        self.msdsSignLabel_s1.setStyleSheet("color:#ffffff;")
        self.msdsSignLabel_s1.setAlignment(Qt.AlignCenter)
        self.msdsSignLabel_s1.resize(20 * self.screen_ratio, 20 * self.screen_ratio)
        self.msdsSignLabel_s1.move(220 * self.screen_ratio, 180 * self.screen_ratio)

        self.msdsSignLabel_d = QLabel("2", self)
        self.msdsSignLabel_d.setFont(QFont("Ubuntu Regular", 14 * self.font_ratio))
        self.msdsSignLabel_d.setStyleSheet("color:#000000;")
        self.msdsSignLabel_d.setAlignment(Qt.AlignCenter)
        self.msdsSignLabel_d.resize(20 * self.screen_ratio, 20 * self.screen_ratio)
        self.msdsSignLabel_d.move(250 * self.screen_ratio, 210 * self.screen_ratio)

        self.msdsSignLabel_s2 = QLabel("\uFFE6", self)
        self.msdsSignLabel_s2.setFont(QFont("Ubuntu Regular", 14 * self.font_ratio))
        self.msdsSignLabel_s2.setStyleSheet("color:#000000;")
        self.msdsSignLabel_s2.setAlignment(Qt.AlignCenter)
        self.msdsSignLabel_s2.resize(20 * self.screen_ratio, 20 * self.screen_ratio)
        self.msdsSignLabel_s2.move(220 * self.screen_ratio, 240 * self.screen_ratio)

        self.msdsSignText_m = QLabel(self.str_sign_health, self)
        if self.lang_main == "en":
            self.msdsSignText_m.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msdsSignText_m.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.advancedSearchTitleLabel.setAlignment(Qt.AlignCenter)
        self.msdsSignText_m.setStyleSheet("background-color:#ffffff; color:#3e6aef;")
        self.msdsSignText_m.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
        self.msdsSignText_m.resize(160 * self.screen_ratio, 120 * self.screen_ratio)
        self.msdsSignText_m.move(50 * self.screen_ratio, 40 * self.screen_ratio)

        self.msdsSignText_s1 = QLabel(self.str_sign_fire, self)
        if self.lang_main == "en":
            self.msdsSignText_s1.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msdsSignText_s1.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.msdsSignText_s1.setStyleSheet("background-color:#ffffff; color:#f01513;")
        self.msdsSignText_s1.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
        self.msdsSignText_s1.resize(160 * self.screen_ratio, 120 * self.screen_ratio)
        self.msdsSignText_s1.move(270 * self.screen_ratio, 40 * self.screen_ratio)

        self.msdsSignText_d = QLabel(self.str_sign_reactivity, self)
        if self.lang_main == "en":
            self.msdsSignText_d.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msdsSignText_d.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.msdsSignText_d.setStyleSheet("background-color:#ffffff; color:#ffae42;")
        self.msdsSignText_d.setAlignment(Qt.AlignLeft)
        self.msdsSignText_d.resize(160 * self.screen_ratio, 120 * self.screen_ratio)
        self.msdsSignText_d.move(270 * self.screen_ratio, 280 * self.screen_ratio)

        self.msdsSignText_s2 = QLabel(self.str_sign_specific, self)
        if self.lang_main == "en":
            self.msdsSignText_s2.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msdsSignText_s2.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.msdsSignText_s2.setStyleSheet("background-color:#ffffff; color:#000000;")
        self.msdsSignText_s2.setAlignment(Qt.AlignLeft)
        self.msdsSignText_s2.resize(160 * self.screen_ratio, 120 * self.screen_ratio)
        self.msdsSignText_s2.move(50 * self.screen_ratio, 280 * self.screen_ratio)

        self.msdsSignButton_m = QPushButton(self)
        self.msdsSignButton_m.setText(self.str_button_health)
        self.msdsSignButton_m.resize(80 * self.screen_ratio, 30 * self.screen_ratio)
        self.msdsSignButton_m.move(80 * self.screen_ratio, 170 * self.screen_ratio)
        self.msdsSignButton_m.clicked.connect(self.msdsSignButton_m_clicked)

        self.msdsSignButton_s1 = QPushButton(self)
        self.msdsSignButton_s1.setText(self.str_button_fire)
        self.msdsSignButton_s1.resize(80 * self.screen_ratio, 30 * self.screen_ratio)
        self.msdsSignButton_s1.move(300 * self.screen_ratio, 170 * self.screen_ratio)
        self.msdsSignButton_s1.clicked.connect(self.msdsSignButton_s1_clicked)

        self.msdsSignButton_d = QPushButton(self)
        self.msdsSignButton_d.setText(self.str_button_reactivity)
        self.msdsSignButton_d.resize(80 * self.screen_ratio, 30 * self.screen_ratio)
        self.msdsSignButton_d.move(300 * self.screen_ratio, 240 * self.screen_ratio)
        self.msdsSignButton_d.clicked.connect(self.msdsSignButton_d_clicked)

        self.msdsSignButton_s2 = QPushButton(self)
        self.msdsSignButton_s2.setText(self.str_button_specific)
        self.msdsSignButton_s2.resize(80 * self.screen_ratio, 30 * self.screen_ratio)
        self.msdsSignButton_s2.move(80 * self.screen_ratio, 240 * self.screen_ratio)
        self.msdsSignButton_s2.clicked.connect(self.msdsSignButton_s2_clicked)

        self.setFixedSize(460 * self.screen_ratio, 410 * self.screen_ratio)
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        self.setWindowIcon(QIcon('MSDS_titlebar_icon.png'))
        self.setWindowTitle('MSDS - ' + self.str_win_title)

    def msdsSignButton_m_clicked(self):
        self.win7 = main7.Window_main7("m")
        self.win7.show()

    def msdsSignButton_s1_clicked(self):
        self.win7 = main7.Window_main7("s1")
        self.win7.show()

    def msdsSignButton_d_clicked(self):
        self.win7 = main7.Window_main7("d")
        self.win7.show()

    def msdsSignButton_s2_clicked(self):
        self.win8 = main8.Window_main8()
        self.win8.show()
