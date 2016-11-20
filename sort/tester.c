#include <time.h>
#include <stdlib.h>

#include "ssort.h"

#define SIZE 5

int main(void)
{
	int a[SIZE];

	srand(time(NULL));

	for (int i = 0; i < SIZE; i++) {
		a[i] = rand() & 10;
	}

	int_ssort(a, 0, SIZE - 1);
	
	return 0;
}
	
