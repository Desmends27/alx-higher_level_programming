#include "lists.h"
/**
 * is_palindrome- checks if a linked list is a palindrome
 * @head: pointer to the the head node pointer
 * Return: 0 if not a palindrome
 * 1 if is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	int list_num[1000];
	int i = 0;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	slow = *head;
	fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		list_num[i++] = slow->n;
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	while (slow != NULL)
	{
		if ((slow->n) != list_num[--i])
		{
			return (0);
		}
		slow = slow->next;
	}
	return (1);
}
