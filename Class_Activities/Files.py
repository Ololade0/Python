with open("hello.txt",mode="r", encoding="utf-8") as file:
    # file.write('ololade')

     read = file.read()
     print(read)
    # for index, line in enumerate(file.readlines()):
    #     print(f"line {index + 1}: {line}")