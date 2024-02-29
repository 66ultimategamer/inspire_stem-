def sum_nums(x,y):
    return x+y

z=sum_nums(10,20)
print (z)

def product_nums(x,y):
    return x*y
z=product_nums(10,20)
print (z)


# how to use for loop inside a fnction inside a function
def print_odds(f_num,l_num):
    for i in range (f_num,l_num):
        print(i%2)

print_odds(0,15)