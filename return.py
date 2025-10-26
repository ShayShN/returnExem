import random

def create_card(rank:str,suite:str) -> dict:
    return dict(rank = str(rank), suite = suite, value = rank)

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return 'p1'
    elif p1_card["value"] < p2_card["value"]:
        return 'p2'
    elif p1_card["value"] == p2_card["value"]:
        return 'WAR'
    
def create_deck() -> list[dict]:
    arr = []
    for i in ["H","C","D","S"]:
        
    