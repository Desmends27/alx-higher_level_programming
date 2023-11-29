#include "lists.h"
/**
 * insert_node - inserts a node into a sorted linked list
 * @head: pointer to a pointer of the head node
 * @number: number to be inserted
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t  *new, *next, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	current = *head;
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	else
	{
		while (current->next != NULL)
		{
			next = current->next;
			if ((*head)->n > number)
			{
				new->next = *head;
				*head = new;
				return (new);
			}
			else if (current->n < number)
			{
				if (next->n > number)
				{
					new->next = next;
					current->next = new;
					return (new);
				}
				else if (next->next == NULL && (next->n > number))
				{
					next->next= new;
					new->next = NULL;
				}
			}
			else if (current->n == number)
			{
				new->next = next;
				current->next = new;
				return (new);
			}
			next = next->next;
			current = current->next;
		}
	}
	if (current->next == NULL)
	{
		current->next = new;
		new->next = NULL;
		return (new);
	}
	return (NULL);
}
