def likes(names):
    if len(names) <= 3:
        dict0123 = {}
        try:
            dict0123 ['0'] = 'no one like this'
            dict0123 ['1'] = f'{names[0]} likes this'
            dict0123 ['2'] = f'{names[0]} and {names[1]} likes this'
            dict0123 ['3'] = f'{names[0]}, {names[1]} and {names[2]} likes this'
        except Exception:
            pass
        result = dict0123[str(len(names))]
    else:
        result = f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
    return result

if __name__ == '__main__':
    print(likes(names=['Paul']))