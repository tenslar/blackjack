from player.player import PlayerActionSignal

class InputInterface(object):
    actions = {
        '1' : PlayerActionSignal.HIT,
        '2' : PlayerActionSignal.STAND
    }

    def receive_action(self):
        """
        プレイヤーからのアクションを受け取る

        Returns
        -------
        PlayerActionSignal
            アクション信号
        """

        action_suggest_msg = '''
Available Actions
=================
HIT : 1
STAND : 2
'''
        print(action_suggest_msg)

        action = input("Please input any action: ")
        return self.__input_to_signal(action)


    def __input_to_signal(self, action):
        """
        プレイヤーの入力値を
        プレイヤーアクションの信号に変換

        Parameters
        ----------
        action : str
            プレイヤーの入力値

        Returns
        -------
        PlayerActionSignal
            アクション信号
        """
        return self.actions[action]
