# coding: UTF-8

from user_interface import InputInterface
from game_component import Deck, Player, Dealer, PlayerActionSignal


if __name__ == '__main__':
    # オブジェクト初期化
    input_interface = InputInterface()
    deck = Deck()
    player = Player()
    dealer = Dealer()

    # プレイヤーにカードを配る
    player.add(deck.draw())
    player.add(deck.draw())
    print("Your cards are {}".format(player.show()))

    # ディーラーにカードを配る
    dealer.add(deck.draw())
    dealer.add(deck.draw())
    print("Dealer cards are {}".format(dealer.first_show()))

    while 1:

        # ユーザーアクション受付
        action = input_interface.receive_action()

        print(action)

        # 今は「スタンド」のみ対応
        # TODO 次はできれば処理を別ファイルに分けたい&「ヒット」の実装
        if action == PlayerActionSignal.STAND:
            while dealer.point() >= 17 :
                if dealer.point() < 17:
                    dealer.add(deck.draw())
                if dealer.point() > 21:
                    print("You are win!!!")
                    exit()

            print("Your cards are {}. Total:{}".format(player.show(), player.point()))
            print("Dealer cards are {}. Total:{}".format(dealer.show(), dealer.point()))
            # 勝利判定
            if dealer.point() < player.point() <= 21:
                print("You are win!!!")
            else:
                print("You are lose...")
            exit()
        if action == PlayerActionSignal.HIT:
            player.add(deck.draw())
            print("Your cards are {}. Total:{}".format(player.show(), player.point()))
            if player.point() > 21:
                print("You are lose...")
                exit()


