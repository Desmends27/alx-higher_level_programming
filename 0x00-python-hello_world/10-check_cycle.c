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
	slow = list;
	if (list == NULL)
		return 0;

	while (fast != NULL && fast->next != NULL)
	{
		if (fast == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
