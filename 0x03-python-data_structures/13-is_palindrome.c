#include "lists.h"
/**
 * is_palindrome : checks if a linked list is a palindrome
 * @head: pointer to the the head node pointer
 * Return: 0 if not a palindrome 
 * 1 if is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	int *check = malloc(10 * sizeof(int));
	int i = 0;

	if (check == NULL)
		return NULL;
	slow = *head;
	fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next;
		if (i > 10)
		{
			check = realloc(check, 10 * sizeof(int));
			if (check == NULL)
				return NULL;
		}
		check[i] = slow->n;
		slow = slow->next;
		i++;
	}
}
