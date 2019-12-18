
# Lecture Notes on 04 Oct 2019

def permute (a, lo):
  hi = len(a)
  if (lo == hi):
    print (a)
  else:
    for i in range (lo, hi):
      a[lo], a[i] = a[i], a[lo]
      permute (a, lo + 1)
      a[lo], a[i] = a[i], a[lo]

def main():
  a = ['A', 'B', 'C', 'D', 'E']
  permute (a, 0)

main()

