def wrapper(function1):
    def fun0(l):
        # complete the function
        function1(["+91 "+i[-10:-5]+" "+i[-5:] for i in l])
    return fun0

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
