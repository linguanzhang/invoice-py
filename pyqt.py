from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow,QLineEdit,QPushButton,QLabel,QDialog
lis=[32104015,1615274,0000000]

app = QApplication([])
def check_ans(target,digits):
    times=10**digits
    for num in lis:
        if(target==num%times):
            return True
    return False
def bonus(p):
    if p==3:
        return 200
    elif p==4:
        return 1000
    elif p==5:
        return 4000
    elif p==6:
        return 10000
    elif p==7:
        return 40000
    elif p==8:
        return 200000

    
  
class Ui(QMainWindow):
    def __init__(self):
        
        super(Ui, self).__init__()
        uic.loadUi('gui.ui', self)
        self.status_jackpot=False
        self.lineEdit=self.findChild(QLineEdit,'lineEdit')
        self.button=self.findChild(QPushButton,'pushButton')
        self.button.clicked.connect(self.actiongo)
        
        self.button_2=self.findChild(QPushButton,'pushButton_2')
        self.button_2.clicked.connect(self.target)
        self.label_input=self.findChild(QLabel, 'label')
    
        
        
        
    def target(self):
        dig=Ui_untitled(self)
        result=dig.exec()
        if (result ==True):
            print('ok')
            print(dig.lineEdit_3.text())
            print(dig.lineEdit_5.text())
            print(dig.lineEdit_6.text())
        else:
            print('cancel')
    def showUp(self):
        self.show()
    
    def change(self):
        dlg = Ui_untitled(self)
        dlg.show()
    def actiongo(self):
        
        print (self.lineEdit.text())
        if self.status_jackpot==False:
            
            if check_ans(int(self.lineEdit.text()),3):
                dlg = Ui_dialog(self)
                dlg.show()
                self.label_input.setText("輸入完整發票號碼")
                self.status_jackpot=True
            else:
                self.label.setText("沒中")
        else:
            print('完整')
            status=True
            p=4

            
              
class Ui_dialog(QDialog):
    def __init__(self, parent = None):
        super(Ui_dialog, self).__init__(parent)
        uic.loadUi('./dialog.ui', self)
        self.label_4 = self.findChild(QLabel, 'label_4')
        self.lineEdit_2=self.findChild(QLineEdit,'lineEdit_2')
        self.button=self.findChild(QPushButton,'pushButton_2')
        self.button.clicked.connect(self.check_fullans)

    def check_fullans(self):
        p = 4
        status = True
        while status:
            print(p)
            times = 10 ** p
            target = int(self.lineEdit_2.text()) % times
            if check_ans(target, p):
                print('恭喜中獎', p)

                if p == 8:
                    status = False
                    money = bonus(8)
                    self.label_4.setText("恭喜中" + str(money) + "元")
                p = p + 1
            else:
                money = bonus(p - 1)
                self.label_4.setText("恭喜中" + str(money) + "元")

                print("沒中獎")
                status = False

class Ui_untitled(QDialog):
    def __init__(self, parent = None):
        super(Ui_untitled, self).__init__(parent)
        uic.loadUi('untitled.ui', self)
        
        self.lineEdit_3=self.findChild(QLineEdit,'lineEdit_3')
        self.lineEdit_5=self.findChild(QLineEdit,'lineEdit_5')
        self.lineEdit_6=self.findChild(QLineEdit,'lineEdit_6')



        
    
        
        

    
        
        
ui = Ui()
ui.showUp()

app.exec()
