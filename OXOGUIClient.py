from GameClient import *
import sys,random 
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import Qt 

class OXOGUIClient(GameClient, QWidget):

    def __init__(self):
        GameClient.__init__(self)
        QWidget.__init__(self)
        self.board = [' '] * BOARD_SIZE
        self.shape = None
        
        self.setWindowTitle("Ten Eleven Games")
        self.setGeometry(250,50,200,150)
        
        ### Creating the GUI for the game:
        
        # Creating the game labels 
        self.title_label1 = QLabel("ULTIMATE", self)  
        self.title_label1.setFont(QFont("Orbitron", 28,QFont.Bold ))
        self.title_label1.setStyleSheet("color: white;")
        
        
        self.oxo_label = QLabel(
            "<span style='color:#2323FF;'>----- O </span>"
            "<span style='color:#FF3131;'>X</span>"
            "<span style='color:#2323FF;'> O -----</span>"
        )
        self.oxo_label.setFont(QFont("Montserrat", 15, QFont.Bold))
        self.oxo_label.setAlignment(Qt.AlignCenter)        
        
                
        self.slogan= QLabel("The Ultimate Tic-Tac-Toe Experience!")
        self.slogan.setFont(QFont("Orbitron", 8,QFont.Bold ))
        self.slogan.setStyleSheet("color: white;")
                
        
        self.info=QLabel("Click on a cell to make your move")
        self.info2=QLabel("Example: 192.168.1.10")
        
        self.status_label = QLabel("Status:",self)
        self.status_label.setFont(QFont("Orbitron",8,QFont.Bold))
        self.status_label.setStyleSheet("color:white;")
                
        self.server_label = QLabel("Enter server:", self)
        self.server_label.setFont(QFont("Arial", 8 ,QFont.Bold ))
        self.server_label.setStyleSheet("color: white;")              
    
        
        self.player = QLabel("Players")
        self.player.setFont(QFont("Arial", 8 ,QFont.Bold ))
        self.player.setStyleSheet("color: white;")        
        
        self.player1= QLabel("Player 1",self)
        self.player2 = QLabel("Player 2",self)    
        
        self.identify1 = QLabel("You",self)
        self.identify2 = QLabel("Opponent",self)
        
        self.player_design_labelX = QLabel("", self)
        self.player_design_labelO = QLabel("",self)          
        
        self.game_messages =  QLabel("Game Messages:")
        self.game_messages.setFont(QFont("Arial", 8 ,QFont.Bold ))
        self.game_messages.setStyleSheet("color: white;")              
        
        #Creating the game buttons 
        self.closebutton= QPushButton("EXIT",self) 
        self.closebutton.clicked.connect(self.cancel_clicked)
        self.closebutton.setStyleSheet("background-color:red; color:white;")
        
        self.newgamebutton= QPushButton("NEW GAME", self)
        self.newgamebutton.clicked.connect(self.new_game_button_clicked)
        self.newgamebutton.setStyleSheet("background-color:green; color:white;")
        
        self.serverbutton =QPushButton("CONNECT", self)
        self.serverbutton.clicked.connect(self.connect_button_clicked)
        self.serverbutton.setStyleSheet("background-color:blue; color:white;")
        
        self.restartbutton =QPushButton("RESTART",self)
        self.restartbutton.clicked.connect(self.restart_button_clicked)
        self.restartbutton.setStyleSheet("background-color:grey; color:white;")
        
        #Creating text spaces 
        self.enterserver =QLineEdit(self)
        self.enterserver.setStyleSheet("background-color:#002147;")
        self.enterserver.setFixedSize(150,25)
        self.serveroutput= QLabel("",self)
        self.serveroutput.setStyleSheet("background-color:#002147;")
        self.serveroutput.setFixedSize(180,25)
        self.statusbar = QLabel("",self)
        self.statusbar.setStyleSheet("background-color:#002147;")

        #Creating the board space 
        cross_grid = QGridLayout()
        cross_grid.setHorizontalSpacing(5)
        cross_grid.setVerticalSpacing(5) 
        
        for i in range(0,3):
            for j in range(0,3):
                self.button = QPushButton("")
                self.button.setFixedSize(80,80)
                self.button.setStyleSheet("background-color:#002147;")
                self.button.clicked.connect(self.grid_button_clicked)
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
        grid_widget1.setPalette(QPalette(QColor('#003153')))
        grid_widget1.setAutoFillBackground(True)
        
        #Players panel
        grid2 = QGridLayout()
        grid2.addWidget(self.player, 0,0)
        grid2.addWidget(self.player1,1,0)
        grid2.addWidget(self.player2,2,0)
        grid2.addWidget(Xlab, 1,1)
        grid2.addWidget(Olab, 2,1)
        grid2.addWidget(self.identify1, 1,2)
        grid2.addWidget(self.identify2, 2,2)
        grid_widget2=QWidget()
        grid_widget2.setLayout(grid2)
        grid_widget2.setPalette(QPalette(QColor('#003153')))
        grid_widget2.setAutoFillBackground(True)
        
        #Game messages panel 
        grid3= QGridLayout()
        grid3.addWidget(self.game_messages, 0,0)
        grid3.addWidget(self.serveroutput,1,0)
        grid_widget3= QWidget()
        grid_widget3.setLayout(grid3)
        grid_widget3.setPalette(QPalette(QColor('#003153')))
        grid_widget3.setAutoFillBackground(True)
        
        #Combined game panel grid 
        vbox = QVBoxLayout()
        vbox.addWidget(grid_widget1)
        vbox.addWidget(grid_widget2)
        vbox.addWidget(grid_widget3) 
        vbox_widget =QWidget()
        vbox_widget.setLayout(vbox)        
        vbox_widget.setFixedWidth(260)
        
        #creating the left panel 
        grid4 = QGridLayout()
        grid4.addWidget(self.title_label1,0,1)
        grid4.addWidget(self.oxo_label,1,1)
        grid4.addWidget(self.slogan,2,1)
        grid4.addWidget(self.status_label, 3,0)
        grid4.addWidget(self.statusbar, 3,1)
        grid_widget4 =QWidget()
        grid_widget4.setLayout(grid4)
        
        vbox2 = QVBoxLayout()
        vbox2.addWidget(grid_widget4)
        vbox2.addWidget(cross_gridWidget)
        vbox2.addWidget(self.info)
        vbox2_widget = QWidget()
        vbox2_widget.setLayout(vbox2)
        vbox2_widget.setPalette(QPalette(QColor('#003153')))
        vbox2_widget.setAutoFillBackground(True)    
        
        hbox = QHBoxLayout() 
        hbox.addWidget(vbox2_widget)
        hbox.addWidget(vbox_widget)
        hbox_widget= QWidget()
        hbox_widget.setLayout(hbox)
        hbox_widget.setPalette(QPalette(QColor('#002147')))
        hbox_widget.setAutoFillBackground(True)        
                
        #Buttons Panel 
        Hbox = QHBoxLayout()
        Hbox.addWidget(self.newgamebutton)
        Hbox.addWidget(self.restartbutton)
        Hbox.addWidget(self.closebutton)
        Hbox_widget = QWidget()
        Hbox_widget.setLayout(Hbox)
        Hbox_widget.setPalette(QPalette(QColor('#003153')))
        Hbox_widget.setAutoFillBackground(True)  
        
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
        self.IP = self.enterserver.text()
        self.connect_to_server(self.IP)
        self.play_loop()
         
                
    def restart_button_clicked(self):
            print("Restart button was clicked") 
            
    def cancel_clicked(self): 
        self.close()     
    
    def clear_board(self):
        self.board = [' '] * BOARD_SIZE

