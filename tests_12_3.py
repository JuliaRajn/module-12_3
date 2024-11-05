import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Runner):
            return self.name == other.name
        return False  # Возвращаем False, если тип other не Runner

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        finished_participants = []  # Отслеживаем финишировавших участников
        while self.participants:
            for i, participant in enumerate(self.participants):
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    finished_participants.append(participant)  # Добавляем в список финишировавших
                    break  # Переход к следующему участнику

        self.participants = finished_participants  # Обновляем список участников
        return finishers


def skip_if_frozen(func):
    def wrapper(self, *args):
        if self.is_frozen:
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        else:
            return func(self, *args)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        runner = Runner('Вася')
        self.assertEqual(runner.speed, 5)

    @skip_if_frozen
    def test_run(self):
        runner = Runner('Вася')
        runner.run()
        self.assertEqual(runner.distance, 10)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner('Вася')
        runner.walk()
        self.assertEqual(runner.distance, 5)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @skip_if_frozen
    def setUp(self):
        self.Usain = Runner("Usain", speed=10)
        self.Andrey = Runner("Andrey", speed=9)
        self.Nick = Runner("Nick", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in sorted(cls.all_results.items()):
            print(f"{key}: {', '.join(str(v) for v in value.values())}")

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.Usain, self.Nick)
        self.all_results[len(self.all_results) + 1] = tournament.start()
        # Проверяем, что Usain финишировал первым
        self.assertTrue(self.all_results[len(self.all_results)][1] == "Usain")

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.Andrey, self.Nick)
        self.all_results[len(self.all_results) + 1] =tournament.start()
        # Проверяем, что Andrey финишировал первым
        self.assertTrue(self.all_results[len(self.all_results)][1] == "Andrey")

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.Usain, self.Andrey, self.Nick)
        self.all_results[len(self.all_results) + 1] = tournament.start()
        # Проверяем, что Usain финишировал первым
        self.assertTrue(self.all_results[len(self.all_results)][1] == "Usain")

    @skip_if_frozen
    def test_usain_andrey_tournament_short_distance(self):
        """Тест для короткой дистанции, чтобы проверить, что Usain приходит первым"""
        tournament = Tournament(20, self.Usain, self.Andrey)
        self.all_results[len(self.all_results) + 1] = tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)][1] == "Usain")

if __name__ == '__main__':
    unittest.main()

