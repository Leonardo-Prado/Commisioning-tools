from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,args):
        self.Network_Scan(MainWindow,args)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NetWork Tools", None))
        self.actionNetwork_Scan.setText(QCoreApplication.translate("MainWindow", u"Network Scan", None))
        self.actionModbus_client.setText(QCoreApplication.translate("MainWindow", u"Modbus Client", None))
        self.actionModbus_Server.setText(QCoreApplication.translate("MainWindow", u"Modbus Server", None))
        self.btnStartScan.setText(QCoreApplication.translate("MainWindow", u"Start Scan", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Host Name", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"MAC", None))
        self.menuFun_o.setTitle(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00e3o", None))
    # retranslateUi

    def Network_Scan(self,MainWindow,args):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(926, 396) #Size of main window
        
        #Menu action
        self.actionNetwork_Scan = QAction(MainWindow)
        self.actionNetwork_Scan.setObjectName(u"actionNetwork_Scan")
        self.actionModbus_client = QAction(MainWindow)
        self.actionModbus_client.setObjectName(u"actionModbus_client")
        self.actionModbus_Server = QAction(MainWindow)
        self.actionModbus_Server.setObjectName(u"actionModbus_Server")

        #Widget principal
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        #Frame de scanner
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 841, 81))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        #Layout do frame de scanner
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 611, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        #TextEdit de start ip do frame de scanner
        self.edStartIP = QTextEdit(self.horizontalLayoutWidget)
        self.edStartIP.setObjectName(u"textEdit_2")
        self.horizontalLayout.addWidget(self.edStartIP)
        #TextEdit de end ip do frame de scanner
        self.edEndIP = QTextEdit(self.horizontalLayoutWidget)
        self.edEndIP.setObjectName(u"textEdit_3")
        self.horizontalLayout.addWidget(self.edEndIP)
        #Botao de scanner
        self.btnStartScan = QPushButton(self.horizontalLayoutWidget)
        self.btnStartScan.setObjectName(u"pushButton")
        self.btnStartScan.clicked.connect(lambda : self.getScanData( args[0](self.edStartIP.toPlainText(),self.edEndIP.toPlainText())))#Callback onclick
        self.horizontalLayout.addWidget(self.btnStartScan)

        #Frame de resultado
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 130, 911, 211))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 909, 209))
        #Tabela de resultado
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setColumnWidth(0, 130)
        self.tableWidget.setColumnWidth(1, 80)  
        self.tableWidget.setColumnWidth(2, 250)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 891, 191))
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        #Menubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 926, 21))
        self.menuFun_o = QMenu(self.menubar)
        self.menuFun_o.setObjectName(u"menuFun_o")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFun_o.menuAction())
        self.menuFun_o.addAction(self.actionNetwork_Scan)
        self.menuFun_o.addSeparator()
        self.menuFun_o.addAction(self.actionModbus_client)
        self.menuFun_o.addAction(self.actionModbus_Server)

        self.retranslateUi(MainWindow)
        self.actionNetwork_Scan.triggered.connect(self.Network_Scan)
        self.actionModbus_client.triggered.connect(self.Modbus_Client)
        self.actionModbus_Server.triggered.connect(self.Modbus_Server)
        QMetaObject.connectSlotsByName(MainWindow)

    def Modbus_Client(self):
        print("Modbus Client")

    def Modbus_Server(self):
        pass

    def getScanData(self,IPs):
        self.tableWidget.setRowCount(0)
        for ip in IPs:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            numcols = self.tableWidget.columnCount()
            numrows = self.tableWidget.rowCount()           
            self.tableWidget.setRowCount(numrows)
            self.tableWidget.setColumnCount(numcols) 
            if ip.status == "up":
                icon = QIcon(QPixmap("./icons/network_up.png"))
            elif ip.status == "down":
                icon = QIcon(QPixmap("./icons/network_down.png"))
            else:
                icon = QIcon(QPixmap("./icons/network.png"))  
            icon_status = QTableWidgetItem()
            icon_status.setIcon(icon)

            self.tableWidget.setItem(numrows -1,0,QTableWidgetItem(ip.ip))
            self.tableWidget.setItem(numrows -1,1,icon_status)
            self.tableWidget.item(numrows -1,1)
            self.tableWidget.setItem(numrows -1,2,QTableWidgetItem(ip.hostname))        
            self.tableWidget.setItem(numrows -1,3,QTableWidgetItem(ip.mac_address))     