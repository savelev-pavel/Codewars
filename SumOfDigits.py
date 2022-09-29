def digital_root(n):
    result = 0
    for dig in str(n):
        result += int(dig)
    if len(str(result)) > 1: result = digital_root(result)
    return result

if __name__ == "__main__":
    n = 0
    try:
        n = input("Enter a number to sum:\n")
        print(digital_root(n))
    except Exception:
        print("Not a number!")