# The job of display board is to update the board.
    def display_on_board(self):   
        pass 
    
    def handle_message(self,msg):
         if msg.startswith('new game,'):
            self.shape = msg.split(',')[1] #SPLIT THE STRING AS A LIST AND USE THE INDEX 1
            self.clear_board()
            print(f"\n New Game! You are playing as {self.shape}")
            self.display_board()
           
        elif msg == 'your move': 
            print("It's your turn!")
            move = self.input_move()
            self.send_message(move)
        
        elif msg == 'opponents move':
            print("Waiting for opponent's move...")
        
        elif msg == 'invalid move':
            print("Invalid move! That position is taken or out of range.")
        
        elif msg.startswith('valid move,'):
            parts = msg.split(',')
            shape = parts[1] 
            position = int(parts[2])
            self.board[position] = shape
            self.display_board()
        
        elif msg.startswith('game over,'):
            winner = msg.split(',')[1]
            self.display_board()
            if winner == 'X':
                print("Game Over! X wins!")
                if self.shape == 'X':
                    print("You won!")
                else:
                    print("You lost!")
            elif winner == 'O':
                print("Game Over! O wins!")
                if self.shape == 'O':
                    print("You won!")
                else:
                    print("You lost!")
            else:  
                print("Game Over! It's a tie!")
        
        elif msg == 'play again':
                play_again = self.input_play_again()
                if play_again == 'y':
                    self.send_message('y')
                else:
                    self.send_message('n')
          
        elif msg == 'exit game':
                print("Game exiting...")
                self.socket.close()
            
        else:
            print(f"Received unknown message: {msg}")
        
    
    def play_loop(self):
        while True:
            msg = self.receive_message()
            if len(msg): self.handle_message(msg)
            break
            
def main():
        
    app = QApplication(sys.argv)
    game = OXOGUIClient()
    game.show()
    sys.exit(app.exec_())
main()
