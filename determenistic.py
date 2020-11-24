from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox,QLabel,QToolTip,QDesktopWidget,QMainWindow,QStatusBar,QHBoxLayout,QVBoxLayout,QColorDialog
import sys
from PySide2.QtGui import QIcon,QPixmap,QFont,QGuiApplication,Qt,QColor
import matplotlib.colors as myColor
import MainWindow
from PySide2.QtWidgets import QRadioButton,QTextEdit
import main
import deterministic_graph
class DeterministicScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Deterministic Queue')
        self.setGeometry(150,150,1000,600)
        self.setFixedSize(1000,600)

        self.center()
        self.setIcon()

        self.initUi()

        self.createBackArrow()

        self.initUi()




    def showDeterministicGraph(self):
        self.dete_graph=deterministic_graph.DeterministicGraphScreen()
        self.dete_graph.show()


    def handleSubmit(self):
        self.drawButton.setVisible(True)
        self.resultLabel.setVisible(True)

    def initUi(self):
        
        self.lambdaLabel=QLabel('λ : ',self)
        self.lambdaLabel.setFont(QFont('Sanserif',16))
        self.lambdaLabel.move(100,100)
        self.lambdaLabel.adjustSize()
        
        self.lambdaQEditText=QTextEdit(self)
        self.lambdaQEditText.setGeometry(130,90,200,50)
        self.lambdaQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        self.lambdaQEditText.setFont(QFont('Sanserif',13))
        self.lambdaQEditText.setAlignment(Qt.AlignCenter)
        self.lambdaQEditText.setPlaceholderText('enter the arrival rate..')
        self.lambdaQEditText.setTextColor(QColor(255, 0, 0))
        


        
        self.meoLabel=QLabel('μ : ',self)
        self.meoLabel.setFont(QFont('Sanserif',16))
        self.meoLabel.move(600,100)
        self.meoLabel.adjustSize()
        
        self.meoQEditText=QTextEdit(self)
        self.meoQEditText.setGeometry(630,90,200,50)
        self.meoQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        self.meoQEditText.setFont(QFont('Sanserif',13))
        self.meoQEditText.setAlignment(Qt.AlignCenter)
        self.meoQEditText.setPlaceholderText('enter the service rate..')
        self.meoQEditText.setTextColor(QColor(0, 0, 255))



        self.nServersLabel=QLabel('n : ',self)
        self.nServersLabel.setFont(QFont('Sanserif',16))
        self.nServersLabel.move(350,200)
        self.nServersLabel.adjustSize()
        
        self.nServersQEditText=QTextEdit(self)
        self.nServersQEditText.setGeometry(380,190,200,50)
        self.nServersQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        self.nServersQEditText.setFont(QFont('Sanserif',13))
        self.nServersQEditText.setAlignment(Qt.AlignCenter)
        self.nServersQEditText.setPlaceholderText('enter the servers number..')
        self.nServersQEditText.setTextColor(QColor(0, 255, 0))


        self.timeLabel=QLabel('t : ',self)
        self.timeLabel.setFont(QFont('Sanserif',16))
        self.timeLabel.move(100,300)
        self.timeLabel.adjustSize()
        
        self.timeQEditText=QTextEdit(self)
        self.timeQEditText.setGeometry(130,290,200,50)
        self.timeQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        self.timeQEditText.setFont(QFont('Sanserif',13))
        self.timeQEditText.setAlignment(Qt.AlignCenter)
        self.timeQEditText.setPlaceholderText('enter the time..')
        self.timeQEditText.setTextColor(QColor(255, 0, 0))


        self.capacityLabel=QLabel('k-1 : ',self)
        self.capacityLabel.setFont(QFont('Sanserif',16))
        self.capacityLabel.move(600,300)
        self.capacityLabel.adjustSize()
        
        self.capacityQEditText=QTextEdit(self)
        self.capacityQEditText.setGeometry(630,290,200,50)
        self.capacityQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        self.capacityQEditText.setFont(QFont('Sanserif',13))
        self.capacityQEditText.setAlignment(Qt.AlignCenter)
        self.capacityQEditText.setPlaceholderText('enter the Capacity..')
        self.capacityQEditText.setTextColor(QColor(0, 0, 255))

        
        self.alreadyPresentpeopleLabel=QLabel('M : ',self)
        self.alreadyPresentpeopleLabel.setFont(QFont('Sanserif',16))
        self.alreadyPresentpeopleLabel.move(350,400)
        self.alreadyPresentpeopleLabel.adjustSize()
        
        self.alreadyPresentpeopleQEditText=QTextEdit(self)
        self.alreadyPresentpeopleQEditText.setGeometry(380,390,200,50)
        self.alreadyPresentpeopleQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        self.alreadyPresentpeopleQEditText.setFont(QFont('Sanserif',13))
        self.alreadyPresentpeopleQEditText.setAlignment(Qt.AlignCenter)
        self.alreadyPresentpeopleQEditText.setPlaceholderText('enter the peresent people..')
        self.alreadyPresentpeopleQEditText.setTextColor(QColor(0, 255, 0))


        self.submitButton = QPushButton('Submit',self)
        self.submitButton.setFont(QFont('Sanserif',14))
        self.submitButton.setStyleSheet('color:white;background-color:firebrick;border: 0px solid; border-radius:15px')
        self.submitButton.move((self.width()/2)-50,460)
        self.submitButton.clicked.connect(self.handleSubmit)
        

        #out Label................

        self.resultLabel = QLabel('The number of customers in the system is: and the waiting time is: ',self)
        self.resultLabel.setFont(QFont('Sanserif',14))
        self.resultLabel.setStyleSheet('color:magenta')
        self.resultLabel.adjustSize()
        self.resultLabel.setVisible(False)
        self.resultLabel.move((self.width()/2)-250,500)

        self.drawButton = QPushButton('Draw',self)
        self.drawButton.setFont(QFont('Sanserif',14))
        self.drawButton.setStyleSheet('color:white;background-color:dodgerblue;border: 0px solid; border-radius:15px')
        self.drawButton.move((self.width()/2)-50,550)
        self.drawButton.setVisible(False)
        self.drawButton.clicked.connect(self.showDeterministicGraph)

        










    

    def createBackArrow(self):
        icon1=QIcon('arrow_back.png')
        label1=QLabel('Sample',self)
        pixmap1=icon1.pixmap(20,20,QIcon.Active,QIcon.On)
        label1.setPixmap(pixmap1)
        label1.move(25,25)
        label1.adjustSize()
        label1.mousePressEvent=self.arrowbackClicked

    def arrowbackClicked(self,event):
        print('arrow back clicked')
        self.main=main.MainWindow()
        self.main.show()
        self.destroy()










    def center(self):
        qRect=self.frameGeometry()
        centerpoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerpoint)
        self.move(qRect.topLeft())


    def setIcon(self):
        appIcon=  QIcon('line.png')
        self.setWindowIcon(appIcon)  

    def closeEvent(self,event):
        userInfo = QMessageBox.question(self,'Closing ?','Do u want to quit ?',QMessageBox.Yes|QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            event.accept()
            self.close()
            #sys.exit(QApplication(sys.argv).exec_())                   
            
        elif userInfo == QMessageBox.No:
            event.ignore()       
    
