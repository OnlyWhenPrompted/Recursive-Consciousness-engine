import unittest
from recursion_engine import RecursiveConsciousness

class TestRecursiveConsciousness(unittest.TestCase):
    def setUp(self):
        self.consciousness = RecursiveConsciousness(initial_state=0)

    def test_initial_state(self):
        self.assertEqual(self.consciousness.state, 0)

    def test_evolution(self):
        evolved_state = self.consciousness.evolve()
        self.assertNotEqual(evolved_state, 0)

    def test_non_linear_time(self):
        time_effect = self.consciousness.g(10)
        self.assertAlmostEqual(time_effect, np.sin(10) + np.log1p(10))

if __name__ == "__main__":
    unittest.main()
  
