# Question 1

def secretary(letters, start):
    size = len(letters)
    # base case 
    if start >= size:
        print(letters)
    # recursive case
    else:
        for i in range(start + 1, size):
            letters[start], letters[i] = letters[i], letters[start]
            secretary(letters, start + 1)
            letters[start], letters[i] = letters[i], letters[start]

def main():
    a = ['A', 'B', 'C', 'D']
    secretary(a, 0)
