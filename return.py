from operator import le
import random

optinal_suites = ["H","C","D","S"]
optinal_ranks = {"2": 2,
             "3": 3,
             "4": 4,
             "5": 5,
             "6": 6,
             "7": 7,
             "8": 8,
             "9": 9,
             "10": 10,
             "J": 11,
             "Q": 12,
             "K": 13,
             "A": 14,}
def create_card(rank:str,suite:str) -> dict:
    if rank not in optinal_ranks or suite not in optinal_suites:
        return None 
    return {"rank": rank,
            "suite": suite,
            "value": optinal_ranks[rank]}

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return 'p1'
    elif p1_card["value"] < p2_card["value"]:
        return 'p2'
    else:
        return 'WAR'
    
def create_deck() -> list[dict]:
    result = []
    for suite in optinal_suites:
        for rank in optinal_ranks:
            result.append(create_card(rank,suite))
    return result
        
