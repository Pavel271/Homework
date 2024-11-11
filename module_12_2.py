import runner_and_tournament as run_turn
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = [
            run_turn.Runner('Усэйн', 10),
            run_turn.Runner('Андрей', 9),
            run_turn.Runner('Ник', 3),
        ]

    @classmethod
    def tearDownClass(cls):
        for i, f in cls.all_results.items():
            print("{}:".format(i))
            for e, d in f.items():
                print("{}: {}".format(e, d))

    def test_1(self):
        turn_1 = run_turn.Tournament(90, self.runners[0], self.runners[2])
        result = turn_1.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Усейн и Ник"] = result

    def test_2(self):
        turn_2 = run_turn.Tournament(90, self.runners[1], self.runners[2])
        result = turn_2.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Андрей и Ник"] = result

    def test_3(self):
        turn_3 = run_turn.Tournament(90, *self.runners)
        result = turn_3.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Усейн, Андрей и Ник"] = result

if __name__ == '__main__':
    unittest.main()