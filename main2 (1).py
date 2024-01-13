import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit,QMainWindow,QTableWidgetItem, QVBoxLayout, QPushButton
from PyQt6 import QtWidgets
from PyQt6.QtGui import QStandardItem,QStandardItemModel, QFont
from giris2zs import Ui_Form
from kaptangiriszs2 import kaptansec
from GİRİSKPTNZS2 import Kptgrs
from anasayfaaZS3 import Uyeekle
from kaptanbirimsecimi import tkmkptnbr
from üyebirimsecimİ import üyebirimsecim
from bilgisayarkptnilkgiriszs2 import bilgr
from uyebilgisayargiris import x
from uyeelektirikgiris import uyeee
from uyemekanikgiris import uyemakina
from uyesponsorgiris import uyess
from mekanikyapılacaklar import mekanikyap
from ELEKTRİRİKYAPILACAKLAR2 import elektirikyap
from SPONSORYAP import sponsoryap
from kaptanlarıslem import islemkaptan
from BİLGİSAYARYAPILACAKLAR2 import bilgisayaryap
import sil
from SİFREMİ2 import sifremiunuttum


from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl

import pymongo
import random
import string
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl

from PyQt6.QtMultimediaWidgets import QVideoWidget

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["DUSCART"]
        self.collection = self.db["users"]
        
        
        self.pushButton_4= None
        self.show_password_checkbox = None
        self.password = None
        self.username = None
        self.ui_login = None
        self.init_ui()
    
    
    def init_ui(self):
        self.ui_login = Ui_Form()
        self.ui_login.setupUi(self)
        self.loginbutton_6 = self.ui_login.pushButton_6
        self.login_buton3=self.ui_login.pushButton_7
        self.login_buton2=self.ui_login.pushButton_8
        self.login_buton2.clicked.connect(self.yeniac)
        self.loginbutton_6.clicked.connect(self.takimkaptanbirimsec)
        self.login_buton3.clicked.connect(self.uyebrsec)
        

    def yeniac(self):
        self.window=QWidget()
        self.ui=Kptgrs()
        self.ui.setupUi(self.window)
        self.login_button = self.ui.login_button
        self.show_checkBox = self.ui.checkBox
        self.pushButtonkaptansifreunuttum=self.ui.pushButton
        self.ui.login_button.clicked.connect(self.login)
        self.ui.password_input.returnPressed.connect(self.login)
        self.ui.checkBox.stateChanged.connect(self.toggle_pwd_visibility)
        self.pushButtonkaptansifreunuttum.clicked.connect(self.sifremiunuttumsayfa)
        self.window.show()
        


    def login(self):
       # if self.ui.username_input.text() == "B1" and self.ui.password_input.text() == "zeynep":
        self.username = self.ui.username_input.text()
        self.password = self.ui.password_input.text()
        if self.collection.find_one({"username": self.username,"password": self.password, "type": "kaptan"}):
            QMessageBox.information(self, 'Başarılı', 'Giriş Başarılı')
            self.yniac()
        
            

            
        else:
            QMessageBox.information(self, 'Başarısız', 'Giriş Başarısız Yeniden Giriş Yapınız')
            self.init_ui() 
         
            
        
            return
       
            
        
            
        
    def toggle_pwd_visibility(self):
        if self.show_checkBox.isChecked():
            self.ui.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.password_input.setEchoMode(QLineEdit.EchoMode.Password)
    def yniac(self):
        self.window=QWidget()
        self.kp=kaptansec()
        self.kp.setupUi(self.window)
        self.loginbuttonkp2 = self.kp.pushButton_2
        self.login_buttonkp3 = self.kp.pushButton_3
        self.login_buttonkp4 = self.kp.pushButton_4
        self.login_buttonkp5 = self.kp.pushButton_5
        self.login_buttonkp= self.kp.pushButton
        self.login_buttonkp.clicked.connect(self.uyeekleme)
        self.login_buttonkp4.clicked.connect(self.mekanik_yap)
        self.login_buttonkp3.clicked.connect(self.elektirik_yap)
        self.login_buttonkp5.clicked.connect(self.sponsor_yap)
        self.loginbuttonkp2.clicked.connect(self.bilgisayar_yap)
        self.window.show()
    def uyeekleme(self):
        self.window=QWidget()
        self.ue=Uyeekle()
        self.ue.setupUi(self.window)
        
        self.btnEkle=self.ue.btnEkle
        
        self.btnSil=self.ue.btnSil
        
        self.adedit=self.ue.lineEdit
        self.soyadedit=self.ue.lineEdit_2
        self.numara=self.ue.lineEdit_3
        self.takvim=self.ue.calendarWidget_2
        self.tablo=self.ue.tableWidget_2
        self.bolumu=self.ue.listWidget_2
        self.combobox=self.ue.comboBox
        self.btnEkle.clicked.connect(self.kayitEkle)
        self.btnSil.clicked.connect(self.kayitSil)
        self.user_data_list = list(self.collection.find())

        for row, user_data in enumerate(reversed(self.user_data_list)):
            self.tablo.insertRow(row)
            for col, key in enumerate(["adi", "soyadi", "cinsiyet", "bolum", "username", "password"]):  
                if key in user_data:  # Anahtar mevcutsa
                    item = QtWidgets.QTableWidgetItem(str(user_data[key]))  # Anahtara göre değeri al
                    self.tablo.setItem(row, col, item)

        self.window.show()

    def kayitEkle(self):
        self.kullaniciGirisi=self.ue.lineEdit_3.text().strip()
        self.kullaniciSoyadi=self.ue.lineEdit_2.text().strip()
        self.kullaniciAdi=self.ue.lineEdit.text().strip()
        self.cinsiyet=self.ue.comboBox.currentText()
        self.bolum=self.ue.listWidget_2.selectedItems()[0].text()
        self.dogumTarihi = self.ue.calendarWidget_2.selectedDate().toString("dd-MM-yyyy")
        print(self.kullaniciAdi, self.kullaniciSoyadi, self.kullaniciGirisi, self.cinsiyet, self.bolum, self.dogumTarihi)
        randomPassword = ""
        charList = string.punctuation + string.ascii_lowercase + string.ascii_uppercase + string.digits
        for i in range(5):
            randomPassword += random.choice(charList)
        self.kullaniciTablosu = self.ue.tableWidget_2
        self.kullaniciTablosu.insertRow(0)
        self.kullaniciTablosu.setItem(0, 0, QTableWidgetItem(self.kullaniciAdi))
        self.kullaniciTablosu.setItem(0, 1, QTableWidgetItem(self.kullaniciSoyadi))
        self.kullaniciTablosu.setItem(0, 2, QTableWidgetItem(self.cinsiyet))
        self.kullaniciTablosu.setItem(0, 3, QTableWidgetItem(self.bolum))
        self.kullaniciTablosu.setItem(0, 4, QTableWidgetItem(self.kullaniciGirisi))
        self.kullaniciTablosu.setItem(0, 5, QTableWidgetItem(randomPassword))

        user_data = {
            'username':self.kullaniciGirisi,
            'password':randomPassword,
            'type': 'uye',
            'adi':self.kullaniciAdi,
            'soyadi':self.kullaniciSoyadi,
            'cinsiyet':self.cinsiyet,
            'bolum':self.bolum,
            'dogum tarihi':self.dogumTarihi
          }

              # Belgeyi 'users' koleksiyonuna ekle
        self.collection.insert_one(user_data)
    def kayitSil(self):
        self.kullaniciGirisi=self.ue.lineEdit_3.text().strip()

        if self.kullaniciGirisi:
            result = self.collection.delete_one({'username': self.kullaniciGirisi})

            if result.deleted_count > 0:
                print(f"{result.deleted_count} kayıt silindi.")
                self.kullaniciTablosu = self.ue.tableWidget_2
                # PyQt tablosundan da ilgili satırı kaldır
                for row in range(self.kullaniciTablosu.rowCount()):
                    if self.kullaniciTablosu.item(row, 4).text() == self.kullaniciGirisi:
                        self.kullaniciTablosu.removeRow(row)
                        break
        
    def takimkaptanbirimsec(self):
        self.window=QWidget()
        self.tkm_kptnbr=tkmkptnbr()
        self.tkm_kptnbr.setupUi(self.window)
        self.elektirikbrpushButton=self.tkm_kptnbr.elektirikbrpushButton
        self.mekanikbrpushButton=self.tkm_kptnbr.mekanikbrpushButton
        self.sponsorbrpushButton=self.tkm_kptnbr.sponsorbrpushButton
        self.bilgisayarbrpushButton=self.tkm_kptnbr.bilgisayarbrpushButton
        self.bilgisayarbrpushButton.clicked.connect(self.kpilkgirisbil)
        self.elektirikbrpushButton.clicked.connect(self.kpilkgirisbil)
        self.mekanikbrpushButton.clicked.connect(self.kpilkgirisbil)
        self.sponsorbrpushButton.clicked.connect(self.kpilkgirisbil)
        self.window.show()
    def kaptanislemleri(self):
        self.window=QWidget()
        self.takimkaptani_islem=islemkaptan()
        self.takimkaptani_islem.setupUi(self.window)
        self.pushButton=self.takimkaptani_islem.pushButton
        self.label=self.takimkaptani_islem.label
        self.pushButton_2=self.takimkaptani_islem.pushButton_2
        self.pushButton.clicked.connect(self.uyeekleme)
        self.pushButton_2.clicked.connect(self.ozelsayfa)
        
        self.window.show()
    
    def ozelsayfa(self):
       user_data = self.collection.find_one({"username": self.loginbilgusername})
    
       if user_data["type"] == "bkaptan":
        self.bilgisayar_yap()
       elif user_data["type"] == "mkaptan":
        self.mekanik_yap()
       elif user_data["type"] == "ekaptan":
        self.elektirik_yap()
       elif user_data["type"] =="skaptan":
        self.sponsor_yap()
        
     
    def kpilkgirisbil(self):
        self.window=QtWidgets.QWidget()
        self.giris_takim_kaptani=bilgr()
        self.giris_takim_kaptani.setupUi(self.window)
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["DUSCART"]
        self.collection = self.db["users"]
        
        self.login_button_2=self.giris_takim_kaptani.login_button_2
        self.checkBox_3=self.giris_takim_kaptani.checkBox_3
        self.pushButtonkaptansponsor=self.giris_takim_kaptani.pushButtonkaptansponsor
       
        self.pushButtonkaptansponsor.clicked.connect(self.sifremiunuttumsayfa)
        self.giris_takim_kaptani.login_button_2.clicked.connect(self.loginbilg)
        self.giris_takim_kaptani.password_input_2.returnPressed.connect(self.loginbilg)
        self.giris_takim_kaptani.checkBox_3.stateChanged.connect(self.toggle_pwd_visibility_bilg)
        
        self.window.show()
    def loginbilg(self):
        #if self.giris_takim_kaptani.username_input_2.text() == "c1" and self.giris_takim_kaptani.password_input_2.text() == "zeynep":
        self.loginbilgusername = self.giris_takim_kaptani.username_input_2.text()
        if self.collection.find_one({"username": self.loginbilgusername,"password": self.giris_takim_kaptani.password_input_2.text(),  "type": {"$in": ["bkaptan", "mkaptan","skaptan","ekaptan"]}}):
            QMessageBox.information(self, 'Başarılı', 'Giriş Başarılı')
            self.kaptanislemleri()
           
            
        else:
            QMessageBox.information(self, 'Başarısız', 'Giriş Başarısız Yeniden Giriş Yapınız')
            
        
            return
    def toggle_pwd_visibility_bilg(self):
        if self.checkBox_3.isChecked():
            self.giris_takim_kaptani.password_input_2.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.giris_takim_kaptani.password_input_2.setEchoMode(QLineEdit.EchoMode.Password)

        

    def uyebrsec(self):
        self.window=QWidget()
        self.üye_br=üyebirimsecim()
        self.üye_br.setupUi(self.window)
        self.uyeelektirikbrpushButton=self.üye_br.uyeelektirikbrpushButton
        self.uyemekanikbrpushButton=self.üye_br.uyemekanikbrpushButton
        self.uyebilgisayarbrpushButton=self.üye_br.uyebilgisayarbrpushButton
        self.uyesponsorbrpushButton=self.üye_br.uyesponsorbrpushButton
        self.uyebilgisayarbrpushButton.clicked.connect(self.uyebilgisayaragit)
        self.uyeelektirikbrpushButton.clicked.connect(self.uyeelektirigeagit)
        self.uyemekanikbrpushButton.clicked.connect(self.uyemekanikegit)
        self.uyesponsorbrpushButton.clicked.connect(self.uyesponsoragit)
      
        self.window.show()
    def uyebilgisayaragit(self):
        self.window=QtWidgets.QWidget()
        self.computer=x()
        self.computer.setupUi(self.window)
        self.login_button_UYEbb=self.computer.login_button_UYEbb
        self.password_input_UYEbb=self.computer.password_input_UYEbb
        self.pushButtonbb=self.computer.pushButtonbb
        self.checkBox_UYEbb=self.computer.checkBox_UYEbb
        self.username_input_UYEbb=self.computer.username_input_UYEbb
        self.pushButtonbb.clicked.connect(self.sifremiunuttumsayfa)
        self.computer.login_button_UYEbb.clicked.connect(self.uyebilg)
        self.computer.password_input_UYEbb.returnPressed.connect(self.uyebilg)
        self.computer.checkBox_UYEbb.stateChanged.connect(self.toggle_pwd_visibility_bilguye)
        self.window.show()
    def uyebilg(self):
        try:
            username_input_UYEbb=self.computer.username_input_UYEbb.text().strip()
            password_input_UYEbb=self.computer.password_input_UYEbb.text().strip()
            user = self.collection.find_one({"username": username_input_UYEbb, "password": password_input_UYEbb, "bolum": "BİLGİSAYAR"})
            if user:
                QMessageBox.information(self, 'Başarılı', 'Giriş Başarılı')
                self.bilgisayar_yap()
            else:
                QMessageBox.information(self, 'Başarısız', 'Giriş Başarısız Yeniden Giriş Yapınız')
        except Exception as e:
            print("Hata Oluştu:", e)
        
            return
    def toggle_pwd_visibility_bilguye(self):
        if self.checkBox_UYEbb.isChecked():
            self.computer.password_input_UYEbb.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.computer.password_input_UYEbb.setEchoMode(QLineEdit.EchoMode.Password)
        self.window.show()
    def bilgisayar_yap(self):
        self.window=QtWidgets.QWidget()
        self.yapılacaklarbb=bilgisayaryap()
        self.yapılacaklarbb.setupUi(self.window)
        self.bbx=self.yapılacaklarbb.listWidget
        self.bby=self.yapılacaklarbb.listWidget_2
        self.bbz=self.yapılacaklarbb.listWidget_4
        self.bbt=self.yapılacaklarbb.listWidget_5
        self.bbk=self.yapılacaklarbb.label
        self.bbl=self.yapılacaklarbb.gridLayout
        self.bbm=self.yapılacaklarbb.gridLayout_2
        self.bbu=self.yapılacaklarbb.gridLayout_3
        self.bbo=self.yapılacaklarbb.gridLayout_4
        self.bbe=self.yapılacaklarbb.gridLayout_5
        self.bbq=self.yapılacaklarbb.gridLayout_6
        self.window.show()
    def uyeelektirigeagit(self):
        self.window=QtWidgets.QWidget()
        self.computeree=uyeee()
        self.computeree.setupUi(self.window)
        self.login_button_UYEee=self.computeree.login_button_UYEee
        self.password_input_UYEee=self.computeree.password_input_UYEee.text().strip()
        self.pushButtonee=self.computeree.pushButtonee
        self.checkBox_UYEee=self.computeree.checkBox_UYEee
        self.username_input_UYEee=self.computeree.username_input_UYEee.text().strip()
        self.computeree.login_button_UYEee.clicked.connect(self.uyebilgelektirik)
        self.computeree.password_input_UYEee.returnPressed.connect(self.uyebilgelektirik)
        self.computeree.checkBox_UYEee.stateChanged.connect(self.toggle_pwd_visibility_bilelektirik) 
        self.pushButtonee.clicked.connect(self.sifremiunuttumsayfa)
        self.window.show()
    def uyebilgelektirik(self):
        try:
            username_input_UYEee=self.computeree.username_input_UYEee.text().strip()
            password_input_UYEee=self.computeree.password_input_UYEee.text().strip()
            user = self.collection.find_one({"username": username_input_UYEee, "password": password_input_UYEee, "bolum": "ELEKTRİK"})
            if user:
                QMessageBox.information(self, 'Başarılı', 'Giriş Başarılı')
                self.elektirik_yap()
            else:
                QMessageBox.information(self, 'Başarısız', 'Giriş Başarısız Yeniden Giriş Yapınız')
        except Exception as e:
            print("Hata Oluştu:", e)

            
    def toggle_pwd_visibility_bilelektirik(self):
        if self.checkBox_UYEee.isChecked():
            self.computeree.password_input_UYEee.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.computeree.password_input_UYEee.setEchoMode(QLineEdit.EchoMode.Password)
        self.window.show()
    def elektirik_yap(self):
        self.window=QtWidgets.QWidget()
        self.yapılacaklaree=elektirikyap()
        self.yapılacaklaree.setupUi(self.window)
        self.eex=self.yapılacaklaree.listWidget
        
        self.pushButtonplayer1=self.yapılacaklaree.pushButton
        self.pushButtonplayer2=self.yapılacaklaree.pushButton_2
        self.pushButtonplayer3=self.yapılacaklaree.pushButton_3
        self.pushButtonplayer4=self.yapılacaklaree.pushButton_4
        self.pushButtonplayer1.clicked.connect(self.yerlesiksarjplayer)
        self.eey=self.yapılacaklaree.listWidget_2
        self.eez=self.yapılacaklaree.listWidget_4
        self.eet=self.yapılacaklaree.listWidget_5
        self.eek=self.yapılacaklaree.label
        self.eel=self.yapılacaklaree.gridLayout
        self.eem=self.yapılacaklaree.gridLayout_2
        self.eeu=self.yapılacaklaree.gridLayout_3
        self.eeo=self.yapılacaklaree.gridLayout_4
        self.eee=self.yapılacaklaree.gridLayout_5
        self.eeq=self.yapılacaklaree.gridLayout_6
        self.window.show()
    def yerlesiksarjplayer(self):
        self.setWindowTitle("Video Oynatıcı")
        self.setGeometry(100, 100, 640, 480)

        self.media_player = QMediaPlayer()
        self.video_widget = QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setSource(QUrl("file:///C:/Users/90507/Desktop/zss2/myvideo.mp4"))
        self.audio = QAudioOutput()
        self.media_player.setAudioOutput(self.audio)
        self.audio.setVolume(50)

        self.pause_button = QPushButton()
        self.pause_button.setText("||")
        font = QFont("Arial", 25)
        self.pause_button.setFont(font)
        self.pause_button.clicked.connect(self.toggle_video)

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addWidget(self.pause_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.media_player.play()

    def toggle_video(self):
        if self.media_player.isPlaying():
            self.media_player.pause()
        else:
            self.media_player.play()


    def uyemekanikegit(self):
        self.window=QtWidgets.QWidget()
        self.computermm=uyemakina()
        self.computermm.setupUi(self.window)
        self.login_button_UYEmm=self.computermm.login_button_UYEmm
        self.password_input_UYEmm=self.computermm.password_input_UYEmm
        self.pushButtonmm=self.computermm.pushButtonmm
        self.checkBox_UYEmm=self.computermm.checkBox_UYEmm
        self.username_input_UYEmm=self.computermm.username_input_UYEmm
        self.computermm.login_button_UYEmm.clicked.connect(self.uyebilgmm)
        self.computermm.password_input_UYEmm.returnPressed.connect(self.uyebilgmm)
        self.computermm.checkBox_UYEmm.stateChanged.connect(self.toggle_pwd_visibility_bilgmm)
        self.pushButtonmm.clicked.connect(self.sifremiunuttumsayfa)
        
        self.window.show()
    def uyebilgmm(self):
        try:
            username_input_UYEmm=self.computermm.username_input_UYEmm.text().strip()
            password_input_UYEmm=self.computermm.password_input_UYEmm.text().strip()
            user = self.collection.find_one({"username": username_input_UYEmm, "password": password_input_UYEmm, "bolum": "MEKANİK"})
            if user:
                QMessageBox.information(self, 'Başarılı', 'Giriş Başarılı')
                self.mekanik_yap()
            else:
                QMessageBox.information(self, 'Başarısız', 'Giriş Başarısız Yeniden Giriş Yapınız')
        except Exception as e:
            print("Hata Oluştu:", e)
    def toggle_pwd_visibility_bilgmm(self):
        if self.checkBox_UYEmm.isChecked():
            self.computermm.password_input_UYEmm.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.computermm.password_input_UYEmm.setEchoMode(QLineEdit.EchoMode.Password)
        self.window.show()
    def mekanik_yap(self):
        self.window=QtWidgets.QWidget()
        self.yapılacaklarmm=mekanikyap()
        self.yapılacaklarmm.setupUi(self.window)
        self.x=self.yapılacaklarmm.listWidget
        self.y=self.yapılacaklarmm.listWidget_2
        self.z=self.yapılacaklarmm.listWidget_4
        self.t=self.yapılacaklarmm.listWidget_5
        self.k=self.yapılacaklarmm.label
        self.l=self.yapılacaklarmm.gridLayout
        self.m=self.yapılacaklarmm.gridLayout_2
        self.u=self.yapılacaklarmm.gridLayout_3
        self.o=self.yapılacaklarmm.gridLayout_4
        self.e=self.yapılacaklarmm.gridLayout_5
        self.q=self.yapılacaklarmm.gridLayout_6
        self.window.show()
    def uyesponsoragit(self):
        self.window=QtWidgets.QWidget()
        self.computerss=uyess()
        self.computerss.setupUi(self.window)
        self.login_button_UYEss=self.computerss.login_button_UYEss
        self.password_input_UYEss=self.computerss.password_input_UYEss
        self.pushButtonss=self.computerss.pushButtonss
        self.checkBox_UYEss=self.computerss.checkBox_UYEss
        self.username_input_UYEss=self.computerss.username_input_UYEss
        self.computerss.login_button_UYEss.clicked.connect(self.uyebilgss)
        self.computerss.password_input_UYEss.returnPressed.connect(self.uyebilgss)
        self.computerss.checkBox_UYEss.stateChanged.connect(self.toggle_pwd_visibility_bilgss)
        self.pushButtonss.clicked.connect(self.sifremiunuttumsayfa)
        self.window.show()
    def uyebilgss(self):
        try:
            username_input_UYEss=self.computerss.username_input_UYEss.text().strip()
            password_input_UYEss=self.computerss.password_input_UYEss.text().strip()
            user = self.collection.find_one({"username": username_input_UYEss, "password": password_input_UYEss, "bolum": "SPONSOR"})
            if user:
                QMessageBox.information(self, 'Başarılı', 'Giriş Başarılı')
                self.sponsor_yap()
            else:
                QMessageBox.information(self, 'Başarısız', 'Giriş Başarısız Yeniden Giriş Yapınız')
        except Exception as e:
            print("Hata Oluştu:", e)
    def toggle_pwd_visibility_bilgss(self):
        if self.checkBox_UYEss.isChecked():
            self.computerss.password_input_UYEss.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.computerss.password_input_UYEss.setEchoMode(QLineEdit.EchoMode.Password)
        self.window.show()

    def sponsor_yap(self):
        self.window=QtWidgets.QWidget()
        self.yapılacaklarss=sponsoryap()
        self.yapılacaklarss.setupUi(self.window)
        self.ssx=self.yapılacaklarss.listWidget
        self.ssy=self.yapılacaklarss.listWidget_2
        self.ssd=self.yapılacaklarss.label
        self.sst=self.yapılacaklarss.listWidget_5
        self.ssk=self.yapılacaklarss.horizontalLayout
        self.ssl=self.yapılacaklarss.gridLayout
        self.ssm=self.yapılacaklarss.gridLayout_2
        self.sss=self.yapılacaklarss.widget
        self.sso=self.yapılacaklarss.gridLayout_4
        self.sse=self.yapılacaklarss.gridLayout_5
        self.window.show()
    def sifremiunuttumsayfa(self):
        self.window=QtWidgets.QWidget()
        self.sifreunut=sifremiunuttum()
        self.sifreunut.setupUi(self.window)
        self.pushButtonsifre=self.sifreunut.pushButton
        self.lineEditsifre=self.sifreunut.lineEdit
        self.window.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w_login = Main()
    w_login.show()
    app.exec()
