import sort

def __swap(input_list, num1, num2):
    t = input_list[num1]
    input_list[num1] = input_list[num2]
    input_list[num2] = t

def new_bubble_sort(input_list, reverse=False, key=None):
    def __ascending(num1, num2):
        if num1 > num2:
            return True
        else:
            return False

    def __descending(num1, num2):
        if num1 < num2:
            return True
        else:
            return False
        
    def __default_key(val):
        return val

    if key is None:
        key = __default_key
    
    if reverse:
        comparator = __descending
    else:
        comparator = __ascending
    
    for i in input_list:
        for j in range(len(input_list) - 1):
            if comparator(key(input_list[j]), key(input_list[j+1])):
                __swap(input_list, j, j+1)
                
if __name__ == '__main__':
    print("testing bubble_sort")
    for i in range(10):
        original = sort.gen_random_int_list()
        copy = original.copy()
        new_bubble_sort(copy, reverse=True)
        if not sort.is_sorted(copy, sort.is_smaller):
            print("list not sorted correctly")
            print(original)
            print(copy)