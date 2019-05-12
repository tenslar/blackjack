
from user_interface.inputinterface import InputInterface
from game_component import board, deck
from player.player import PlayerActionSignal


if __name__ == '__main__':

    input_interface = InputInterface()
    board = board.Board()
    deck = deck.Deck()

    # プレイヤーにカードを配る
    board.player_cards.append(deck.draw())
    board.player_cards.append(deck.draw())
    print("Your cards are {}".format(board.player_cards))

    # ディーラーにカードを配る
    board.dealer_cards.append(deck.draw())
    board.dealer_cards.append(deck.draw())
    print("Dealer cards are [{}, *]".format(next(iter(board.dealer_cards), None)))

    print(deck.open())

    action = input_interface.receive_action()

    print(action)

    if action == PlayerActionSignal.STAND:
        player_card_count = 0
        for card in board.player_cards:
            player_card_count += card
        dealer_card_count = 0
        for card in board.dealer_cards:
            dealer_card_count += card

        print("Your cards are {}. Total:{}".format(board.player_cards, player_card_count))
        print("Dealer cards are {}. Total:{}".format(board.dealer_cards, dealer_card_count))
        # 勝利判定
        if dealer_card_count < player_card_count <= 21:
            print("You are win!!!")
        else:
            print("You are lose...")


