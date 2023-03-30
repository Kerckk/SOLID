class Team:
    def __init__(self, name, coach, list_player):
        self.name = name
        self.coach = coach
        self.list_player = list_player

    def add_player(self, new_player):
        self.list_player.append(new_player)


class Training:
    def __init__(self):
        pass

    def start(self, team: Team):
        return f"Тренировка началась для команды {team.name}"


class Player:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def join_the_team(self, team):
        team.addplayer(self)


player1 = Player("John", "Doe", "Forward")
player2 = Player("Mary", "Smith", "Defender")
player3 = Player("Peter", "Jones", "Midfielder")
team1 = Team("Team A", "Coach X", [player1, player2])
team1.add_player(player3)
training_session = Training()
print(training_session.start(team1))