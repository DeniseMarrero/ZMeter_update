from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import serial.tools.list_ports

class Ui_MainWindow(object):
    def get_serialInfo(self, MainWindow):
        self.ports = [port[0] for port in serial.tools.list_ports.comports()]
        self.list_ports.addItems(self.ports)
        self.list_ports.setCurrentRow(0)        

    def OpenSerial(self):
        self.com = self.list_ports.currentItem().text()
        try:
            self.ser = serial.Serial(self.com, baudrate = 115200, timeout=None)
            print('Connected to:' , self.ser.name)
        except Exception as error:
            print('exception: opening serial port: ' + str(error))

        if self.ser.isOpen():
            read_data = self.ser.read_all()
            print("Data recieved:",read_data)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_connect = QtWidgets.QPushButton(self.centralwidget)
        self.button_connect.setGeometry(QtCore.QRect(100, 250, 461, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_connect.sizePolicy().hasHeightForWidth())
        self.button_connect.setSizePolicy(sizePolicy)
        self.button_connect.setMinimumSize(QtCore.QSize(60, 20))
        self.button_connect.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";")
        self.button_connect.setObjectName("button_connect")
        self.text_portsavailable = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_portsavailable.setGeometry(QtCore.QRect(100, 50, 461, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_portsavailable.sizePolicy().hasHeightForWidth())
        self.text_portsavailable.setSizePolicy(sizePolicy)
        self.text_portsavailable.setMinimumSize(QtCore.QSize(110, 22))
        self.text_portsavailable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_portsavailable.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";")
        self.text_portsavailable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_portsavailable.setLineWidth(0)
        self.text_portsavailable.setObjectName("text_portsavailable")
        self.list_ports = QtWidgets.QListWidget(self.centralwidget)
        self.list_ports.setGeometry(QtCore.QRect(100, 110, 461, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_ports.sizePolicy().hasHeightForWidth())
        self.list_ports.setSizePolicy(sizePolicy)
        self.list_ports.setMinimumSize(QtCore.QSize(170, 110))
        self.list_ports.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.list_ports.setLineWidth(0)
        self.list_ports.setObjectName("list_ports")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.button_connect.clicked.connect(self.OpenSerial)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZMeter APP 2.0 l IMB-CNM"))
        self.button_connect.setText(_translate("MainWindow", "Conectar"))
        self.text_portsavailable.setPlainText(_translate("MainWindow", "Puertos disponibles: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.get_serialInfo(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
