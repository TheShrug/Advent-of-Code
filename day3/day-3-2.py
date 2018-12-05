class Claim:
    def __init__(self, claim_string):
        claim_list = claim_string.split()
        self.id = int(claim_list[0].replace("#", ""))
        self.x = int(claim_list[2].split(",")[0])
        self.y = int(claim_list[2].split(",")[1].replace(":", ""))
        self.width = int(claim_list[3].split("x")[0])
        self.height = int(claim_list[3].split("x")[1])
        self.overlapped = False

    def mark_claim(self, cloth):
        for x in list(range(self.width)):
            for y in list(range(self.height)):
                cloth[x + self.x][y + self.y][0] += 1
                cloth[x + self.x][y + self.y][1].append(self.id)


# list that will contain instances of the Claim class
elf_claims = []

file = open("input.txt")
for line in file:
    claim = Claim(line.strip("\n"))
    elf_claims.append(claim)

cloth_matrix = []
for row in range(1000):
    cloth_matrix.append([])

for row in cloth_matrix:
    for i in range(1000):
        row.append([0,[]])

for claim in elf_claims:
    claim.mark_claim(cloth_matrix)

overlapped_squared_inches = 0
set_of_overlapped_claims = set()

for x in cloth_matrix:
    for y in x:
        if y[0] > 1:
            overlapped_squared_inches += 1
            for id in y[1]:
                set_of_overlapped_claims.add(id)

for claim in elf_claims:
    if claim.id not in set_of_overlapped_claims:
        print("Claim that does not overlap any others:", claim.id)

print("Number of overlapped square inches: ", overlapped_squared_inches)
