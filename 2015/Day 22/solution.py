from os.path import dirname, abspath
from dataclasses import dataclass, field

TEST: str = open(f'{dirname(abspath(__file__))}\\test.txt').read()
DATA: str = open(f'{dirname(abspath(__file__))}\\input.txt').read()

def fetchData(data: str) -> list[int]:
    return list(map(int, [line.split(': ')[1] for line in data.splitlines() if len(line)]))

class Character():
    def __init__(self, hp, armor, dmg, mana):
        self.hp = hp
        self.armor = armor
        self.dmg = dmg
        self.mana = mana

class Insta():
    def __init__(self, dmg, heal):
        self.dmg = dmg
        self.heal = heal

    def perform(self, player, boss):
        player.hp += self.heal
        boss.hp -= self.dmg

class Effect:
    def __init__(self, id_: int, turns: int, armor_boost: int, dmg: int, mana_up: int):
        self.id_ = id_
        self.turns = turns
        self.armor_boost = armor_boost
        self.dmg = dmg
        self.mana_up = mana_up
        self.total_turns = turns

    def reset(self):
        return Effect(self.id_, self.total_turns, self.armor_boost, self.dmg, self.mana_up)

    def __hash__(self):
        return self.id_

    def __eq__(self, other: object):
        return self.id_ == other.id_

    def use(self, player: Character, boss: Character):
        if self.turns == self.total_turns:
            player.armor += self.armor_boost
        boss.hp -= self.dmg
        player.mana += self.mana_up
        self.turns -= 1
        if self.turns == 0:
            player.armor -= self.armor_boost

EMPTY_EFFECT = Effect(-1, 0, 0, 0, 0)

class Spell:
    def __init__(self, name: str, mana: int, effect: Effect=None, insta: Insta=None):
        self.name: str = name
        self.mana: int = mana
        self.effect: Effect = effect
        self.insta: Insta = insta

    def cast_spell(self, player: Character, boss: Character, effects):
        player.mana -= self.mana
        if player.mana < 0 or self.effect in effects:
            return False
        if self.insta is not None:
            self.insta.perform(player, boss)
        if self.effect != EMPTY_EFFECT:
            effects.add(self.effect)
        return True

def total_mana(spells: list[Spell]):
    return sum([sp.mana for sp in spells])

def use_effects(effects: list[Effect], player: Character, boss: Character):
    for effect in effects:
        effect.use(player, boss)
    return set([e for e in effects if e.turns > 0])

def simulate_battle(spell_order: list[Spell], bossHP: int, bossATK: int, hardMode: bool=False) -> int:
    spell_order = [Spell(s.name, s.mana, s.effect.reset(), s.insta) for s in spell_order]
    boss = Character(bossHP, 0, bossATK, 0)
    player = Character(50, 0, 0, 500)
    effects = set()
    for sp in range(len(spell_order)):
        player.hp -= hardMode
        if player.hp <= 0:
            return -3
        effects = use_effects(effects, player, boss)
        if boss.hp <= 0:
            return total_mana(spell_order[:sp])
        if not spell_order[sp].cast_spell(player, boss, effects):
            return -2
        effects = use_effects(effects, player, boss)
        if boss.hp <= 0:
            return total_mana(spell_order[:sp+1])
        player.hp -= max(1, boss.dmg - player.armor)
        if player.hp <= 0:
            return -3
    return -1

SPELLS = [
    Spell('Magic Missile', 53, EMPTY_EFFECT, Insta(4, 0)),
    Spell('Drain', 73, EMPTY_EFFECT, Insta(2, 2)),
    Spell('Shield', 113, Effect(1, 6, 7, 0, 0), None),
    Spell('Poison', 173, Effect(2, 6, 0, 3, 0), None),
    Spell('Recharge', 229, Effect(3, 5, 0, 0, 101), None)
]

def parts(data: list[int], hardMode: bool=False) -> int:
    performed_spells: list[list[Spell]] = [[]]
    while True:
        new_spells: list[Spell] = []
        for combination in performed_spells:
            for spell in SPELLS:
                new_spells.append(combination + [spell])
        performed_spells = new_spells
        spentMana: int = -1
        next_spells = []
        for spells in performed_spells:
            value: int = simulate_battle(spells, *data, hardMode)
            if value == -1:
                next_spells.append(spells)
                continue
            if value in [-2, -3]:
                continue
            if spentMana == -1 or value < spentMana:
                spentMana = value
        if spentMana != -1:
            break
        performed_spells = next_spells
    return spentMana

if __name__ == "__main__":
    data: list[int] = fetchData(DATA)
    print(parts(data, hardMode=False))
    print(parts(data, hardMode=True))
