import random


class TicTacToeWithAi:

    def __init__(self):
        self.user_input = "         "
        self.count = 0

    def cells_input(self):
        self.user_input = input()

    def replace_character_move(self, x, y, user_move):
        char_pos = self.coord_to_field(x, y)
        self.user_input = self.user_input[:char_pos] + user_move + self.user_input[char_pos + 1:]

    def replace_character(self, char_pos, user_move):
        self.user_input = self.user_input[:char_pos] + user_move + self.user_input[char_pos + 1:]

    def replace_character_o(self, x, y):
        char_pos = self.coord_to_field(x, y)
        new_string = "O"
        self.user_input = self.user_input[:char_pos] + new_string + self.user_input[char_pos + 1:]

    def max(self):  # O player
        max_v = -2
        px = None
        py = None

        result = self.win_check()

        if result == "X wins!":
            return -1, 0, 0
        elif result == "O wins!":
            return 1, 0, 0
        elif result == "Draw!":
            return 0, 0, 0

        for i in range(1, 3):
            for j in range(1, 3):
                index = self.coord_to_field(i, j)
                if self.user_input[index] == " ":
                    self.replace_character_move(i, j, "O")
                    (m, min_i, min_j) = self.min()
                    if m > max_v:
                        max_v = m
                        px = i
                        py = j
                    self.replace_character_move(i, j, " ")
        return max_v, px, py

    def min(self):  # X player

        min_v = 2
        qx = None
        qy = None

        result = self.win_check()

        if result == "X wins!":
            return -1, 0, 0
        elif result == "O wins!":
            return 1, 0, 0
        elif result == "Draw!":
            return 0, 0, 0

        for i in range(1, 3):
            for j in range(1, 3):
                index = self.coord_to_field(i, j)
                if self.user_input[index] == " ":
                    self.replace_character_move(i, j, "X")
                    (m, max_i, max_j) = self.max()
                    if m < min_v:
                        min_v = m
                        qx = i
                        qy = j
                    self.replace_character_move(i, j, " ")

        return min_v, qx, qy

    def coord_to_field(self, x, y):
        if x == 1 and y == 1:
            return 6
        elif x == 2 and y == 1:
            return 7
        elif x == 3 and y == 1:
            return 8
        elif x == 1 and y == 2:
            return 3
        elif x == 1 and y == 3:
            return 0
        elif x == 2 and y == 2:
            return 4
        elif x == 3 and y == 2:
            return 5
        elif x == 2 and y == 3:
            return 1
        elif x == 3 and y == 3:
            return 2

    def is_input_valid(self, x, y):
        x = int(x)
        y = int(y)

        if type(x) is not int and type(y) is not int:
            print("You should enter numbers!")
            return False
        elif 1 > x or x > 3 or 1 > y or y > 3:
            print("Coordinates should be from 1 to 3!")
            return False
        elif self.user_input[self.coord_to_field(x, y)] == "X" or self.user_input[self.coord_to_field(x, y)] == "O":
            print("This cell is occupied! Choose another one!")
            return False
        else:
            return True

    def computer_move_easy_o(self):

        x = random.randint(1, 3)
        y = random.randint(1, 3)
        while self.user_input[self.coord_to_field(x, y)] == "X" or self.user_input[self.coord_to_field(x, y)] == "O":
            # print('Making move level "easy"')
            x = random.randint(1, 3)
            y = random.randint(1, 3)

        self.replace_character_o(x, y)
        print('Making move level "easy"')
        self.print_field()

    def computer_move_easy_x(self):

        x = random.randint(1, 3)
        y = random.randint(1, 3)
        while self.user_input[self.coord_to_field(x, y)] == "X" or self.user_input[self.coord_to_field(x, y)] == "O":
            # print('Making move level "easy"')
            x = random.randint(1, 3)
            y = random.randint(1, 3)

        self.replace_character_move(x, y, "X")
        print('Making move level "easy"')
        self.print_field()

    def computer_move_medium_x(self):
        win_poss = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]
        user_move = "X"
        opponent_move = "O"
        if self.user_input.count(user_move) >= 2 or self.user_input.count(opponent_move) >= 2:
            if self.potential_winner(user_move):
                return True
            elif self.potential_loser(opponent_move, user_move):
                return True
            else:
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                while self.user_input[self.coord_to_field(x, y)] == "X" or self.user_input[self.coord_to_field(x, y)] == "O":
                    x = random.randint(1, 3)
                    y = random.randint(1, 3)

                self.replace_character_move(x, y, "X")
                print('Making move level "medium"')
                self.print_field()
        else:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            while self.user_input[self.coord_to_field(x, y)] == "X" or self.user_input[self.coord_to_field(x, y)] == "O":
                x = random.randint(1, 3)
                y = random.randint(1, 3)

            self.replace_character_move(x, y, "X")
            print('Making move level "medium"')
            self.print_field()

    def computer_move_medium_o(self):
        win_poss = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]
        user_move = "O"
        opponent_move = "X"
        if self.user_input.count(user_move) >= 2 or self.user_input.count(opponent_move) >= 2:
            if self.potential_winner(user_move):
                return True
            elif self.potential_loser(opponent_move, user_move):
                return True
            else:
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                while self.user_input[self.coord_to_field(x, y)] == "X" or self.user_input[self.coord_to_field(x, y)] == "O":
                    x = random.randint(1, 3)
                    y = random.randint(1, 3)

                self.replace_character_move(x, y, "O")
                print('Making move level "medium"')
                self.print_field()
        else:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            while self.user_input[self.coord_to_field(x, y)] == "X" or self.user_input[self.coord_to_field(x, y)] == "O":
                x = random.randint(1, 3)
                y = random.randint(1, 3)

            self.replace_character_move(x, y, "O")
            print('Making move level "medium"')
            self.print_field()

    def computer_move_hard_x(self):
        m, x, y = self.min()
        if x is None or y is None:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            while self.user_input[self.coord_to_field(x, y)] == "X" or self.user_input[self.coord_to_field(x, y)] == "O":
                x = random.randint(1, 3)
                y = random.randint(1, 3)

            self.replace_character_move(x, y, "X")
            print('Making move level "hard"')
            self.print_field()
        else:
            self.replace_character_move(x, y, "X")
            print('Making move level "hard"')
            self.print_field()

    def computer_move_hard_o(self):
        m, x, y = self.max()
        if x is None or y is None:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            while self.user_input[self.coord_to_field(x, y)] == "X" or self.user_input[self.coord_to_field(x, y)] == "O":
                x = random.randint(1, 3)
                y = random.randint(1, 3)

            self.replace_character_move(x, y, "O")
            print('Making move level "hard"')
            self.print_field()
        else:
            self.replace_character_move(x, y, "O")
            print('Making move level "hard"')
            self.print_field()

    def user_move_x(self):
        print("Enter the coordinates: ")
        x, y = input().split()
        while not self.is_input_valid(x, y):
            print("Enter the coordinates: ")
            x, y = input().split()
        x = int(x)
        y = int(y)

        self.replace_character_move(x, y, "X")
        self.print_field()

    def user_move_o(self):
        print("Enter the coordinates: ")
        x, y = input().split()
        while not self.is_input_valid(x, y):
            print("Enter the coordinates: ")
            x, y = input().split()
        x = int(x)
        y = int(y)

        self.replace_character_o(x, y)
        self.print_field()

    def print_field(self):

        print("---------")
        print("| {} {} {} |".format(self.user_input[0], self.user_input[1], self.user_input[2]))
        print("| {} {} {} |".format(self.user_input[3], self.user_input[4], self.user_input[5]))
        print("| {} {} {} |".format(self.user_input[6], self.user_input[7], self.user_input[8]))
        print("---------")

    def potential_winner(self, user_move):
        win_poss = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]
        for win_line in win_poss:
            if self.user_input[win_line[0]] == self.user_input[win_line[1]] == user_move:
                self.replace_character(2, user_move)
                return True
            elif self.user_input[win_line[0]] == self.user_input[win_line[2]] == user_move:
                self.replace_character(1, user_move)
                return True
            elif self.user_input[win_line[1]] == self.user_input[win_line[2]] == user_move:
                self.replace_character(0, user_move)
                return True
            else:
                return False

    def potential_loser(self, opponent_move, user_move):
        win_poss = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]
        for win_line in win_poss:
            if self.user_input[win_line[0]] == self.user_input[win_line[1]] == opponent_move:
                self.replace_character(2, user_move)
                return True
            elif self.user_input[win_line[0]] == self.user_input[win_line[2]] == opponent_move:
                self.replace_character(1, user_move)
                return True
            elif self.user_input[win_line[1]] == self.user_input[win_line[2]] == opponent_move:
                self.replace_character(0, user_move)
                return True
            else:
                return False

    def win_check(self):
        win_poss = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]

        for win_line in win_poss:
            if self.user_input[win_line[0]] == self.user_input[win_line[1]] == \
                    self.user_input[win_line[2]] == "X":
                print("X wins")
                return "X wins"
            elif self.user_input[win_line[0]] == self.user_input[win_line[1]] == \
                    self.user_input[win_line[2]] == "O":
                print("O wins")
                return "O wins"
        if self.count == 9:  # or "_" not in self.user_input:
            print("Draw")
            return "Draw"

        return "Game not finished"

    def main_menu(self):
        input_command = input("Input command: ")
        if input_command == "start easy easy":  # computer vs computer
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.computer_move_easy_x()
                    count += 1

                else:
                    self.computer_move_easy_o()
                    count += 1
                self.count += 1
        elif input_command == "start user easy":  # user vs computer
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.user_move_x()
                    count += 1
                else:
                    self.computer_move_easy_o()
                    count += 1
                self.count += 1
        elif input_command == "start easy user":  # computer vs user
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.computer_move_easy_x()
                    count += 1
                else:
                    self.user_move_o()
                    count += 1
                self.count += 1
        elif input_command == "start user user":  # user vs user
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.user_move_x()
                    count += 1
                else:
                    self.user_move_o()
                    count += 1
                self.count += 1
        elif input_command == "start medium user":  # computer vs user  medium level
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.computer_move_medium_x()
                    count += 1
                else:
                    self.user_move_o()
                    count += 1
                self.count += 1
        elif input_command == "start medium medium":  # computer vs computer  medium level
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.computer_move_medium_x()
                    count += 1
                else:
                    self.computer_move_medium_o()
                    count += 1
                self.count += 1
        elif input_command == "start user medium":  # user vs computer  medium level
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.user_move_x()
                    count += 1
                else:
                    self.computer_move_medium_o()
                    count += 1
                self.count += 1
        elif input_command == "start medium easy":  # computer medium vs computer easy medium level
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.computer_move_medium_x()
                    count += 1
                else:
                    self.computer_move_easy_o()
                    count += 1
                self.count += 1
        elif input_command == "start easy medium":  # computer easy vs computer medium medium level
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.computer_move_easy_x()
                    count += 1
                else:
                    self.computer_move_medium_o()
                    count += 1
                self.count += 1
        elif input_command == "start hard hard":
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.computer_move_hard_x()
                    count += 1
                else:
                    self.computer_move_hard_o()
                    count += 1
                self.count += 1
        elif input_command == "start user hard":
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.user_move_x()
                    count += 1
                else:
                    self.computer_move_hard_o()
                    count += 1
                self.count += 1
        elif input_command == "start hard user":
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.computer_move_hard_x()
                    count += 1
                else:
                    self.user_move_o()
                    count += 1
                self.count += 1
        elif input_command == "start hard easy":
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.computer_move_hard_x()
                    count += 1
                else:
                    self.computer_move_easy_o()
                    count += 1
                self.count += 1
        elif input_command == "start easy hard":
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.computer_move_easy_x()
                    count += 1
                else:
                    self.computer_move_hard_o()
                    count += 1
                self.count += 1
        elif input_command == "start hard medium":
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.computer_move_hard_x()
                    count += 1
                else:
                    self.computer_move_medium_o()
                    count += 1
                self.count += 1
        elif input_command == "start medium hard":
            self.print_field()
            count = 1
            while self.win_check() == "Game not finished":
                if count % 2 != 0:
                    self.computer_move_medium_x()
                    count += 1
                else:
                    self.computer_move_hard_o()
                    count += 1
                self.count += 1

        else:
            print("Bad parameters!")


game = TicTacToeWithAi()

game.main_menu()

