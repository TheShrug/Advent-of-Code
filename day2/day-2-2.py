file = open("input.txt")
boxes = []
for line in file:
    boxes.append(line.strip("\n"))

for index, box in enumerate(boxes):
    i = index
    while i < boxes.__len__():
        misMatched = 0
        brokenIndex = 0
        for charIndex, char in enumerate(box):
            if boxes[i][charIndex] != char:
                misMatched += 1
                brokenIndex = charIndex
        if misMatched == 1:
            commonLetters = box[:brokenIndex] + box[brokenIndex + 1:]
            print("Common letters between the correct box IDs: ", commonLetters)
        i += 1
