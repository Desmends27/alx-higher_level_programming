#include "lists.h"
/**
 * check_cycle - check if node has a cycle
 * @list: head of linked list
 * Return: 1 if cycle, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	fast = list->next;
	slow = list->next;

	while (slow->next != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
			return (1);
	}
	return (0);
}
