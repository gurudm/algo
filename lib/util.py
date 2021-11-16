import json
import re

SYM = json.loads(open('data/symbols.json').read())

def get_token(symbol):
    stoken = SYM.get(symbol)
    if not stoken:
        exit()
    return stoken
