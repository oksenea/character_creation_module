from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character():
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name) -> None:
        self.name = name

    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный '
                f'{value_attack}')

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} урона')

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'«{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}»')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_SKILL = 'Выносливость'
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    BRIEF_DESC_CHAR_CLASS = ' дерзкий воин ближнего боя. Сильный, ' \
                            'выносливый и отважный'


class Mage(Character):
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_SKILL = 'Атака'
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    BRIEF_DESC_CHAR_CLASS = ' находчивый воин дальнего боя. Обладает ' \
                            'высоким интеллектом'


class Healer(Character):
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_SKILL = 'Защита'
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    BRIEF_DESC_CHAR_CLASS = ' могущественный заклинатель. Черпает силы из ' \
                            'природы, веры и духов'


def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    # Замените конструкцию условных операторов на словарь.
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = {'attack': character.attack(),
           'defence': character.defence(),
           'special': character.special()}
    comand = None
    while comand != 'skip':
        comand = input('Введи команду: ')
        # Вместо блока условных операторов добавьте условие
        # принадлежности введённой команды словарю.
        # В функции print() будет вызываться метод класса,
        # который соответствует введённой команде.
        if comand in cmd:
            print(cmd[comand])
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    game_classes = {
                    'warrior': Warrior,
                    'mage': Mage,
                    'healer': Healer,
    }

    approve_choice: str = ''

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        if selected_class in game_classes:
            char_class: Character = game_classes[selected_class](char_name)
        # Вывели в терминал описание персонажа.
            print(char_class)
            approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                                   'или любую другую кнопку, '
                                   'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    #  run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class(char_name)
    game_classes_training = {
                    'Warrior': ' ты Воитель — великий мастер ближнего боя.',
                    'Mage': ' ты Маг — превосходный укротитель стихий.',
                    'Healer': ' ты Лекарь — чародей, способный исцелять раны.',
    }

    print(char_class.name,
          game_classes_training[char_class.__class__.__name__])
    print(start_training(char_class))
