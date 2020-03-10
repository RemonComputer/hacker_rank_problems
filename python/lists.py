# Link: https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        command_with_args = input().split()
        if command_with_args[0] == 'insert':
            l.insert(int(command_with_args[1]), int(command_with_args[2]))
        elif command_with_args[0] == 'print':
            print(l)
        elif command_with_args[0] == 'remove':
            l.remove(int(command_with_args[1]))
        elif command_with_args[0] == 'append': 
            l.append(int(command_with_args[1]))
        elif command_with_args[0] == 'sort':
            l.sort()
        elif command_with_args[0] == 'pop':
            l.pop()
        elif command_with_args[0] == 'reverse':
            l.reverse()
