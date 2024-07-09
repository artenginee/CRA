from random import randrange

from IGame import IGame


class Player:
    def __init__(self):
        self.player_names = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [False] * 6

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

    @property
    def how_many_players(self):
        return len(self.player_names)

    def is_playable(self):
        return self.how_many_players >= 2


class GameBetter(IGame):
    def __init__(self):
        self.player = Player()

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        for i in range(50):
            self.pop_questions.append(f'Pop Question {i}')
            self.science_questions.append(f'Science Question {i}')
            self.sports_questions.append(f'Sports Question {i}')
            self.rock_questions.append(self.create_rock_question(i))

    def create_rock_question(self, index):
        return f'Rock Question {index}'

    def add(self, player_name):
        self.player.player_names.append(player_name)
        self.player.places[self.player.how_many_players - 1] = 0
        self.player.purses[self.player.how_many_players - 1] = 0
        self.player.in_penalty_box[self.player.how_many_players - 1] = False

        print(player_name + ' was added')
        print(f'They are player number {len(self.player.player_names)}')

        return True

    def rolling(self, roll):
        print(f'{self.player.player_names[self.player.current_player]} is the current player')
        print(f'They have rolled a {roll}')

        if self.player.in_penalty_box[self.player.current_player] and roll % 2 == 0:
            self.update_penalty_state(False)
            return

        if self.player.in_penalty_box[self.player.current_player] and roll % 2 == 1:
            self.update_penalty_state(True)

        self.change_position(roll)
        self._ask_question()
        self.player.in_penalty_box[self.player.current_player] = False  # 버그 fix

    def change_position(self, roll):
        self.player.places[self.player.current_player] += roll
        if self.player.places[self.player.current_player] >= 12:
            self.player.places[self.player.current_player] -= 12
        print(f'{self.player.player_names[self.player.current_player]}\'s new location is ',
              f'{self.player.places[self.player.current_player]}')
        print(f'The category is {self._current_category}')

    def update_penalty_state(self, state):
        self.player.is_getting_out_of_penalty_box = state
        if self.player.is_getting_out_of_penalty_box:
            print(f'{self.player.player_names[self.player.current_player]} is getting out of the penalty box')
        else:
            print(f'{self.player.player_names[self.player.current_player]} is not getting out of the penalty box')

    def _ask_question(self):
        if self._current_category == 'Pop':
            print(self.pop_questions.pop(0))
        if self._current_category == 'Science':
            print(self.science_questions.pop(0))
        if self._current_category == 'Sports':
            print(self.sports_questions.pop(0))
        if self._current_category == 'Rock':
            print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        if self.player.places[self.player.current_player] == 0:
            return 'Pop'
        if self.player.places[self.player.current_player] == 4:
            return 'Pop'
        if self.player.places[self.player.current_player] == 8:
            return 'Pop'
        if self.player.places[self.player.current_player] == 1:
            return 'Science'
        if self.player.places[self.player.current_player] == 5:
            return 'Science'
        if self.player.places[self.player.current_player] == 9:
            return 'Science'
        if self.player.places[self.player.current_player] == 2:
            return 'Sports'
        if self.player.places[self.player.current_player] == 6:
            return 'Sports'
        if self.player.places[self.player.current_player] == 10:
            return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.player.in_penalty_box[self.player.current_player]:
            if not self.player.is_getting_out_of_penalty_box:
                self.change_player_turn()
                return True

        self.update_purse()
        winner = self._did_player_win()
        self.change_player_turn()
        return winner

    def update_purse(self):
        print('Answer was correct!!!!')
        self.player.purses[self.player.current_player] += 1
        print(f'{self.player.player_names[self.player.current_player]} now has '
              f'{self.player.purses[self.player.current_player]} Gold Coins.')

    def change_player_turn(self):
        self.player.current_player += 1
        if self.player.current_player == len(self.player.player_names):
            self.player.current_player = 0

    def wrong_answer(self):
        if self.player.in_penalty_box[self.player.current_player]:
            if not self.player.is_getting_out_of_penalty_box:
                self.change_player_turn()
                return True

        print('Question was incorrectly answered')
        print(self.player.player_names[self.player.current_player] + ' was sent to the penalty box')
        self.player.in_penalty_box[self.player.current_player] = True
        self.change_player_turn()
        return True

    def _did_player_win(self):
        return not (self.player.purses[self.player.current_player] == 6)


if __name__ == '__main__':
    not_a_winner = False

    game = GameBetter()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        roll = randrange(6) + 1
        game.rolling(roll)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break
