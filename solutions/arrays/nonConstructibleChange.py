from typing import Sequence
def nonConstructibleChange(coins):
    class MinChange:
        def __init__(self, coins: Sequence[int] ):
            self.coins = coins
            self.coinCounter: int = 0
        def getMinChange(self) -> int:
            self.coins.sort()
            coinsLen: int = len(coins)
            for coin in coins:
                if coin > self.coinCounter + 1:
                    return self.coinCounter + 1
                self.coinCounter += coin
                print(self.coinCounter)
            return self.coinCounter + 1
    minChange = MinChange(coins)
    test = minChange.getMinChange()

    return test
    
