#include "lists.h"

/**
 * check_cycle - check if a linked list is a cycle
 * @list: pointer to head node
 * Return: 0 if no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	const listint_t *slow, *fast;
	/* use hare and tortise algorithim */
	if (list == NULL)
		return 0;
	fast = list->next;/* fast is always 2 steps ahead*/
	slow = list;
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
