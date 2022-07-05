import random

# generate a list of random ints (between start and stop) of a length between start and stop.
def gen_random_int_list(start_int=0, stop_int=10, start_len=5, stop_len=10):
  l = []
  for i in range(random.randint(start_len,stop_len)):
    l.append(random.randint(start_int,stop_int))
  return l

def is_bigger(x, y):
  return x >= y

def is_smaller(x, y):
  return x <= y

def is_sorted(l, fun):
  for i in range(1, len(l)):
    if not fun(l[i-1], l[i]):
      return False
  return True

def swap(l, x, y):
  t = l[x]
  l[x] = l[y]
  l[y] = t

def bubble_sort(nums):
  n = len(nums) - 1
  for i in range(0, n):
    for j in range(0,n-i):
      if nums[j] > nums[j+1]:
        swap(nums, j, j+1)

def merge_sort(nums):
  n = len(nums)
  if n > 1:
    m = n//2
    l = nums[:m]
    r = nums[m:]
    a = merge_sort(l)
    b = merge_sort(r)
    return merge(a, b)
  else:
    return nums

def quick_sort(nums, start, end):
  n = end - start
  if n > 0:
    i = start
    p = end
    while i != p:
      if nums[i] > nums[p]:
        while nums[i] > nums[p]:
          if i == (p - 1):
            swap(nums, p, i)
            p -= 1
          else:
            swap(nums, p, p-1)
            swap(nums, i, p)
            p -= 1
      else:
        i += 1

    if p != start:
      l_start = start
      l_end = p - 1
      quick_sort(nums, l_start, l_end)

    if p != end:
      r_start = p + 1
      r_end = end
      quick_sort(nums, r_start, r_end)

  else:
    return

def merge(l, r):
  c =[]
  while len(l) > 0 and len(r) > 0:
    if l[0] < r[0]:
      c.append(l[0])
      del l[0]
    else:
      c.append(r[0])
      del r[0]
  while len(l) > 0:
    v = l.pop(0)
    c.append(v)
  while len(r) > 0:
    v = r.pop(0)
    c.append(v)
  return c

def radix_sort_lsb(nums):
  def max_radix(nums):
    max_radix = 1
    for i in range(len(nums)):
      num_len = len(str(nums[i]))
      if num_len > max_radix:
        max_radix = num_len
    return max_radix

  max_radix = max_radix(nums)
  i = 0
  #bucket = [ [] for i in range(10 ** max_radix) ]
  bucket = [ [] for i in range(10) ]
  while i < max_radix:
    if i == 0:
      for j in range(len(nums)):
        # Calculate max radix
        num = str(nums[j])
        num_len = len(num)
        if num_len > max_radix:
          max_radix = num_len
        # Add values to bucket
        lsb = num[-1:]
        bucket[int(lsb)].append(num)
    else:
      #copy bucket
      copy = bucket.copy()
      #create new empty bucket
      bucket = [ [] for i in range(10) ]
      for partition in copy:
        if len(partition) > 0:
          for num in partition:
            if len(num) <= i:
              num = '0' + num
              bucket[0].append(num)
            else:
              digit = int(num[-1 - i])
              bucket[digit].append(num)
    i += 1
  res = []
  for partition in bucket:
    if len(partition) > 0:
      for num in partition:
        res.append(int(num))
  return res


if __name__ == '__main__':
  print("testing quick_sort")
  for i in range(10):
    original = gen_random_int_list()
    copy = original.copy()
    quick_sort(copy, 0, len(copy)-1)
    if not is_sorted(copy, is_smaller):
      print("list not sorted correctly")
      print(original)
      print(copy)
  print("testing bubble_sort")
  for i in range(10):
    original = gen_random_int_list()
    copy = original.copy()
    bubble_sort(copy)
    if not is_sorted(copy, is_smaller):
      print("list not sorted correctly")
      print(original)
      print(copy)
  print("testing merge_sort")
  for i in range(10):
    original = gen_random_int_list()
    copy = original.copy()
    copy = merge_sort(copy)
    if not is_sorted(copy, is_smaller):
      print("list not sorted correctly")
      print(original)
      print(copy)

  print("testing radix_sort")
  for i in range(10):
    original = gen_random_int_list()
    copy = radix_sort_lsb(original)
    print(copy)
    if not is_sorted(copy, is_smaller):
      print("list not sorted correctly")
      print(original)
      print(copy)
