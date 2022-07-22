#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * main - creates 5 zombie processes
 *
 * Return: void
 */

int main(void)
{
	pid_t childPid;
	int i;

	for (i = 0; i < 5; i++)
	{
		childPid = fork();
		if (childPid == 0)
		{
			printf("Zombie process created, PID: %i\n", getpid());
			exit(0);
		}
	}

	while (1)
	{
		sleep(1);
	}
	return (0);
}
