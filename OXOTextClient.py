from GameClient import *
import sys 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import*


class OXOTextClient(GameClient):

    def __init__(self):
        GameClient.__init__(self)
        self.board = [' '] * BOARD_SIZE
        self.shape = None
        
    def clear_board(self):
        self.board = [' '] * BOARD_SIZE
        
    def input_server(self):
        return input('enter server:')
     
    def input_move(self):
        return input('enter move(0-8):')
     
    def input_play_again(self):
        return input('play again(y/n):')
    
    
    def TicTacToe(QWidget):
        pass 
    

    def display_board(self):
        pass 
            
        

    def ok(self):
            pass


    def new_game(self):
        self.history_text = ""
        self.history.setText("")
        self.input.clear()
        self.btn_guess.setEnabled(True)

    
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
            else: break
            
def main():
    otc = OXOTextClient()
    while True:
        try:
            otc.connect_to_server(otc.input_server())
            break
        except:
            print('Error connecting to server!')
    otc.play_loop()
    input('Press click to exit.')

    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec_())