#include <stdio.h>

#define DLLEXPORT extern "C" __declspec(dllexport)

int test();

DLLEXPORT int sum(int a, int b) {
//	test();
	return a + b;
}


DLLEXPORT get_str_list(int n, char *b[2])
{
	for(int i=0;i<n;i++)
 	{
  		printf("%s\n", *(b+i));
 	}
}

DLLEXPORT get_int_list(int n, int *b[])
{
	for(int i=0;i<n;i++)
 	{
  		printf("%d:%d,", i,b[i]);
 	}
}

DLLEXPORT call_func(void *func())
{
	(*func)();
}