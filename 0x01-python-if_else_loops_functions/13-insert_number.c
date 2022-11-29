#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *prev;
	listint_t *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t *));
	if (new == NULL)
		return (NULL);
	temp = *head;
	new->n = number;
	while (temp != NULL)
	{
		if (number > temp->n)
		{
			prev->next = new;
			new->next = temp;
		}
		prev = temp;
		temp = temp->next;
	}
	free_listint(temp);
	free_listint(prev);
	return (new);
}
