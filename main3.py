from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QAction, QFormLayout, QHBoxLayout, QVBoxLayout, \
    QSlider, QRadioButton, QTabWidget, QLabel, QDesktopWidget, QLineEdit, QTextEdit, \
    QCheckBox, QRadioButton, QScrollArea, QGridLayout, QListWidget, QListWidgetItem, \
    QTableWidget, QPushButton, QMessageBox, QGroupBox, QMainWindow, QProgressBar, QApplication, QFrame, QComboBox
import sys
import codecs
import main4


class Window_main3(QMainWindow):

    screen_ratio = 1
    font_ratio = 1

    # strings_en:
    str_win_title_en = "Advanced Search"
    str_advanced_search_title_en = "Advanced Search"
    str_health_en = "Health hazard"
    str_fire_en = "Fire hazard"
    str_reactivity_en = "Reactivity"
    str_select_lang_en = "Language to search"
    str_search_en = "Search"
    # -----------
    # strings_fa:
    str_win_title_fa = "جستجوی پیشرفته"
    str_advanced_search_title_fa = "جستجوی پیشرفته"
    str_health_fa = "خطر سلامت"
    str_fire_fa = "خطر اشتعال"
    str_reactivity_fa = "واکنش پزیری"
    str_select_lang_fa = "زبان جستجو"
    str_search_fa = "جستجو"
    # -----------
    # strings_final:
    str_win_title = ""
    str_advanced_search_title = ""
    str_health = ""
    str_fire = ""
    str_reactivity = ""
    str_select_lang = ""
    str_search = ""
    # -----------

    lang_main = ""

    m_1_int = 0
    m_2_int = 4
    s1_1_int = 0
    s1_2_int = 4
    d_1_int = 0
    d_2_int = 4
    selected_lang_string = "en"

    def __init__(self):
        super(Window_main3, self).__init__()
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
            self.str_advanced_search_title = self.str_advanced_search_title_en
            self.str_health = self.str_health_en
            self.str_fire = self.str_fire_en
            self.str_reactivity = self.str_reactivity_en
            self.str_select_lang = self.str_select_lang_en
            self.str_search = self.str_search_en
        elif self.lang_main == "fa":
            self.str_win_title = self.str_win_title_fa
            self.str_advanced_search_title = self.str_advanced_search_title_fa
            self.str_health = self.str_health_fa
            self.str_fire = self.str_fire_fa
            self.str_reactivity = self.str_reactivity_fa
            self.str_select_lang = self.str_select_lang_fa
            self.str_search = self.str_search_fa

        global m_1_int
        global m_2_int
        global s1_1_int
        global s1_2_int
        global d_1_int
        global d_2_int
        global selected_lang_string

        self.backgroundImage1 = QLabel(self)
        self.backgroundImage1.setStyleSheet("background-color:#ffffff;")
        self.backgroundImage1.setScaledContents(True)
        self.backgroundImage1.resize(300 * self.screen_ratio, 420 * self.screen_ratio)
        self.backgroundImage1.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        self.advancedSearchTitleLabel = QLabel(self.str_advanced_search_title, self)
        if self.lang_main == "en":
            self.advancedSearchTitleLabel.setFont(QFont("Times New Roman", 17 * self.font_ratio, weight=QFont.Bold))
        elif self.lang_main == "fa":
            self.advancedSearchTitleLabel.setFont(QFont("B Nazanin", 17 * self.font_ratio, weight=QFont.Bold))
        self.advancedSearchTitleLabel.setAlignment(Qt.AlignCenter)
        self.advancedSearchTitleLabel.resize(280 * self.screen_ratio, 20 * self.screen_ratio)
        self.advancedSearchTitleLabel.move(10 * self.screen_ratio, 10 * self.screen_ratio)

        self.backgroundImage_m = QLabel(self)
        self.backgroundImage_m.setStyleSheet("background-color:#365fd4;")
        self.backgroundImage_m.setScaledContents(True)
        self.backgroundImage_m.resize(300 * self.screen_ratio, 90 * self.screen_ratio)
        self.backgroundImage_m.move(0 * self.screen_ratio, 40 * self.screen_ratio)

        self.title_m = QLabel(self.str_health, self)
        if self.lang_main == "en":
            self.title_m.setFont(QFont("Times New Roman", 12 * self.font_ratio, weight=QFont.Bold))
        elif self.lang_main == "fa":
            self.title_m.setFont(QFont("B Nazanin", 12 * self.font_ratio, weight=QFont.Bold))
        self.title_m.setAlignment(Qt.AlignCenter)
        self.title_m.setStyleSheet("color:#ffffff;")
        self.title_m.resize(280 * self.screen_ratio, 20 * self.screen_ratio)
        self.title_m.move(10 * self.screen_ratio, 50 * self.screen_ratio)

        self.combo_m_1 = QComboBox(self)
        for i in range(5):
            self.combo_m_1.addItem(str(i))
        self.combo_m_1.resize(70 * self.screen_ratio, 20 * self.screen_ratio)
        self.combo_m_1.move(30 * self.screen_ratio, 80 * self.screen_ratio)
        self.combo_m_1.activated[str].connect(self.onActivated_m)

        self.to_text_m = QLabel("~", self)
        self.to_text_m.setFont(QFont("Times New Roman", 13 * self.font_ratio))
        self.to_text_m.setAlignment(Qt.AlignCenter)
        self.to_text_m.resize(10 * self.screen_ratio, 10 * self.screen_ratio)
        self.to_text_m.move(145 * self.screen_ratio, 80 * self.screen_ratio)

        self.combo_m_2 = QComboBox(self)
        for i in range(5):
            self.combo_m_2.addItem(str(i))
        self.combo_m_2.setCurrentIndex(4)
        self.combo_m_2.resize(70 * self.screen_ratio, 20 * self.screen_ratio)
        self.combo_m_2.move(200 * self.screen_ratio, 80 * self.screen_ratio)
        self.combo_m_2.activated[str].connect(self.onActivated_m)

        self.num_m_1 = QLabel("0", self)
        self.num_m_1.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        self.num_m_1.setAlignment(Qt.AlignCenter)
        self.num_m_1.resize(10 * self.screen_ratio, 10 * self.screen_ratio)
        self.num_m_1.move(120 * self.screen_ratio, 110 * self.screen_ratio)

        self.num_m_to = QLabel("to", self)
        self.num_m_to.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        self.num_m_to.setAlignment(Qt.AlignCenter)
        self.num_m_to.resize(10 * self.screen_ratio, 10 * self.screen_ratio)
        self.num_m_to.move(145 * self.screen_ratio, 110 * self.screen_ratio)

        self.num_m_2 = QLabel("4", self)
        self.num_m_2.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        self.num_m_2.setAlignment(Qt.AlignCenter)
        self.num_m_2.resize(10 * self.screen_ratio, 10 * self.screen_ratio)
        self.num_m_2.move(170 * self.screen_ratio, 110 * self.screen_ratio)

        self.backgroundImage_s1 = QLabel(self)
        self.backgroundImage_s1.setStyleSheet("background-color:#ec1f1f;")
        self.backgroundImage_s1.setScaledContents(True)
        self.backgroundImage_s1.resize(300 * self.screen_ratio, 90 * self.screen_ratio)
        self.backgroundImage_s1.move(0 * self.screen_ratio, 130 * self.screen_ratio)

        self.title_s1 = QLabel(self.str_fire, self)
        if self.lang_main == "en":
            self.title_s1.setFont(QFont("Times New Roman", 12 * self.font_ratio, weight=QFont.Bold))
        elif self.lang_main == "fa":
            self.title_s1.setFont(QFont("B Nazanin", 12 * self.font_ratio, weight=QFont.Bold))
        self.title_s1.setAlignment(Qt.AlignCenter)
        self.title_s1.setStyleSheet("color:#ffffff;")
        self.title_s1.resize(280 * self.screen_ratio, 20 * self.screen_ratio)
        self.title_s1.move(10 * self.screen_ratio, 140 * self.screen_ratio)

        self.combo_s1_1 = QComboBox(self)
        for i in range(5):
            self.combo_s1_1.addItem(str(i))
        self.combo_s1_1.resize(70 * self.screen_ratio, 20 * self.screen_ratio)
        self.combo_s1_1.move(30 * self.screen_ratio, 170 * self.screen_ratio)
        self.combo_s1_1.activated[str].connect(self.onActivated_s1)

        self.to_text_s1 = QLabel("~", self)
        self.to_text_s1.setFont(QFont("Times New Roman", 13 * self.font_ratio))
        self.to_text_s1.setAlignment(Qt.AlignCenter)
        self.to_text_s1.resize(10 * self.screen_ratio, 10 * self.screen_ratio)
        self.to_text_s1.move(145 * self.screen_ratio, 170 * self.screen_ratio)

        self.combo_s1_2 = QComboBox(self)
        for i in range(5):
            self.combo_s1_2.addItem(str(i))
        self.combo_s1_2.setCurrentIndex(4)
        self.combo_s1_2.resize(70 * self.screen_ratio, 20 * self.screen_ratio)
        self.combo_s1_2.move(200 * self.screen_ratio, 170 * self.screen_ratio)
        self.combo_s1_2.activated[str].connect(self.onActivated_s1)

        self.num_s1_1 = QLabel("0", self)
        self.num_s1_1.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        self.num_s1_1.setAlignment(Qt.AlignCenter)
        self.num_s1_1.resize(10 * self.screen_ratio, 10 * self.screen_ratio)
        self.num_s1_1.move(120 * self.screen_ratio, 200 * self.screen_ratio)

        self.num_s1_to = QLabel("to", self)
        self.num_s1_to.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        self.num_s1_to.setAlignment(Qt.AlignCenter)
        self.num_s1_to.resize(10 * self.screen_ratio, 10 * self.screen_ratio)
        self.num_s1_to.move(145 * self.screen_ratio, 200 * self.screen_ratio)

        self.num_s1_2 = QLabel("4", self)
        self.num_s1_2.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        self.num_s1_2.setAlignment(Qt.AlignCenter)
        self.num_s1_2.resize(10 * self.screen_ratio, 10 * self.screen_ratio)
        self.num_s1_2.move(170 * self.screen_ratio, 200 * self.screen_ratio)

        self.backgroundImage_d = QLabel(self)
        self.backgroundImage_d.setStyleSheet("background-color:#fffc00;")
        self.backgroundImage_d.setScaledContents(True)
        self.backgroundImage_d.resize(300 * self.screen_ratio, 90 * self.screen_ratio)
        self.backgroundImage_d.move(0 * self.screen_ratio, 220 * self.screen_ratio)

        self.title_d = QLabel(self.str_reactivity, self)
        if self.lang_main == "en":
            self.title_d.setFont(QFont("Times New Roman", 12 * self.font_ratio, weight=QFont.Bold))
        elif self.lang_main == "fa":
            self.title_d.setFont(QFont("B Nazanin", 12 * self.font_ratio, weight=QFont.Bold))
        self.title_d.setAlignment(Qt.AlignCenter)
        self.title_d.setStyleSheet("color:#000000;")
        self.title_d.resize(280 * self.screen_ratio, 20 * self.screen_ratio)
        self.title_d.move(10 * self.screen_ratio, 230 * self.screen_ratio)

        self.combo_d_1 = QComboBox(self)
        for i in range(5):
            self.combo_d_1.addItem(str(i))
        self.combo_d_1.resize(70 * self.screen_ratio, 20 * self.screen_ratio)
        self.combo_d_1.move(30 * self.screen_ratio, 260 * self.screen_ratio)
        self.combo_d_1.activated[str].connect(self.onActivated_d)

        self.to_text_d = QLabel("~", self)
        self.to_text_d.setFont(QFont("Times New Roman", 13 * self.font_ratio))
        self.to_text_d.setAlignment(Qt.AlignCenter)
        self.to_text_d.resize(10 * self.screen_ratio, 10 * self.screen_ratio)
        self.to_text_d.move(145 * self.screen_ratio, 260 * self.screen_ratio)

        self.combo_d_2 = QComboBox(self)
        for i in range(5):
            self.combo_d_2.addItem(str(i))
        self.combo_d_2.setCurrentIndex(4)
        self.combo_d_2.resize(70 * self.screen_ratio, 20 * self.screen_ratio)
        self.combo_d_2.move(200 * self.screen_ratio, 260 * self.screen_ratio)
        self.combo_d_2.activated[str].connect(self.onActivated_d)

        self.num_d_1 = QLabel("0", self)
        self.num_d_1.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        self.num_d_1.setAlignment(Qt.AlignCenter)
        self.num_d_1.resize(10 * self.screen_ratio, 10 * self.screen_ratio)
        self.num_d_1.move(120 * self.screen_ratio, 290 * self.screen_ratio)

        self.num_d_to = QLabel("to", self)
        self.num_d_to.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        self.num_d_to.setAlignment(Qt.AlignCenter)
        self.num_d_to.resize(10 * self.screen_ratio, 10 * self.screen_ratio)
        self.num_d_to.move(145 * self.screen_ratio, 290 * self.screen_ratio)

        self.num_d_2 = QLabel("4", self)
        self.num_d_2.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        self.num_d_2.setAlignment(Qt.AlignCenter)
        self.num_d_2.resize(10 * self.screen_ratio, 10 * self.screen_ratio)
        self.num_d_2.move(170 * self.screen_ratio, 290 * self.screen_ratio)

        self.backgroundImage_searchLang = QLabel(self)
        self.backgroundImage_searchLang.setStyleSheet("background-color:#ffffff;")
        self.backgroundImage_searchLang.setScaledContents(True)
        self.backgroundImage_searchLang.resize(300 * self.screen_ratio, 110 * self.screen_ratio)
        self.backgroundImage_searchLang.move(0 * self.screen_ratio, 310 * self.screen_ratio)

        self.title_searchLang = QLabel(self.str_select_lang, self)
        if self.lang_main == "en":
            self.title_searchLang.setFont(QFont("Times New Roman", 12 * self.font_ratio, weight=QFont.Bold))
        elif self.lang_main == "fa":
            self.title_searchLang.setFont(QFont("B Nazanin", 12 * self.font_ratio, weight=QFont.Bold))
        self.title_searchLang.setAlignment(Qt.AlignCenter)
        self.title_searchLang.setStyleSheet("color:#000000;")
        self.title_searchLang.resize(280 * self.screen_ratio, 20 * self.screen_ratio)
        self.title_searchLang.move(10 * self.screen_ratio, 320 * self.screen_ratio)

        self.radioButton_en_searchLang = QRadioButton(self)
        self.radioButton_en_searchLang.setText("English")
        self.radioButton_en_searchLang.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        if self.lang_main == "en":
            self.radioButton_en_searchLang.setChecked(True)
        self.radioButton_en_searchLang.resize(70 * self.screen_ratio, 20 * self.screen_ratio)
        self.radioButton_en_searchLang.move(80 * self.screen_ratio, 350 * self.screen_ratio)

        self.radioButton_fa_searchLang = QRadioButton(self)
        self.radioButton_fa_searchLang.setText("فارسی")
        if self.lang_main == "fa":
            self.radioButton_fa_searchLang.setChecked(True)
        self.radioButton_fa_searchLang.setFont(QFont("B Nazanin", 10 * self.font_ratio))
        self.radioButton_fa_searchLang.resize(70 * self.screen_ratio, 20 * self.screen_ratio)
        self.radioButton_fa_searchLang.move(160 * self.screen_ratio, 350 * self.screen_ratio)

        self.advancedSearchButton = QPushButton(self)
        self.advancedSearchButton.setText(self.str_search)
        self.advancedSearchButton.resize(50 * self.screen_ratio, 30 * self.screen_ratio)
        self.advancedSearchButton.move(125 * self.screen_ratio, 380 * self.screen_ratio)
        self.advancedSearchButton.clicked.connect(self.advancedSearchButton_clicked)

        self.setFixedSize(300 * self.screen_ratio, 420 * self.screen_ratio)
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        self.setWindowIcon(QIcon('MSDS_titlebar_icon.png'))
        self.setWindowTitle('MSDS - ' + self.str_win_title)

    def onActivated_m(self, text):
        self.m_1_int = int(self.combo_m_1.currentText())
        self.m_2_int = int(self.combo_m_2.currentText())
        if self.m_1_int <= self.m_2_int:
            self.num_m_1.setText(str(self.m_1_int))
            self.num_m_2.setText(str(self.m_2_int))
        elif self.m_1_int > self.m_2_int:
            self.num_m_1.setText(str(self.m_2_int))
            self.num_m_2.setText(str(self.m_1_int))

    def onActivated_s1(self, text):
        self.s1_1_int = int(self.combo_s1_1.currentText())
        self.s1_2_int = int(self.combo_s1_2.currentText())
        if self.s1_1_int <= self.s1_2_int:
            self.num_s1_1.setText(str(self.s1_1_int))
            self.num_s1_2.setText(str(self.s1_2_int))
        elif self.s1_1_int > self.s1_2_int:
            self.num_s1_1.setText(str(self.s1_2_int))
            self.num_s1_2.setText(str(self.s1_1_int))

    def onActivated_d(self, text):
        self.d_1_int = int(self.combo_d_1.currentText())
        self.d_2_int = int(self.combo_d_2.currentText())
        if self.d_1_int <= self.d_2_int:
            self.num_d_1.setText(str(self.d_1_int))
            self.num_d_2.setText(str(self.d_2_int))
        elif self.d_1_int > self.d_2_int:
            self.num_d_1.setText(str(self.d_2_int))
            self.num_d_2.setText(str(self.d_1_int))

    def advancedSearchButton_clicked(self):
        if self.radioButton_en_searchLang.isChecked():
            self.selected_lang_string = "en"
        elif self.radioButton_fa_searchLang.isChecked():
            self.selected_lang_string = "fa"

        if self.m_1_int > self.m_2_int:
            self.x = self.m_1_int
            self.m_1_int = self.m_2_int
            self.m_2_int = self.x

        if self.s1_1_int > self.s1_2_int:
            self.x = self.s1_1_int
            self.s1_1_int = self.s1_2_int
            self.s1_2_int = self.x

        if self.d_1_int > self.d_2_int:
            self.x = self.d_1_int
            self.d_1_int = self.d_2_int
            self.d_2_int = self.x

        self.win4 = main4.Window_main4(self.m_1_int, self.m_2_int, self.s1_1_int, self.s1_2_int, self.d_1_int, self.d_2_int, self.selected_lang_string)
        self.win4.show()
