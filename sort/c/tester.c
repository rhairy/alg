#include <time.h>
#include <stdlib.h>

#include "ssort.h"

#define SIZE 5

int main(void)
{
	int a[SIZE];
	int f[5] = { 1, 2, 3, 4, 3 };

	srand(time(NULL));

	for (int i = 0; i < SIZE; i++) {
		a[i] = rand();
	}

	int_ssort(a, 0, SIZE - 1);

	if (!int_chk(f, 5)) {
		return -1;
	}

	if (int_chk(a, SIZE)) {
		return -1;
	}

	return 0;
}
	
