# import the django models module
from django.db import models

# Classes will more or less map to a table in the database
class ToDoList(models.Model):
	"""
	A Model for representing single line items in
	a ToDo List.
	"""
	# defines a required text field of 100 characters.
	title = models.CharField(max_length=100)

# This will represent individual tasks in a todo list
class ToDoListItem(models.Model):
	"""
	A Model for representing single line items in
	a ToDo List.
	"""
	# Define a foreign key relating this model to the todo list model.
	# The parent will be able to access it's items with the related_name
	# 'items'. When a parent is deleted, this will be deleted as well.
	todo_list = models.ForeignKey(
		ToDoList,
		related_name='items',
		on_delete=models.CASCADE
	)
	# this defines a required title that cannot be more than 100 characters.
	title = models.CharField(max_length=100)
	# this defines an arbitrary length text field which is optional.
	description = models.TextField(blank=True, default='')
