N = int(input())
arr = list()
nope = list()
want_print_list = list()

for i in range(2*N):
    if i % 2 == 0:
        nope.append(input())
    if i % 2 == 1:
        arr.append(input())


for string in arr:
    want_print = True
    for position in range(len(string)):
        if string[position] in string[position+1:] and string[position] != string[position + 1]:
            print("NO")
            want_print = False
            break
    if want_print:
        print("Yes")
