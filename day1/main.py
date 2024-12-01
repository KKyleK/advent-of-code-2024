inputText = open('input.txt')
list1 = []
list2 = []

nextLine = inputText.read().splitlines()

for n in nextLine:
    lineValues = n.split(' ')
    list1.append(lineValues[0])
    list2.append(lineValues[1])

list1.sort()
list2.sort()

counter=0
difference = 0
while counter < len(list1):
    difference += abs(int(list1[counter]) - int(list2[counter]))
    counter+=1
print(difference)

#2: add up each number in the left list, after multiplying it by the number of times it appears in the left list.
counter = 0
similarity=0
for l in list1:
    count = 0
    for r in list2:
        if int(l) == int(r):
            count+=1
    similarity+= int(l)*count

print(similarity)