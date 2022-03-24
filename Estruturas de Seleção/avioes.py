competidores, nFolhas, nFolhasNecessarias = input().split()
competidores, nFolhas, nFolhasNecessarias = int(competidores),int(nFolhas), int(nFolhasNecessarias)


if competidores * nFolhasNecessarias  > nFolhas:
    print("N")
else:
    print("S")
