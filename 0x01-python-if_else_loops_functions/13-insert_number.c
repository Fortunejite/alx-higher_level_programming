#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, prev, new;

	if (head == NULL || number == NULL)
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
