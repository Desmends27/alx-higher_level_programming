#include "lists.h"
/**
 * check_cycle - check if node has a cycle
 * @list: head of linked list
 * Return: 1 if cycle, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	const listint_t *slow;
	const listint_t *fast;

	fast = list->next;
	slow = list->next;
	if (list == NULL)
		return 0;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
			return (1);
	}
	return (0);
}
