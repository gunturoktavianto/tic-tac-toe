import tkinter #tk-interface (graphical user interface library)

def set_tile(row, column):
    global curr_player
    global curr_player_text

    if (game_over):
        return

    if board[row][column]["text"] != "":
        #already taken spot
        return
    
    board[row][column]["text"] = curr_player #mark the board

    if curr_player == playerO: #switch player
        curr_player = playerX
        curr_player_text = player1
    else:
        curr_player = playerO
        curr_player_text = player2

    
    label["text"] = curr_player_text+"'s turn"

    #check winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    #horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            if board[row][0]["text"] == "X":
                label.config(text=player1 + " is the winner!", foreground=color_yellow)
            elif board[row][0]["text"] == "O":
                label.config(text=player2 + " is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
    
    #vertically, check 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            if board[0][column]["text"] == "X":
                label.config(text = player1 +" is the winner!", foreground=color_yellow)
            elif board[0][column]["text"] == "O":
                label.config(text = player2 +" is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
    
    #diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        if board[0][0]["text"] == "X":
            label.config(text= player1 +" is the winner!", foreground=color_yellow)
        elif board[0][0]["text"] == "O":
            label.config(text= player2 +" is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    #anti-diagionally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):

        if board[0][2]["text"] == "X":
            label.config(text= player1 +" is the winner!", foreground=color_yellow)
        if board[0][2]["text"] == "O":
            label.config(text= player2 +" is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return
    
    #tie
    if (turns == 9):
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)


def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text=curr_player_text+"'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)


#game setup
playerX = "X"
playerO = "O"

curr_player = playerX

player1 = "Rhyver"
player2 = "Jees"

curr_player_text = player1

board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0
game_over = False

#window setup
window = tkinter.Tk() #create the game window
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player_text+"'s turn", font=("Consolas", 20), background=color_gray,
                      foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_gray, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="restart", font=("Consolas", 20), background=color_gray,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

#center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()