# Create a function that takes a list of numbers as parameter
# Returns a list where the elements are sorted in ascending numerical order
# Make a second boolean parameter, if it's true sort that list descending

my_list = [12, 5, 13, 8, 9, 65]
# switch
descent = False

def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False

    while not sorted and descent is False:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
    while not sorted and descent is True:
        sorted = True
        for i in range(length):
            if bad_list[i] < bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
    else:
            return bad_list

print(bubble(my_list))

