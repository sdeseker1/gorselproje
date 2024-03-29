# Form implementation generated from reading ui file 'kaptangiriszs2.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class kaptansec(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(837, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(471, 0))
        self.label.setStyleSheet("font: 15pt \"Snap ITC\";\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("font: 10pt \"Snap ITC\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("font: 10pt \"Snap ITC\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("font: 10pt \"Snap ITC\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("font: 10pt \"Snap ITC\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet("font: 10pt \"Snap ITC\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "     Yapmak İstediğiniz İşlemi Seçin"))
        self.pushButton.setText(_translate("Form", "Üye işlemleri"))
        self.pushButton_2.setText(_translate("Form", "Bilgisayar Bİrimine Git"))
        self.pushButton_3.setText(_translate("Form", "Elektirik Birimine Git"))
        self.pushButton_4.setText(_translate("Form", "Mekanik Birimine Git"))
        self.pushButton_5.setText(_translate("Form", "Sponsor Birimine Git"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = kaptansec()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
