# Exercise 3-2
#Function to repeat twice

# passing function object as a parameter to do_twice function
def do_twice(func):
    func() # call the function object twice
    func()
    
def print_spam():
    print("Printing the output twice by passing function object to a function")

# call do_twicw function and pass print_spam function as parameter
do_twice(print_spam)

# Modified the above function as per the problem
# passing function object as a parameter and text as value to do_twicewithvalObj function
def do_twicewithvalObj(func,text):
    func(text) # call the function object twice
    func(text)
    
def print_spam(print_text):
    print(print_text)

# call do_twicw function and pass print_spam function as parameter and text as value
do_twicewithvalObj(print_spam,"Printing the output twice by passing function object and value as parameters to a function")

# Exercise 3-3.
# write a function to draw a grid

def draw_grid():
    print('+','-','-','-','-','+','-','-','-','-','+')
    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
    print('+','-','-','-','-','+','-','-','-','-','+')
    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
    print('+','-','-','-','-','+','-','-','-','-','+')
    
draw_grid()

def row_column_grid():
    print('-','-','-','-','-','-','-','-','-')
    print('|',' ','|',' ','|',' ','|',' ','|') 
    print('|',' ','|',' ','|',' ','|',' ','|')
    print('-','-','-','-','-','-','-','-','-')
    print('|',' ','|',' ','|',' ','|',' ','|') 
    print('|',' ','|',' ','|',' ','|',' ','|')
    print('-','-','-','-','-','-','-','-','-')
    print('|',' ','|',' ','|',' ','|',' ','|') 
    print('|',' ','|',' ','|',' ','|',' ','|')
    print('-','-','-','-','-','-','-','-','-')
    print('|',' ','|',' ','|',' ','|',' ','|') 
    print('|',' ','|',' ','|',' ','|',' ','|')
    print('-','-','-','-','-','-','-','-','-')

row_column_grid()