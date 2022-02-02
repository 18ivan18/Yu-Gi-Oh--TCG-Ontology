from owlready2 import *


def createModel(onto):
    '''
    BASIC CLASSES DEFINITION
    '''

    with onto:
        class Card(Thing):
            pass

        class Monster(Card):
            pass

        class Spell(Card):
            pass

        class Trap(Card):
            pass

        AllDisjoint([Monster, Spell, Trap])
        Card.equivalent_to.append(Monster | Spell | Trap)

        class Effect(Thing):
            pass

        class has_text(Effect >> str, FunctionalProperty):
            pass

        class effect(Card >> Effect):
            pass
        Monster.is_a.append(effect.max(2))
        Spell.is_a.append(effect.max(1))
        Trap.is_a.append(effect.max(1))

        class rank(Monster >> int, FunctionalProperty):
            pass

        class link_rating(Monster >> int, FunctionalProperty):
            pass

        # There are different kinds of Monsters, Spells and Traps based on their type:
        class NonEffectMonster(Monster):
            equivalent_to = [Monster & Not(
                effect.some(Effect))]

        class XyzMonster(Monster):
            equivalent_to = [Monster & rank.some(int)]

        class LinkMonster(Monster):
            equivalent_to = [Monster & link_rating.some(int)]

        class EffectMonster(Monster):
            equivalent_to = [
                Monster & effect.exactly(1, Effect)]

        class PendulumMonster(Monster):
            equivalent_to = [
                Monster & effect.min(2, Effect)]

        class FusionMonster(Monster):
            pass

        class SynchroMonster(Monster):
            pass

        class RitualMonster(Monster):
            pass

        class NormalMonster(NonEffectMonster):
            pass

        class level(Monster >> int, FunctionalProperty):
            pass
        # Link and Xyz monsters don't have levels
        XyzMonster.is_a.append(level.exactly(0))
        LinkMonster.is_a.append(level.exactly(0))

        # cannot use def here because it's a key word
        # Link monsters don't have def
        class defense(Monster >> int, FunctionalProperty):
            pass
        LinkMonster.is_a.append(defense.exactly(0))

        class atk(Monster >> int, FunctionalProperty):
            pass

        class name(Card >> str):
            pass

        class rarity(DataProperty, FunctionalProperty):
            domain = [Card]
            range = [OneOf(["Common", "Rare", "Super Rare",
                           "Ultra Rare", "Ultimate Rare", "Ghost Rare"])]

        Card.equivalent_to.append(name.some(str))

        # There are 20 types in total

        class Type(Thing):
            pass
        dragon = Type("Dragon")
        fairy = Type("Fairy")
        machine = Type("Machine")
        warrior = Type("Warrior")
        spellcaster = Type("Spellcaster")
        Type.equivalent_to.append(OneOf(
            [dragon, fairy, machine, warrior, spellcaster]))

        class Ability(Thing):
            pass
        union = Ability("Union")
        tuner = Ability("Tuner")
        spirit = Ability("Spirit")
        toon = Ability("Toon")
        gemini = Ability("Gemini")
        flip = Ability("Flip")
        Ability.equivalent_to.append(OneOf(
            [union, tuner, spirit, toon, gemini,
             flip]))

        class has_type(Monster >> Type, FunctionalProperty):
            pass

        class has_ability(Monster >> Ability):
            pass

        class Attribute(Thing):
            pass
        dark = Attribute("Dark")
        light = Attribute("Light")
        divine = Attribute("Divine")
        earth = Attribute("Earth")
        fire = Attribute("Fire")
        water = Attribute("Water")
        wind = Attribute("Wind")
        Attribute.equivalent_to.append(OneOf(
            [dark, light, divine, earth, fire, water, wind]))

        class has_attribute(Monster >> Attribute, FunctionalProperty):
            pass

        # Spells
        # Continious Spell, Normal Spell, Equip Spell, QuickPlay Spell, Ritual Spell, Field Spell
        class ContiniousSpell(Spell):
            pass

        class NormalSpell(Spell):
            pass

        class EquipSpell(Spell):
            pass

        class QuickPlaySpell(Spell):
            pass

        class RitualSpell(Spell):
            pass

        class FieldSpell(Spell):
            pass
        Spell.equivalent_to.append(ContiniousSpell | NormalSpell |
                                   EquipSpell | QuickPlaySpell | RitualSpell | FieldSpell)
        AllDisjoint([ContiniousSpell, NormalSpell, EquipSpell,
                    QuickPlaySpell, RitualSpell, FieldSpell])

        # Traps
        # Counter Trap, Normal Trap, Continious Trap
        class ContiniousTrap(Trap):
            pass

        class NormalTrap(Trap):
            pass

        class CounterTrap(Trap):
            pass
        Trap.equivalent_to.append(CounterTrap | NormalTrap | ContiniousTrap)
        AllDisjoint([CounterTrap, NormalTrap, ContiniousTrap])

        '''
        MORE MODEL DEFINITION
        '''
        class Deck(Thing):
            pass

        # TODO: This can be an external class
        class Person(Thing):
            pass

        class Player(Person):
            pass

        class Match(Thing):
            pass

        class Round(Thing):
            pass

        # TODO: This can be an external class
        class Event(Thing):
            pass

        class Tournament(Event):
            pass

        class Locals(Tournament):
            pass

        class Regionals(Tournament):
            pass

        class WorldChampionshipQualifier(Tournament):
            pass
        Tournament.equivalent_to.append(
            Locals | Regionals | WorldChampionshipQualifier)
        AllDisjoint([Locals, Regionals, WorldChampionshipQualifier])

        class has_rounds(Tournament >> Round):
            pass

        class has_matches(Round >> Match):
            pass

        class has_players(Match >> Player):
            pass

        class plays_in_match(Player >> Match):
            inverse_property = has_players

        class uses(Player >> Deck, FunctionalProperty):
            pass

        class is_used_in(Card >> Deck):
            pass

        class has_cards(Deck >> Card):
            inverse_property = is_used_in

        class archtype(Deck >> str):
            pass

        class has_winner(Match >> Player, FunctionalProperty):
            pass

        class has_points(Player >> int, FunctionalProperty):
            pass

        class number_of_wins(Player >> int, FunctionalProperty):
            pass

        class number_of_draws(Player >> int, FunctionalProperty):
            pass

        class years_experience(Player >> float, FunctionalProperty):
            pass

        class cossyId(Player >> ConstrainedDatatype(str, pattern=r'\d{10}'), FunctionalProperty):
            pass
        Match.is_a.append(has_players.exactly(2, Player))
        # Decks have min 40 cards, but this is too much for this example
        # Deck.is_a.append(has_cards.min(40, Card))

        class CrowdFavourite(Player):
            equivalent_to = [Player & years_experience.only(
                ConstrainedDatatype(float, min_exclusive=5))]

        class ExperiencedPlayer(Player):
            pass

        class Draw(Match):
            equivalent_to = [Match & Not(has_winner.some(Player))]

        ExperiencedPlayer.is_a.append(years_experience.only(
            ConstrainedDatatype(float, min_exclusive=7)))

        '''
        ANNOTATIONS DEFINITION
        '''

        Card.label = "Yu-Gi-Oh TCG card"
        Card.comment = "There are three main types of cards: Monster , Spell, Trap"

        # Calculate the points based on the number of wins/draws
        # rule = Imp()
        # rule.set_as_rule(
        #     """Player(?p), number_of_wins(?p, ?w), number_of_draws(?p, ?d), multiply(?r1, ?w, 3), multiply(?r2, ?d, 1), add(?r, ?r1, ?r2) -> has_points(?p, ?r)""")

        class participates_in(Player >> Tournament):
            pass

        # If a player has played in a match of the tournament that means the player participated in the tournament
        rule = Imp()
        rule.set_as_rule(
            """Player(?p), plays_in_match(?p, ?m), has_matches(?r, ?m), has_rounds(?t, ?r) -> participates_in(?p, ?t)""")
