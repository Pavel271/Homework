import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        item_walk = runner.Runner('Ran1')
        for i in range(10):
            item_walk.walk()
        self.assertEqual(item_walk.distance, 50)

    def test_run(self):
        item_run = runner.Runner('Ran2')
        for i in range(10):
            item_run.run()
        self.assertEqual(item_run.distance, 100)

    def test_challenge(self):
        item1 = runner.Runner('Ran3')
        item2 = runner.Runner('Ran4')
        for i in range(10):
            item1.walk()
            item2.run()
        self.assertNotEqual(item1.distance, item2.distance)

if __name__ == '__main__':
    unittest.main()

