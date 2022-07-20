def swap(nums, x, y):
    t = nums[x]
    nums[x] = nums[y]
    nums[y] = t

def bubble_sort(nums):
    for i in nums:
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                swap(nums, j, j+1)

def merge(l, r):
    c = []
    while len(l) > 0 and len(r) > 0:
        if l[0] < r[0]:
            c.append(l[0])
            l.pop(0)
        else:
            c.append(r[0])
            r.pop(0)
    while len(l) > 0:
        c.append(l.pop())
    while len(r) > 0:
        c.append(r.pop())
    
    return c
            
def merge_sort(nums):
    print(nums)
    n = len(nums)

    if n > 1:
        m = n // 2
        l = merge_sort(nums[:m])
        r = merge_sort(nums[m:])
        return merge(l,r)
    else:
        return nums

def quick_sort(nums):
    if len(nums) > 1:
        # use last index as pivot
        p = nums[-1]

        new_list = []
        for i in ( x for x in nums if x <= p ):
            new_list.append(i)
        for i in ( x for x in nums if x > p):
            new_list.append(i)

        # find position to divide list
        m = new_list.index(p)

        l = quick_sort(new_list[:m])
        r = quick_sort(new_list[m:])

        for i in r:
            l.append(i)
        return l
    else:
        return nums
    
def radix_sort(nums):
    r = 0
    for i in nums:
        if len(str(i)) > r:
            r = len(str(i))
    l = [ [] for i in range(10**r) ]
    
    while i < r:
        
        
   # i = 0
   # while i < r:
        #c = l.copy()
        #for i in l:
            #if len(i) > 0:
                #for j in i:
                    #v = str(j)
                    
                        
            
        #i += 1
        
    return l
        
    
    
if __name__ == '__main__':
    nums = [5, 1, 3, 2, 0]
    rnums = [10,5,3,2,0]
    #bubble_sort(nums)
    print(radix_sort(rnums))
                