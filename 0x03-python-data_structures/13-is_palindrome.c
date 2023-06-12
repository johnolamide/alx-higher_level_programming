#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palimdrome - checks if a single linked list is palindrome
 * @head: pointer to the head node
 * Return: returns 0 if not palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int len = 0, i = 0;
	int arr[4096];

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (current != NULL)
	{
		arr[len] = current->n;
		len++;
		current = current->next;
	}

	for (i = 0; i < len / 2; i++)
	{
		if (arr[i] != arr[len - i - 1])
		return (0);
	}
	return (1);
}
