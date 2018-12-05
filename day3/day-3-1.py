import numpy as numpy


class Claim:
    def __init__(self, claimString):
        claim_list = claimString.split()
        self.id = int(claim_list[0].replace("#", ""))
        self.x = int(claim_list[2].split(",")[0])
        self.y = int(claim_list[2].split(",")[1].replace(":", ""))
        self.width = int(claim_list[3].split("x")[0])
        self.height = int(claim_list[3].split("x")[1])

    def mark_claim(self, cloth):
        for x in list(range(self.width)):
            for y in list(range(self.height)):
                cloth[x + self.x, y + self.y] += 1
        return cloth


# list that will contain instances of the Claim class
elf_claims = []
file = open("input.txt")
for line in file:
    elf_claims.append(Claim(line.strip("\n")))

cloth_matrix = numpy.zeros((1000, 1000))

for claim in elf_claims:
    claim.mark_claim(cloth_matrix)

overlapped_squared_inches = 0
for x in cloth_matrix:
    for y in x:
        if y > 1:
            overlapped_squared_inches += 1

print("Number of overlapped square inches: ", overlapped_squared_inches)
