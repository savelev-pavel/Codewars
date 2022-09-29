def is_valid_walk(walk):
    result = True
    directions = {"n":0, "s":0, "w":0, "e":0}
    if len(walk)!=10:
        result = False
    for dir in walk:
        directions[dir] += 1
    if directions['s'] != directions['n']:
        result = False
    if directions['w'] != directions['e']:
        result = False
    return result

if __name__ == "__main__":
    print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))