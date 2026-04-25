import sys, random
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ten Eleven OXO Game")
        self.setGeometry(250,250,200, 150)
        
        # Creating the game labels 
        self.title_label = QLabel("ULTIMATE OXO GAME", self)   
        self.slogan= QLabel("The Ultimate Tic-Tac-Toe Experience")
        self.info=QLabel("Click on a cell to make your move")
        self.info2=QLabel("Example: 192.168.1.10")
        
        self.server_label = QLabel("Enter server:", self)
    
        
        self.player = QLabel("PLAYERS")
        self.player1= QLabel("Player 1",self)
        self.player2 = QLabel("Player 2",self)    
        
        self.player_design_labelX = QLabel("", self)
        self.player_design_labelO = QLabel("",self)          
        
        self.game_messages =  QLabel("GAME MESSSAGES")
        
        #Creating the game buttons 
        self.closebutton= QPushButton("EXIT",self) 
        self.closebutton.clicked.connect(self.cancel_clicked)
        
        self.newgamebutton= QPushButton("NEW GAME", self)
        self.newgamebutton.clicked.connect(self.new_game_button_clicked)
        
        self.serverbutton =QPushButton("CONNECT", self)
        self.serverbutton.clicked.connect(self.connect_button_clicked)
        
        self.restartbutton =QPushButton("RESTART",self)
        self.restartbutton.clicked.connect(self.restart_button_clicked)
        
        #Creating text spaces 
        self.enterserver =QLineEdit(self)
        self.serveroutput= QLabel("",self)
       

        #Creating the board space 
        cross_grid = QGridLayout()
        for i in range(0,3):
            for j in range(0,3):
                self.button = QPushButton("")
                self.button.clicked.connect(self.button_clicked)
                cross_grid.addWidget(self.button,i,j)
        cross_gridWidget = QWidget()
        cross_gridWidget.setLayout(cross_grid)
       
       
        
        #Creating the X and O images 
        Xlab = QLabel() 
        Olab = QLabel() 
        cross = QPixmap("cross.gif")
        naught =QPixmap("nought.gif")
        Xlab.setPixmap(cross)
        Olab.setPixmap(naught)
       
       #Creating layout for the right panel 
       
        # Server panel 
       
        grid1 = QGridLayout() 
        grid1.addWidget(self.server_label,0,0)
        grid1.addWidget(self.enterserver,1,0)
        grid1.addWidget(self.serverbutton,1,1)
        grid1.addWidget(self.info2,2,0)
        grid_widget1=QWidget()
        grid_widget1.setLayout(grid1)
        
        #Players panel
        grid2 = QGridLayout()
        grid2.addWidget(self.player, 0,0)
        grid2.addWidget(self.player1,1,0)
        grid2.addWidget(self.player2,2,0)
        grid2.addWidget(Xlab, 1,1)
        grid2.addWidget(Olab, 2,1)
        grid_widget2=QWidget()
        grid_widget2.setLayout(grid2)
        
        #Game messages panel 
        grid3= QGridLayout()
        grid3.addWidget(self.game_messages, 0,0)
        grid3.addWidget(self.serveroutput,1,0)
        grid_widget3= QWidget()
        grid_widget3.setLayout(grid3)
    
        
        #Combined game panel grid 
        vbox = QVBoxLayout()
        vbox.addWidget(grid_widget1)
        vbox.addWidget(grid_widget2)
        vbox.addWidget(grid_widget3) 
        vbox_widget =QWidget()
        vbox_widget.setLayout(vbox)        
        
        #creating the left panel 
        
        grid4 = QGridLayout()
        grid4.addWidget(self.title_label,0,1)
        grid4.addWidget(self.slogan,1,1)
        grid_widget4 =QWidget()
        grid_widget4.setLayout(grid4)
        
        vbox2 = QVBoxLayout()
        vbox2.addWidget(grid_widget4)
        vbox2.addWidget(cross_gridWidget)
        vbox2_widget = QWidget()
        vbox2_widget.setLayout(vbox2)
        
        
        hbox = QHBoxLayout() 
        hbox.addWidget(vbox2_widget)
        hbox.addWidget(vbox_widget)
        hbox_widget= QWidget()
        hbox_widget.setLayout(hbox)
          
        #Buttons Panel 
        Hbox = QHBoxLayout()
        Hbox.addWidget(self.newgamebutton)
        Hbox.addWidget(self.restartbutton)
        Hbox.addWidget(self.closebutton)
        Hbox_widget = QWidget()
        Hbox_widget.setLayout(Hbox)
        
        #Putting everything together 
        Final_vbox = QVBoxLayout()
        Final_vbox.addWidget(hbox_widget)
        Final_vbox.addWidget(Hbox_widget)
        self.setLayout(Final_vbox)
        
    def grid_button_clicked(self):
            print("Grid button was clicked")
        
    def new_game_button_clicked(self):
            print("New game button was clicked")     
    
    def connect_button_clicked(self):
            print("Connect button was clicked") 

    def restart_button_clicked(self):
            print("Restart button was clicked") 
            
    def cancel_clicked(self): 
        self.close()     
    
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec_())
        
