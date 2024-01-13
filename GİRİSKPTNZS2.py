
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Kptgrs(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(791, 536)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setStyleSheet("\n"
"/* Ana pencere */\n"
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
"}\n"
"font: 11pt \"Snap ITC\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setStyleSheet("font: 9pt \"Snap ITC\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 4, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 5, 3, 1, 1)
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("\n"
"/* Ana pencere */\n"
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
"}\n"
"font: 11pt \"Snap ITC\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("/* Giriş kutusu üzerine gelindiğinde */\n"
"font: 9pt \"Snap ITC\";\n"
"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.username_input = QtWidgets.QLineEdit(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_input.sizePolicy().hasHeightForWidth())
        self.username_input.setSizePolicy(sizePolicy)
        self.username_input.setText("")
        self.username_input.setObjectName("username_input")
        self.verticalLayout_3.addWidget(self.username_input)
        self.label_6 = QtWidgets.QLabel(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(30, 39, 46))
        gradient.setColorAt(1.0, QtGui.QColor(52, 73, 94))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.label_6.setPalette(palette)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"Snap ITC\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.password_input = QtWidgets.QLineEdit(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_input.sizePolicy().hasHeightForWidth())
        self.password_input.setSizePolicy(sizePolicy)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("password_input")
        self.verticalLayout_3.addWidget(self.password_input)
        self.checkBox = QtWidgets.QCheckBox(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setStyleSheet("font: 9pt \"Snap ITC\";\n"
"color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton.setStyleSheet("font: 9pt \"Snap ITC\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.login_button = QtWidgets.QPushButton(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        self.login_button.setStyleSheet("font: 9pt \"Snap ITC\";\n"
"color: rgb(255, 255, 255);")
        self.login_button.setObjectName("login_button")
        self.verticalLayout_3.addWidget(self.login_button)
        self.gridLayout_2.addWidget(self.widget_3, 3, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 3, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 2, 3, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "KAPTAN GİRİŞİNE HOŞ GELDİNİZ"))
        self.label_5.setText(_translate("Form", "   KULLANICI ADI :"))
        self.label_6.setText(_translate("Form", "   ŞİFRE :"))
        self.checkBox.setText(_translate("Form", " Şifre Göster"))
        self.pushButton.setText(_translate("Form", "ŞİFREMİ UNUTTUM"))
        self.login_button.setText(_translate("Form", "GİRİŞ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Kptgrs()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
