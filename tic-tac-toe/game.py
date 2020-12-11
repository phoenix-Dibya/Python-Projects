from player import Human,Computer
import time
class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)] #represent 3*3 board in list
        self.current_winner = None #keep track of current winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    #check for available spaces to move
    def available_moves(self):
        return[i for i,spot in enumerate(self.board) if spot ==  ' ']
        # moves = []
        #  for i,spot in enumerate(self.board):
        #     if spot == ' ':
        #          moves.append(i)
        #  return move
    def empty_square(self):
        return " " in self.board

    def non_empty_square(self):
        return len(self.available_moves())

    def make_move(self, square,letter):
        if self.board[square] == ' ':
            self.board[square] = letter 
            if self.winner(square,letter):
                self.current_winner = letter
            return True 
        return False
    def winner(self, square,letter):
        #winner if 3 in row anywhere
        # check for row
        row_ind = square//3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        #check for columns
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check for diagonals
        if square%2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]#left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i]
                         for i in [2, 4, 6]]  # left to right diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        #if these check fail
        return False

def play(game,x_player,o_player,print_game = True):
    if print_game:
        game.print_board_nums()

    letter ='X'

    while game.empty_square():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square,letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')
        
        if game.current_winner:
            if print_game:
                print(letter + 'wins the game.')
            return letter
            #after we made our move, we need to alternate letters
        letter = "O" if letter == 'X' else 'X'
        time.sleep(1)
    if print_game:
        print('It\'s a tie.')

if __name__ == '__main__':
    x_player = Human('X')
    o_player = Computer('O')
    t = TicTacToe()
    play(t,x_player,o_player,print_game=True)

