#  File: BST_Cipher.py

#  Description: Creates a binary search tree given an encryption key. Can be used to encrypt or decrypt messages based
#  on traversal through the tree

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11/17/2019

#  Date Last Modified: 11/17/2019
class Node (object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = Node(encrypt_str[0])
        for ch in encrypt_str:
            self.insert(ch)

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        previous = self.root
        current = self.root
        while current != None:
            previous = current
            if ch == current.data:
                return
            elif ch > current.data:
                current = current.right_child
            else:
                current = current.left_child
        if ch > previous.data:
            previous.right_child = Node(ch)
        else:
            previous.left_child = Node(ch)

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        current = self.root
        string = ''
        if ch == current.data:
            return '*'
        while current != None:
            if ch == current.data:
                return string
            elif ch > current.data:
                string += '>'
                current = current.right_child
            else:
                string += '<'
                current = current.left_child
        return ''

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        if len(st) == 0:
            return ''
        current = self.root
        if st == '*':
            return self.root.data
        for ch in st:
            if current == None:
                return ''
            elif ch == '>':
                current = current.right_child
            else:
                current = current.left_child
        return current.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        st = st.lower()
        encryptSt = ''
        for ch in st:
            if len(self.search(ch)) != 0:
                encryptSt += self.search(ch) + '!'
        return encryptSt[:-1]

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        decryptList = st.split('!')
        decryptSt = ''
        for i in decryptList:
            decryptSt += self.traverse(i)
        return decryptSt

def main():
    encryptKey = input('Enter encryption key: ')
    encryptionTree = Tree(encryptKey)
    print()
    encryptStr = input('Enter string to be encrypted: ')
    print('Encrypted string:', encryptionTree.encrypt(encryptStr))
    print()
    decryptStr = input('Enter stirng to be decrypted: ')
    print('Decrypted string: ', encryptionTree.decrypt(decryptStr))
main()
