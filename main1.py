from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QAction, QFormLayout, QHBoxLayout, QVBoxLayout, \
    QSlider, QRadioButton, QTabWidget, QLabel, QDesktopWidget, QLineEdit, QTextEdit, \
    QCheckBox, QRadioButton, QScrollArea, QGridLayout, QListWidget, QListWidgetItem, \
    QTableWidget, QPushButton, QMessageBox, QGroupBox, QMainWindow, QProgressBar, QApplication, QFrame, QComboBox
import sys
import sqlite3
import codecs
import webbrowser
import time
import msds
import main2
import main3
import main5
import main6
import main8
import main9
import main_about


class Window_main(QMainWindow):

    screen_ratio = 1
    font_ratio = 1

    # strings_en:
    str_textbox_text_en = "Compound or Element Name"
    str_menu_label_en = "Menu"
    str_menu_1_en = "Advanced Search"
    str_menu_2_en = "Search By CAS#"
    str_menu_3_en = "Material Safety Data Sheet(MSDS) signs"
    str_menu_4_en = "Hazardous Material Index Ratings(HMIS) guide"
    str_menu_5_en = "Language"
    str_menu_6_en = "Settings"
    str_menu_7_en = "Visit msds.ir"
    str_menu_8_en = "Visit pharmacy.tums.ac.ir"
    str_menu_9_en = "About Us"
    str_menu_10_en = "Contact"
    str_lang_alert_title_en = "Language"
    str_lang_alert_messege_en = "Select app language:"
    str_lang_alert_change_alert_en = "Language change alert!"
    str_lang_alert_change_alert_message_en = "App will close to save changes!\nPlease restart app manually."
    str_lang_alert_change_alert_ok_en = "OK"
    # -----------
    # strings_fa:
    str_textbox_text_fa = "نام ترکیب یا عنصر"
    str_menu_label_fa = "منو"
    str_menu_1_fa = "جستجوی پیشرفته"
    str_menu_2_fa = "CAS جستجو بر اساس شماره"
    str_menu_3_fa = "(MSDS)علائم برگه های اطلاعات ایمنی"
    str_menu_4_fa = "(HMIS)راهنمای رتبه بندی فهرست مواد خطرناک"
    str_menu_5_fa = "زبان"
    str_menu_6_fa = "تنظیمات"
    str_menu_7_fa = "msds.ir بازدید از"
    str_menu_8_fa = "pharmacy.tums.ac.ir بازدید از"
    str_menu_9_fa = "درباره ما"
    str_menu_10_fa = "ارتباط"
    str_lang_alert_title_fa = "زبان"
    str_lang_alert_messege_fa = "زبان برنامه را انتخاب کنید:"
    str_lang_alert_change_alert_fa = "اخطار تغییر زبان!"
    str_lang_alert_change_alert_message_fa = "برنامه برای ذخیره تغییرات بسته خواهد شد!\nلطفا برنامه را به صورت دستی دوباره اجرا کنید."
    str_lang_alert_change_alert_ok_fa = "باشه"
    # -----------
    # strings_final:
    str_textbox_text = ""
    str_menu_label = ""
    str_menu_1 = ""
    str_menu_2 = ""
    str_menu_3 = ""
    str_menu_4 = ""
    str_menu_5 = ""
    str_menu_6 = ""
    str_menu_7 = ""
    str_menu_8 = ""
    str_menu_9 = ""
    str_menu_10 = ""
    str_lang_alert_title = ""
    str_lang_alert_messege = ""
    str_lang_alert_change_alert = ""
    str_lang_alert_change_alert_message = ""
    str_lang_alert_change_alert_ok = ""
    # -----------

    lang_main = ""
    list_type_set = "tums-fda"

    maintitle_full = []
    maintitle_full_fa = []
    maintitle_full_fa_fda = []

    subtitle_full = []
    subtitle_full_fa = []
    subtitle_full_fa_fda = []

    menuStatus = False
    list_lang = "en"
    list_item = ""
    list_type = ""

    def __init__(self):
        super(Window_main, self).__init__()
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
            self.str_textbox_text = self.str_textbox_text_en
            self.str_menu_label = self.str_menu_label_en
            self.str_menu_1 = self.str_menu_1_en
            self.str_menu_2 = self.str_menu_2_en
            self.str_menu_3 = self.str_menu_3_en
            self.str_menu_4 = self.str_menu_4_en
            self.str_menu_5 = self.str_menu_5_en
            self.str_menu_6 = self.str_menu_6_en
            self.str_menu_7 = self.str_menu_7_en
            self.str_menu_8 = self.str_menu_8_en
            self.str_menu_9 = self.str_menu_9_en
            self.str_menu_10 = self.str_menu_10_en
            self.str_lang_alert_title = self.str_lang_alert_title_en
            self.str_lang_alert_messege = self.str_lang_alert_messege_en
            self.str_lang_alert_change_alert = self.str_lang_alert_change_alert_en
            self.str_lang_alert_change_alert_message = self.str_lang_alert_change_alert_message_en
            self.str_lang_alert_change_alert_ok = self.str_lang_alert_change_alert_ok_en
        elif self.lang_main == "fa":
            self.str_textbox_text = self.str_textbox_text_fa
            self.str_menu_label = self.str_menu_label_fa
            self.str_menu_1 = self.str_menu_1_fa
            self.str_menu_2 = self.str_menu_2_fa
            self.str_menu_3 = self.str_menu_3_fa
            self.str_menu_4 = self.str_menu_4_fa
            self.str_menu_5 = self.str_menu_5_fa
            self.str_menu_6 = self.str_menu_6_fa
            self.str_menu_7 = self.str_menu_7_fa
            self.str_menu_8 = self.str_menu_8_fa
            self.str_menu_9 = self.str_menu_9_fa
            self.str_menu_10 = self.str_menu_10_fa
            self.str_lang_alert_title = self.str_lang_alert_title_fa
            self.str_lang_alert_messege = self.str_lang_alert_messege_fa
            self.str_lang_alert_change_alert = self.str_lang_alert_change_alert_fa
            self.str_lang_alert_change_alert_message = self.str_lang_alert_change_alert_message_fa
            self.str_lang_alert_change_alert_ok = self.str_lang_alert_change_alert_ok_fa

        self.maintitle_full = []
        self.maintitle_full_fa = []
        self.maintitle_full_fa_fda = []

        self.subtitle_full = []
        self.subtitle_full_fa = []
        self.subtitle_full_fa_fda = []

        conn = sqlite3.connect("data/msds_1.0.2.db")

        cursor = conn.execute("SELECT cas_int, name_en, chem_formula from msds_table_en")
        for row in cursor:
            self.maintitle_full.append(row[1])
            self.subtitle_full.append(row[2])
        cursor.close()

        cursor = conn.execute("SELECT cas_int, name_fa, chem_formula from msds_table_fa")
        for row in cursor:
            self.maintitle_full_fa.append(row[1])
            self.subtitle_full_fa.append(row[2])
        cursor.close()

        cursor = conn.execute("SELECT cas_int, name, chem_formula from msds_table_fda")
        for row in cursor:
            self.maintitle_full_fa_fda.append(row[1])
            self.subtitle_full_fa_fda.append(row[2])
        cursor.close()

        list_type_get = codecs.open("data/list_type.txt", encoding='utf-8', mode="r")
        self.list_type_set = list_type_get.read()
        list_type_get.close()

        self.backgroundImage1 = QLabel(self)
        self.backgroundImage1.setPixmap(QPixmap("src/msds_title.png"))
        self.backgroundImage1.setScaledContents(True)
        self.backgroundImage1.resize(300 * self.screen_ratio, 80 * self.screen_ratio)
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

        self.searchBox = QLineEdit(self)
        self.searchBox.setPlaceholderText(self.str_textbox_text)
        self.searchBox.setFont(QFont("Ubuntu Regular", 10 * self.font_ratio))
        self.searchBox.setStyleSheet("padding-left:15px;padding-right:15px")
        #self.searchbox.setStyleSheet("background-color:#000000;")
        self.searchBox.resize(280 * self.screen_ratio, 30 * self.screen_ratio)
        self.searchBox.move(10 * self.screen_ratio, 40 * self.screen_ratio)
        self.searchBox.textChanged[str].connect(self.searchBox_textChanged)

        #self.backgroundImage2 = QLabel(self)
        #self.backgroundImage2.setPixmap(QPixmap("src/msds_title_3.png"))
        #self.backgroundImage2.setScaledContents(True)
        #self.backgroundImage2.resize(300 * self.screen_ratio, 360 * self.screen_ratio)
        #self.backgroundImage2.move(0 * self.screen_ratio, 80 * self.screen_ratio)

        self.tabView = QTabWidget(self)
        self.tabView.tab1 = QWidget()
        self.tabView.tab2 = QWidget()
        self.tabView.addTab(self.tabView.tab1, "Tab 1")
        self.tabView.addTab(self.tabView.tab2, "Tab 2")
        self.tab1UI()
        self.tab2UI()
        if self.lang_main == "en":
            self.tabView.setCurrentIndex(0)
        elif self.lang_main == "fa":
            self.tabView.setCurrentIndex(1)
        self.tabView.move(10 * self.screen_ratio, 90 * self.screen_ratio)
        self.tabView.currentChanged[int].connect(self.tabView_tabChanged)

        #self.menuButton = QLabel(self)
        self.menuButton = ClickLabel(self)
        self.menuButton.setPixmap(QPixmap("src/menu_1.png"))
        self.menuButton.setScaledContents(True)
        self.menuButton.resize(40 * self.screen_ratio, 40 * self.screen_ratio)
        self.menuButton.move(250 * self.screen_ratio, 390 * self.screen_ratio)
        self.menuButton.clicked.connect(self.menuButton_clicked)

        #self.backgroundImage3 = QLabel(self)
        #self.backgroundImage3.setPixmap(QPixmap("src/msds_title_3.png"))
        #self.backgroundImage3.setScaledContents(True)
        #self.backgroundImage3.resize(300 * self.screen_ratio, 440 * self.screen_ratio)
        #self.backgroundImage3.move(300 * self.screen_ratio, 0 * self.screen_ratio)

        self.titleLabelMenu = QLabel(self.str_menu_label, self)
        if self.lang_main == "en":
            self.titleLabelMenu.setFont(QFont("Times New Roman", 17 * self.font_ratio, weight=QFont.Bold))
        elif self.lang_main == "fa":
            self.titleLabelMenu.setFont(QFont("B Nazanin", 17 * self.font_ratio, weight=QFont.Bold))
        self.titleLabelMenu.setAlignment(Qt.AlignCenter)
        self.titleLabelMenu.resize(300 * self.screen_ratio, 40 * self.screen_ratio)
        self.titleLabelMenu.move(300 * self.screen_ratio, 0 * self.screen_ratio)

        self.menuButton1 = QPushButton(self)
        self.menuButton1.setText(self.str_menu_1)
        self.menuButton1.resize(280 * self.screen_ratio, 30 * self.screen_ratio)
        self.menuButton1.move(310 * self.screen_ratio, 40 * self.screen_ratio)
        self.menuButton1.clicked.connect(self.menuButton1_clicked)

        self.menuButton2 = QPushButton(self)
        self.menuButton2.setText(self.str_menu_2)
        self.menuButton2.resize(280 * self.screen_ratio, 30 * self.screen_ratio)
        self.menuButton2.move(310 * self.screen_ratio, 80 * self.screen_ratio)
        self.menuButton2.clicked.connect(self.menuButton2_clicked)

        self.menuButton3 = QPushButton(self)
        self.menuButton3.setText(self.str_menu_3)
        self.menuButton3.resize(280 * self.screen_ratio, 30 * self.screen_ratio)
        self.menuButton3.move(310 * self.screen_ratio, 120 * self.screen_ratio)
        self.menuButton3.clicked.connect(self.menuButton3_clicked)

        self.menuButton4 = QPushButton(self)
        self.menuButton4.setText(self.str_menu_4)
        self.menuButton4.resize(280 * self.screen_ratio, 30 * self.screen_ratio)
        self.menuButton4.move(310 * self.screen_ratio, 160 * self.screen_ratio)
        self.menuButton4.clicked.connect(self.menuButton4_clicked)

        self.menuButton5 = QPushButton(self)
        self.menuButton5.setText(self.str_menu_5)
        self.menuButton5.resize(280 * self.screen_ratio, 30 * self.screen_ratio)
        self.menuButton5.move(310 * self.screen_ratio, 200 * self.screen_ratio)
        self.menuButton5.clicked.connect(self.menuButton5_clicked)

        self.menuButton6 = QPushButton(self)
        self.menuButton6.setText(self.str_menu_6)
        self.menuButton6.resize(280 * self.screen_ratio, 30 * self.screen_ratio)
        self.menuButton6.move(310 * self.screen_ratio, 240 * self.screen_ratio)
        self.menuButton6.clicked.connect(self.menuButton6_clicked)

        self.menuButton7 = QPushButton(self)
        self.menuButton7.setText(self.str_menu_7)
        self.menuButton7.resize(280 * self.screen_ratio, 30 * self.screen_ratio)
        self.menuButton7.move(310 * self.screen_ratio, 280 * self.screen_ratio)
        self.menuButton7.clicked.connect(self.menuButton7_clicked)

        self.menuButton8 = QPushButton(self)
        self.menuButton8.setText(self.str_menu_8)
        self.menuButton8.resize(280 * self.screen_ratio, 30 * self.screen_ratio)
        self.menuButton8.move(310 * self.screen_ratio, 320 * self.screen_ratio)
        self.menuButton8.clicked.connect(self.menuButton8_clicked)

        self.menuButton9 = QPushButton(self)
        self.menuButton9.setText(self.str_menu_9)
        self.menuButton9.resize(135 * self.screen_ratio, 30 * self.screen_ratio)
        self.menuButton9.move(310 * self.screen_ratio, 360 * self.screen_ratio)
        self.menuButton9.clicked.connect(self.menuButton9_clicked)

        self.menuButton10 = QPushButton(self)
        self.menuButton10.setText(self.str_menu_10)
        self.menuButton10.resize(135 * self.screen_ratio, 30 * self.screen_ratio)
        self.menuButton10.move(455 * self.screen_ratio, 360 * self.screen_ratio)
        self.menuButton10.clicked.connect(self.menuButton10_clicked)

        version_get = codecs.open("data/version.txt", encoding='utf-8', mode="r")
        self.version = version_get.read()
        version_get.close()
        self.versionLabel = QLabel('v' + str(self.version), self)
        self.versionLabel.setAlignment(Qt.AlignCenter)
        self.versionLabel.resize(300 * self.screen_ratio, 20 * self.screen_ratio)
        self.versionLabel.move(300 * self.screen_ratio, 410 * self.screen_ratio)

        self.setFixedSize(300 * self.screen_ratio, 440 * self.screen_ratio)
        #self.setMaximumSize(600, 400)
        #self.setMinimumSize(300, 400)
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        self.setWindowIcon(QIcon('MSDS_titlebar_icon.png'))
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle('MSDS')

    def tab1UI(self):
        layout = QVBoxLayout()
        self.tabView.list_en = QListWidget(self)
        self.tabView.list_en.setFrameShape(QFrame.NoFrame)
        #self.tabView.list_en.setStyleSheet("background-color:#ffffff;")
        self.tabView.list_en.clear()
        for i in range(len(self.maintitle_full)):
            self.tabView.list_en.addItem(self.maintitle_full[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full[i] + "]")
        self.tabView.list_en.setFont(QFont("Times New Roman", 11 * self.font_ratio))
        self.tabView.resize(280 * self.screen_ratio, 340 * self.screen_ratio)
        layout.addWidget(self.tabView.list_en)
        self.tabView.setTabText(0, "English")
        self.tabView.tab1.setLayout(layout)
        self.tabView.list_en.itemActivated.connect(self.tabView_en_doubleClicked)

    def tab2UI(self):
        layout = QVBoxLayout()
        self.tabView.list_fa = QListWidget(self)
        self.tabView.list_fa.setFrameShape(QFrame.NoFrame)
        #self.tabView.list_fa.setStyleSheet("background-color:#ffffff;")
        self.tabView.list_fa.clear()
        if self.list_type_set == "tums-fda":
            for i in range(len(self.maintitle_full_fa)):
                self.tabView.list_fa.addItem(self.maintitle_full_fa[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full_fa[i] + "]")
            for i in range(len(self.maintitle_full_fa_fda)):
                self.tabView.list_fa.addItem(self.maintitle_full_fa_fda[i] + "\n" + "[ FDA ] " + " [" + self.subtitle_full_fa_fda[i] + "]")
        elif self.list_type_set == "tums":
            for i in range(len(self.maintitle_full_fa)):
                self.tabView.list_fa.addItem(self.maintitle_full_fa[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full_fa[i] + "]")
        elif self.list_type_set == "fda":
            for i in range(len(self.maintitle_full_fa_fda)):
                self.tabView.list_fa.addItem(self.maintitle_full_fa_fda[i] + "\n" + "[ FDA ] " + " [" + self.subtitle_full_fa_fda[i] + "]")
        self.tabView.list_fa.setFont(QFont("B Nazanin", 11 * self.font_ratio))
        self.tabView.resize(280 * self.screen_ratio, 340 * self.screen_ratio)
        layout.addWidget(self.tabView.list_fa)
        self.tabView.setTabText(1, "فارسی")
        self.tabView.tab2.setLayout(layout)
        self.tabView.list_fa.itemActivated.connect(self.tabView_fa_doubleClicked)

    def searchBox_textChanged(self, text):
        if self.tabView.currentIndex() == 0:
            self.tabView.list_en.clear()
            for i in range(len(self.maintitle_full)):
                if text.lower() in self.maintitle_full[i].lower():
                    self.tabView.list_en.addItem(self.maintitle_full[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full[i] + "]")
        elif self.tabView.currentIndex() == 1:
            self.tabView.list_fa.clear()
            if self.list_type_set == "tums-fda":
                for i in range(len(self.maintitle_full_fa)):
                    if text.lower() in self.maintitle_full_fa[i].lower():
                        self.tabView.list_fa.addItem(self.maintitle_full_fa[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full_fa[i] + "]")
                for i in range(len(self.maintitle_full_fa_fda)):
                    if text.lower() in self.maintitle_full_fa_fda[i].lower():
                        self.tabView.list_fa.addItem(self.maintitle_full_fa_fda[i] + "\n" + "[ FDA ] " + " [" + self.subtitle_full_fa_fda[i] + "]")
            elif self.list_type_set == "tums":
                for i in range(len(self.maintitle_full_fa)):
                    if text.lower() in self.maintitle_full_fa[i].lower():
                        self.tabView.list_fa.addItem(self.maintitle_full_fa[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full_fa[i] + "]")
            elif self.list_type_set == "fda":
                for i in range(len(self.maintitle_full_fa_fda)):
                    if text.lower() in self.maintitle_full_fa_fda[i].lower():
                        self.tabView.list_fa.addItem(self.maintitle_full_fa_fda[i] + "\n" + "[ FDA ] " + " [" + self.subtitle_full_fa_fda[i] + "]")

    def tabView_en_doubleClicked(self, text):
        for i in range(len(self.maintitle_full)):
            if text.text() == (self.maintitle_full[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full[i] + "]"):
                self.list_lang = "en"
                self.list_item = self.maintitle_full[i]
                self.list_type = "tums"
        self.win2 = main2.Window_main2(self.list_lang, self.list_item, self.list_type)
        self.win2.show()

    def tabView_fa_doubleClicked(self, text):
        for i in range(len(self.maintitle_full_fa)):
            if text.text() == (self.maintitle_full_fa[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full_fa[i] + "]"):
                self.list_lang = "fa"
                self.list_item = self.maintitle_full_fa[i]
                self.list_type = "tums"
        for i in range(len(self.maintitle_full_fa_fda)):
            if text.text() == (self.maintitle_full_fa_fda[i] + "\n" + "[ FDA ] " + " [" + self.subtitle_full_fa_fda[i] + "]"):
                self.list_lang = "fa"
                self.list_item = self.maintitle_full_fa_fda[i]
                self.list_type = "fda"
        self.win2 = main2.Window_main2(self.list_lang, self.list_item, self.list_type)
        self.win2.show()

    def tabView_tabChanged(self, i):
        self.searchBox.setText("")
        if self.tabView.currentIndex() == 0:
            self.tabView.list_en.clear()
            for i in range(len(self.maintitle_full)):
                self.tabView.list_en.addItem(self.maintitle_full[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full[i] + "]")
        elif self.tabView.currentIndex() == 1:
            self.tabView.list_fa.clear()
            if self.list_type_set == "tums-fda":
                for i in range(len(self.maintitle_full_fa)):
                    self.tabView.list_fa.addItem(self.maintitle_full_fa[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full_fa[i] + "]")
                for i in range(len(self.maintitle_full_fa_fda)):
                    self.tabView.list_fa.addItem(self.maintitle_full_fa_fda[i] + "\n" + "[ FDA ] " + " [" + self.subtitle_full_fa_fda[i] + "]")
            elif self.list_type_set == "tums":
                for i in range(len(self.maintitle_full_fa)):
                    self.tabView.list_fa.addItem(self.maintitle_full_fa[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full_fa[i] + "]")
            elif self.list_type_set == "fda":
                for i in range(len(self.maintitle_full_fa_fda)):
                    self.tabView.list_fa.addItem(self.maintitle_full_fa_fda[i] + "\n" + "[ FDA ] " + " [" + self.subtitle_full_fa_fda[i] + "]")

    def menuButton_clicked(self):
        if self.menuStatus == False:
            self.setFixedSize(600 * self.screen_ratio, 440 * self.screen_ratio)
            self.menuButton.setPixmap(QPixmap("src/menu_2.png"))
            self.menuStatus = True
        elif self.menuStatus == True:
            self.setFixedSize(300 * self.screen_ratio, 440 * self.screen_ratio)
            self.menuButton.setPixmap(QPixmap("src/menu_1.png"))
            self.menuStatus = False

    def menuButton1_clicked(self):
        self.win3 = main3.Window_main3()
        self.win3.show()

    def menuButton2_clicked(self):
        self.win5 = main5.Window_main5()
        self.win5.show()

    def menuButton3_clicked(self):
        self.win6 = main6.Window_main6()
        self.win6.show()

    def menuButton4_clicked(self):
        self.win8 = main8.Window_main8()
        self.win8.show()

    def menuButton5_clicked(self):
        self.lang_msg = QMessageBox(self)
        self.lang_msg.setText(self.str_lang_alert_title)
        self.lang_msg.setInformativeText(self.str_lang_alert_messege)
        self.lang_msg.setWindowTitle("MSDS - Language")

        self.lang_msg_btn_en = QPushButton(self.lang_msg)
        self.lang_msg_btn_en.setText("English")
        self.lang_msg_btn_en.setStyleSheet("background-color:#ffffff;")
        self.lang_msg_btn_en.clicked.connect(self.msgButton_en)

        self.lang_msg_btn_fa = QPushButton(self.lang_msg)
        self.lang_msg_btn_fa.setText("فارسی")
        self.lang_msg_btn_fa.setStyleSheet("background-color:#ffffff;")
        self.lang_msg_btn_fa.clicked.connect(self.msgButton_fa)

        self.lang_msg.addButton(self.lang_msg_btn_en, QMessageBox.YesRole)
        self.lang_msg.addButton(self.lang_msg_btn_fa, QMessageBox.NoRole)
        self.lang_msg.exec_()

    def msgButton_en(self):
        lang_write_en = codecs.open("data/lang.txt", encoding='utf-8', mode="w")
        lang_write_en.write("en")
        lang_write_en.close()
        self.msg_will_close()

    def msgButton_fa(self):
        lang_write_fa = codecs.open("data/lang.txt", encoding='utf-8', mode="w")
        lang_write_fa.write("fa")
        lang_write_fa.close()
        self.msg_will_close()

    def msg_will_close(self):
        #self.close_msg = QMessageBox(self)
        #self.close_msg.setText(self.str_lang_alert_change_alert)
        #self.close_msg.setInformativeText(self.str_lang_alert_change_alert_message)
        #self.close_msg.setWindowTitle("Alert!")

        #self.close_msg_btn_ok = QPushButton(self.close_msg)
        #self.close_msg_btn_ok.setText(self.str_lang_alert_change_alert_ok)
        #self.close_msg_btn_ok.setStyleSheet("background-color:#ffffff;")
        #self.close_msg_btn_ok.setFixedWidth(250 * self.screen_ratio)
        #self.close_msg_btn_ok.clicked.connect(self.close)
        self.hide()
        time.sleep(0.1)
        self.winSplash = msds.Window_splash()
        self.winSplash.show()

        #self.close_msg.addButton(self.close_msg_btn_ok, QMessageBox.YesRole)
        #self.close_msg.exec_()

    def menuButton6_clicked(self):
        self.win9 = main9.Window_main9()
        self.win9.show()
        self.hide()

    def menuButton7_clicked(self):
        webbrowser.open_new("https://msds.ir")

    def menuButton8_clicked(self):
        webbrowser.open_new("https://pharmacy.tums.ac.ir")

    def menuButton9_clicked(self):
        self.win_about = main_about.Window_main_about()
        self.win_about.show()

    def menuButton10_clicked(self):
        webbrowser.open_new("https://mail.google.com/mail/?view=cm&fs=1&to=orgchemlab.pharm@gmail.com&su=Contact to organic chem lab")

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white, 0.0001, Qt.SolidLine))

        grad1 = QLinearGradient(0, 1000, 0, 100)

        grad1.setColorAt(0.5, QColor("#ffffff"))
        grad1.setColorAt(1.0, QColor("#365fd4"))
        painter.setBrush(QBrush(grad1))

        painter.drawRect(0 * self.screen_ratio, 0 * self.screen_ratio, 75 * self.screen_ratio,
                         440 * self.screen_ratio)

        grad2 = QLinearGradient(0, 1000, 0, 100)

        grad2.setColorAt(0.5, QColor("#ffffff"))
        grad2.setColorAt(1.0, QColor("#ec1f1f"))
        painter.setBrush(QBrush(grad2))

        painter.drawRect(75 * self.screen_ratio, 0 * self.screen_ratio, 75 * self.screen_ratio,
                         440 * self.screen_ratio)

        grad3 = QLinearGradient(0, 1000, 0, 100)

        grad3.setColorAt(0.5, QColor("#ffffff"))
        grad3.setColorAt(1.0, QColor("#fffc00"))
        painter.setBrush(QBrush(grad3))

        painter.drawRect(150 * self.screen_ratio, 0 * self.screen_ratio, 75 * self.screen_ratio,
                         440 * self.screen_ratio)

        grad4 = QLinearGradient(0, 1000, 0, 100)

        grad4.setColorAt(0.5, QColor("#ffffff"))
        grad4.setColorAt(1.0, QColor("#ffffff"))
        painter.setBrush(QBrush(grad4))

        painter.drawRect(225 * self.screen_ratio, 0 * self.screen_ratio, 75 * self.screen_ratio,
                         440 * self.screen_ratio)

        grad1 = QLinearGradient(0, 1000, 0, 100)

        grad1.setColorAt(0.5, QColor("#ffffff"))
        grad1.setColorAt(1.0, QColor("#365fd4"))
        painter.setBrush(QBrush(grad1))

        painter.drawRect(300 * self.screen_ratio, 0 * self.screen_ratio, 75 * self.screen_ratio,
                         440 * self.screen_ratio)

        grad2 = QLinearGradient(0, 1000, 0, 100)

        grad2.setColorAt(0.5, QColor("#ffffff"))
        grad2.setColorAt(1.0, QColor("#ec1f1f"))
        painter.setBrush(QBrush(grad2))

        painter.drawRect(375 * self.screen_ratio, 0 * self.screen_ratio, 75 * self.screen_ratio,
                         440 * self.screen_ratio)

        grad3 = QLinearGradient(0, 1000, 0, 100)

        grad3.setColorAt(0.5, QColor("#ffffff"))
        grad3.setColorAt(1.0, QColor("#fffc00"))
        painter.setBrush(QBrush(grad3))

        painter.drawRect(450 * self.screen_ratio, 0 * self.screen_ratio, 75 * self.screen_ratio,
                         440 * self.screen_ratio)

        grad4 = QLinearGradient(0, 1000, 0, 100)

        grad4.setColorAt(0.5, QColor("#ffffff"))
        grad4.setColorAt(1.0, QColor("#ffffff"))
        painter.setBrush(QBrush(grad4))

        painter.drawRect(525 * self.screen_ratio, 0 * self.screen_ratio, 75 * self.screen_ratio,
                         440 * self.screen_ratio)


class ClickLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)
