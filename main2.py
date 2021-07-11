from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QAction, QFormLayout, QHBoxLayout, QVBoxLayout, \
    QSlider, QRadioButton, QTabWidget, QLabel, QDesktopWidget, QLineEdit, QTextEdit, \
    QCheckBox, QRadioButton, QScrollArea, QGridLayout, QListWidget, QListWidgetItem, \
    QTableWidget, QPushButton, QMessageBox, QGroupBox, QMainWindow, QProgressBar, QApplication, QFrame, QComboBox
import sys
import sqlite3
import codecs


class Window_main2(QMainWindow):

    screen_ratio = 1
    font_ratio = 1

    # strings_en:
    str_section_select_en = "Select Section:"
    str_CAS_en = "CAS#:"
    # -----------
    # strings_fa:
    str_section_select_fa = "انتخاب بخش:"
    str_CAS_fa = "شماره CAS:"
    # -----------
    # strings_final:
    str_section_select = ""
    str_CAS = ""
    # -----------

    lang_main = ""

    sec_title_1_en = "Section 1: \nChemical Product and Properties"
    sec_title_2_en = "Section 2: \nHazards Identification"
    sec_title_3_en = "Section 3: \nFirst Aid Measures"
    sec_title_4_en = "Section 4: \nAccidental Release Measures"
    sec_title_5_en = "Section 5: \nFire and Explosion Data"
    sec_title_6_en = "Section 6: \nHandling and Storage"
    sec_title_7_en = "Section 7: \nPersonal Protection"
    sec_title_8_en = "Section 8: \nStability and Reactivity Data"
    sec_title_9_en = "Section 9: \nEcological Information and \nDisposal Considerations"

    sec_title_1_fa = "بخش 1: \nترکیب شیمیایی و خصوصیات"
    sec_title_2_fa = " بخش 2: \nشناسایی خطرات"
    sec_title_3_fa = " بخش 3: \nکمک های اولیه"
    sec_title_4_fa = " بخش 4: \nاقدامات مربوط به نشت تصادفی"
    sec_title_5_fa = " بخش 5: \nاطلاعات مربوط به حریق و انفجار"
    sec_title_6_fa = " بخش 6: \nحمل و نگه داری"
    sec_title_7_fa = " بخش 7: \nحفاظت فردی"
    sec_title_8_fa = " بخش 8: \nپایداری و واکنش پذیری"
    sec_title_9_fa = " بخش 9: \nاطلاعات زیست محیطی و \nملاحظات دفع"

    list_lang_get = "en"
    list_item_get = ""

    sec1_text = ""
    sec2_text = ""
    sec3_text = ""
    sec4_text = ""
    sec5_text = ""
    sec6_text = ""
    sec7_text = ""
    sec8_text = ""
    sec9_text = ""

    def __init__(self, list_lang, list_item, list_type):
        super(Window_main2, self).__init__()
        global list_lang_get
        global list_item_get
        global list_type_get
        list_lang_get = list_lang
        list_item_get = list_item
        list_type_get = list_type
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
            self.str_section_select = self.str_section_select_en
            self.str_CAS = self.str_CAS_en
        elif self.lang_main == "fa":
            self.str_section_select = self.str_section_select_fa
            self.str_CAS = self.str_CAS_fa

        conn = sqlite3.connect("data/msds_1.0.2.db")

        self.backgroundImage1 = QLabel(self)
        self.backgroundImage1.setStyleSheet("background-color:#ffffff;")
        self.backgroundImage1.setScaledContents(True)
        self.backgroundImage1.resize(220 * self.screen_ratio, 400 * self.screen_ratio)
        self.backgroundImage1.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        global list_lang_get
        global list_item_get

        global sec1_text
        global sec2_text
        global sec3_text
        global sec4_text
        global sec5_text
        global sec6_text
        global sec7_text
        global sec8_text
        global sec9_text

        cas_num_list = []
        name_list = []
        msds_m_list = []
        msds_s1_list = []
        msds_d_list = []
        msds_s2_list = []
        sec1_list = []
        sec2_list = []
        sec3_list = []
        sec4_list = []
        sec5_list = []
        sec6_list = []
        sec7_list = []
        sec8_list = []
        sec9_list = []

        if list_lang_get == "en" and list_type_get == "tums":
            cursor = conn.execute("SELECT * from msds_table_en")
            for row in cursor:
                cas_num_list.append(row[1])
                name_list.append(row[2])
                msds_m_list.append(row[5])
                msds_s1_list.append(row[6])
                msds_d_list.append(row[7])
                msds_s2_list.append(row[8])
                sec1_list.append(row[9])
                sec2_list.append(row[10])
                sec3_list.append(row[11])
                sec4_list.append(row[12])
                sec5_list.append(row[13])
                sec6_list.append(row[14])
                sec7_list.append(row[15])
                sec8_list.append(row[16])
                sec9_list.append(row[17])
            cursor.close()
        elif list_lang_get == "fa" and list_type_get == "tums":
            cursor = conn.execute("SELECT * from msds_table_fa")
            for row in cursor:
                cas_num_list.append(row[1])
                name_list.append(row[2])
                msds_m_list.append(row[5])
                msds_s1_list.append(row[6])
                msds_d_list.append(row[7])
                msds_s2_list.append(row[8])
                sec1_list.append(row[9])
                sec2_list.append(row[10])
                sec3_list.append(row[11])
                sec4_list.append(row[12])
                sec5_list.append(row[13])
                sec6_list.append(row[14])
                sec7_list.append(row[15])
                sec8_list.append(row[16])
                sec9_list.append(row[17])
            cursor.close()
        elif list_lang_get == "fa" and list_type_get == "fda":
            cursor = conn.execute("SELECT * from msds_table_fda")
            for row in cursor:
                cas_num_list.append(row[1])
                name_list.append(row[3])
                msds_m_list.append(row[6])
                msds_s1_list.append(row[7])
                msds_d_list.append(row[8])
                msds_s2_list.append(row[9])
                sec1_list.append(row[10])
                sec3_list.append(row[12])
                sec4_list.append(row[12])
                sec6_list.append(row[11])
                sec9_list.append(row[12])
            cursor.close()

        if list_type_get == "tums":
            cas_num_text = cas_num_list[name_list.index(list_item_get)]
            msds_m_text = msds_m_list[name_list.index(list_item_get)]
            msds_s1_text = msds_s1_list[name_list.index(list_item_get)]
            msds_d_text = msds_d_list[name_list.index(list_item_get)]
            msds_s2_text = msds_s2_list[name_list.index(list_item_get)]
            sec1_text = sec1_list[name_list.index(list_item_get)]
            sec2_text = sec2_list[name_list.index(list_item_get)]
            sec3_text = sec3_list[name_list.index(list_item_get)]
            sec4_text = sec4_list[name_list.index(list_item_get)]
            sec5_text = sec5_list[name_list.index(list_item_get)]
            sec6_text = sec6_list[name_list.index(list_item_get)]
            sec7_text = sec7_list[name_list.index(list_item_get)]
            sec8_text = sec8_list[name_list.index(list_item_get)]
            sec9_text = sec9_list[name_list.index(list_item_get)]
        if list_type_get == "fda":
            cas_num_text = cas_num_list[name_list.index(list_item_get)]
            msds_m_text = msds_m_list[name_list.index(list_item_get)]
            msds_s1_text = msds_s1_list[name_list.index(list_item_get)]
            msds_d_text = msds_d_list[name_list.index(list_item_get)]
            msds_s2_text = msds_s2_list[name_list.index(list_item_get)]
            sec1_text = sec1_list[name_list.index(list_item_get)]
            sec3_text = sec3_list[name_list.index(list_item_get)]
            sec4_text = sec4_list[name_list.index(list_item_get)]
            sec6_text = sec6_list[name_list.index(list_item_get)]
            sec9_text = sec9_list[name_list.index(list_item_get)]

        self.nameLabel = QLabel(list_item_get, self)
        if list_lang_get == "en":
            self.nameLabel.setFont(QFont("Times New Roman", 18 * self.font_ratio, weight=QFont.Bold))
        elif list_lang_get == "fa":
            self.nameLabel.setFont(QFont("B Nazanin", 18 * self.font_ratio, weight=QFont.Bold))
        self.nameLabel.resize(200 * self.screen_ratio, 20 * self.screen_ratio)
        self.nameLabel.move(10 * self.screen_ratio, 10 * self.screen_ratio)

        self.casTitleLabel = QLabel(self.str_CAS, self)
        if self.lang_main == "en":
            self.casTitleLabel.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        elif self.lang_main == "fa":
            self.casTitleLabel.setFont(QFont("B Nazanin", 10 * self.font_ratio))
        self.casTitleLabel.setAlignment(Qt.AlignLeft)
        self.casTitleLabel.resize(200 * self.screen_ratio, 20 * self.screen_ratio)
        self.casTitleLabel.move(10 * self.screen_ratio, 40 * self.screen_ratio)

        self.casContentLabel = QLabel(cas_num_text, self)
        if list_lang_get == "en":
            self.casContentLabel.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        elif list_lang_get == "fa":
            self.casContentLabel.setFont(QFont("B Nazanin", 10 * self.font_ratio))
        self.casContentLabel.setAlignment(Qt.AlignLeft)
        self.casContentLabel.resize(120 * self.screen_ratio, 20 * self.screen_ratio)
        if self.lang_main == "en":
            self.casContentLabel.move(60 * self.screen_ratio, 40 * self.screen_ratio)
        elif self.lang_main == "fa":
            self.casContentLabel.move(90 * self.screen_ratio, 40 * self.screen_ratio)

        self.msdsSignImage = QLabel(self)
        self.msdsSignImage.setPixmap(QPixmap("src/msds_sign.png"))
        self.msdsSignImage.setScaledContents(True)
        self.msdsSignImage.resize(80 * self.screen_ratio, 80 * self.screen_ratio)
        self.msdsSignImage.move(70 * self.screen_ratio, 70 * self.screen_ratio)

        self.msdsSignLabel_m = QLabel(msds_m_text, self)
        self.msdsSignLabel_m.setFont(QFont("Ubuntu Regular", 10 * self.font_ratio))
        self.msdsSignLabel_m.setStyleSheet("color:#ffffff;")
        self.msdsSignLabel_m.setAlignment(Qt.AlignCenter)
        self.msdsSignLabel_m.resize(20 * self.screen_ratio, 20 * self.screen_ratio)
        self.msdsSignLabel_m.move(80 * self.screen_ratio, 100 * self.screen_ratio)

        self.msdsSignLabel_s1 = QLabel(msds_s1_text, self)
        self.msdsSignLabel_s1.setFont(QFont("Ubuntu Regular", 10 * self.font_ratio))
        self.msdsSignLabel_s1.setStyleSheet("color:#ffffff;")
        self.msdsSignLabel_s1.setAlignment(Qt.AlignCenter)
        self.msdsSignLabel_s1.resize(20 * self.screen_ratio, 20 * self.screen_ratio)
        self.msdsSignLabel_s1.move(100 * self.screen_ratio, 80 * self.screen_ratio)

        self.msdsSignLabel_d = QLabel(msds_d_text, self)
        self.msdsSignLabel_d.setFont(QFont("Ubuntu Regular", 10 * self.font_ratio))
        self.msdsSignLabel_d.setAlignment(Qt.AlignCenter)
        self.msdsSignLabel_d.resize(20 * self.screen_ratio, 20 * self.screen_ratio)
        self.msdsSignLabel_d.move(120 * self.screen_ratio, 100 * self.screen_ratio)

        self.msdsSignLabel_s2 = QLabel(msds_s2_text, self)
        self.msdsSignLabel_s2.setFont(QFont("Ubuntu Regular", 10 * self.font_ratio))
        self.msdsSignLabel_s2.setAlignment(Qt.AlignCenter)
        self.msdsSignLabel_s2.resize(20 * self.screen_ratio, 20 * self.screen_ratio)
        self.msdsSignLabel_s2.move(100 * self.screen_ratio, 120 * self.screen_ratio)

        self.secSelectLabel = QLabel(self.str_section_select, self)
        if self.lang_main == "en":
            self.secSelectLabel.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        elif self.lang_main == "fa":
            self.secSelectLabel.setFont(QFont("B Nazanin", 10 * self.font_ratio))
        self.secSelectLabel.setAlignment(Qt.AlignCenter)
        self.secSelectLabel.resize(200 * self.screen_ratio, 20 * self.screen_ratio)
        self.secSelectLabel.move(10 * self.screen_ratio, 170 * self.screen_ratio)

        self.titleList = QListWidget(self)
        #self.titleList.setStyleSheet("background-color:#ffffff;")
        if list_lang_get == "en" and list_type_get == "tums":
            self.titleList.setFont(QFont("Times New Roman", 11 * self.font_ratio))
            #self.titleList.addItem(self.sec_title_1_en)
            for i in range(9):
                exec("item = QListWidgetItem(self.sec_title_" + str(i + 1) + "_en)")
                exec("item.setTextAlignment(Qt.AlignCenter)")
                exec("self.titleList.addItem(item)")
        elif list_lang_get == "fa" and list_type_get == "tums":
            self.titleList.setFont(QFont("B Nazanin", 11 * self.font_ratio))
            for i in range(9):
                exec("item = QListWidgetItem(self.sec_title_" + str(i + 1) + "_fa)")
                exec("item.setTextAlignment(Qt.AlignCenter)")
                exec("self.titleList.addItem(item)")
        elif list_lang_get == "fa" and list_type_get == "fda":
            self.titleList.setFont(QFont("B Nazanin", 11 * self.font_ratio))
            item1 = QListWidgetItem(self.sec_title_1_fa)
            item3 = QListWidgetItem(self.sec_title_3_fa)
            item4 = QListWidgetItem(self.sec_title_4_fa)
            item6 = QListWidgetItem(self.sec_title_6_fa)
            item9 = QListWidgetItem(self.sec_title_9_fa)
            item1.setTextAlignment(Qt.AlignCenter)
            item3.setTextAlignment(Qt.AlignCenter)
            item4.setTextAlignment(Qt.AlignCenter)
            item6.setTextAlignment(Qt.AlignCenter)
            item9.setTextAlignment(Qt.AlignCenter)
            self.titleList.addItem(item1)
            self.titleList.addItem(item3)
            self.titleList.addItem(item4)
            self.titleList.addItem(item6)
            self.titleList.addItem(item9)

        self.titleList.resize(220 * self.screen_ratio, 200 * self.screen_ratio)
        self.titleList.move(0 * self.screen_ratio, 200 * self.screen_ratio)
        self.titleList.itemActivated.connect(self.titleList_doubleClicked)

        #self.backgroundImage2 = QLabel(self)
        #self.backgroundImage2.setPixmap(QPixmap("src/msds_title_3.png"))
        #self.backgroundImage2.setScaledContents(True)
        #self.backgroundImage2.resize(380 * self.screen_ratio, 400 * self.screen_ratio)
        #self.backgroundImage2.move(220 * self.screen_ratio, 0 * self.screen_ratio)

        if list_lang_get == "en":
            self.secTitleLabel = QLabel(self.sec_title_1_en, self)
            self.secTitleLabel.setFont(QFont("Times New Roman", 12 * self.font_ratio, weight=QFont.Bold))
            self.secTitleLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.secTitleLabel.resize(360 * self.screen_ratio, 40 * self.screen_ratio)
            self.secTitleLabel.move(230 * self.screen_ratio, 10 * self.screen_ratio)
        elif list_lang_get == "fa":
            self.secTitleLabel = QLabel(self.sec_title_1_fa, self)
            self.secTitleLabel.setFont(QFont("B Nazanin", 12 * self.font_ratio, weight=QFont.Bold))
            self.secTitleLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.secTitleLabel.resize(360 * self.screen_ratio, 40 * self.screen_ratio)
            self.secTitleLabel.move(230 * self.screen_ratio, 10 * self.screen_ratio)

        self.scrollArea = QScrollArea(self)

        self.secContentLabel = QLabel(sec1_text, self)
        if list_lang_get == "en":
            self.secContentLabel.setFont(QFont("Times New Roman", 12 * self.font_ratio))
        elif list_lang_get == "fa":
            self.secContentLabel.setFont(QFont("B Nazanin", 12 * self.font_ratio))
        self.secContentLabel.setStyleSheet("background-color:#ffffff;")
        self.secContentLabel.setAlignment(Qt.AlignLeft)
        self.secContentLabel.setWordWrap(True)
        self.secContentLabel.setMargin(10)
        self.secContentLabel.resize(340 * self.screen_ratio, 330 * self.screen_ratio)
        #self.secContentLabel.move(230 * self.screen_ratio, 60 * self.screen_ratio)

        self.scrollArea.setStyleSheet("background-color:#ffffff;")
        self.scrollArea.setWidget(self.secContentLabel)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.resize(360 * self.screen_ratio, 330 * self.screen_ratio)
        self.scrollArea.move(230 * self.screen_ratio, 60 * self.screen_ratio)

        self.setFixedSize(600 * self.screen_ratio, 400 * self.screen_ratio)
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        self.setWindowIcon(QIcon('MSDS_titlebar_icon.png'))
        self.setWindowTitle('MSDS - ' + list_item_get)

    def titleList_doubleClicked(self, text):
        global list_lang_get
        global list_item_get

        global sec1_text
        global sec2_text
        global sec3_text
        global sec4_text
        global sec5_text
        global sec6_text
        global sec7_text
        global sec8_text
        global sec9_text

        if list_lang_get == "en":
            if text.text() == self.sec_title_1_en:
                self.secTitleLabel.setText(self.sec_title_1_en)
                self.secContentLabel.setText(sec1_text)
            elif text.text() == self.sec_title_2_en:
                self.secTitleLabel.setText(self.sec_title_2_en)
                self.secContentLabel.setText(sec2_text)
            elif text.text() == self.sec_title_3_en:
                self.secTitleLabel.setText(self.sec_title_3_en)
                self.secContentLabel.setText(sec3_text)
            elif text.text() == self.sec_title_4_en:
                self.secTitleLabel.setText(self.sec_title_4_en)
                self.secContentLabel.setText(sec4_text)
            elif text.text() == self.sec_title_5_en:
                self.secTitleLabel.setText(self.sec_title_5_en)
                self.secContentLabel.setText(sec5_text)
            elif text.text() == self.sec_title_6_en:
                self.secTitleLabel.setText(self.sec_title_6_en)
                self.secContentLabel.setText(sec6_text)
            elif text.text() == self.sec_title_7_en:
                self.secTitleLabel.setText(self.sec_title_7_en)
                self.secContentLabel.setText(sec7_text)
            elif text.text() == self.sec_title_8_en:
                self.secTitleLabel.setText(self.sec_title_8_en)
                self.secContentLabel.setText(sec8_text)
            elif text.text() == self.sec_title_9_en:
                self.secTitleLabel.setText("Section 9: \nEcological Information and Disposal Considerations")
                self.secContentLabel.setText(sec9_text)
        elif list_lang_get == "fa":
            if text.text() == self.sec_title_1_fa:
                self.secTitleLabel.setText(self.sec_title_1_fa)
                self.secContentLabel.setText(sec1_text)
            elif text.text() == self.sec_title_2_fa:
                self.secTitleLabel.setText(self.sec_title_2_fa)
                self.secContentLabel.setText(sec2_text)
            elif text.text() == self.sec_title_3_fa:
                self.secTitleLabel.setText(self.sec_title_3_fa)
                self.secContentLabel.setText(sec3_text)
            elif text.text() == self.sec_title_4_fa:
                self.secTitleLabel.setText(self.sec_title_4_fa)
                self.secContentLabel.setText(sec4_text)
            elif text.text() == self.sec_title_5_fa:
                self.secTitleLabel.setText(self.sec_title_5_fa)
                self.secContentLabel.setText(sec5_text)
            elif text.text() == self.sec_title_6_fa:
                self.secTitleLabel.setText(self.sec_title_6_fa)
                self.secContentLabel.setText(sec6_text)
            elif text.text() == self.sec_title_7_fa:
                self.secTitleLabel.setText(self.sec_title_7_fa)
                self.secContentLabel.setText(sec7_text)
            elif text.text() == self.sec_title_8_fa:
                self.secTitleLabel.setText(self.sec_title_8_fa)
                self.secContentLabel.setText(sec8_text)
            elif text.text() == self.sec_title_9_fa:
                self.secTitleLabel.setText("بخش 9: \nاطلاعات زیست محیطی و ملاحظات دفع")
                self.secContentLabel.setText(sec9_text)
        elif list_lang_get == "fa":
            if text.text() == self.sec_title_1_fa:
                self.secTitleLabel.setText(self.sec_title_1_fa)
                self.secContentLabel.setText(sec1_text)
            elif text.text() == self.sec_title_2_fa:
                self.secTitleLabel.setText(self.sec_title_2_fa)
                self.secContentLabel.setText(sec2_text)
            elif text.text() == self.sec_title_3_fa:
                self.secTitleLabel.setText(self.sec_title_3_fa)
                self.secContentLabel.setText(sec3_text)
            elif text.text() == self.sec_title_4_fa:
                self.secTitleLabel.setText(self.sec_title_4_fa)
                self.secContentLabel.setText(sec4_text)
            elif text.text() == self.sec_title_5_fa:
                self.secTitleLabel.setText(self.sec_title_5_fa)
                self.secContentLabel.setText(sec5_text)
            elif text.text() == self.sec_title_6_fa:
                self.secTitleLabel.setText(self.sec_title_6_fa)
                self.secContentLabel.setText(sec6_text)
            elif text.text() == self.sec_title_7_fa:
                self.secTitleLabel.setText(self.sec_title_7_fa)
                self.secContentLabel.setText(sec7_text)
            elif text.text() == self.sec_title_8_fa:
                self.secTitleLabel.setText(self.sec_title_8_fa)
                self.secContentLabel.setText(sec8_text)
            elif text.text() == self.sec_title_9_fa:
                self.secTitleLabel.setText("بخش 9: \nاطلاعات زیست محیطی و ملاحظات دفع")
                self.secContentLabel.setText(sec9_text)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white, 0.0001, Qt.SolidLine))

        grad1 = QLinearGradient(0, 1000, 0, 100)

        grad1.setColorAt(0.5, QColor("#ffffff"))
        grad1.setColorAt(1.0, QColor("#365fd4"))
        painter.setBrush(QBrush(grad1))

        painter.drawRect(220 * self.screen_ratio, 0 * self.screen_ratio, 95 * self.screen_ratio,
                         400 * self.screen_ratio)

        grad2 = QLinearGradient(0, 1000, 0, 100)

        grad2.setColorAt(0.5, QColor("#ffffff"))
        grad2.setColorAt(1.0, QColor("#ec1f1f"))
        painter.setBrush(QBrush(grad2))

        painter.drawRect(315 * self.screen_ratio, 0 * self.screen_ratio, 95 * self.screen_ratio,
                         400 * self.screen_ratio)

        grad3 = QLinearGradient(0, 1000, 0, 100)

        grad3.setColorAt(0.5, QColor("#ffffff"))
        grad3.setColorAt(1.0, QColor("#fffc00"))
        painter.setBrush(QBrush(grad3))

        painter.drawRect(410 * self.screen_ratio, 0 * self.screen_ratio, 95 * self.screen_ratio,
                         400 * self.screen_ratio)

        grad4 = QLinearGradient(0, 1000, 0, 100)

        grad4.setColorAt(0.5, QColor("#ffffff"))
        grad4.setColorAt(1.0, QColor("#ffffff"))
        painter.setBrush(QBrush(grad4))

        painter.drawRect(505 * self.screen_ratio, 0 * self.screen_ratio, 95 * self.screen_ratio,
                         400 * self.screen_ratio)
