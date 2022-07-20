import sort

def swap(numbers, x, y):
    t = numbers[x]
    numbers[x] = numbers[y]
    numbers[y] = t

def quick_sort(numbers, start=None, end=None):
    if start is None:
        start = 0
        end = len(numbers) - 1
        
    p = end
    ls = 0
    s = False

    i = start
    while i < end:
        if numbers[i] > numbers[p]:
            if s:
                i += 1
                continue
            else:
                s = True
                ls = i
                i += 1
        else:
            if s:
                swap(numbers, i, ls)
                ls += 1
                i += 1
            else:
                i += 1
                continue
    if s:
        swap(numbers, p, ls)
    
if __name__ == '__main__':
    test = [8,12]
    nums = [10,7,12,8,3,2,6]
    nums2 = [1,5,8,4,7,3]
    quick_sort(test)
    quick_sort(nums2)
    print(nums2)
    print(test)