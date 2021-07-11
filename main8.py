from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QAction, QFormLayout, QHBoxLayout, QVBoxLayout, \
    QSlider, QRadioButton, QTabWidget, QLabel, QDesktopWidget, QLineEdit, QTextEdit, \
    QCheckBox, QRadioButton, QScrollArea, QGridLayout, QListWidget, QListWidgetItem, \
    QTableWidget, QPushButton, QMessageBox, QGroupBox, QMainWindow, QProgressBar, QApplication, QFrame, QComboBox
import sys
import codecs


class Window_main8(QMainWindow):

    screen_ratio = 1
    font_ratio = 1

    # strings_en:
    str_win_title_en = "Hazardous Material Index Ratings(HMIS) guide"
    str_hmis_title_en = "Required Equipment"
    str_hmis_title2_en = "HMIS\nLetter"
    str_hmis_l_en = "Site-specific label. Ask your supervisor or safety specialist for handling instructions"
    # -----------
    # strings_fa:
    str_win_title_fa = "(HMIS)راهنمای رتبه بندی فهرست مواد خطرناک"
    str_hmis_title_fa = "تجهیزات مورد نیاز"
    str_hmis_title2_fa = "حرف\nHMIS"
    str_hmis_l_fa = "برچسب مخصوص. از سرپرست یا متخصص ایمنی خود برای اداره دستورالعمل ها بخواهید."
    # -----------
    # strings_final:
    str_win_title = ""
    str_hmis_title = ""
    str_hmis_title2 = ""
    str_hmis_l = ""
    # -----------

    lang_main = ""

    def __init__(self):
        super(Window_main8, self).__init__()
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
            self.str_hmis_title = self.str_hmis_title_en
            self.str_hmis_title2 = self.str_hmis_title2_en
            self.str_hmis_l = self.str_hmis_l_en
        elif self.lang_main == "fa":
            self.str_win_title = self.str_win_title_fa
            self.str_hmis_title = self.str_hmis_title_fa
            self.str_hmis_title2 = self.str_hmis_title2_fa
            self.str_hmis_l = self.str_hmis_l_fa

        self.hmisLetterTitle_0 = QLabel(self.str_hmis_title2, self)
        if self.lang_main == "en":
            self.hmisLetterTitle_0.setFont(QFont("Times New Roman", 13 * self.font_ratio, weight=QFont.Bold))
        elif self.lang_main == "fa":
            self.hmisLetterTitle_0.setFont(QFont("B Nazanin", 13 * self.font_ratio, weight=QFont.Bold))
        self.hmisLetterTitle_0.setStyleSheet("background-color:#ffffff;")
        self.hmisLetterTitle_0.setAlignment(Qt.AlignCenter)
        self.hmisLetterTitle_0.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetterTitle_0.setFixedWidth(60 * self.screen_ratio)
        self.hmisLetterTitle_0.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        self.hmisLetterTitle_1 = QLabel(self.str_hmis_title, self)
        if self.lang_main == "en":
            self.hmisLetterTitle_1.setFont(QFont("Times New Roman", 15 * self.font_ratio, weight=QFont.Bold))
        elif self.lang_main == "fa":
            self.hmisLetterTitle_1.setFont(QFont("B Nazanin", 15 * self.font_ratio, weight=QFont.Bold))
        self.hmisLetterTitle_1.setStyleSheet("background-color:#ffffff;")
        self.hmisLetterTitle_1.setAlignment(Qt.AlignCenter)
        self.hmisLetterTitle_1.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetterTitle_1.setFixedWidth(300 * self.screen_ratio)
        self.hmisLetterTitle_1.move(60 * self.screen_ratio, 0 * self.screen_ratio)

        self.hmisLetter_a = QLabel("A", self)
        if self.lang_main == "en":
            self.hmisLetter_a.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.hmisLetter_a.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.hmisLetter_a.setStyleSheet("background-color:#ffffff;")
        self.hmisLetter_a.setAlignment(Qt.AlignCenter)
        self.hmisLetter_a.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetter_a.setFixedWidth(60 * self.screen_ratio)
        self.hmisLetter_a.move(0 * self.screen_ratio, 60 * self.screen_ratio)

        self.hmisImage_a_0 = QLabel(self)
        self.hmisImage_a_0.setPixmap(QPixmap("src/hmis_safety_glass.png"))
        self.hmisImage_a_0.setScaledContents(True)
        self.hmisImage_a_0.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_a_0.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_a_0.move(60 * self.screen_ratio, 60 * self.screen_ratio)

        self.hmisLetter_b = QLabel("B", self)
        if self.lang_main == "en":
            self.hmisLetter_b.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.hmisLetter_b.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.hmisLetter_b.setStyleSheet("background-color:#ffffff;")
        self.hmisLetter_b.setAlignment(Qt.AlignCenter)
        self.hmisLetter_b.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetter_b.setFixedWidth(60 * self.screen_ratio)
        self.hmisLetter_b.move(0 * self.screen_ratio, 120 * self.screen_ratio)

        self.hmisImage_b_0 = QLabel(self)
        self.hmisImage_b_0.setPixmap(QPixmap("src/hmis_safety_glass.png"))
        self.hmisImage_b_0.setScaledContents(True)
        self.hmisImage_b_0.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_b_0.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_b_0.move(60 * self.screen_ratio, 120 * self.screen_ratio)

        self.hmisImage_b_1 = QLabel(self)
        self.hmisImage_b_1.setPixmap(QPixmap("src/hmis_gloves.png"))
        self.hmisImage_b_1.setScaledContents(True)
        self.hmisImage_b_1.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_b_1.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_b_1.move(120 * self.screen_ratio, 120 * self.screen_ratio)

        self.hmisLetter_c = QLabel("C", self)
        if self.lang_main == "en":
            self.hmisLetter_c.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.hmisLetter_c.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.hmisLetter_c.setStyleSheet("background-color:#ffffff;")
        self.hmisLetter_c.setAlignment(Qt.AlignCenter)
        self.hmisLetter_c.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetter_c.setFixedWidth(60 * self.screen_ratio)
        self.hmisLetter_c.move(0 * self.screen_ratio, 180 * self.screen_ratio)

        self.hmisImage_c_0 = QLabel(self)
        self.hmisImage_c_0.setPixmap(QPixmap("src/hmis_safety_glass.png"))
        self.hmisImage_c_0.setScaledContents(True)
        self.hmisImage_c_0.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_c_0.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_c_0.move(60 * self.screen_ratio, 180 * self.screen_ratio)

        self.hmisImage_c_1 = QLabel(self)
        self.hmisImage_c_1.setPixmap(QPixmap("src/hmis_gloves.png"))
        self.hmisImage_c_1.setScaledContents(True)
        self.hmisImage_c_1.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_c_1.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_c_1.move(120 * self.screen_ratio, 180 * self.screen_ratio)

        self.hmisImage_c_2 = QLabel(self)
        self.hmisImage_c_2.setPixmap(QPixmap("src/hmis_protective_apron.png"))
        self.hmisImage_c_2.setScaledContents(True)
        self.hmisImage_c_2.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_c_2.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_c_2.move(180 * self.screen_ratio, 180 * self.screen_ratio)

        self.hmisLetter_d = QLabel("D", self)
        if self.lang_main == "en":
            self.hmisLetter_d.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.hmisLetter_d.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.hmisLetter_d.setStyleSheet("background-color:#ffffff;")
        self.hmisLetter_d.setAlignment(Qt.AlignCenter)
        self.hmisLetter_d.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetter_d.setFixedWidth(60 * self.screen_ratio)
        self.hmisLetter_d.move(0 * self.screen_ratio, 240 * self.screen_ratio)

        self.hmisImage_d_0 = QLabel(self)
        self.hmisImage_d_0.setPixmap(QPixmap("src/hmis_face_shield.png"))
        self.hmisImage_d_0.setScaledContents(True)
        self.hmisImage_d_0.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_d_0.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_d_0.move(60 * self.screen_ratio, 240 * self.screen_ratio)

        self.hmisImage_d_1 = QLabel(self)
        self.hmisImage_d_1.setPixmap(QPixmap("src/hmis_gloves.png"))
        self.hmisImage_d_1.setScaledContents(True)
        self.hmisImage_d_1.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_d_1.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_d_1.move(120 * self.screen_ratio, 240 * self.screen_ratio)

        self.hmisImage_d_2 = QLabel(self)
        self.hmisImage_d_2.setPixmap(QPixmap("src/hmis_protective_apron.png"))
        self.hmisImage_d_2.setScaledContents(True)
        self.hmisImage_d_2.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_d_2.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_d_2.move(180 * self.screen_ratio, 240 * self.screen_ratio)

        self.hmisLetter_e = QLabel("E", self)
        if self.lang_main == "en":
            self.hmisLetter_e.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.hmisLetter_e.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.hmisLetter_e.setStyleSheet("background-color:#ffffff;")
        self.hmisLetter_e.setAlignment(Qt.AlignCenter)
        self.hmisLetter_e.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetter_e.setFixedWidth(60 * self.screen_ratio)
        self.hmisLetter_e.move(0 * self.screen_ratio, 300 * self.screen_ratio)

        self.hmisImage_e_0 = QLabel(self)
        self.hmisImage_e_0.setPixmap(QPixmap("src/hmis_safety_glass.png"))
        self.hmisImage_e_0.setScaledContents(True)
        self.hmisImage_e_0.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_e_0.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_e_0.move(60 * self.screen_ratio, 300 * self.screen_ratio)

        self.hmisImage_e_1 = QLabel(self)
        self.hmisImage_e_1.setPixmap(QPixmap("src/hmis_gloves.png"))
        self.hmisImage_e_1.setScaledContents(True)
        self.hmisImage_e_1.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_e_1.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_e_1.move(120 * self.screen_ratio, 300 * self.screen_ratio)

        self.hmisImage_e_2 = QLabel(self)
        self.hmisImage_e_2.setPixmap(QPixmap("src/hims_dust_respirator.png"))
        self.hmisImage_e_2.setScaledContents(True)
        self.hmisImage_e_2.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_e_2.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_e_2.move(180 * self.screen_ratio, 300 * self.screen_ratio)

        self.hmisLetter_f = QLabel("F", self)
        if self.lang_main == "en":
            self.hmisLetter_f.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.hmisLetter_f.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.hmisLetter_f.setStyleSheet("background-color:#ffffff;")
        self.hmisLetter_f.setAlignment(Qt.AlignCenter)
        self.hmisLetter_f.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetter_f.setFixedWidth(60 * self.screen_ratio)
        self.hmisLetter_f.move(0 * self.screen_ratio, 360 * self.screen_ratio)

        self.hmisImage_f_0 = QLabel(self)
        self.hmisImage_f_0.setPixmap(QPixmap("src/hmis_safety_glass.png"))
        self.hmisImage_f_0.setScaledContents(True)
        self.hmisImage_f_0.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_f_0.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_f_0.move(60 * self.screen_ratio, 360 * self.screen_ratio)

        self.hmisImage_f_1 = QLabel(self)
        self.hmisImage_f_1.setPixmap(QPixmap("src/hmis_gloves.png"))
        self.hmisImage_f_1.setScaledContents(True)
        self.hmisImage_f_1.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_f_1.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_f_1.move(120 * self.screen_ratio, 360 * self.screen_ratio)

        self.hmisImage_f_2 = QLabel(self)
        self.hmisImage_f_2.setPixmap(QPixmap("src/hmis_protective_apron.png"))
        self.hmisImage_f_2.setScaledContents(True)
        self.hmisImage_f_2.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_f_2.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_f_2.move(180 * self.screen_ratio, 360 * self.screen_ratio)

        self.hmisImage_f_3 = QLabel(self)
        self.hmisImage_f_3.setPixmap(QPixmap("src/hims_dust_respirator.png"))
        self.hmisImage_f_3.setScaledContents(True)
        self.hmisImage_f_3.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_f_3.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_f_3.move(240 * self.screen_ratio, 360 * self.screen_ratio)

        self.hmisLetter_g = QLabel("G", self)
        if self.lang_main == "en":
            self.hmisLetter_g.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.hmisLetter_g.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.hmisLetter_g.setStyleSheet("background-color:#ffffff;")
        self.hmisLetter_g.setAlignment(Qt.AlignCenter)
        self.hmisLetter_g.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetter_g.setFixedWidth(60 * self.screen_ratio)
        self.hmisLetter_g.move(0 * self.screen_ratio, 420 * self.screen_ratio)

        self.hmisImage_g_0 = QLabel(self)
        self.hmisImage_g_0.setPixmap(QPixmap("src/hmis_safety_glass.png"))
        self.hmisImage_g_0.setScaledContents(True)
        self.hmisImage_g_0.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_g_0.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_g_0.move(60 * self.screen_ratio, 420 * self.screen_ratio)

        self.hmisImage_g_1 = QLabel(self)
        self.hmisImage_g_1.setPixmap(QPixmap("src/hmis_gloves.png"))
        self.hmisImage_g_1.setScaledContents(True)
        self.hmisImage_g_1.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_g_1.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_g_1.move(120 * self.screen_ratio, 420 * self.screen_ratio)

        self.hmisImage_g_2 = QLabel(self)
        self.hmisImage_g_2.setPixmap(QPixmap("src/hmis_vapor_respirator.png"))
        self.hmisImage_g_2.setScaledContents(True)
        self.hmisImage_g_2.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_g_2.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_g_2.move(180 * self.screen_ratio, 420 * self.screen_ratio)

        self.hmisLetter_h = QLabel("H", self)
        if self.lang_main == "en":
            self.hmisLetter_h.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.hmisLetter_h.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.hmisLetter_h.setStyleSheet("background-color:#ffffff;")
        self.hmisLetter_h.setAlignment(Qt.AlignCenter)
        self.hmisLetter_h.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetter_h.setFixedWidth(60 * self.screen_ratio)
        self.hmisLetter_h.move(0 * self.screen_ratio, 480 * self.screen_ratio)

        self.hmisImage_h_0 = QLabel(self)
        self.hmisImage_h_0.setPixmap(QPixmap("src/hmis_splash_goggles.png"))
        self.hmisImage_h_0.setScaledContents(True)
        self.hmisImage_h_0.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_h_0.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_h_0.move(60 * self.screen_ratio, 480 * self.screen_ratio)

        self.hmisImage_h_1 = QLabel(self)
        self.hmisImage_h_1.setPixmap(QPixmap("src/hmis_gloves.png"))
        self.hmisImage_h_1.setScaledContents(True)
        self.hmisImage_h_1.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_h_1.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_h_1.move(120 * self.screen_ratio, 480 * self.screen_ratio)

        self.hmisImage_h_2 = QLabel(self)
        self.hmisImage_h_2.setPixmap(QPixmap("src/hmis_protective_apron.png"))
        self.hmisImage_h_2.setScaledContents(True)
        self.hmisImage_h_2.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_h_2.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_h_2.move(180 * self.screen_ratio, 480 * self.screen_ratio)

        self.hmisImage_h_3 = QLabel(self)
        self.hmisImage_h_3.setPixmap(QPixmap("src/hmis_vapor_respirator.png"))
        self.hmisImage_h_3.setScaledContents(True)
        self.hmisImage_h_3.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_h_3.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_h_3.move(240 * self.screen_ratio, 480 * self.screen_ratio)

        self.hmisLetter_i = QLabel("I", self)
        if self.lang_main == "en":
            self.hmisLetter_i.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.hmisLetter_i.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.hmisLetter_i.setStyleSheet("background-color:#ffffff;")
        self.hmisLetter_i.setAlignment(Qt.AlignCenter)
        self.hmisLetter_i.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetter_i.setFixedWidth(60 * self.screen_ratio)
        self.hmisLetter_i.move(0 * self.screen_ratio, 540 * self.screen_ratio)

        self.hmisImage_i_0 = QLabel(self)
        self.hmisImage_i_0.setPixmap(QPixmap("src/hmis_safety_glass.png"))
        self.hmisImage_i_0.setScaledContents(True)
        self.hmisImage_i_0.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_i_0.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_i_0.move(60 * self.screen_ratio, 540 * self.screen_ratio)

        self.hmisImage_i_1 = QLabel(self)
        self.hmisImage_i_1.setPixmap(QPixmap("src/hmis_gloves.png"))
        self.hmisImage_i_1.setScaledContents(True)
        self.hmisImage_i_1.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_i_1.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_i_1.move(120 * self.screen_ratio, 540 * self.screen_ratio)

        self.hmisImage_i_2 = QLabel(self)
        self.hmisImage_i_2.setPixmap(QPixmap("src/hims_dust_respirator.png"))
        self.hmisImage_i_2.setScaledContents(True)
        self.hmisImage_i_2.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_i_2.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_i_2.move(180 * self.screen_ratio, 540 * self.screen_ratio)

        self.hmisImage_i_3 = QLabel(self)
        self.hmisImage_i_3.setPixmap(QPixmap("src/hmis_vapor_respirator.png"))
        self.hmisImage_i_3.setScaledContents(True)
        self.hmisImage_i_3.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_i_3.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_i_3.move(240 * self.screen_ratio, 540 * self.screen_ratio)

        self.hmisLetter_j = QLabel("J", self)
        if self.lang_main == "en":
            self.hmisLetter_j.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.hmisLetter_j.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.hmisLetter_j.setStyleSheet("background-color:#ffffff;")
        self.hmisLetter_j.setAlignment(Qt.AlignCenter)
        self.hmisLetter_j.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetter_j.setFixedWidth(60 * self.screen_ratio)
        self.hmisLetter_j.move(0 * self.screen_ratio, 600 * self.screen_ratio)

        self.hmisImage_j_0 = QLabel(self)
        self.hmisImage_j_0.setPixmap(QPixmap("src/hmis_splash_goggles.png"))
        self.hmisImage_j_0.setScaledContents(True)
        self.hmisImage_j_0.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_j_0.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_j_0.move(60 * self.screen_ratio, 600 * self.screen_ratio)

        self.hmisImage_j_1 = QLabel(self)
        self.hmisImage_j_1.setPixmap(QPixmap("src/hmis_gloves.png"))
        self.hmisImage_j_1.setScaledContents(True)
        self.hmisImage_j_1.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_j_1.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_j_1.move(120 * self.screen_ratio, 600 * self.screen_ratio)

        self.hmisImage_j_2 = QLabel(self)
        self.hmisImage_j_2.setPixmap(QPixmap("src/hmis_protective_apron.png"))
        self.hmisImage_j_2.setScaledContents(True)
        self.hmisImage_j_2.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_j_2.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_j_2.move(180 * self.screen_ratio, 600 * self.screen_ratio)

        self.hmisImage_j_3 = QLabel(self)
        self.hmisImage_j_3.setPixmap(QPixmap("src/hims_dust_respirator.png"))
        self.hmisImage_j_3.setScaledContents(True)
        self.hmisImage_j_3.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_j_3.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_j_3.move(240 * self.screen_ratio, 600 * self.screen_ratio)

        self.hmisImage_j_4 = QLabel(self)
        self.hmisImage_j_4.setPixmap(QPixmap("src/hmis_vapor_respirator.png"))
        self.hmisImage_j_4.setScaledContents(True)
        self.hmisImage_j_4.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_j_4.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_j_4.move(300 * self.screen_ratio, 600 * self.screen_ratio)

        self.hmisLetter_k = QLabel("K", self)
        if self.lang_main == "en":
            self.hmisLetter_k.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.hmisLetter_k.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.hmisLetter_k.setStyleSheet("background-color:#ffffff;")
        self.hmisLetter_k.setAlignment(Qt.AlignCenter)
        self.hmisLetter_k.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetter_k.setFixedWidth(60 * self.screen_ratio)
        self.hmisLetter_k.move(0 * self.screen_ratio, 660 * self.screen_ratio)

        self.hmisImage_k_0 = QLabel(self)
        self.hmisImage_k_0.setPixmap(QPixmap("src/hmis_air_line_mask_or_hood.png"))
        self.hmisImage_k_0.setScaledContents(True)
        self.hmisImage_k_0.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_k_0.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_k_0.move(60 * self.screen_ratio, 660 * self.screen_ratio)

        self.hmisImage_k_1 = QLabel(self)
        self.hmisImage_k_1.setPixmap(QPixmap("src/hmis_gloves.png"))
        self.hmisImage_k_1.setScaledContents(True)
        self.hmisImage_k_1.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_k_1.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_k_1.move(120 * self.screen_ratio, 660 * self.screen_ratio)

        self.hmisImage_k_2 = QLabel(self)
        self.hmisImage_k_2.setPixmap(QPixmap("src/hmis_full_suit.png"))
        self.hmisImage_k_2.setScaledContents(True)
        self.hmisImage_k_2.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_k_2.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_k_2.move(180 * self.screen_ratio, 660 * self.screen_ratio)

        self.hmisImage_k_3 = QLabel(self)
        self.hmisImage_k_3.setPixmap(QPixmap("src/hmis_boots.png"))
        self.hmisImage_k_3.setScaledContents(True)
        self.hmisImage_k_3.setFixedHeight(60 * self.screen_ratio)
        self.hmisImage_k_3.setFixedWidth(60 * self.screen_ratio)
        self.hmisImage_k_3.move(240 * self.screen_ratio, 660 * self.screen_ratio)

        self.hmisLetter_l_z = QLabel("L - Z", self)
        if self.lang_main == "en":
            self.hmisLetter_l_z.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.hmisLetter_l_z.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.hmisLetter_l_z.setStyleSheet("background-color:#ffffff;")
        self.hmisLetter_l_z.setAlignment(Qt.AlignCenter)
        self.hmisLetter_l_z.setFixedHeight(60 * self.screen_ratio)
        self.hmisLetter_l_z.setFixedWidth(60 * self.screen_ratio)
        self.hmisLetter_l_z.move(0 * self.screen_ratio, 720 * self.screen_ratio)

        self.hmisText_l_z = QLabel(self.str_hmis_l, self)
        if self.lang_main == "en":
            self.hmisText_l_z.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif self.lang_main == "fa":
            self.hmisText_l_z.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.hmisText_l_z.setStyleSheet("background-color:#ffffff;")
        self.hmisText_l_z.setWordWrap(True)
        self.hmisText_l_z.setAlignment(Qt.AlignCenter)
        self.hmisText_l_z.setFixedHeight(60 * self.screen_ratio)
        self.hmisText_l_z.setFixedWidth(300 * self.screen_ratio)
        self.hmisText_l_z.move(60 * self.screen_ratio, 720 * self.screen_ratio)

        self.scrollArea = QScrollArea(self)

        self.vlayout = QVBoxLayout(self.scrollArea)

        self.hmisHLayout_title = QHBoxLayout()
        self.hmisHLayout_title.addWidget(self.hmisLetterTitle_0)
        self.hmisHLayout_title.addWidget(self.hmisLetterTitle_1)
        self.hmisHLayout_title.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_title)

        self.hmisHLayout_a = QHBoxLayout()
        self.hmisHLayout_a.addWidget(self.hmisLetter_a)
        self.hmisHLayout_a.addWidget(self.hmisImage_a_0)
        self.hmisHLayout_a.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_a)

        self.hmisHLayout_b = QHBoxLayout()
        self.hmisHLayout_b.addWidget(self.hmisLetter_b)
        self.hmisHLayout_b.addWidget(self.hmisImage_b_0)
        self.hmisHLayout_b.addWidget(self.hmisImage_b_1)
        self.hmisHLayout_b.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_b)

        self.hmisHLayout_c = QHBoxLayout()
        self.hmisHLayout_c.addWidget(self.hmisLetter_c)
        self.hmisHLayout_c.addWidget(self.hmisImage_c_0)
        self.hmisHLayout_c.addWidget(self.hmisImage_c_1)
        self.hmisHLayout_c.addWidget(self.hmisImage_c_2)
        self.hmisHLayout_c.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_c)

        self.hmisHLayout_d = QHBoxLayout()
        self.hmisHLayout_d.addWidget(self.hmisLetter_d)
        self.hmisHLayout_d.addWidget(self.hmisImage_d_0)
        self.hmisHLayout_d.addWidget(self.hmisImage_d_1)
        self.hmisHLayout_d.addWidget(self.hmisImage_d_2)
        self.hmisHLayout_d.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_d)

        self.hmisHLayout_e = QHBoxLayout()
        self.hmisHLayout_e.addWidget(self.hmisLetter_e)
        self.hmisHLayout_e.addWidget(self.hmisImage_e_0)
        self.hmisHLayout_e.addWidget(self.hmisImage_e_1)
        self.hmisHLayout_e.addWidget(self.hmisImage_e_2)
        self.hmisHLayout_e.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_e)

        self.hmisHLayout_f = QHBoxLayout()
        self.hmisHLayout_f.addWidget(self.hmisLetter_f)
        self.hmisHLayout_f.addWidget(self.hmisImage_f_0)
        self.hmisHLayout_f.addWidget(self.hmisImage_f_1)
        self.hmisHLayout_f.addWidget(self.hmisImage_f_2)
        self.hmisHLayout_f.addWidget(self.hmisImage_f_3)
        self.hmisHLayout_f.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_f)

        self.hmisHLayout_g = QHBoxLayout()
        self.hmisHLayout_g.addWidget(self.hmisLetter_g)
        self.hmisHLayout_g.addWidget(self.hmisImage_g_0)
        self.hmisHLayout_g.addWidget(self.hmisImage_g_1)
        self.hmisHLayout_g.addWidget(self.hmisImage_g_2)
        self.hmisHLayout_g.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_g)

        self.hmisHLayout_h = QHBoxLayout()
        self.hmisHLayout_h.addWidget(self.hmisLetter_h)
        self.hmisHLayout_h.addWidget(self.hmisImage_h_0)
        self.hmisHLayout_h.addWidget(self.hmisImage_h_1)
        self.hmisHLayout_h.addWidget(self.hmisImage_h_2)
        self.hmisHLayout_h.addWidget(self.hmisImage_h_3)
        self.hmisHLayout_h.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_h)

        self.hmisHLayout_i = QHBoxLayout()
        self.hmisHLayout_i.addWidget(self.hmisLetter_i)
        self.hmisHLayout_i.addWidget(self.hmisImage_i_0)
        self.hmisHLayout_i.addWidget(self.hmisImage_i_1)
        self.hmisHLayout_i.addWidget(self.hmisImage_i_2)
        self.hmisHLayout_i.addWidget(self.hmisImage_i_3)
        self.hmisHLayout_i.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_i)

        self.hmisHLayout_j = QHBoxLayout()
        self.hmisHLayout_j.addWidget(self.hmisLetter_j)
        self.hmisHLayout_j.addWidget(self.hmisImage_j_0)
        self.hmisHLayout_j.addWidget(self.hmisImage_j_1)
        self.hmisHLayout_j.addWidget(self.hmisImage_j_2)
        self.hmisHLayout_j.addWidget(self.hmisImage_j_3)
        self.hmisHLayout_j.addWidget(self.hmisImage_j_4)
        self.hmisHLayout_j.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_j)

        self.hmisHLayout_k = QHBoxLayout()
        self.hmisHLayout_k.addWidget(self.hmisLetter_k)
        self.hmisHLayout_k.addWidget(self.hmisImage_k_0)
        self.hmisHLayout_k.addWidget(self.hmisImage_k_1)
        self.hmisHLayout_k.addWidget(self.hmisImage_k_2)
        self.hmisHLayout_k.addWidget(self.hmisImage_k_3)
        self.hmisHLayout_k.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_k)

        self.hmisHLayout_l_z = QHBoxLayout()
        self.hmisHLayout_l_z.addWidget(self.hmisLetter_l_z)
        self.hmisHLayout_l_z.addWidget(self.hmisText_l_z)
        self.hmisHLayout_l_z.setAlignment(Qt.AlignLeft)
        self.vlayout.addLayout(self.hmisHLayout_l_z)

        self.vlayout.setSpacing(0)
        self.vlayout.setContentsMargins(0, 0, 0, 0)

        self.vlayoutGPBox = QGroupBox("")
        self.vlayoutGPBox.setLayout(self.vlayout)

        self.scrollArea.setWidget(self.vlayoutGPBox)
        self.scrollArea.setStyleSheet("background-color:#ffffff;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.resize(400 * self.screen_ratio, 540 * self.screen_ratio)
        self.scrollArea.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        self.setFixedSize(400 * self.screen_ratio, 540 * self.screen_ratio)
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        self.setWindowIcon(QIcon('MSDS_titlebar_icon.png'))
        self.setWindowTitle('MSDS - ' + self.str_win_title)
