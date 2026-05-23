Ultimate OXO Game 🎮❌⭕

A network-based multiplayer Tic-Tac-Toe game built with Python and PyQt5.

Project Overview

Ultimate OXO is a two-player network Tic-Tac-Toe game that allows players to connect through a server and play against each other in real time. The project combines socket programming, GUI development, and game logic to create an interactive multiplayer experience.

The backend networking structure and server-side framework were provided. Our contribution focused on designing and developing the final user interface and enhancing the overall gameplay experience in final_oxo_game.py.

Features ✨
Multiplayer gameplay over a local network
Interactive PyQt5 graphical user interface
Real-time game updates between players
Dynamic scoreboard tracking wins for X and O
Dark and light theme switching
Restart and new match functionality
Help screen for user guidance
Connection status updates and game logs
Color-coded game pieces for better visual feedback
Technologies Used 🛠️
Python 3
PyQt5
Socket Programming
Object-Oriented Programming (OOP)
File Structure 📂
Backend / Provided Files

These files were provided as the networking and server framework:

GameIni.py

Contains game constants such as:

Port number
Buffer size
Game name
Board size
GameClient.py

Handles:

Client-side socket communication
Sending and receiving messages
Logging client activity
GameServer.py

Handles:

Server setup
Accepting client connections
Sending and receiving data between players
Server-side logging
OXOGameServer.py

Implements:

Core game server logic
Move validation
Winner detection
Turn switching
Replay handling
Our Contribution 💡

The main work completed by Mukona and Tumisho was the development and enhancement of the final game interface in:

Final_oxo_game.py
Features implemented by us:
Designed and developed the complete GUI using PyQt5
Created the interactive Tic-Tac-Toe board layout
Added a modern game dashboard and interface styling
Implemented:
Scoreboard system
Theme switching (Dark/Light mode)
Help functionality
Restart and New Match controls
Connection interface
Status and game message displays
Added color styling for X and O moves
Improved user interaction and overall gameplay experience
Managed GUI updates based on server messages
Added timers for continuous network checking
Enhanced usability and visual presentation
How the Game Works 🎲
The server is started first using OXOGameServer.py
Two clients run Final_oxo_game.py
Players connect using the server IP address
The server randomly assigns:
Which player starts
Which shape each player receives (X or O)
Players take turns selecting cells
The server validates moves and updates both clients
The game ends when:
A player gets 3 in a row
The board is full (Tie)
Players can restart or disconnect after the match
Running the Project ▶️
Step 1: Start the Server

Run:

python OXOGameServer.py
Step 2: Start the Clients

On two separate devices/windows run:

python Final_oxo_game.py
Step 3: Connect to Server
Enter the server IP address
Click CONNECT
Wait for another player to join
Requirements 📋

Install PyQt5 before running the project:

pip install PyQt5
Learning Outcomes 📚

Through this project we gained practical experience with:

GUI development using PyQt5
Socket programming and networking
Client-server communication
Event-driven programming
Python OOP principles
Real-time multiplayer game design
User experience and interface design
Authors 👩🏽‍💻
Tumisho Bopape
Mukona Gwele
Future Improvements 🚀

Possible future enhancements include:

Online matchmaking
Chat functionality
Sound effects and animations
AI single-player mode
Improved graphics and responsiveness
Persistent player statistics
