// ssort.h - a delightful collection of selection sort algorithms for different types.

// Checks that an int array has been sorted.
int int_chk(int *a, const size_t len);

// Swaps ints in a[i] and a[j].
void int_swap(int *a, const unsigned i, const unsigned j);

// Sorts the int array a, from index l to index r.
void int_ssort(int *a, const unsigned l, const unsigned r);
