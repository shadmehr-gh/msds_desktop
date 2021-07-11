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


class Window_main5(QMainWindow):
    screen_ratio = 1
    font_ratio = 1

    # strings_en:
    str_win_title_en = "Search By CAS#"
    str_cas_text_en = "CAS#"
    str_cas_search_en = "Search"
    str_cas_msg_title_en = "CAS Number NOT Found!"
    str_cas_msg_btn_en = "OK"
    # -----------
    # strings_fa:
    str_win_title_fa = "CAS جستجو بر اساس شماره"
    str_cas_text_fa = "CAS شماره"
    str_cas_search_fa = "جستجو"
    str_cas_msg_title_fa = "شماره CAS یافت نشد!"
    str_cas_msg_btn_fa = "باشه"
    # -----------
    # strings_final:
    str_win_title = ""
    str_cas_text = ""
    str_cas_search = ""
    str_cas_msg_title = ""
    str_cas_msg_btn = ""
    # -----------

    lang_main = ""

    maintitle_full = []
    maintitle_full_fa = []
    maintitle_full_fa_fda = []

    subtitle_full = []
    subtitle_full_fa = []
    subtitle_full_fa_fda = []

    def __init__(self):
        super(Window_main5, self).__init__()
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
            self.str_cas_text = self.str_cas_text_en
            self.str_cas_search = self.str_cas_search_en
            self.str_cas_msg_title = self.str_cas_msg_title_en
            self.str_cas_msg_btn = self.str_cas_msg_btn_en
        elif self.lang_main == "fa":
            self.str_win_title = self.str_win_title_fa
            self.str_cas_text = self.str_cas_text_fa
            self.str_cas_search = self.str_cas_search_fa
            self.str_cas_msg_title = self.str_cas_msg_title_fa
            self.str_cas_msg_btn = self.str_cas_msg_btn_fa

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

        # self.backgroundImage1 = QLabel(self)
        # self.backgroundImage1.setPixmap(QPixmap("src/msds_title_3.png"))
        # self.backgroundImage1.setScaledContents(True)
        # self.backgroundImage1.resize(340 * self.screen_ratio, 170 * self.screen_ratio)
        # self.backgroundImage1.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        self.cas_searchBox = QLineEdit(self)
        self.cas_searchBox.setPlaceholderText(self.str_cas_text)
        self.cas_searchBox.setFont(QFont("Ubuntu Regular", 10 * self.font_ratio))
        self.cas_searchBox.setStyleSheet("padding-left:15px;padding-right:15px")
        self.cas_searchBox.setFont(QFont("MS Shell Dlg 2", 10))
        self.cas_searchBox.resize(280 * self.screen_ratio, 30 * self.screen_ratio)
        self.cas_searchBox.move(30 * self.screen_ratio, 30 * self.screen_ratio)

        self.radioButton_en_cas = QRadioButton(self)
        self.radioButton_en_cas.setText("English")
        self.radioButton_en_cas.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        if self.lang_main == "en":
            self.radioButton_en_cas.setChecked(True)
        self.radioButton_en_cas.resize(70 * self.screen_ratio, 20 * self.screen_ratio)
        self.radioButton_en_cas.move(100 * self.screen_ratio, 70 * self.screen_ratio)

        self.radioButton_fa_cas = QRadioButton(self)
        self.radioButton_fa_cas.setText("فارسی")
        self.radioButton_fa_cas.setFont(QFont("B Nazanin", 10 * self.font_ratio))
        if self.lang_main == "fa":
            self.radioButton_fa_cas.setChecked(True)
        self.radioButton_fa_cas.resize(70 * self.screen_ratio, 20 * self.screen_ratio)
        self.radioButton_fa_cas.move(180 * self.screen_ratio, 70 * self.screen_ratio)

        self.cas_SearchButton = QPushButton(self)
        self.cas_SearchButton.setText(self.str_cas_search)
        self.cas_SearchButton.resize(50 * self.screen_ratio, 30 * self.screen_ratio)
        self.cas_SearchButton.move(145 * self.screen_ratio, 100 * self.screen_ratio)
        self.cas_SearchButton.clicked.connect(self.cas_SearchButton_clicked)

        self.setFixedSize(340 * self.screen_ratio, 150 * self.screen_ratio)
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        self.setWindowIcon(QIcon('MSDS_titlebar_icon.png'))
        self.setWindowTitle('MSDS - ' + self.str_win_title)

    def cas_SearchButton_clicked(self):
        cas_list = []
        cas_num_list = []
        name_list = []

        conn = sqlite3.connect("data/msds_1.0.2.db")

        cursor = conn.execute("SELECT * from msds_table_en")
        for row in cursor:
            cas_num_list.append(row[0])
            cas_list.append(row[1])
        cursor.close()
        cursor = conn.execute("SELECT * from msds_table_fda")
        for row in cursor:
            cas_num_list.append(row[0])
            cas_list.append(row[1])
        cursor.close()

        if self.cas_searchBox.text() != "":
            if self.cas_searchBox.text() in cas_list:
                if self.radioButton_en_cas.isChecked():
                    if cas_list.index(self.cas_searchBox.text()) <= (len(self.maintitle_full) - 1):
                        self.win2 = main2.Window_main2("en", self.maintitle_full[cas_list.index(self.cas_searchBox.text())], "tums")
                        self.win2.show()
                    elif cas_list.index(self.cas_searchBox.text()) > (len(self.maintitle_full) - 1):
                        self.cas_msg = QMessageBox(self)
                        self.cas_msg.setText(self.str_cas_msg_title)
                        self.cas_msg.setWindowTitle("MSDS - CAS#")

                        self.cas_msg_btn_ok = QPushButton(self.cas_msg)
                        self.cas_msg_btn_ok.setText(self.str_cas_msg_btn)
                        self.cas_msg_btn_ok.setStyleSheet("background-color:#ffffff;")
                        self.cas_msg_btn_ok.clicked.connect(self.cas_msgButton_ok)

                        self.cas_msg.addButton(self.cas_msg_btn_ok, QMessageBox.AcceptRole)
                        self.cas_msg.exec_()
                elif self.radioButton_fa_cas.isChecked():
                    if cas_list.index(self.cas_searchBox.text()) <= (len(self.maintitle_full_fa) - 1):
                        self.win2 = main2.Window_main2("fa", self.maintitle_full_fa[cas_list.index(self.cas_searchBox.text())], "tums")
                        self.win2.show()
                    elif cas_list.index(self.cas_searchBox.text()) > (len(self.maintitle_full_fa) - 1):
                        self.win2 = main2.Window_main2("fa", self.maintitle_full_fa_fda[(cas_list.index(self.cas_searchBox.text())) - len(self.maintitle_full_fa)], "fda")
                        self.win2.show()
            elif int(self.cas_searchBox.text()) in cas_num_list:
                if self.radioButton_en_cas.isChecked():
                    if cas_num_list.index(int(self.cas_searchBox.text())) <= (len(self.maintitle_full) - 1):
                        self.win2 = main2.Window_main2("en", self.maintitle_full[cas_num_list.index(int(self.cas_searchBox.text()))], "tums")
                        self.win2.show()
                    elif cas_num_list.index(int(self.cas_searchBox.text())) > (len(self.maintitle_full) - 1):
                        self.cas_msg = QMessageBox(self)
                        self.cas_msg.setText(self.str_cas_msg_title)
                        self.cas_msg.setWindowTitle("MSDS - CAS#")

                        self.cas_msg_btn_ok = QPushButton(self.cas_msg)
                        self.cas_msg_btn_ok.setText(self.str_cas_msg_btn)
                        self.cas_msg_btn_ok.setStyleSheet("background-color:#ffffff;")
                        self.cas_msg_btn_ok.clicked.connect(self.cas_msgButton_ok)

                        self.cas_msg.addButton(self.cas_msg_btn_ok, QMessageBox.AcceptRole)
                        self.cas_msg.exec_()
                elif self.radioButton_fa_cas.isChecked():
                    if cas_num_list.index(int(self.cas_searchBox.text())) <= (len(self.maintitle_full_fa) - 1):
                        self.win2 = main2.Window_main2("fa", self.maintitle_full_fa[cas_num_list.index(int(self.cas_searchBox.text()))], "tums")
                        self.win2.show()
                    elif cas_num_list.index(int(self.cas_searchBox.text())) > (len(self.maintitle_full_fa) - 1):
                        self.win2 = main2.Window_main2("fa", self.maintitle_full_fa_fda[(cas_num_list.index(int(self.cas_searchBox.text()))) - len(self.maintitle_full_fa)], "fda")
                        self.win2.show()
            else:
                self.cas_msg = QMessageBox(self)
                self.cas_msg.setText(self.str_cas_msg_title)
                self.cas_msg.setWindowTitle("MSDS - CAS#")

                self.cas_msg_btn_ok = QPushButton(self.cas_msg)
                self.cas_msg_btn_ok.setText(self.str_cas_msg_btn)
                self.cas_msg_btn_ok.setStyleSheet("background-color:#ffffff;")
                self.cas_msg_btn_ok.clicked.connect(self.cas_msgButton_ok)

                self.cas_msg.addButton(self.cas_msg_btn_ok, QMessageBox.AcceptRole)
                self.cas_msg.exec_()

        else:
            self.cas_msg = QMessageBox(self)
            self.cas_msg.setText(self.str_cas_msg_title)
            self.cas_msg.setWindowTitle("MSDS - CAS#")

            self.cas_msg_btn_ok = QPushButton(self.cas_msg)
            self.cas_msg_btn_ok.setText(self.str_cas_msg_btn)
            self.cas_msg_btn_ok.setStyleSheet("background-color:#ffffff;")
            self.cas_msg_btn_ok.clicked.connect(self.cas_msgButton_ok)

            self.cas_msg.addButton(self.cas_msg_btn_ok, QMessageBox.AcceptRole)
            self.cas_msg.exec_()

    def cas_msgButton_ok(self):
        self.cas_msg.close()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white, 0.0001, Qt.SolidLine))

        grad1 = QLinearGradient(0, 400, 0, 100)

        grad1.setColorAt(0.5, QColor("#ffffff"))
        grad1.setColorAt(1.0, QColor("#365fd4"))
        painter.setBrush(QBrush(grad1))

        painter.drawRect(0 * self.screen_ratio, 0 * self.screen_ratio, 340 * self.screen_ratio,
                         150 * self.screen_ratio)
