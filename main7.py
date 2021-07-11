from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QAction, QFormLayout, QHBoxLayout, QVBoxLayout, \
    QSlider, QRadioButton, QTabWidget, QLabel, QDesktopWidget, QLineEdit, QTextEdit, \
    QCheckBox, QRadioButton, QScrollArea, QGridLayout, QListWidget, QListWidgetItem, \
    QTableWidget, QPushButton, QMessageBox, QGroupBox, QMainWindow, QProgressBar, QApplication, QFrame, QComboBox
import sys
import sqlite3
import codecs

class Window_main7(QMainWindow):

    screen_ratio = 1
    font_ratio = 1

    # strings_en:
    str_win_title_en = "Material Safety Data Sheet(MSDS) signs"
    str_health_en = "Health hazard"
    str_fire_en = "Fire hazard"
    str_reactivity_en = "Reactivity"
    # -----------
    # strings_fa:
    str_win_title_fa = "(MSDS)علائم برگه های اطلاعات ایمنی"
    str_health_fa = "خطر سلامت"
    str_fire_fa = "خطر اشتعال"
    str_reactivity_fa = "واکنش پزیری"
    # -----------
    # strings_final:
    str_win_title = ""
    str_health = ""
    str_fire = ""
    str_reactivity = ""
    # -----------

    lang_main = ""

    msds_sign_letter_get = ""

    def __init__(self, msds_sign_letter):
        super(Window_main7, self).__init__()
        self.msds_sign_letter_get = msds_sign_letter
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
            self.str_health = self.str_health_en
            self.str_fire = self.str_fire_en
            self.str_reactivity = self.str_reactivity_en
        elif self.lang_main == "fa":
            self.str_win_title = self.str_win_title_fa
            self.str_health = self.str_health_fa
            self.str_fire = self.str_fire_fa
            self.str_reactivity = self.str_reactivity_fa

        conn = sqlite3.connect("data/msds_1.0.2.db")

        help_id_list = []
        #help_type_list = []
        #help_lang_list = []
        help_text_0_list = []
        help_text_1_list = []
        help_text_2_list = []
        help_text_3_list = []
        help_text_4_list = []

        cursor = conn.execute("SELECT * from msds_help_table")
        for row in cursor:
            help_id_list.append(row[0])
            #help_type_list.append(row[1])
            #help_lang_list.append(row[2])
            help_text_0_list.append(row[3])
            help_text_1_list.append(row[4])
            help_text_2_list.append(row[5])
            help_text_3_list.append(row[6])
            help_text_4_list.append(row[7])
        cursor.close()

        if self.lang_main == "en":
            msds_text_m_0_get = help_text_0_list[help_id_list.index(11)]
            msds_text_m_1_get = help_text_1_list[help_id_list.index(11)]
            msds_text_m_2_get = help_text_2_list[help_id_list.index(11)]
            msds_text_m_3_get = help_text_3_list[help_id_list.index(11)]
            msds_text_m_4_get = help_text_4_list[help_id_list.index(11)]
            msds_text_s1_0_get = help_text_0_list[help_id_list.index(21)]
            msds_text_s1_1_get = help_text_1_list[help_id_list.index(21)]
            msds_text_s1_2_get = help_text_2_list[help_id_list.index(21)]
            msds_text_s1_3_get = help_text_3_list[help_id_list.index(21)]
            msds_text_s1_4_get = help_text_4_list[help_id_list.index(21)]
            msds_text_d_0_get = help_text_0_list[help_id_list.index(31)]
            msds_text_d_1_get = help_text_1_list[help_id_list.index(31)]
            msds_text_d_2_get = help_text_2_list[help_id_list.index(31)]
            msds_text_d_3_get = help_text_3_list[help_id_list.index(31)]
            msds_text_d_4_get = help_text_4_list[help_id_list.index(31)]
        elif self.lang_main == "fa":
            msds_text_m_0_get = help_text_0_list[help_id_list.index(12)]
            msds_text_m_1_get = help_text_1_list[help_id_list.index(12)]
            msds_text_m_2_get = help_text_2_list[help_id_list.index(12)]
            msds_text_m_3_get = help_text_3_list[help_id_list.index(12)]
            msds_text_m_4_get = help_text_4_list[help_id_list.index(12)]
            msds_text_s1_0_get = help_text_0_list[help_id_list.index(22)]
            msds_text_s1_1_get = help_text_1_list[help_id_list.index(22)]
            msds_text_s1_2_get = help_text_2_list[help_id_list.index(22)]
            msds_text_s1_3_get = help_text_3_list[help_id_list.index(22)]
            msds_text_s1_4_get = help_text_4_list[help_id_list.index(22)]
            msds_text_d_0_get = help_text_0_list[help_id_list.index(32)]
            msds_text_d_1_get = help_text_1_list[help_id_list.index(32)]
            msds_text_d_2_get = help_text_2_list[help_id_list.index(32)]
            msds_text_d_3_get = help_text_3_list[help_id_list.index(32)]
            msds_text_d_4_get = help_text_4_list[help_id_list.index(32)]

        self.backgroundImage1 = QLabel(self)
        self.backgroundImage1.setStyleSheet("background-color:#ffffff;")
        self.backgroundImage1.setScaledContents(True)
        self.backgroundImage1.resize(400 * self.screen_ratio, 460 * self.screen_ratio)
        self.backgroundImage1.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        self.msds_title = QLabel(self)
        if self.msds_sign_letter_get == "m":
            self.msds_title.setText(self.str_health)
        elif self.msds_sign_letter_get == "s1":
            self.msds_title.setText(self.str_fire)
        elif self.msds_sign_letter_get == "d":
            self.msds_title.setText(self.str_reactivity)
        if self.lang_main == "en":
            self.msds_title.setFont(QFont("Times New Roman", 17 * self.font_ratio, weight=QFont.Bold))
        elif self.lang_main == "fa":
            self.msds_title.setFont(QFont("B Nazanin", 17 * self.font_ratio, weight=QFont.Bold))
        self.msds_title.setStyleSheet("background-color:#ffffff;")
        self.msds_title.setAlignment(Qt.AlignCenter)
        self.msds_title.setFixedHeight(60 * self.screen_ratio)
        self.msds_title.setFixedWidth(370 * self.screen_ratio)
        self.msds_title.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        self.msds_spacer_v_0 = QLabel(self)
        self.msds_spacer_v_0.setStyleSheet("background-color:#000000;")
        self.msds_spacer_v_0.setAlignment(Qt.AlignCenter)
        self.msds_spacer_v_0.setFixedHeight(4 * self.screen_ratio)
        self.msds_spacer_v_0.setFixedWidth(380 * self.screen_ratio)
        self.msds_spacer_v_0.move(0 * self.screen_ratio, 60 * self.screen_ratio)

        self.msds_num_0 = QLabel("0", self)
        if self.lang_main == "en":
            self.msds_num_0.setFont(QFont("Times New Roman", 13 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msds_num_0.setFont(QFont("B Nazanin", 13 * self.font_ratio))
        self.msds_num_0.setStyleSheet("background-color:#ffffff;")
        self.msds_num_0.setAlignment(Qt.AlignCenter)
        self.msds_num_0.setFixedHeight(60 * self.screen_ratio)
        self.msds_num_0.setFixedWidth(60 * self.screen_ratio)
        self.msds_num_0.move(0 * self.screen_ratio, 64 * self.screen_ratio)

        self.msds_spacer_h_0 = QLabel(self)
        self.msds_spacer_h_0.setStyleSheet("background-color:#000000;")
        self.msds_spacer_h_0.setAlignment(Qt.AlignCenter)
        self.msds_spacer_h_0.setFixedHeight(60 * self.screen_ratio)
        self.msds_spacer_h_0.setFixedWidth(4 * self.screen_ratio)
        self.msds_spacer_h_0.move(60 * self.screen_ratio, 64 * self.screen_ratio)

        self.msds_text_0 = QLabel(self)
        if self.msds_sign_letter_get == "m":
            self.msds_text_0.setText(msds_text_m_0_get)
        elif self.msds_sign_letter_get == "s1":
            self.msds_text_0.setText(msds_text_s1_0_get)
        elif self.msds_sign_letter_get == "d":
            self.msds_text_0.setText(msds_text_d_0_get)
        if self.lang_main == "en":
            self.msds_text_0.setFont(QFont("Times New Roman", 13 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msds_text_0.setFont(QFont("B Nazanin", 13 * self.font_ratio))
        self.msds_text_0.setStyleSheet("background-color:#ffffff;")
        self.msds_text_0.setAlignment(Qt.AlignLeft)
        self.msds_text_0.setWordWrap(True)
        self.msds_text_0.setMargin(10)
        #self.msds_text_0.setFixedHeight(60 * self.screen_ratio)
        self.msds_text_0.setFixedWidth(306 * self.screen_ratio)
        self.msds_text_0.move(64 * self.screen_ratio, 64 * self.screen_ratio)

        self.msds_spacer_v_1 = QLabel(self)
        self.msds_spacer_v_1.setStyleSheet("background-color:#000000;")
        self.msds_spacer_v_1.setFixedHeight(4 * self.screen_ratio)
        self.msds_spacer_v_1.setFixedWidth(380 * self.screen_ratio)
        self.msds_spacer_v_1.move(0 * self.screen_ratio, 124 * self.screen_ratio)

        self.msds_num_1 = QLabel("1", self)
        if self.lang_main == "en":
            self.msds_num_1.setFont(QFont("Times New Roman", 13 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msds_num_1.setFont(QFont("B Nazanin", 13 * self.font_ratio))
        self.msds_num_1.setStyleSheet("background-color:#ffffff;")
        self.msds_num_1.setAlignment(Qt.AlignCenter)
        #self.msds_num_1.setFixedHeight(60 * self.screen_ratio)
        self.msds_num_1.setFixedWidth(60 * self.screen_ratio)
        self.msds_num_1.move(0 * self.screen_ratio, 128 * self.screen_ratio)

        self.msds_spacer_h_1 = QLabel(self)
        self.msds_spacer_h_1.setStyleSheet("background-color:#000000;")
        self.msds_spacer_h_1.setFixedHeight(60 * self.screen_ratio)
        self.msds_spacer_h_1.setFixedWidth(4 * self.screen_ratio)
        self.msds_spacer_h_1.move(60 * self.screen_ratio, 128 * self.screen_ratio)

        self.msds_text_1 = QLabel(self)
        if self.msds_sign_letter_get == "m":
            self.msds_text_1.setText(msds_text_m_1_get)
        elif self.msds_sign_letter_get == "s1":
            self.msds_text_1.setText(msds_text_s1_1_get)
        elif self.msds_sign_letter_get == "d":
            self.msds_text_1.setText(msds_text_d_1_get)
        if self.lang_main == "en":
            self.msds_text_1.setFont(QFont("Times New Roman", 13 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msds_text_1.setFont(QFont("B Nazanin", 13 * self.font_ratio))
        self.msds_text_1.setStyleSheet("background-color:#ffffff;")
        self.msds_text_1.setAlignment(Qt.AlignLeft)
        self.msds_text_1.setWordWrap(True)
        self.msds_text_1.setMargin(10)
        #self.msds_text_1.setFixedHeight(60 * self.screen_ratio)
        self.msds_text_1.setFixedWidth(306 * self.screen_ratio)
        self.msds_text_1.move(64 * self.screen_ratio, 128 * self.screen_ratio)

        self.msds_spacer_v_2 = QLabel(self)
        self.msds_spacer_v_2.setStyleSheet("background-color:#000000;")
        self.msds_spacer_v_2.setFixedHeight(4 * self.screen_ratio)
        self.msds_spacer_v_2.setFixedWidth(380 * self.screen_ratio)
        self.msds_spacer_v_2.move(0 * self.screen_ratio, 188 * self.screen_ratio)

        self.msds_num_2 = QLabel("2", self)
        if self.lang_main == "en":
            self.msds_num_2.setFont(QFont("Times New Roman", 13 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msds_num_2.setFont(QFont("B Nazanin", 13 * self.font_ratio))
        self.msds_num_2.setStyleSheet("background-color:#ffffff;")
        self.msds_num_2.setAlignment(Qt.AlignCenter)
        self.msds_num_2.setFixedHeight(60 * self.screen_ratio)
        self.msds_num_2.setFixedWidth(60 * self.screen_ratio)
        self.msds_num_2.move(0 * self.screen_ratio, 192 * self.screen_ratio)

        self.msds_spacer_h_2 = QLabel(self)
        self.msds_spacer_h_2.setStyleSheet("background-color:#000000;")
        self.msds_spacer_h_2.setFixedHeight(60 * self.screen_ratio)
        self.msds_spacer_h_2.setFixedWidth(4 * self.screen_ratio)
        self.msds_spacer_h_2.move(60 * self.screen_ratio, 192 * self.screen_ratio)

        self.msds_text_2 = QLabel(self)
        if self.msds_sign_letter_get == "m":
            self.msds_text_2.setText(msds_text_m_2_get)
        elif self.msds_sign_letter_get == "s1":
            self.msds_text_2.setText(msds_text_s1_2_get)
        elif self.msds_sign_letter_get == "d":
            self.msds_text_2.setText(msds_text_d_2_get)
        if self.lang_main == "en":
            self.msds_text_2.setFont(QFont("Times New Roman", 13 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msds_text_2.setFont(QFont("B Nazanin", 13 * self.font_ratio))
        self.msds_text_2.setStyleSheet("background-color:#ffffff;")
        self.msds_text_2.setAlignment(Qt.AlignLeft)
        self.msds_text_2.setWordWrap(True)
        self.msds_text_2.setMargin(10)
        #self.msds_text_2.setFixedHeight(60 * self.screen_ratio)
        self.msds_text_2.setFixedWidth(306 * self.screen_ratio)
        self.msds_text_2.move(64 * self.screen_ratio, 192 * self.screen_ratio)

        self.msds_spacer_v_3 = QLabel(self)
        self.msds_spacer_v_3.setStyleSheet("background-color:#000000;")
        self.msds_spacer_v_3.setFixedHeight(4 * self.screen_ratio)
        self.msds_spacer_v_3.setFixedWidth(380 * self.screen_ratio)
        self.msds_spacer_v_3.move(0 * self.screen_ratio, 252 * self.screen_ratio)

        self.msds_num_3 = QLabel("3", self)
        if self.lang_main == "en":
            self.msds_num_3.setFont(QFont("Times New Roman", 13 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msds_num_3.setFont(QFont("B Nazanin", 13 * self.font_ratio))
        self.msds_num_3.setStyleSheet("background-color:#ffffff;")
        self.msds_num_3.setAlignment(Qt.AlignCenter)
        self.msds_num_3.setFixedHeight(60 * self.screen_ratio)
        self.msds_num_3.setFixedWidth(60 * self.screen_ratio)
        self.msds_num_3.move(0 * self.screen_ratio, 256 * self.screen_ratio)

        self.msds_spacer_h_3 = QLabel(self)
        self.msds_spacer_h_3.setStyleSheet("background-color:#000000;")
        self.msds_spacer_h_3.setFixedHeight(60 * self.screen_ratio)
        self.msds_spacer_h_3.setFixedWidth(4 * self.screen_ratio)
        self.msds_spacer_h_3.move(60 * self.screen_ratio, 256 * self.screen_ratio)

        self.msds_text_3 = QLabel(self)
        if self.msds_sign_letter_get == "m":
            self.msds_text_3.setText(msds_text_m_3_get)
        elif self.msds_sign_letter_get == "s1":
            self.msds_text_3.setText(msds_text_s1_3_get)
        elif self.msds_sign_letter_get == "d":
            self.msds_text_3.setText(msds_text_d_3_get)
        if self.lang_main == "en":
            self.msds_text_3.setFont(QFont("Times New Roman", 13 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msds_text_3.setFont(QFont("B Nazanin", 13 * self.font_ratio))
        self.msds_text_3.setStyleSheet("background-color:#ffffff;")
        self.msds_text_3.setAlignment(Qt.AlignLeft)
        self.msds_text_3.setWordWrap(True)
        self.msds_text_3.setMargin(10)
        #self.msds_text_3.setFixedHeight(60 * self.screen_ratio)
        self.msds_text_3.setFixedWidth(306 * self.screen_ratio)
        self.msds_text_3.move(64 * self.screen_ratio, 256 * self.screen_ratio)

        self.msds_spacer_v_4 = QLabel(self)
        self.msds_spacer_v_4.setStyleSheet("background-color:#000000;")
        self.msds_spacer_v_4.setFixedHeight(4 * self.screen_ratio)
        self.msds_spacer_v_4.setFixedWidth(380 * self.screen_ratio)
        self.msds_spacer_v_4.move(0 * self.screen_ratio, 316 * self.screen_ratio)

        self.msds_num_4 = QLabel("4", self)
        if self.lang_main == "en":
            self.msds_num_4.setFont(QFont("Times New Roman", 13 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msds_num_4.setFont(QFont("B Nazanin", 13 * self.font_ratio))
        self.msds_num_4.setStyleSheet("background-color:#ffffff;")
        self.msds_num_4.setAlignment(Qt.AlignCenter)
        self.msds_num_4.setFixedHeight(60 * self.screen_ratio)
        self.msds_num_4.setFixedWidth(60 * self.screen_ratio)
        self.msds_num_4.move(0 * self.screen_ratio, 320 * self.screen_ratio)

        self.msds_spacer_h_4 = QLabel(self)
        self.msds_spacer_h_4.setStyleSheet("background-color:#000000;")
        self.msds_spacer_h_4.setFixedHeight(60 * self.screen_ratio)
        self.msds_spacer_h_4.setFixedWidth(4 * self.screen_ratio)
        self.msds_spacer_h_4.move(60 * self.screen_ratio, 320 * self.screen_ratio)

        self.msds_text_4 = QLabel(self)
        if self.msds_sign_letter_get == "m":
            self.msds_text_4.setText(msds_text_m_4_get)
        elif self.msds_sign_letter_get == "s1":
            self.msds_text_4.setText(msds_text_s1_4_get)
        elif self.msds_sign_letter_get == "d":
            self.msds_text_4.setText(msds_text_d_4_get)
        if self.lang_main == "en":
            self.msds_text_4.setFont(QFont("Times New Roman", 13 * self.font_ratio))
        elif self.lang_main == "fa":
            self.msds_text_4.setFont(QFont("B Nazanin", 13 * self.font_ratio))
        self.msds_text_4.setStyleSheet("background-color:#ffffff;")
        self.msds_text_4.setAlignment(Qt.AlignLeft)
        self.msds_text_4.setWordWrap(True)
        self.msds_text_4.setMargin(10)
        #self.msds_text_4.setFixedHeight(60 * self.screen_ratio)
        self.msds_text_4.setFixedWidth(306 * self.screen_ratio)
        self.msds_text_4.move(64 * self.screen_ratio, 320 * self.screen_ratio)

        #self.msds_spacer_v_5 = QLabel(self)
        #self.msds_spacer_v_5.setStyleSheet("background-color:#ffffff;")
        #self.msds_spacer_v_5.setFixedHeight(4 * self.screen_ratio)
        #self.msds_spacer_v_5.setFixedWidth(370 * self.screen_ratio)
        #self.msds_spacer_v_5.move(0 * self.screen_ratio, 380 * self.screen_ratio)

        self.scrollArea = QScrollArea(self)

        self.vlayout = QVBoxLayout(self.scrollArea)

        self.hmisHLayout_title = QHBoxLayout()
        self.hmisHLayout_title.addWidget(self.msds_title)
        self.hmisHLayout_title.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_title)

        self.hmisHLayout_spacer_0 = QHBoxLayout()
        self.hmisHLayout_spacer_0.addWidget(self.msds_spacer_v_0)
        self.hmisHLayout_spacer_0.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_spacer_0)

        self.hmisHLayout_num_0 = QHBoxLayout()
        self.hmisHLayout_num_0.addWidget(self.msds_num_0)
        self.hmisHLayout_num_0.addWidget(self.msds_spacer_h_0)
        self.hmisHLayout_num_0.addWidget(self.msds_text_0)
        self.hmisHLayout_num_0.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_num_0)

        self.hmisHLayout_spacer_1 = QHBoxLayout()
        self.hmisHLayout_spacer_1.addWidget(self.msds_spacer_v_1)
        self.hmisHLayout_spacer_1.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_spacer_1)

        self.hmisHLayout_num_1 = QHBoxLayout()
        self.hmisHLayout_num_1.addWidget(self.msds_num_1)
        self.hmisHLayout_num_1.addWidget(self.msds_spacer_h_1)
        self.hmisHLayout_num_1.addWidget(self.msds_text_1)
        self.hmisHLayout_num_1.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_num_1)

        self.hmisHLayout_spacer_2 = QHBoxLayout()
        self.hmisHLayout_spacer_2.addWidget(self.msds_spacer_v_2)
        self.hmisHLayout_spacer_2.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_spacer_2)

        self.hmisHLayout_num_2 = QHBoxLayout()
        self.hmisHLayout_num_2.addWidget(self.msds_num_2)
        self.hmisHLayout_num_2.addWidget(self.msds_spacer_h_2)
        self.hmisHLayout_num_2.addWidget(self.msds_text_2)
        self.hmisHLayout_num_2.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_num_2)

        self.hmisHLayout_spacer_3 = QHBoxLayout()
        self.hmisHLayout_spacer_3.addWidget(self.msds_spacer_v_3)
        self.hmisHLayout_spacer_3.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_spacer_3)

        self.hmisHLayout_num_3 = QHBoxLayout()
        self.hmisHLayout_num_3.addWidget(self.msds_num_3)
        self.hmisHLayout_num_3.addWidget(self.msds_spacer_h_3)
        self.hmisHLayout_num_3.addWidget(self.msds_text_3)
        self.hmisHLayout_num_3.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_num_3)

        self.hmisHLayout_spacer_4 = QHBoxLayout()
        self.hmisHLayout_spacer_4.addWidget(self.msds_spacer_v_4)
        self.hmisHLayout_spacer_4.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_spacer_4)

        self.hmisHLayout_num_4 = QHBoxLayout()
        self.hmisHLayout_num_4.addWidget(self.msds_num_4)
        self.hmisHLayout_num_4.addWidget(self.msds_spacer_h_4)
        self.hmisHLayout_num_4.addWidget(self.msds_text_4)
        self.hmisHLayout_num_4.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_num_4)

        #self.hmisHLayout_spacer_5 = QHBoxLayout(self.scrollArea)
        #self.hmisHLayout_spacer_5.addWidget(self.msds_spacer_v_5)
        #self.hmisHLayout_spacer_5.setAlignment(Qt.AlignLeft)
        #self.vlayout.addLayout(self.hmisHLayout_spacer_5)

        self.vlayout.setSpacing(0)
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setAlignment(Qt.AlignTop)

        self.vlayoutGPBox = QGroupBox("")
        self.vlayoutGPBox.setLayout(self.vlayout)

        self.scrollArea.setWidget(self.vlayoutGPBox)
        self.scrollArea.setStyleSheet("background-color:#ffffff;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.resize(400 * self.screen_ratio, 460 * self.screen_ratio)
        self.scrollArea.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        if self.lang_main == "en":
            self.msds_num_0.setFixedHeight(self.msds_text_0.height())
            self.msds_spacer_h_0.setFixedHeight(self.msds_text_0.height())
            self.msds_num_1.setFixedHeight(self.msds_text_1.height())
            self.msds_spacer_h_1.setFixedHeight(self.msds_text_1.height())
            self.msds_num_2.setFixedHeight(self.msds_text_2.height())
            self.msds_spacer_h_2.setFixedHeight(self.msds_text_2.height())
            self.msds_num_3.setFixedHeight(self.msds_text_3.height())
            self.msds_spacer_h_3.setFixedHeight(self.msds_text_3.height())
            self.msds_num_4.setFixedHeight(self.msds_text_4.height())
            self.msds_spacer_h_4.setFixedHeight(self.msds_text_4.height() + 30)
        elif self.lang_main == "fa":
            self.msds_num_0.setFixedHeight(self.msds_text_0.height())
            self.msds_spacer_h_0.setFixedHeight(self.msds_text_0.height() + 20)
            self.msds_num_1.setFixedHeight(self.msds_text_1.height())
            self.msds_spacer_h_1.setFixedHeight(self.msds_text_1.height() + 20)
            self.msds_num_2.setFixedHeight(self.msds_text_2.height())
            self.msds_spacer_h_2.setFixedHeight(self.msds_text_2.height() + 20)
            self.msds_num_3.setFixedHeight(self.msds_text_3.height())
            self.msds_spacer_h_3.setFixedHeight(self.msds_text_3.height() + 20)
            self.msds_num_4.setFixedHeight(self.msds_text_4.height())
            self.msds_spacer_h_4.setFixedHeight(self.msds_text_4.height() + 50)

        if self.msds_sign_letter_get == "m":
            self.msds_title.setStyleSheet("color:#3e6aef;")
            self.msds_num_0.setStyleSheet("color:#3e6aef;")
            self.msds_text_0.setStyleSheet("color:#3e6aef;")
            self.msds_num_1.setStyleSheet("color:#3e6aef;")
            self.msds_text_1.setStyleSheet("color:#3e6aef;")
            self.msds_num_2.setStyleSheet("color:#3e6aef;")
            self.msds_text_2.setStyleSheet("color:#3e6aef;")
            self.msds_num_3.setStyleSheet("color:#3e6aef;")
            self.msds_text_3.setStyleSheet("color:#3e6aef;")
            self.msds_num_4.setStyleSheet("color:#3e6aef;")
            self.msds_text_4.setStyleSheet("color:#3e6aef;")
        elif self.msds_sign_letter_get == "s1":
            self.msds_title.setStyleSheet("color:#f01513;")
            self.msds_num_0.setStyleSheet("color:#f01513;")
            self.msds_text_0.setStyleSheet("color:#f01513;")
            self.msds_num_1.setStyleSheet("color:#f01513;")
            self.msds_text_1.setStyleSheet("color:#f01513;")
            self.msds_num_2.setStyleSheet("color:#f01513;")
            self.msds_text_2.setStyleSheet("color:#f01513;")
            self.msds_num_3.setStyleSheet("color:#f01513;")
            self.msds_text_3.setStyleSheet("color:#f01513;")
            self.msds_num_4.setStyleSheet("color:#f01513;")
            self.msds_text_4.setStyleSheet("color:#f01513;")
        elif self.msds_sign_letter_get == "d":
            self.msds_title.setStyleSheet("color:#ffae42;")
            self.msds_num_0.setStyleSheet("color:#ffae42;")
            self.msds_text_0.setStyleSheet("color:#ffae42;")
            self.msds_num_1.setStyleSheet("color:#ffae42;")
            self.msds_text_1.setStyleSheet("color:#ffae42;")
            self.msds_num_2.setStyleSheet("color:#ffae42;")
            self.msds_text_2.setStyleSheet("color:#ffae42;")
            self.msds_num_3.setStyleSheet("color:#ffae42;")
            self.msds_text_3.setStyleSheet("color:#ffae42;")
            self.msds_num_4.setStyleSheet("color:#ffae42;")
            self.msds_text_4.setStyleSheet("color:#ffae42;")

        self.setFixedSize(400 * self.screen_ratio, 460 * self.screen_ratio)
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        self.setWindowIcon(QIcon('MSDS_titlebar_icon.png'))
        self.setWindowTitle('MSDS - ' + self.str_win_title)
