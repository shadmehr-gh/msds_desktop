from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QAction, QFormLayout, QHBoxLayout, QVBoxLayout, \
    QSlider, QRadioButton, QTabWidget, QLabel, QDesktopWidget, QLineEdit, QTextEdit, \
    QCheckBox, QRadioButton, QScrollArea, QGridLayout, QListWidget, QListWidgetItem, \
    QTableWidget, QPushButton, QMessageBox, QGroupBox, QMainWindow, QProgressBar, QApplication, QFrame, QComboBox
import sys
import codecs
import main1


class Window_main9(QMainWindow):

    screen_ratio = 1
    font_ratio = 1

    # strings_en:
    str_win_title_en = "Settings"
    str_setting1_label_en = "Add IRFDA MSDSs:"
    str_setting1_combo_list_en = ["All MSDSs", "TUMS MSDSs Only", "IRFDA MSDSs Only"]
    str_setting2_button_en = "Update MSDSs From Server"
    # -----------
    # strings_fa:
    str_win_title_fa = "تنظیمات"
    str_setting1_label_fa = "افزودن MSDS های سازمان غذا و دارو:"
    str_setting1_combo_list_fa = ["ها MSDS همه", "های دانشگاه علوم پزشکی تهران MSDS فقط", "های سازمان غذا و دارو MSDS فقط"]
    str_setting2_button_fa = "ها از سرور MSDS آپدیت"
    # -----------
    # strings_final:
    str_win_title = ""
    str_setting1_label = ""
    str_setting1_combo_list = []
    str_setting2_button = ""
    # -----------

    lang_main = ""

    def __init__(self):
        super(Window_main9, self).__init__()
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
            self.str_setting1_label = self.str_setting1_label_en
            self.str_setting1_combo_list = self.str_setting1_combo_list_en
            self.str_setting2_button = self.str_setting2_button_en
        elif self.lang_main == "fa":
            self.str_win_title = self.str_win_title_fa
            self.str_setting1_label = self.str_setting1_label_fa
            self.str_setting1_combo_list = self.str_setting1_combo_list_fa
            self.str_setting2_button = self.str_setting2_button_fa

        list_type_get = codecs.open("data/list_type.txt", encoding='utf-8', mode="r")
        self.list_type = list_type_get.read()
        list_type_get.close()

        self.backgroundImage1 = QLabel(self)
        self.backgroundImage1.setStyleSheet("background-color:#bbbbbb;")
        self.backgroundImage1.setScaledContents(True)
        self.backgroundImage1.resize(300 * self.screen_ratio, 110 * self.screen_ratio)
        self.backgroundImage1.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        self.backgroundImageSetting1 = QLabel(self)
        self.backgroundImageSetting1.setStyleSheet("background-color:#ffffff;")
        self.backgroundImageSetting1.setScaledContents(True)
        self.backgroundImageSetting1.resize(300 * self.screen_ratio, 59 * self.screen_ratio)
        self.backgroundImageSetting1.move(0 * self.screen_ratio, 0 * self.screen_ratio)

        self.settingLabel1 = QLabel(self.str_setting1_label, self)
        if self.lang_main == "en":
            self.settingLabel1.setFont(QFont("Times New Roman", 10 * self.font_ratio))
        elif self.lang_main == "fa":
            self.settingLabel1.setFont(QFont("B Nazanin", 10 * self.font_ratio))
        self.settingLabel1.setAlignment(Qt.AlignLeft)
        self.settingLabel1.setWordWrap(True)
        self.settingLabel1.setMargin(15)
        self.settingLabel1.resize(240 * self.screen_ratio, 40 * self.screen_ratio)
        self.settingLabel1.move(50 * self.screen_ratio, 0 * self.screen_ratio)

        self.comboSetting1 = QComboBox(self)
        if self.lang_main == "en":
            self.comboSetting1.setFont(QFont('Times New Roman', 10))
        elif self.lang_main == "fa":
            self.comboSetting1.setFont(QFont('B Nazanin', 10))
        #self.comboSetting1.setEditable(True)
        #line_edit = self.comboSetting1.lineEdit()
        #line_edit.setAlignment(Qt.AlignCenter)
        #line_edit.setReadOnly(True)
        for i in self.str_setting1_combo_list:
            self.comboSetting1.addItem(str(i))
        if self.list_type == "tums":
            self.comboSetting1.setCurrentIndex(1)
        elif self.list_type == "fda":
            self.comboSetting1.setCurrentIndex(2)
        else:
            self.comboSetting1.setCurrentIndex(0)
        self.comboSetting1.resize(240 * self.screen_ratio, 20 * self.screen_ratio)
        self.comboSetting1.move(50 * self.screen_ratio, 30 * self.screen_ratio)
        self.comboSetting1.activated[str].connect(self.onActivatedSettingCombo)

        self.settingImage1 = QLabel(self)
        self.settingImage1.setPixmap(QPixmap("src/fda_logo.png"))
        self.settingImage1.setScaledContents(True)
        self.settingImage1.resize(30 * self.screen_ratio, 40 * self.screen_ratio)
        self.settingImage1.move(10 * self.screen_ratio, 10 * self.screen_ratio)

        self.backgroundImageSetting2 = QLabel(self)
        self.backgroundImageSetting2.setStyleSheet("background-color:#ffffff;")
        self.backgroundImageSetting2.setScaledContents(True)
        self.backgroundImageSetting2.resize(300 * self.screen_ratio, 50 * self.screen_ratio)
        self.backgroundImageSetting2.move(0 * self.screen_ratio, 60 * self.screen_ratio)

        self.buttonSetting2 = QPushButton(self)
        self.buttonSetting2.setText(self.str_setting2_button)
        self.buttonSetting2.setEnabled(False)
        self.buttonSetting2.resize(280 * self.screen_ratio, 30 * self.screen_ratio)
        self.buttonSetting2.move(10 * self.screen_ratio, 70 * self.screen_ratio)
        self.buttonSetting2.clicked.connect(self.buttonSetting2_clicked)

        self.setFixedSize(300 * self.screen_ratio, 110 * self.screen_ratio)
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        self.setWindowIcon(QIcon('MSDS_titlebar_icon.png'))
        self.setWindowTitle('MSDS - ' + self.str_win_title)

    def onActivatedSettingCombo(self):
        index = self.comboSetting1.currentIndex()
        if index == 0:
            lang_write_en = codecs.open("data/list_type.txt", encoding='utf-8', mode="w")
            lang_write_en.write("tums-fda")
            lang_write_en.close()
            self.comboSetting1.setCurrentIndex(0)
        elif index == 1:
            lang_write_en = codecs.open("data/list_type.txt", encoding='utf-8', mode="w")
            lang_write_en.write("tums")
            lang_write_en.close()
            self.comboSetting1.setCurrentIndex(1)
        elif index == 2:
            lang_write_en = codecs.open("data/list_type.txt", encoding='utf-8', mode="w")
            lang_write_en.write("fda")
            lang_write_en.close()
            self.comboSetting1.setCurrentIndex(2)
        self.win = main1.Window_main()
        self.win.show()
        self.hide()

    def buttonSetting2_clicked(self):
        return
