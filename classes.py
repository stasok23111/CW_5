from dataclasses import dataclass

from skills import FuryPunch, HardShot, Skill, FireBall


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name='Воин',
    max_health=60,
    max_stamina=30,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryPunch(),
)

ThiefClass = UnitClass(
    name='Разбойник',
    max_health=50,
    max_stamina=25,
    attack=1.5,
    stamina=1.2,
    armor=1,
    skill=HardShot(),
)

MageClass = UnitClass(
    name='Маг',
    max_health=45,
    max_stamina=35,
    attack=0.5,
    stamina=1.4,
    armor=0.8,
    skill=FireBall(),
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass,
    MageClass.name: MageClass,
}