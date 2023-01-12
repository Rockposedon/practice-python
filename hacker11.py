# def split_and_join(line):
#     line = line.split(" ")
#     line = "-".join(line)
#     return line
#
# if __name__ == '__main__':
#     line = input("enter the string : ")
#     result = split_and_join(line)
#     print(result)

# def print_full_name(first, last):
#     first_name = first
#     last_name = last
#     print('Hello', first, last+"!",'You just delved into python')
#
#
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# def mutate_string(string, position, character):
#     n = list(string)
#     n[position] = character
#     string = "".join(n)
#     return string

def mutate_string(string, position, character):


    l=list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)