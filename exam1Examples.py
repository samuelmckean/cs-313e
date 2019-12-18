# Question 1
def permute(a, lo, correct):
    hi = len(a)
    if lo == hi:
        envelope_correct = False
        for i in range(hi):
            if a[i] == correct[i]:
                envelope_correct = True
                break
        if not envelope_correct:
            print(a)
    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            permute(a, lo + 1, correct)
            a[lo], a[i] = a[i], a[lo]

# Question 2
def books(a, lo):
    hi = len(a)
    if lo == hi:
        print(a)
    else:
        for i in range(lo, hi, 2):
            a[lo], a[i] = a[i], a[lo]
            a[lo+1], a[i+1] = a[i+1], a[lo+1]
            books(a, lo + 2)
            a[lo], a[lo+1] = a[lo+1], a[lo]
            books(a, lo + 2)
            # put the values back
            a[lo], a[i+1] = a[i+1], a[lo]
            a[lo+1], a[i] = a[i], a[lo+1]

# Question 3
def ballgame(a, lo):
    # A and B sit together, C and D do not sit together
    hi = len(a)
    if lo == hi:
        is_valid = True
        for i in range(len(a) - 1):
            if not ((a[i] == 'A' and a[i+1] == 'B') 
                    or (a[i] == 'B' and a[i+1] == 'A')):
                is_valid = False
            elif (a[i] == 'C' and a[i+1] == 'D') or (a[i] == 'D' and a[i+1] == 'C'):
                is_valid = False
        if is_valid:
            print(a)
    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            ballgame(a, lo + 1)
            a[lo], a[i] = a[i], a[lo]

# Question 4
def home_owners(a, b, lo):
    hi = len(a)
    if lo == hi:
        if len(b) == 3:
            is_valid = True
            if 'A' in b and 'B' not in b:
                is_valid = False
            elif 'C' in b and 'D' in b:
                is_valid = False
            if is_valid:
                print(b)
        return
    else:
        c = b[:]
        b.append(a[lo])
        home_owners(a, b, lo + 1)
        home_owners(a, c, lo + 1)

def main():
    a = ['A', 'B', 'C', 'D']
    #permute(a, 0, a[:])

    b = ["War and Peace", "Anna Karenina", "Magic Mountain", "Death in Venice", "Arms and the Man", "Candida"]
    #books(b, 0)

    c = ['A', 'B', 'C', 'D', 'E']
    ballgame(c, 0)

    d = ['A', 'B', 'C', 'D', 'E', 'F']
    #home_owners(d, [], 0)

main()
                                        
        
