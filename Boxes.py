#  File: Boxes.py

#  Description: Determines the set(s) where each box can be nested within the next box given a list of boxes and their
#               dimensions

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/13/19

#  Date Last Modified: 10/13/19

#finds all subsets of boxes regardless of nesting
def subsets_boxes(boxes,workingSubset,i,boxesSubset):
    if i == len(boxes):
        boxesSubset.append(workingSubset)
    else:
        c = workingSubset[:]
        workingSubset.append(boxes[i])
        i += 1
        subsets_boxes(boxes,c,i,boxesSubset)
        subsets_boxes(boxes,workingSubset,i,boxesSubset)

#checks subsets to see if they can be nested
def check_nesting(boxesSubset):
    maxNumNestingBoxes = 1
    maxNestingBoxes = []
    for i in range(len(boxesSubset)):
        validNest = True
        #compares adjacent boxes in a sorted subset
        for j in range(len(boxesSubset[i])-1):
            #compares each dimension
            for k in range(3):
                if boxesSubset[i][j][k] >= boxesSubset[i][j+1][k]:
                    validNest = False
                    break
            if not validNest:
                break
        #if number of boxes is greater, redefine the number of maximum nesting boxes
        if validNest and len(boxesSubset[i]) > maxNumNestingBoxes:
            maxNumNestingBoxes = len(boxesSubset[i])
            maxNestingBoxes = [boxesSubset[i]]
        #if number of boxes is the same, add the subset to a list of qualifying subsets
        elif validNest and len(boxesSubset[i]) == maxNumNestingBoxes:
            maxNestingBoxes.append(boxesSubset[i])
    return maxNumNestingBoxes, maxNestingBoxes

def main():
    with open('boxes.txt','r') as inFile:
        numBox = int(inFile.readline())
        boxes = []
        for i in range(numBox):
            listLine = list(map(int,inFile.readline().strip().split()))
            listLine.sort()
            boxes.append(tuple(listLine))
        boxes = sorted(boxes)
    boxesSubset = []
    subsets_boxes(boxes, [], 0, boxesSubset)
    maxNumNestingBoxes, maxNestingBoxes = check_nesting(boxesSubset)
    if maxNumNestingBoxes > 1:
        print('Largest Subset of Nesting Boxes')
        for i in range(len(maxNestingBoxes)-1,-1,-1):
            for j in range(len(maxNestingBoxes[0])):
                print(maxNestingBoxes[i][j])
            print()
    else:
        print('No Nesting Boxes')
main()