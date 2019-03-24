test_list1 = [2, 4, 5, 6, 10]
test_list2 = []


for item in test_list1:
    print item
else: # The 'else' block will be runned only if the main loop was not ended for a 'break' statement
    print "list done!"

for item in test_list1:
    if item % 2 == 0:
        print item
    else:
        print "The list contains an odd number! breaking the loop!"
        break
else: # it should not be executed.
    print "list done!"

# The 'test_list2' list is empty, therefore the interpreter will go directly to the else statement of the loop.
for item in test_list2:
    print item
else:
    print "list done!"
