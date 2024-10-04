info = list(input().split(' '))
health = info[0]
score = info[1]
level = info[2]
with open("task2.txt", "w") as file:
    file.write(f"Health: {health}\n"
               f"Score: {score}\n"
               f"Level: {level}\n")
    file.close()

print("[1] read from text file")
print("[2] get info from text file")
option = input()

if option == "1":
    with open("task2.txt", "r") as file:
        print(file.read())
    with open("task2.txt", "w") as file:
        health = info[0]
        score = info[1]
        level = info[2]
        file.write(f"Health: {health}\n"
                   f"Score: {score}\n"
                  f"Level: {level}\n")
        file.close()
elif option == "2":
    with open("task2.txt", "w") as file:
        get_info = input()
        if get_info == "health":
            with open("task2.txt", "r") as file:
                for x in file:
                    if x == 1:
                        print(file.readline())
                        file.close()
        elif get_info == "score":
            with open("task2.txt", "r") as file:
                for x in file:
                    if x == 2:
                        print(file.readline())
                        file.close()
        elif get_info == "level":
            with open("task2.txt", "r") as file:
                for x in file:
                    if x == 3:
                        print(file.readline())
                        file.close()
        else:
            get_info = input()
else:
    print("[1] read from text file")
    print("[2] get info from text file")
    option = input()