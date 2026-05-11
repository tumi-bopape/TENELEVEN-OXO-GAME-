import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QTimer
from GameClient import * 
from GameIni import *

class TicTacToe(QWidget, GameClient):
    def __init__(self):
        QWidget.__init__(self)
        GameClient.__init__(self)
        
        self.current_theme = "dark"
        self.shape = None  
        self.board = [' '] * BOARD_SIZE
        
        # Win Counters
        self.score_x = 0
        self.score_o = 0
        
        # Setup Timer
        self.network_timer = QTimer()
        self.network_timer.timeout.connect(self.check_network)
        
        self.init_ui()
        self.apply_theme()

    def init_ui(self):
        self.setWindowTitle("Ten Eleven OXO - Ultimate Edition")
        self.setGeometry(250, 250, 900, 650)

        # Labels & Headers
        self.title_label1 = QLabel("ULTIMATE", self)  
        self.title_label1.setFont(QFont("Orbitron", 28, QFont.Bold))
        self.title_label1.setAlignment(Qt.AlignCenter)
        
        self.oxo_label = QLabel(
            "<span style='color:#2323FF;'>----- O </span>"
            "<span style='color:#FF3131;'>X</span>"
            "<span style='color:#2323FF;'> O -----</span>"
        )
        self.oxo_label.setFont(QFont("Montserrat", 15, QFont.Bold))
        self.oxo_label.setAlignment(Qt.AlignCenter)        
        
        self.slogan = QLabel("The Ultimate Tic-Tac-Toe Experience!")
        self.slogan.setFont(QFont("Orbitron", 8, QFont.Bold))
        self.slogan.setAlignment(Qt.AlignCenter)
        
        self.status_label = QLabel("STATUS:", self)
        self.status_label.setFont(QFont("Orbitron", 10, QFont.Bold))
        self.statusbar = QLabel("Disconnected. Enter IP to start.", self)
        self.statusbar.setStyleSheet("font-weight: bold; color: #FFA500;")

        # Networking Section
        self.enterserver = QLineEdit(self)
        self.enterserver.setPlaceholderText(" localhost")
        self.serverbutton = QPushButton("CONNECT", self)
        self.serverbutton.clicked.connect(self.connect_button_clicked)
        
        # Game Info Panel
        self.game_messages = QLabel("GAME LOGS:")
        self.game_messages.setFont(QFont("Orbitron", 10, QFont.Bold))
        self.serveroutput = QLabel("System Ready.", self)
        self.serveroutput.setWordWrap(True)

        # The Game Board
        self.board_buttons = []
        cross_grid = QGridLayout()
        cross_grid.setSpacing(10)
        for i in range(3):
            row = []
            for j in range(3):
                btn = QPushButton("")
                btn.setFixedSize(120, 120)
                btn.setFont(QFont("Arial", 32, QFont.Bold))
                btn.setEnabled(False) 
                btn.clicked.connect(self.grid_button_clicked)
                cross_grid.addWidget(btn, i, j)
                row.append(btn)
            self.board_buttons.append(row)

        grid_wrapper = QHBoxLayout()
        grid_wrapper.addStretch()
        grid_wrapper.addLayout(cross_grid)
        grid_wrapper.addStretch()

        # Control Buttons
        self.newgamebutton = QPushButton("NEW MATCH", self)
        self.newgamebutton.clicked.connect(self.new_game_clicked)
        self.restartbutton = QPushButton("RESTART", self)
        self.restartbutton.clicked.connect(self.restart_clicked)
        self.helpbutton = QPushButton("HELP", self)
        self.helpbutton.clicked.connect(self.show_help_screen)
        self.themebutton = QPushButton("THEME", self)
        self.themebutton.clicked.connect(self.switch_theme)
        self.closebutton = QPushButton("EXIT", self) 
        self.closebutton.clicked.connect(self.close)

        # Score Display
        self.score_display = QLabel("X: 0  |  O: 0")
        self.score_display.setFont(QFont("Orbitron", 16, QFont.Bold))
        self.score_display.setAlignment(Qt.AlignCenter)
        self.score_display.setStyleSheet("color: #FFFFFF; padding: 5px; border: 1px solid #555;")

        # Layouts
        left_panel = QVBoxLayout()
        left_panel.addWidget(self.title_label1)
        left_panel.addWidget(self.oxo_label)
        left_panel.addWidget(self.slogan)
        left_panel.addSpacing(10)
        
        status_box = QHBoxLayout()
        status_box.addStretch()
        status_box.addWidget(self.status_label)
        status_box.addWidget(self.statusbar)
        status_box.addStretch()
        left_panel.addLayout(status_box)
        left_panel.addLayout(grid_wrapper)
        left_panel.addStretch(1)

        right_panel = QVBoxLayout()
        right_panel.addWidget(QLabel("<b>SCOREBOARD:</b>"))
        right_panel.addWidget(self.score_display)
        right_panel.addSpacing(20)
        right_panel.addWidget(QLabel("<b>Server Address:</b>"))
        right_panel.addWidget(self.enterserver)
        right_panel.addWidget(self.serverbutton)
        right_panel.addSpacing(30)
        right_panel.addWidget(self.game_messages)
        right_panel.addWidget(self.serveroutput)
        right_panel.addStretch()

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_panel, 2)
        main_layout.addLayout(right_panel, 1)

        bottom_buttons = QHBoxLayout()
        bottom_buttons.addWidget(self.newgamebutton)
        bottom_buttons.addWidget(self.restartbutton)
        bottom_buttons.addWidget(self.helpbutton)
        bottom_buttons.addWidget(self.themebutton)
        bottom_buttons.addWidget(self.closebutton)

        final_layout = QVBoxLayout()
        final_layout.addLayout(main_layout)
        final_layout.addLayout(bottom_buttons)
        self.setLayout(final_layout)

    def check_network(self):
        try:
            if hasattr(self, 'socket') and self.socket:
                self.socket.setblocking(False)
                msg = self.receive_message()
                if msg:
                    self.handle_message(msg)
        except:
            pass

    def handle_message(self, msg):
        if msg.startswith('new game,'):
            self.shape = msg.split(',')[1]
            self.clear_gui_board()
            self.statusbar.setText(f"ACTIVE: You are {self.shape}")
            self.serveroutput.setText(f"Game session started. Your mark: {self.shape}")
           
        elif msg == 'your move': 
            self.statusbar.setText("IT'S YOUR TURN!")
            self.set_board_enabled(True)
        
        elif msg == 'opponents move':
            self.statusbar.setText("Waiting for opponent...")
            self.set_board_enabled(False)
        
        elif msg.startswith('valid move,'):
            _, shape, pos = msg.split(',')
            r, c = int(pos) // 3, int(pos) % 3
            self.board_buttons[r][c].setText(shape)
            self.board_buttons[r][c].setEnabled(False)
            
            # Apply color based on mark
            color = "#FF3131" if shape == 'X' else "#04D9FF"
            self.board_buttons[r][c].setStyleSheet(f"color: {color}; background-color: rgba(255,255,255,10%); border: 1px solid gray;")
        
        elif msg.startswith('game over,'):
            winner = msg.split(',')[1]
            self.set_board_enabled(False)
            
            if winner == 'T':
                result = "It's a Tie!"
            elif winner == self.shape:
                result = "YOU WIN!"
                if self.shape == 'X': self.score_x += 1
                else: self.score_o += 1
            else:
                result = "YOU LOST!"
                if self.shape == 'X': self.score_o += 1
                else: self.score_x += 1
                
            self.score_display.setText(f"X: {self.score_x}  |  O: {self.score_o}")
            self.statusbar.setText(f"MATCH OVER: {result}")
            self.serveroutput.setText(f"Result: {result}. Press RESTART for another round or NEW MATCH to disconnect.")

    def grid_button_clicked(self):
        sender = self.sender()
        for i in range(3):
            for j in range(3):
                if self.board_buttons[i][j] == sender:
                    self.send_message(str(i * 3 + j))

    def connect_button_clicked(self):
        ip = self.enterserver.text() or "localhost"
        try:
            self.connect_to_server(ip)
            self.network_timer.start(100)
            self.serverbutton.setEnabled(False)
            self.enterserver.setEnabled(False)
            self.statusbar.setText("CONNECTING...")
        except Exception as e:
            self.serveroutput.setText(f"Connection Error: {e}")

    def new_game_clicked(self):
        """Resets scoreboard, clears board, and disconnects."""
        self.clear_gui_board()
        self.score_x = 0
        self.score_o = 0
        self.score_display.setText("X: 0  |  O: 0")
        
        try:
            self.network_timer.stop()
            if hasattr(self, 'socket') and self.socket:
                self.socket.close()
                self.socket = None 
                
            self.statusbar.setText("Disconnected. Enter IP to start.")
            self.serveroutput.setText("Session ended. Scoreboard reset.")
            self.serverbutton.setEnabled(True)
            self.enterserver.setEnabled(True)
        except Exception as e:
            self.serveroutput.setText(f"Reset Error: {e}")

    def restart_clicked(self):     
        self.clear_gui_board()
        try: self.send_message('y')
        except: self.serveroutput.setText("Not connected to a server.")

    def clear_gui_board(self):
        for i in range(3):
            for j in range(3):
                self.board_buttons[i][j].setText("")
                self.board_buttons[i][j].setEnabled(False)
                # Keep the buttons visible against the background
                self.board_buttons[i][j].setStyleSheet("background-color: rgba(255,255,255,5%); border: 1px solid #444;")

    def set_board_enabled(self, status):
        for i in range(3):
            for j in range(3):
                if self.board_buttons[i][j].text() == "":
                    self.board_buttons[i][j].setEnabled(status)
                    if status:
                        self.board_buttons[i][j].setStyleSheet("background-color: rgba(255,255,255,15%); border: 1px solid #888;")

    def show_help_screen(self):
        self.serveroutput.setText("HELP: Connect to a server, wait for your turn, and click an empty cell. 3 in a row wins!")

    def switch_theme(self):
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        self.apply_theme()

    def apply_theme(self):
        if self.current_theme == "dark":
            bg, text, btn_box = "#002147", "white", "#004488"
            self.closebutton.setStyleSheet("background-color:#aa3333; color:white;")
        else:
            bg, text, btn_box = "#f0f0f0", "#111111", "#d0d0d0"
            self.closebutton.setStyleSheet("background-color:#ff6666; color:black;")
        
        self.setStyleSheet(f"background-color: {bg}; color: {text};")
        self.serveroutput.setStyleSheet(f"background-color: {btn_box}; border: 1px solid gray; padding: 10px; border-radius: 5px; color: {text};")
        self.score_display.setStyleSheet(f"color: {text}; border: 1px solid gray; padding: 5px;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec_())
