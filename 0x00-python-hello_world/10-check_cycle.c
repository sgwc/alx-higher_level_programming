#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if the linked list has a cycle or not
 * @list: head the of the cycle
 *
 * Return: 0 if no cycle 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *hare = list;

	while (turtle != NULL && hare != NULL && hare->next != NULL)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if (turtle == hare)
			return (1);
	}
	return (0);
}
