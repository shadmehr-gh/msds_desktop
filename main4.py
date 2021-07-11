from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QAction, QFormLayout, QHBoxLayout, QVBoxLayout, \
    QSlider, QRadioButton, QTabWidget, QLabel, QDesktopWidget, QLineEdit, QTextEdit, \
    QCheckBox, QRadioButton, QScrollArea, QGridLayout, QListWidget, QListWidgetItem, \
    QTableWidget, QPushButton, QMessageBox, QGroupBox, QMainWindow, QProgressBar, QApplication, QFrame, QComboBox
import sys
import sqlite3
import codecs
import main2


class Window_main4(QMainWindow):

    screen_ratio = 1
    font_ratio = 1

    # strings_en:
    str_win_title_en = "Advanced search Results"
    str_search_result_title_en = "Search Results:"
    # -----------
    # strings_fa:
    str_win_title_fa = "نتایج جستجو پیشرفته"
    str_search_result_title_fa = "نتایج جستجو:"
    # -----------
    # strings_final:
    str_win_title = ""
    str_search_result_title = ""
    # -----------

    lang_main = ""

    maintitle_full = []
    maintitle_full_fa = []
    maintitle_full_fa_fda = []

    subtitle_full = []
    subtitle_full_fa = []
    subtitle_full_fa_fda = []

    m_1_int_get = 0
    m_2_int_get = 4
    s1_1_int_get = 0
    s1_2_int_get = 4
    d_1_int_get = 0
    d_2_int_get = 4
    selected_lang_string_get = "en"

    def __init__(self, m_1_int, m_2_int, s1_1_int, s1_2_int, d_1_int, d_2_int, selected_lang_string):
        super(Window_main4, self).__init__()
        self.m_1_int_get = m_1_int
        self.m_2_int_get = m_2_int
        self.s1_1_int_get = s1_1_int
        self.s1_2_int_get = s1_2_int
        self.d_1_int_get = d_1_int
        self.d_2_int_get = d_2_int
        self.selected_lang_string_get = selected_lang_string
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
            self.str_search_result_title = self.str_search_result_title_en
        elif self.lang_main == "fa":
            self.str_win_title = self.str_win_title_fa
            self.str_search_result_title = self.str_search_result_title_fa

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

        #self.backgroundImage1 = QLabel(self)
        #self.backgroundImage1.setPixmap(QPixmap("src/msds_title_3.png"))
        #self.backgroundImage1.setScaledContents(True)
        #self.backgroundImage1.resize(280 * self.screen_ratio, 390 * self.screen_ratio)
        #self.backgroundImage1.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        self.advancedSearchTitleLabel = QLabel(self.str_search_result_title, self)
        if self.lang_main == "en":
            self.advancedSearchTitleLabel.setFont(QFont("Times New Roman", 17 * self.font_ratio, weight=QFont.Bold))
        elif self.lang_main == "fa":
            self.advancedSearchTitleLabel.setFont(QFont("B Nazanin", 17 * self.font_ratio, weight=QFont.Bold))
        self.advancedSearchTitleLabel.setAlignment(Qt.AlignCenter)
        self.advancedSearchTitleLabel.resize(260 * self.screen_ratio, 20 * self.screen_ratio)
        self.advancedSearchTitleLabel.move(10 * self.screen_ratio, 10 * self.screen_ratio)

        name_list = []
        msds_m_list = []
        msds_s1_list = []
        msds_d_list = []

        self.search_list = QListWidget(self)
        self.search_list.setFrameShape(QFrame.NoFrame)
        #self.search_list.setStyleSheet("background-color:#ffffff;")
        if self.selected_lang_string_get == "en":
            for i in range(len(self.maintitle_full)):
                cursor = conn.execute("SELECT * from msds_table_en")
                for row in cursor:
                    name_list.append(row[2])
                    msds_m_list.append(row[5])
                    msds_s1_list.append(row[6])
                    msds_d_list.append(row[7])
                cursor.close()
                msds_m_text = msds_m_list[name_list.index(self.maintitle_full[i])]
                msds_s1_text = msds_s1_list[name_list.index(self.maintitle_full[i])]
                msds_d_text = msds_d_list[name_list.index(self.maintitle_full[i])]

                if self.m_1_int_get <= int(msds_m_text) <= self.m_2_int_get and self.s1_1_int_get <= int(msds_s1_text) <= self.s1_2_int_get and self.d_1_int_get <= int(msds_d_text) <= self.d_2_int_get:
                    self.search_list.addItem(self.maintitle_full[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full[i] + "]")

        elif self.selected_lang_string_get == "fa":
            for i in range(len(self.maintitle_full_fa)):
                cursor = conn.execute("SELECT * from msds_table_fa")
                for row in cursor:
                    name_list.append(row[2])
                    msds_m_list.append(row[5])
                    msds_s1_list.append(row[6])
                    msds_d_list.append(row[7])
                cursor.close()
                msds_m_text = msds_m_list[name_list.index(self.maintitle_full_fa[i])]
                msds_s1_text = msds_s1_list[name_list.index(self.maintitle_full_fa[i])]
                msds_d_text = msds_d_list[name_list.index(self.maintitle_full_fa[i])]

                if self.m_1_int_get <= int(msds_m_text) <= self.m_2_int_get and self.s1_1_int_get <= int(msds_s1_text) <= self.s1_2_int_get and self.d_1_int_get <= int(msds_d_text) <= self.d_2_int_get:
                    self.search_list.addItem(self.maintitle_full_fa[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full_fa[i] + "]")
            for i in range(len(self.maintitle_full_fa_fda)):
                cursor = conn.execute("SELECT * from msds_table_fda")
                for row in cursor:
                    name_list.append(row[3])
                    msds_m_list.append(row[6])
                    msds_s1_list.append(row[7])
                    msds_d_list.append(row[8])
                cursor.close()
                msds_m_text = msds_m_list[name_list.index(self.maintitle_full_fa_fda[i])]
                msds_s1_text = msds_s1_list[name_list.index(self.maintitle_full_fa_fda[i])]
                msds_d_text = msds_d_list[name_list.index(self.maintitle_full_fa_fda[i])]

                if self.m_1_int_get <= int(msds_m_text) <= self.m_2_int_get and self.s1_1_int_get <= int(msds_s1_text) <= self.s1_2_int_get and self.d_1_int_get <= int(msds_d_text) <= self.d_2_int_get:
                    self.search_list.addItem(self.maintitle_full_fa_fda[i] + "\n" + "[ FDA ] " + " [" + self.subtitle_full_fa_fda[i] + "]")

        if self.selected_lang_string_get == "en":
            self.search_list.setFont(QFont("Times New Roman", 11 * self.font_ratio))
        elif self.selected_lang_string_get == "fa":
            self.search_list.setFont(QFont("B Nazanin", 11 * self.font_ratio))
        self.search_list.resize(260 * self.screen_ratio, 340 * self.screen_ratio)
        self.search_list.move(10 * self.screen_ratio, 40 * self.screen_ratio)
        self.search_list.itemActivated.connect(self.search_list_doubleClicked)

        self.setFixedSize(280 * self.screen_ratio, 390 * self.screen_ratio)
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        self.setWindowIcon(QIcon('MSDS_titlebar_icon.png'))
        self.setWindowTitle('MSDS - ' + self.str_win_title)

    def search_list_doubleClicked(self, text):
        if self.selected_lang_string_get == "en":
            for i in range(len(self.maintitle_full)):
                if text.text() == (self.maintitle_full[i] + "\n" + "[ TUMS ] " + " [" + self.subtitle_full[i] + "]"):
                    self.list_lang = "en"
                    self.list_item = self.maintitle_full[i]
                    self.list_type = "tums"
        elif self.selected_lang_string_get == "fa":
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

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white, 0.0001, Qt.SolidLine))

        grad1 = QLinearGradient(0, 1000, 0, 100)

        grad1.setColorAt(0.5, QColor("#ffffff"))
        grad1.setColorAt(1.0, QColor("#365fd4"))
        painter.setBrush(QBrush(grad1))

        painter.drawRect(0 * self.screen_ratio, 0 * self.screen_ratio, 70 * self.screen_ratio,
                         390 * self.screen_ratio)

        grad2 = QLinearGradient(0, 1000, 0, 100)

        grad2.setColorAt(0.5, QColor("#ffffff"))
        grad2.setColorAt(1.0, QColor("#ec1f1f"))
        painter.setBrush(QBrush(grad2))

        painter.drawRect(70 * self.screen_ratio, 0 * self.screen_ratio, 70 * self.screen_ratio,
                         390 * self.screen_ratio)

        grad3 = QLinearGradient(0, 1000, 0, 100)

        grad3.setColorAt(0.5, QColor("#ffffff"))
        grad3.setColorAt(1.0, QColor("#fffc00"))
        painter.setBrush(QBrush(grad3))

        painter.drawRect(140 * self.screen_ratio, 0 * self.screen_ratio, 70 * self.screen_ratio,
                         390 * self.screen_ratio)

        grad4 = QLinearGradient(0, 1000, 0, 100)

        grad4.setColorAt(0.5, QColor("#ffffff"))
        grad4.setColorAt(1.0, QColor("#ffffff"))
        painter.setBrush(QBrush(grad4))

        painter.drawRect(210 * self.screen_ratio, 0 * self.screen_ratio, 70 * self.screen_ratio,
                         390 * self.screen_ratio)
