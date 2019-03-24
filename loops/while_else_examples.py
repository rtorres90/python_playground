test_list = [2, 4, 5, 6, 10]

while test_list:
    print test_list.pop()
else:
    print "The list is empty."

test_list = [2, 4, 5, 6, 10]

while test_list:
    current_item = test_list.pop()
    if current_item % 2 == 0:
        print current_item
    else:
        print "An odd number was found!! Breaking the loop" 
else:
    print "The list is empty."

test_list = []

# The 'test_list' list is empty, therefore the interpreter will go directly to the else statement of the loop.
while test_list:
    print test_list.pop()
else:
    print "list done!"
