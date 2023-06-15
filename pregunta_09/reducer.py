import sys

elements = []

for row in sys.stdin:
    elements.append(row)

else:
    elements = sorted(
                        elements,
                        key = lambda data: (int(data.split()[2]))
                        )

    lista = elements[0:6]
    for element in lista:
        sys.stdout.write("{}".format(element))
