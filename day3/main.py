import re

multPattern = re.compile("(mul\\([0-9]+,[0-9]+\\)|don't\\(\\)|do\\(\\))")
text = open('input.txt').read()
allOccurrences = multPattern.findall(text)

sum = 0
do = True
doPattern = "do()"
dontPattern = "don't()"
for m in allOccurrences:
    if m == doPattern:
        do = True
    elif m == dontPattern:
        do = False
    else:
        if do:
            print(m)
            nums = m.split('(')[1].split(')')[0].split(',')
            sum += (int(nums[0]) * int(nums[1]))
print(sum)