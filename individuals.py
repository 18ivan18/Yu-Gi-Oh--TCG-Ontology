from owlready2 import *


def addInstances(onto):
    '''
    INSTANCES INVOLVING A FOUR PLAYER TOURNAMENT
    '''
    ivan = onto.Player("Ivan", years_experience=8)
    kostadin = onto.Player("Kostadin")
    ventseslav = onto.Player("Ventseslav")
    ivaylo = onto.Player("Ivaylo", years_experience=4)

    tournament = onto.Regionals("SofiaRegionals30.11.2022")

    r1 = onto.Round()
    r2 = onto.Round()

    m1 = onto.Match()
    m2 = onto.Match()
    m3 = onto.Match()
    m4 = onto.Match()

    m1.has_players = [ivan, ivaylo]
    m1.has_winner = ivan
    m2.has_players = [kostadin, ventseslav]
    m2.has_winner = kostadin
    r1.has_matches = [m1, m2]

    m3.has_players = [ivan, kostadin]
    m3.has_winner = ivan
    m4.has_players = [ivaylo, ventseslav]
    r2.has_matches = [m3, m4]

    ivan.has_points = 6
    kostadin.has_points = 3
    ventseslav.has_points = 1
    ivaylo.has_points = 1

    tournament.has_rounds = [r1, r2]

    c1 = onto.Monster(name="SkyStrikerAce-Raye", level=4, atk=1500,
                      defense=1500, has_type=onto.Warrior, has_attribute=onto.Dark, effect=[onto.Effect(has_text="(Quick Effect): You can Tribute this card; Special Summon 1 \"Sky Striker Ace\" monster from your Extra Deck to the Extra Monster Zone. While this card is in your GY, if a face-up \"Sky Striker Ace\" Link Monster you control is destroyed by battle, or leaves the field because of an opponent's card effect: You can Special Summon this card. You can only use each effect of \"Sky Striker Ace - Raye\" once per turn.")])
    c2 = onto.QuickPlaySpell(name="SkyStrikerMecha-WidowAnchor", effect=[onto.Effect(
        has_text="If you control no monsters in your Main Monster Zone: Target 1 face-up Effect Monster on the field; negate that face-up monster's effects until the end of this turn, then, if you have 3 or more Spells in your GY, you can take control of that monster until the End Phase.")])
    c3 = onto.Monster(name="AshBlossom&JoyousSpring", effect=[onto.Effect(
        has_text="When a card or effect is activated that includes any of these effects (Quick Effect): You can discard this card; negate that effect.● Add a card from the Deck to the hand.● Special Summon from the Deck.● Send a card from the Deck to the GY.You can only use this effect of \"Ash Blossom & Joyous Spring\" once per turn.")],
        has_attribute=onto.Fire, has_type=onto.Type("Zombie"), has_ability=[onto.Tuner])
    d1 = onto.Deck(name="SkyStriker", archtype=[
                   "sky striker", "dpe", "going 2nd"], has_cards=[c1, c2, c3])

    ivan.uses = d1

    c4 = onto.Monster(name="Odd-EyesRagingDragon", effect=[onto.Effect(has_text="Pendulum Effect: Once per turn, if you have no cards in your other Pendulum Zone: You can place 1 Pendulum Monster from your Deck in your Pendulum Zone."), onto.Effect(
        has_text="Monster Effect: 2 Level 7 Dragon-Type monsters If you can Pendulum Summon Level 7, you can Pendulum Summon this face-up card in your Extra Deck. If this card in the Monster Zone is destroyed: You can place it in your Pendulum Zone. If this card is Xyz Summoned using an Xyz Monster as Material, it gains these effects. ● It can make a second attack during each Battle Phase. ● Once per turn: You can detach 1 Xyz Material from it; destroy as many cards your opponent controls as possible, and if you do, this card gains 200 ATK for each, until the end of this turn.")],
        rank=7, atk=3000, defense=2500, has_type=onto.Dragon, has_attribute=onto.Dark)
    d2 = onto.Deck(name="Odd-Eyes",
                   archtype=["combo", "pendulum"], has_cards=[c4])

    close_world(c1)
    close_world(c2)
    close_world(c3)
    close_world(c4)
    close_world(m4)
    '''
    OTHER INSTANCES
    '''
    e1 = onto.Effect(has_text="Draw 2 cards.")
    s = onto.NormalSpell(name="PotOfGreed", effect=[e1], rarity="Common")
