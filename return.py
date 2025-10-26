import random

def create_card(rank:str,suite:str) -> dict:
    suites = ["H","C","D","S"]
    ranks = {"2": 2,
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
    if rank not in ranks or suite not in suites:
        return None
    
    return {"rank": rank,
            "suite": suite,
            "value": ranks[rank]}


        
    