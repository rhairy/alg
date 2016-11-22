// Checks that an int array has been sorted.

#include <stdlib.h>

int int_chk(int *a, const size_t len)
{
	for (int i = 0; i < len - 1; i++) {
		if (a[i] > a[i + 1]) {
			return -1;
		}
	}
	return 0;
}

void int_swap(int *a, const int i, const int j)
{
	int tmp = a[i];
	a[i] = a[j];
	a[j] = tmp;
}

void int_ssort(int *a, const unsigned l, const unsigned r)
{
	int min;
	  
	for (unsigned i = 0; i < r; i++) {
		min = i;
		for (unsigned j = i + 1; j <= r; j++) {
			if (a[j] < a[min]) {
				min = j;	
			}	
		}
		int_swap(a, i, min);
	}
}

