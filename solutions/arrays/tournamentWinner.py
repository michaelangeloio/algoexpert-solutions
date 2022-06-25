from typing import Sequence
def tournamentWinner(competitions, results):
    class ScoreCalculator:
        def __init__(self, competitions: Sequence[Sequence[str]], results: Sequence[int]):
            self.competitions = competitions
            self.results = results
            self.winners = []
        def findWinners(self) -> Sequence[str]:
            for i, val in enumerate(self.competitions):
                if self.results[i] == 0:
                    winner = val[1]
                    self.winners.append(winner)
                else:
                    winner = val[0]
                    self.winners.append(winner)
        def getTopWinner(self):
            if len(self.winners) == 0:
                raise Exception('No winners, did you call findWinners()?')
            winnerTotals = {}
            for winner in self.winners:
                if winner not in winnerTotals:
                    winnerTotals[winner] = 1
                else:
                    winnerTotals[winner] += 1
            return max(winnerTotals, key=winnerTotals.get)
    scoreCalculator = ScoreCalculator(competitions, results)
    scoreCalculator.findWinners()
    winner = scoreCalculator.getTopWinner()
    return winner
