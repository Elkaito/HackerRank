def wrapper(f):
    def fun(l):
        # complete the function
        fun = [] 
        for i in l:
            num = i[-10:]
            formated_num = '+91 {} {}'.format(num[:5],num[-5:])
            fun.append(formated_num)    
        fun = f(fun)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 