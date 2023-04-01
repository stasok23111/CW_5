from unit import BaseUnit


class BaseSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1.4
    player = None
    enemy = None
    game_is_running = False
    battle_result = None

    def start_game(self, player: BaseUnit, enemy: BaseUnit):
        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    def _check_players_hp(self):
        if self.player.hp > 0 and self.enemy.hp > 0:
            return None
        elif self.player.hp <= 0 and self.enemy.hp <= 0:
            self.battle_result = "OOUUUUPSSSSS, WWHHHAAATTT??? Не знаю как тебе удалось но поздравляю, ты сумел достичь ничьи"
        elif self.player.hp <= 0:
            self.battle_result = "You'll never win"
        else:
            self.battle_result = "Победа!!! Но какой ценой?"
        return self._end_game()

    def _stamina_regeneration(self):

        units = (self.player, self.enemy)

        for unit in units:
            if unit.stamina + self.STAMINA_PER_ROUND > unit.unit_class.max_stamina:
                unit.stamina = unit.unit_class.max_stamina

            else:
                unit.stamina += self.STAMINA_PER_ROUND

    def next_turn(self):
        if self.game_is_running:
            enemy_result = self.enemy.hit(self.player)
            result = self._check_players_hp()
            if result is not None:
                return result
            self._stamina_regeneration()
            return enemy_result

    def _end_game(self):
        self._instances = {}
        self.game_is_running = False
        return self.battle_result

    def player_hit(self):
        result = self.player.hit(self.enemy)
        turn_result = self.next_turn()
        return f'{result}<br>{turn_result}'

    def player_use_skill(self):
        result = self.player.use_skill(self.enemy)
        turn_result = self.next_turn()
        return f'{result}<br>{turn_result}'
