def get_roots(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Cette fonction n'admet pas de solution reelle pour y=0!")
    elif delta == 0:
        x = -b/(2*a)
    else:
        x = (-b-delta)/(2*a), (-b+delta)/(2*a)
    return x

if __name__ == "__main__":
    ...