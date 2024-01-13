# Form implementation generated from reading ui file 'BİLGİSAYARYAPILACAKLAR2.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class bilgisayaryap(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1215, 656)
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
        self.gridLayout_6 = QtWidgets.QGridLayout(Form)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget_6 = QtWidgets.QWidget(parent=Form)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.widget_6)
        self.label.setStyleSheet("font: 20pt \"Snap ITC\";\n"
"color: rgb(240, 124, 41);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout_6.addWidget(self.widget_6, 0, 1, 1, 3)
        self.widget_2 = QtWidgets.QWidget(parent=Form)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listWidget = QtWidgets.QListWidget(parent=self.widget_2)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(12)
        item.setFont(font)
        icon = QtGui.QIcon.fromTheme("accessories-dictionary")
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(255, 186, 126))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.gridLayout_4.addWidget(self.listWidget, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget_2, 1, 1, 1, 2)
        self.widget_4 = QtWidgets.QWidget(parent=Form)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget_5 = QtWidgets.QListWidget(parent=self.widget_4)
        self.listWidget_5.setObjectName("listWidget_5")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(11)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 186, 126))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 186, 126))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.listWidget_5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_5.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_5.addItem(item)
        self.gridLayout_2.addWidget(self.listWidget_5, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget_4, 1, 3, 2, 1)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.widget)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(11)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 186, 126))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        self.gridLayout_5.addWidget(self.listWidget_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget, 2, 1, 3, 1)
        self.widget_5 = QtWidgets.QWidget(parent=Form)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget_4 = QtWidgets.QListWidget(parent=self.widget_5)
        self.listWidget_4.setObjectName("listWidget_4")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(11)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 186, 126))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_4.addItem(item)
        self.gridLayout.addWidget(self.listWidget_4, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(parent=self.widget_5)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget_3 = QtWidgets.QListWidget(parent=self.widget_3)
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(11)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 186, 126))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.listWidget_3.addItem(item)
        self.gridLayout_3.addWidget(self.listWidget_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget_5, 3, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "                           BİLGİSAYAR BİRİMİ YAPILACAKLAR"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "NESNE TESPİTİ İÇİN GÖREV SIRALAMASI"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "1-VERİ ETİKETLEME"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "2-MİMARİ ARAŞTIRMASI"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "3-İLK TEMEL MODEL EĞİTİMLERİ"))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "4-GERÇEK MODEL EĞİTİMİ"))
        item = self.listWidget.item(5)
        item.setText(_translate("Form", "5-ZED2 KAMERA İLE NESNE TESPİTİ"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        item = self.listWidget_5.item(0)
        item.setText(_translate("Form", "ARAYÜZ İÇİN GÖREV SIRALAMALARI"))
        item = self.listWidget_5.item(1)
        item.setText(_translate("Form", "1-ARAYÜZ İÇİN ARAŞTIRMA"))
        item = self.listWidget_5.item(2)
        item.setText(_translate("Form", "2-ARAYÜZ İÇİN PROGRAM SEÇİMİ"))
        item = self.listWidget_5.item(3)
        item.setText(_translate("Form", "3-SEÇİLEN PROGRAM ÜZERİNDE ÖRNEK ÇALIŞMALAR"))
        item = self.listWidget_5.item(4)
        item.setText(_translate("Form", "4-SAHTE ARAÇ VERİLERİ İLE ÖRNEK ARAYÜZ"))
        item = self.listWidget_5.item(5)
        item.setText(_translate("Form", "5-GERÇEK VERİLER İLE ARAYÜZ OLUŞTURMA"))
        self.listWidget_5.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Form", "ŞERİT TESPİTİ İÇİN GÖREV SIRALAMASI"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("Form", "1-VERİ TOPLAMA"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("Form", "2-VERİ ETİKETLEME"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("Form", "3-MİMARİ ARAŞTIRMASI(SEGMANTASYON)"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("Form", "4-İLK TEMEL MODEL EĞİTİMLERİ"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("Form", "5-GERÇEK MODEL EĞİTİMLERİ"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("Form", "6-PID ÇALIŞMALARI"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        item = self.listWidget_4.item(0)
        item.setText(_translate("Form", "PATH PLANNİNG İÇİN GÖREV SIRALAMASI"))
        item = self.listWidget_4.item(1)
        item.setText(_translate("Form", "ALGORİTMA ARAŞTIRMALARI (GLOBAL-YEREL)"))
        item = self.listWidget_4.item(2)
        item.setText(_translate("Form", "ALGORİTMA KARŞILAŞTIRMALARI"))
        item = self.listWidget_4.item(3)
        item.setText(_translate("Form", "SEÇİLEN PROGRAM ÜZERİNDE ÖRNEK ÇALIŞMALAR"))
        item = self.listWidget_4.item(4)
        item.setText(_translate("Form", "SAHTE ARAÇ VERİLERİ İLE ÖRNEK ARAYÜZ"))
        item = self.listWidget_4.item(5)
        item.setText(_translate("Form", "GERÇEK VERİLER İLE ARAYÜZ OLUŞTURMA"))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("Form", "ROS & ROS2 İÇİN GÖREV SIRALAMASI"))
        item = self.listWidget_3.item(1)
        item.setText(_translate("Form", "1-ROS Çalışmaları -Temel Haberleşme-Arduino ile Haberleşme"))
        item = self.listWidget_3.item(2)
        item.setText(_translate("Form", "2-ROS İle Örnek Haberleşme Uygulamaları"))
        item = self.listWidget_3.item(3)
        item.setText(_translate("Form", "3-ROS2 İçin Çalışmalar"))
        item = self.listWidget_3.item(4)
        item.setText(_translate("Form", "4-Sahte Araç Verileri İle Örnek Arayüz"))
        item = self.listWidget_3.item(5)
        item.setText(_translate("Form", "5-Gerçek Araç Verileri İle Arayüz Oluşturma"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = bilgisayaryap()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
