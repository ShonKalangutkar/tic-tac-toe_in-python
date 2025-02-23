class TicTacToe:
    def __init__(self):
        self.board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        self.current_player = "X"
        self.winner = None
        self.game_running = True

    def print_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def player_input(self):
        while True:
            inp = int(input(f"Player {self.current_player}, enter a number (1-9): "))
            if 1 <= inp <= 9 and self.board[inp - 1] == "-":
                self.board[inp - 1] = self.current_player
                break
            else:
                print("This spot is already taken or out of range. Try again.")

    def check_horizontal(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[3] == self.board[4] == self.board[5] and self.board[3] != "-":
            self.winner = self.board[3]
            return True
        elif self.board[6] == self.board[7] == self.board[8] and self.board[6] != "-":
            self.winner = self.board[6]
            return True
        return False

    def check_row(self):
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != "-":
            self.winner = self.board[1]
            return True
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != "-":
            self.winner = self.board[2]
            return True
        return False

    def check_diagonal(self):
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[2] == self.board[4] == self.board[6] and self.board[2] != "-":
            self.winner = self.board[2]
            return True
        elif self.board[6] == self.board[4] == self.board[2] and self.board[6] != "-":
            self.winner = self.board[2]
            return True
        return False

    def check_tie(self):
        if "-" not in self.board:
            self.print_board()
            print("It's a tie!")
            self.game_running = False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        if self.check_diagonal() or self.check_horizontal() or self.check_row():
            self.print_board()
            print(f"The winner is {self.winner}!")
            self.game_running = False

    def play_game(self):
        while self.game_running:
            self.print_board()
            self.player_input()
            self.check_win()
            self.check_tie()
            if self.game_running:
                self.switch_player()

# Run the game
game = TicTacToe()
game.play_game()
