# TODO Найдите количество книг, которое можно разместить на дискете
memory = 1.44*1024**2
pages = 100
linesPerPage = 50
symbolsPerLine = 25
symbolMemory = 4

memoryPerBook = pages * linesPerPage * symbolsPerLine * symbolMemory

print("Количество книг, помещающихся на дискету:", int(memory/memoryPerBook))
