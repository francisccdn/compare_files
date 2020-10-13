import sys
import unidecode

if len(sys.argv) != 3:
    print("Error: Needs 2 files")
    sys.exit

filePaths = [sys.argv[i] for i in range(1, len(sys.argv))]

lines = []
for path in filePaths:
    file = open(path, "r")
    lines.append(file.readlines())

for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        lines[i][j] = unidecode.unidecode(lines[i][j].lower().rstrip("\n"))

commonLines = []
for i in range(0, len(lines[0])):
    for j in range(0, len(lines[1])):
        if lines[0][i] == lines[1][j]:
            commonLines.append(lines[0][i])

found = True
while found:
    found = False

    for line in lines[0]:
        for commonLine in commonLines:
            if line == commonLine:
                lines[0].remove(line)
                found = True

    for line in lines[1]:
        for commonLine in commonLines:
            if line == commonLine:
                lines[1].remove(line)
                found = True


result = "Common to both:\n----------\n"
for line in commonLines:
    result = result + line + "\n"
for i in range(0, 2):
    result = result + "----------\nOnly in " + filePaths[i] + ":\n----------\n"
    for line in lines[i]:
        result = result + line + "\n"

output = open("output.txt", "w+")
output.write(result)