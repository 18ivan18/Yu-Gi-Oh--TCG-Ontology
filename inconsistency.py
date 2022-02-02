from owlready2 import *


def defense(onto):
    onto.CrystronHalqifibrax.defense = 2


def level(onto):
    onto['Number39:Utopia'].level = 4


def rarity(onto):
    onto.CrystronHalqifibrax.rarity = "Not Rare"


def match(onto):
    onto.match4.has_players.append(onto.Player())
