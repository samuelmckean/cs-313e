#  File: Reducible.py

#  Description: Prints the longest reducible words in the English language.
#               Uses hashing for faster array accessing and memoized 
#               recursion in determining if a word is reducible.

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/24/19

#  Date Last Modified: 10/25/19

import time

# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime(n):
  if n == 1:
    return False

  limit = int(n ** 0.5) + 1
  div = 2
  while div < limit:
    if n % div == 0:
      return False
    div += 1
  return True

# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word(s, size):
  hash_idx = 0
  for j in range(len(s)):
    letter = ord(s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word (s, hash_table):
  key = hash_word(s, len(hash_table))
  if hash_table[key] == "":
    hash_table[key] = s
    return
  # collision occured so double hash
  i = 1
  # find good sized prime number for double hashing
  prime = len(hash_table) // 5
  while not is_prime(prime):
    prime += 1
  step_size = prime - (key % prime)
  while hash_table[(key + i * step_size) % len(hash_table)] != "":
    i += 1
  hash_table[(key + i * step_size) % len(hash_table)] = s

# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word (s, hash_table):
  key = hash_word(s, len(hash_table))
  if hash_table[key] == "":
    return False
  elif hash_table[key] == s:
    return True
  # find good sized prime number for double hashing
  prime = len(hash_table) // 5
  while not is_prime(prime):
    prime += 1
  step_size = prime - (key % prime)
  for i in range(len(hash_table)):
    if hash_table[(key + i * step_size) % len(hash_table)] == "":
      return False
    elif hash_table[(key + i * step_size) % len(hash_table)] == s:
      return True
  return False

# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise
def is_reducible (s, hash_table, hash_memo):
  # base case: reduced word in hash_memo
  if find_word(s, hash_memo):
    return True
  # base case: length of word is 1 and not in hash_memo
  elif len(s) == 1:
    return False
  # base case: word not in hash_table (not a word)
  elif not find_word(s, hash_table):
    return False
  # recursive case
  else:
    for i in range(len(s)):
      if is_reducible(s[:i] + s[i+1:], hash_table, hash_memo):
        insert_word(s, hash_memo)
        return True
    return False

# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words (string_list):
  max_length = 0
  for word in string_list:
    if len(word) > max_length:
      max_length = len(word)
  longest_word_list = []
  for word in string_list:
    if len(word) == max_length:
      longest_word_list.append(word)
  return longest_word_list      

def main():
  # create an empty word_list
  word_list = []

  # open the file words.txt
  with open("words.txt", 'r') as in_file:
    # read words from words.txt and append to word_list
    for word in in_file:
      word_list.append(word.strip())
  # close file words.txt

  # find length of word_list
  num_of_words = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  N = 2 * num_of_words + 1
  while not is_prime(N):
    N += 1

  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  for i in range(N):
    hash_list.append("")

  # hash each word in word_list into hash_list
  # for collisions use double hashing
  for word in word_list:
    insert_word(word, hash_list)
  
  # create an empty hash_memo
  hash_memo = []

  # populate the hash_memo with M blank strings
  M = 27001
  while not is_prime(M):
    M += 1
  for i in range(M):
    hash_memo.append("")

  # populate hash_memo with a, i, and o
  one_letter_words = ['a', 'i', 'o']
  for word in one_letter_words:
    insert_word(word, hash_memo)

  # create an empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  for word in word_list:
    if is_reducible(word, hash_list, hash_memo):
      reducible_words.append(word)

  # find words of the maximum length in reducible_words
  max_length_words = get_longest_words(reducible_words)
  
  # print the words of maximum length in alphabetical order
  # one word per line
  for word in max_length_words:
    print(word)

# This line above main is for grading purposes. It will not 
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()