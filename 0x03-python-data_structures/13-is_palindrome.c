#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - main
 * @head : list
 * Return: 1 if palindrome or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t **last = head;
	int i = 0, j = 0;
	int flag = 0;

	if (head == NULL)
	{
		return (1);
	}
	while ((*last)->next != NULL)
	{
		i = i + 1;
		*last = (*last)->next;
	}
	i = i - 1;
	while (head != NULL)
	{
		if (head == last)
		{
			*head = (*head)->next;
			last = head;
			for (j = 0; j <= i; j++)
			{
				*last = (*last)->next;
			}
			i--;
			flag = 1;
		}
		else
			return (0);
	}
	return (flag);
}
