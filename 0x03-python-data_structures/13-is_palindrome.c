#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - A function that checks if a list is it a palin or not
 * @head: A struct
 * Return: 1 or 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *first = *head, *last = NULL;

	while (first)
	{
		while (*head)
		{
			if (*head == last)
				break;
			*head = (*head)->next;
		}
		last = *head;
		if (first->n != last->n)
			return (0);
		first->next = first;
	}
	return (1);
}
