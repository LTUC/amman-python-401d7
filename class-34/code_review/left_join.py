syno_hash={
    'diligent': 'employed',
    'fond':'enamored',
    'guide':'usher',
    'outfit':'garb',
    'wrath':'anger'
    }
anto_hash={
    'diligent': 'idle',
    'fond':'averse',
    'guide':'follow',
    'flow':'jam',
    'wrath':'delight'
    }

def left_join(h1, h2):
    result = []
    # edge case: check if h1 is empty
    if not h1:
        return result
    for i,k in enumerate(h1):
        # one liner if statement
        # condition : else_condition (JS)
        anto_word = h2[k] if k in h2 else None
        result.append([k,h1[k],anto_word])
    return result

print(left_join({}, anto_hash))


