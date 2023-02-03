
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

#PRINT OUTER STRAW
def print_space1(num):
    if num == 1:
        return
    print(' ', end='')
    return print_space1(num-1)
def print_straw(num):
    if num == 0:
        return
    print_straw(num - 1)
    print_space1(num)
    print('o')
#print_straw(straw_pos)
# PRINT DRINK
def print_star(n):
    if n == 1:
        return
    print('*', end='')
    print_star(n - 1)
# PRINT GLASS
def print_glass(n,i):
    if n == 0:
        return
    print_space1(glass_size-n+1)
    print('\\', end='')
    if glass_size-n>= i:
        print_star(n * 2 + 1)
    else:
        print_space1(straw_pos)
        print('o', end='')
        print_space1(2*n-straw_pos+1)
    print('/')
    print_glass(n - 1, i)

# BOTTOM1 OF THE GLASS
#print_space1(glass_size+1)
def print_bottom1(n):
    # base
    if n==0:
        return
    print('-', end='')
    # recursive call
    print_bottom1(n - 1)
#print_bottom1(2)
#print()
# BOTTOM2 OF THE GLASS
def print_line(n):
    if n==0:
        return
    print('|', end='')
    #recursive call
    print_line(n-1)
def print_bottom2(n):
    if n==0:
        return
    print_space1(glass_size + 1)
    print_line(2)
    print()
    # recursive call
    print_bottom2(n-1)
#print_bottom2(glass_size)

def number_of_glass(i,e):
    if i<=e:
        print_straw(straw_pos)
        print_glass(glass_size,i)
        print_space1(glass_size + 1)
        print_bottom1(2)
        print()
        print_bottom2(glass_size)
        number_of_glass(i+1,e)

c = 2*glass_size-straw_pos

if c%2 == 0:
    n = (c+2)//2
else:
    n = (c+1)//2
number_of_glass(0,n)


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

