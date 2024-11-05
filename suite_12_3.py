# suite_12_3.py

import unittest

# Импортируем TestCase из предыдущих задач
from tests_12_2 import TournamentTest
from tests_12_1 import RunnerTest

# Создаем TestSuite
test_suite = unittest.TestSuite()

# Добавляем тесты в TestSuite
test_suite.addTest(unittest.makeSuite(RunnerTest))
test_suite.addTest(unittest.makeSuite(TournamentTest))

# Создаем объект класса TextTestRunner с verbosity=2
runner = unittest.TextTestRunner(verbosity=2)

# Запускаем тесты
runner.run(test_suite)
