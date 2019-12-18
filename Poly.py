#  File: Poly.py

#  Description: Uses the LinkedList class to represent polynomial functions with methods to add and multiply
#               two polynomials.

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11/10/19

#  Date Last Modified: 11/10/19

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
    def __init__ (self):
        self.first = None

    # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        link = Link(coeff, exp)
        current = self.first
        # check if LinkedList is empty
        if current == None:
            self.first = link
            return
        # new link should go at head
        if current.exp <= exp:
            link.next = self.first
            self.first = link
            return
        # loop through the rest of the list
        while current.next != None and current.next.exp >= exp:
            current = current.next
        current.next = link
        return

    # add polynomial p to this polynomial and return the sum
    def add (self, p):
        newPoly = LinkedList()
        # check if either polynomial is empty
        if self.first == None:
            if p.first == None:
                print('Both polynomials are empty')
                return
            return p
        if p.first == None:
            return self
        currentSelf = self.first
        currentP = p.first
        # loop while either polynomial is not None
        while currentSelf != None or currentP != None:
            # self has run out
            if currentSelf == None:
                while currentP != None:
                    newPoly.insert_in_order(currentP.coeff, currentP.exp)
                    currentP = currentP.next
                return newPoly
            # p has run out
            if currentP == None:
                while currentSelf != None:
                    newPoly.insert_in_order(currentSelf.coeff, currentSelf.exp)
                    currentSelf = currentSelf.next
                return newPoly
            # self and p have the same order
            if currentSelf.exp == currentP.exp:
                newCoeff = currentSelf.coeff + currentP.coeff
                # check that the coefficient is non-zero
                if newCoeff != 0:
                    newPoly.insert_in_order(newCoeff, currentSelf.exp)
                currentSelf = currentSelf.next
                currentP = currentP.next
            else:
                # self is greater order
                if currentSelf.exp > currentP.exp:
                    newPoly.insert_in_order(currentSelf.coeff, currentSelf.exp)
                    currentSelf = currentSelf.next
                # p is greater order
                else:
                    newPoly.insert_in_order(currentP.coeff, currentP.exp)
                    currentP = currentP.next
        return newPoly

    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        newPoly = LinkedList()
        # check if either is empty
        if self.first == None:
            if p.first == None:
                print('Both polynomials are empty')
                return
            return p
        if p.first == None:
            return self
        currentSelf = self.first
        # loop through self polynomial
        while currentSelf != None:
            tempPoly = LinkedList()
            currentP = p.first
            # loop through p polynomial
            while currentP != None:
                tempPoly.insert_in_order(currentSelf.coeff * currentP.coeff, currentSelf.exp + currentP.exp)
                currentP = currentP.next
            newPoly = newPoly.add(tempPoly)
            currentSelf = currentSelf.next
        return newPoly

    # create a string representation of the polynomial
    def __str__(self):
        string = ''
        current = self.first
        # check if LinkedList is empty
        if current == None:
            print('Polynomial is empty')
            return string
        while current.next != None:
            tupe = (current.coeff, current.exp)
            string += str(tupe) + ' + '
            current = current.next
        string += str((current.coeff, current.exp))
        return string

def main():
    # read input file
    with open('poly.txt','r') as inFile:
        linksP = int(inFile.readline())
        p = LinkedList()
        # create linked lists p and q
        for i in range(linksP):
            coeff, exp = list(map(int, inFile.readline().strip().split()))
            p.insert_in_order(coeff, exp)
        inFile.readline()
        linksQ = int(inFile.readline())
        q = LinkedList()
        for i in range(linksQ):
            coeff, exp = list(map(int, inFile.readline().strip().split()))
            q.insert_in_order(coeff, exp)
        # sum p and q
        print('Sum:', p.add(q))
        # multiply p and q
        print('Product:', p.mult(q))

if __name__ == "__main__":
    main()
