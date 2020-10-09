import re as re
from typing import List, Any

def predassembling( train_texts: List[str]) -> Any:
    result = list()
    for i in range(len(train_texts)):
        tmp = re.split('[^0-9a-z]', train_texts[i].lower())
        tmp = [j for j in tmp if j]
        result.append(tmp)
    return result

inp = ["Very good, thank you!!", "Awful, i'm kidding, lol:)", "As     fddhfg99 said, shiiiit", "Niiice))))"]
print(predassembling(inp))