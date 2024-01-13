# Form implementation generated from reading ui file 'kaptanbirimsecimi.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import bolumm


class tkmkptnbr(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1179, 575)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setStyleSheet("/* Ana pencere */\n"
"QWidget {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 #1e272e, stop:1 #34495e); /* Gradient arka plan */\n"
"    color: #ecf0f1; /* Beyaz metin */\n"
"}\n"
"\n"
"/* Başlık çubuğu */\n"
"QHeaderView::section {\n"
"    background-color: #3498db; /* Mavi başlık arka planı */\n"
"    color: #ecf0f1; /* Beyaz başlık metni */\n"
"}\n"
"\n"
"/* Butonlar */\n"
"QPushButton {\n"
"    background-color: #e74c3c; /* Turuncu buton arka planı */\n"
"    border: 2px solid #c0392b; /* Kenarlık rengi */\n"
"    color: white; /* Beyaz buton metni */\n"
"    padding: 10px 20px; /* İç boşluklar */\n"
"    border-radius: 5px; /* Kenar yuvarlaklığı */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d35400; /* Butona hover olduğunda daha koyu turuncu arka plan */\n"
"}\n"
"\n"
"/* Giriş kutusu */\n"
"QLineEdit {\n"
"    background-color: rgba(30, 39, 46, 0.7); /* Yarı saydam koyu gri arka plan */\n"
"    color: #bdc3c7; /* Gri metin */\n"
"    padding: 8px; /* İç boşluklar */\n"
"    border: 2px solid #2c3e50; /* Kenarlık rengi */\n"
"    border-radius: 5px; /* Kenar yuvarlaklığı */\n"
"}\n"
"\n"
"/* Giriş kutusu üzerine gelindiğinde */\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3498db; /* Kenarlık rengini mavi yap */\n"
"}\n"
"\n"
"/* Calendar Widget */\n"
"QCalendarWidget {\n"
"    background-color: #2c3e50; /* Koyu mavi arka plan */\n"
"    color: #ecf0f1; /* Beyaz metin */\n"
"    selection-background-color: #3498db; /* Mavi seçili gün arka planı */\n"
"}\n"
"\n"
"/* Header (Ay ve yıl gösterim alanı) */\n"
"QCalendarWidget QHeaderView {\n"
"    background-color: #34495e; /* Gri arka plan */\n"
"    color: #ecf0f1; /* Beyaz metin */\n"
"    border: 1px solid #2c3e50; /* Kenarlık rengi */\n"
"    padding: 6px; /* İç boşluklar */\n"
"}\n"
"\n"
"/* Previous ve Next ay geçiş düğmeleri */\n"
"QCalendarWidget QToolButton {\n"
"    background-color: #2c3e50; /* Koyu mavi arka plan */\n"
"    color: #ecf0f1; /* Beyaz metin */\n"
"    border: 1px solid #2c3e50; /* Kenarlık rengi */\n"
"    border-radius: 5px; /* Kenar yuvarlaklığı */\n"
"    min-width: 20px; /* Minimum genişlik */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #34495e; /* Hover olduğunda daha koyu gri arka plan */\n"
"}\n"
"\n"
"/* Günlük hücreler */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    color: #ecf0f1; /* Beyaz metin */\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled {\n"
"    color: #95a5a6; /* Gri renkli devre dışı bırakılmış günler */\n"
"}\n"
"\n"
"/* Seçili günün arka planı */\n"
"QCalendarWidget QAbstractItemView:selected {\n"
"    background-color: #3498db; /* Mavi seçili gün arka planı */\n"
"}\n"
"\n"
"/* Hafta başlıkları */\n"
"QCalendarWidget QAbstractItemView:section {\n"
"    background-color: #34495e; /* Gri hafta başlığı arka planı */\n"
"    color: #ecf0f1; /* Beyaz metin */\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(" border: 2px solid #c0392b; /* Kenarlık rengi */\n"
"    \n"
"    border-radius:10px; /* Kenar yuvarlaklığı */\n"
"font: 18pt \"Snap ITC\";\n"
"\n"
"background-color: rgba(255, 82, 66,0.89);\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("border-image: url(:/blm/bolumzs.png);")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("font: 9pt \"Snap ITC\";")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mekanikbrpushButton = QtWidgets.QPushButton(parent=self.widget_3)
        self.mekanikbrpushButton.setObjectName("mekanikbrpushButton")
        self.gridLayout_2.addWidget(self.mekanikbrpushButton, 0, 11, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 13, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 7, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 4, 1, 1)
        self.elektirikbrpushButton = QtWidgets.QPushButton(parent=self.widget_3)
        self.elektirikbrpushButton.setObjectName("elektirikbrpushButton")
        self.gridLayout_2.addWidget(self.elektirikbrpushButton, 0, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 15, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 0, 14, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 0, 12, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 0, 9, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 0, 10, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 0, 6, 1, 1)
        self.sponsorbrpushButton = QtWidgets.QPushButton(parent=self.widget_3)
        self.sponsorbrpushButton.setObjectName("sponsorbrpushButton")
        self.gridLayout_2.addWidget(self.sponsorbrpushButton, 0, 17, 1, 1)
        self.bilgisayarbrpushButton = QtWidgets.QPushButton(parent=self.widget_3)
        self.bilgisayarbrpushButton.setStyleSheet("font: 9pt \"Snap ITC\";")
        self.bilgisayarbrpushButton.setObjectName("bilgisayarbrpushButton")
        self.gridLayout_2.addWidget(self.bilgisayarbrpushButton, 0, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 0, 16, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "                                       HANGİ BÖLÜM KAPTANISINIZ ?"))
        self.mekanikbrpushButton.setText(_translate("Form", "MEKANİK BİRİMİ"))
        self.elektirikbrpushButton.setText(_translate("Form", "ELEKTİRİK BİRİMİ"))
        self.sponsorbrpushButton.setText(_translate("Form", "SPONSOR BİRİMİ"))
        self.bilgisayarbrpushButton.setText(_translate("Form", "BİLGİSAYAR BİRİMİ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = tkmkptnbr()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
