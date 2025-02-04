def board(brd):
    print(f" {brd[0]} | {brd[1]} | {brd[2]}")
    print(f"---|---|---")
    print(f" {brd[3]} | {brd[4]} | {brd[5]}")
    print(f"---|---|---")
    print(f" {brd[6]} | {brd[7]} | {brd[8]}")


def game(x, o):
    brd = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    brd[0] = "X" if x[0] == 1 else "O" if o[0] == 1 else 1
    brd[1] = "X" if x[1] == 1 else "O" if o[1] == 1 else 2
    brd[2] = "X" if x[2] == 1 else "O" if o[2] == 1 else 3
    brd[3] = "X" if x[3] == 1 else "O" if o[3] == 1 else 4
    brd[4] = "X" if x[4] == 1 else "O" if o[4] == 1 else 5
    brd[5] = "X" if x[5] == 1 else "O" if o[5] == 1 else 6
    brd[6] = "X" if x[6] == 1 else "O" if o[6] == 1 else 7
    brd[7] = "X" if x[7] == 1 else "O" if o[7] == 1 else 8
    brd[8] = "X" if x[8] == 1 else "O" if o[8] == 1 else 9
    return brd


class win_check:
    def __init__(self, player):
        self.player_pos = player
        if (
            (
                self.player_pos[0] > 0
                and self.player_pos[1] > 0
                and self.player_pos[2] > 0
            )
            or (
                self.player_pos[3] > 0
                and self.player_pos[4] > 0
                and self.player_pos[5] > 0
            )
            or (
                self.player_pos[6] > 0
                and self.player_pos[7] > 0
                and self.player_pos[8] > 0
            )
            or (
                self.player_pos[0] > 0
                and self.player_pos[3] > 0
                and self.player_pos[6] > 0
            )
            or (
                self.player_pos[1] > 0
                and self.player_pos[4] > 0
                and self.player_pos[7] > 0
            )
            or (
                self.player_pos[2] > 0
                and self.player_pos[5] > 0
                and self.player_pos[8] > 0
            )
            or (
                self.player_pos[0] > 0
                and self.player_pos[4] > 0
                and self.player_pos[8] > 0
            )
            or (
                self.player_pos[2] > 0
                and self.player_pos[4] > 0
                and self.player_pos[6] > 0
            )
        ):
            self.rslt = "win"
        else:
            self.rslt = "not"


def result_check(a, b, c):
    player_1 = win_check(a)
    player_2 = win_check(b)

    if player_1.rslt == "win":
        return 1
    elif player_2.rslt == "win":
        return 2
    elif c > 9:
        return 3
    else:
        return 0


def result_print(first_player, second_player, game_cycle_count):
    if result_check(first_player, second_player, game_cycle_count) == 1:
        print("'X' is win!!")
    elif result_check(first_player, second_player, game_cycle_count) == 2:
        print("'O' is Win!!")
    elif result_check(first_player, second_player, game_cycle_count) == 3:
        print("Match is Draw....")
    else:
        print("Error...........!")


chanse = 0
xplayer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
oplayer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 0

print("Welcome to TiC-tAc-ToI\n\tenter 'CTRL + C' for exit the Game\n\n")
board(game(xplayer, oplayer))

while True:
    count += 1
    if result_check(xplayer, oplayer, count) > 0:
        print("Game over")
        break

    if chanse == 0:
        Xplayer_choice = int(input("'X' player Enter your choice: "))
        if xplayer[Xplayer_choice - 1] == 0:
            xplayer[Xplayer_choice - 1] = 1
            chanse = 1
            if (
                xplayer[Xplayer_choice - 1] == oplayer[Xplayer_choice - 1]
                or Xplayer_choice > 9
                or Xplayer_choice < 1
            ):
                print("Enter a valid value, those are not enterd by other player")
                xplayer[Xplayer_choice - 1] = 0
                chanse = 0
        else:
            print("Enter e unique value, That is not enterd before ")
            chanse = 0

    elif chanse == 1:
        Oplayer_choice = int(input("'O' player Enter your choice: "))
        if oplayer[Oplayer_choice - 1] == 0:
            oplayer[Oplayer_choice - 1] = 1
            chanse = 0
            if (
                xplayer[Oplayer_choice - 1] == oplayer[Oplayer_choice - 1]
                or Oplayer_choice > 9
                or Oplayer_choice < 1
            ):
                print("Enter a valid value, those are not enterd by other player")
                oplayer[Oplayer_choice - 1] = 0
                chanse = 1
        else:
            print("Enter e unique value, That is not enterd before ")
            chanse = 1

    else:
        print("Error")

    board(game(xplayer, oplayer))

result_print(xplayer, oplayer, count)
