# Write code for algorithm 2 below

#  2. Write a function that prints the natural numbers from 1 to n.

def natural_numbers(x,i=1):
	#your code 
    if i > x:
        return
    else:
        print(i)
        natural_numbers(x, i+1)

natural_numbers(3)
#output: 1 2 3