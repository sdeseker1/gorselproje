# Form implementation generated from reading ui file 'anasayfaaZS.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class D(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(838, 668)
        Form.setStyleSheet("/* Ana pencere */\n"
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
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_4 = QtWidgets.QWidget(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnEkle = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnEkle.setObjectName("btnEkle")
        self.verticalLayout_2.addWidget(self.btnEkle)
        self.btnAra = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnAra.setObjectName("btnAra")
        self.verticalLayout_2.addWidget(self.btnAra)
        self.btnSil = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnSil.setObjectName("btnSil")
        self.verticalLayout_2.addWidget(self.btnSil)
        self.btnListele = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnListele.setObjectName("btnListele")
        self.verticalLayout_2.addWidget(self.btnListele)
        self.btnGuncelle = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnGuncelle.setObjectName("btnGuncelle")
        self.verticalLayout_2.addWidget(self.btnGuncelle)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.widget_2 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cwDTarihi_2 = QtWidgets.QLabel(parent=self.widget_2)
        self.cwDTarihi_2.setObjectName("cwDTarihi_2")
        self.verticalLayout_4.addWidget(self.cwDTarihi_2)
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(parent=self.widget_2)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.verticalLayout_4.addWidget(self.calendarWidget_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lneSporcuAdi = QtWidgets.QLabel(parent=self.widget_3)
        self.lneSporcuAdi.setObjectName("lneSporcuAdi")
        self.horizontalLayout.addWidget(self.lneSporcuAdi)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget_3)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lneSporcuSoyadi = QtWidgets.QLabel(parent=self.widget_3)
        self.lneSporcuSoyadi.setObjectName("lneSporcuSoyadi")
        self.horizontalLayout_3.addWidget(self.lneSporcuSoyadi)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cmbCinsiyet = QtWidgets.QLabel(parent=self.widget_3)
        self.cmbCinsiyet.setObjectName("cmbCinsiyet")
        self.horizontalLayout_4.addWidget(self.cmbCinsiyet)
        self.comboBox = QtWidgets.QComboBox(parent=self.widget_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.chkMedeniHal = QtWidgets.QLabel(parent=self.widget_3)
        self.chkMedeniHal.setObjectName("chkMedeniHal")
        self.horizontalLayout_5.addWidget(self.chkMedeniHal)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.widget_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lwBolum = QtWidgets.QLabel(parent=self.widget_3)
        self.lwBolum.setObjectName("lwBolum")
        self.horizontalLayout_2.addWidget(self.lwBolum)
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.widget_3)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.horizontalLayout_2.addWidget(self.listWidget_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.widget_3)
        self.widget_5 = QtWidgets.QWidget(parent=self.widget_4)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.gridLayout_2.addWidget(self.tableWidget_2, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(15, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.widget_5)
        self.horizontalLayout_7.addWidget(self.widget_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnEkle.setText(_translate("Form", "KAYIT EKLE"))
        self.btnAra.setText(_translate("Form", "KAYIT ARA"))
        self.btnSil.setText(_translate("Form", "KAYIT SİL"))
        self.btnListele.setText(_translate("Form", "KAYIT LİSTELE"))
        self.btnGuncelle.setText(_translate("Form", "GÜNCELLE"))
        self.pushButton_6.setText(_translate("Form", "ÇIKIŞ"))
        self.cwDTarihi_2.setText(_translate("Form", "Doğum Tarihi"))
        self.lneSporcuAdi.setText(_translate("Form", "Kullanıcı Adı"))
        self.lneSporcuSoyadi.setText(_translate("Form", "Kullanıcının Soyadı"))
        self.cmbCinsiyet.setText(_translate("Form", "Kullanıcı Cinsiyeti"))
        self.comboBox.setItemText(0, _translate("Form", "kadın"))
        self.comboBox.setItemText(1, _translate("Form", "erkek"))
        self.chkMedeniHal.setText(_translate("Form", "Numarası"))
        self.lwBolum.setText(_translate("Form", "Bölümü"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Form", "BİLGİSAYAR"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("Form", "ELEKTİRİK"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("Form", "MEKANİK"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("Form", "SPONSOR"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Form", "1.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("Form", "2.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("Form", "3.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("Form", "4.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("Form", "5.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("Form", "6.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("Form", "7.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("Form", "8.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("Form", "9.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("Form", "10.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("Form", "11.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(11)
        item.setText(_translate("Form", "12.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(12)
        item.setText(_translate("Form", "13.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(13)
        item.setText(_translate("Form", "14.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(14)
        item.setText(_translate("Form", "15.ÜYE"))
        item = self.tableWidget_2.verticalHeaderItem(15)
        item.setText(_translate("Form", "16.ÜYE"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ADI"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "SOYADI"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "CİNSİYETİ"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "BÖLÜMÜ"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "NUMARASI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = D()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
