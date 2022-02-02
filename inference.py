from owlready2 import *


def addInstances(onto):
    effect1 = onto.Effect(
        has_text="When a monster declares an attack: You can detach 1 material from this card; negate the attack. If this card is targeted for an attack, while it has no material: Destroy this card.")
    effect2 = onto.Effect(
        has_text="Monster Effect: If this card battles an opponent's monster, any battle damage this card inflicts to your opponent is doubled.")
    effect3 = onto.Effect(has_text="Pendulum Effect: You can reduce the battle damage you take from an attack involving a Pendulum Monster you control to 0. During your End Phase: You can destroy this card, and if you do, add 1 Pendulum Monster with 1500 or less ATK from your Deck to your hand. You can only use each Pendulum Effect of \"Odd-Eyes Pendulum Dragon\" once per turn.")
    effect4 = onto.Effect(has_text="If this card is Link Summoned: You can Special Summon 1 Level 3 or lower Tuner from your hand or Deck in Defense Position, but it cannot activate its effects this turn. During your opponent's Main Phase or Battle Phase (Quick Effect): You can banish this card you control; Special Summon 1 Tuner Synchro Monster from your Extra Deck. (This is treated as a Synchro Summon.) You can only use each effect of \"Crystron Halqifibrax\" once per turn.")

    AllDifferent([effect1, effect2, effect3, effect4])

    monster1 = onto.Monster(name="Number39:Utopia",
                            rank=4, effect=[effect1], atk=2500, defense=2000, has_attribute=onto.Light, has_type=onto.Warrior)
    monster2 = onto.Monster(
        name="Odd-EyesPendulumDragon", effect=[effect2, effect3], atk=2500, defense=2000, level=7, has_attribute=onto.Dark, has_type=onto.Dragon)
    monster3 = onto.Monster(name="DarkMagician",
                            effect=[], atk=2500, defense=2100, level=7, has_attribute=onto.Dark, has_type=onto.Spellcaster)
    monster4 = onto.Monster(name="CrystronHalqifibrax",
                            effect=[effect4], link_rating=2, atk=1500, has_attribute=onto.Water, has_type=onto.Machine)

    close_world(monster1)
    close_world(monster2)
    close_world(monster3)
    close_world(monster4)
