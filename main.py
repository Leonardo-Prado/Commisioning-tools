import sys
from gui.main_window import *
from network_tools.network_scan import *
window = None
def main(args=None):
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window,args)
    window.show()
    sys.exit(app.exec_())

def scan(start_ip,end_ip):
    n = NetworkScan(start_ip,end_ip)
    n.scan_network()
    return n.get_ip_address_list()

if __name__ == "__main__":
    args = (scan,)
    main(args)
    
