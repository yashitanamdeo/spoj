t = int(input())
for _ in range(t):
    string = input()
    length = len(string)
    for i in range(0,(length//2), 2):
        print(string[i],end="")
    print("")