from django.test import TestCase
from todo.models import ToDoList, ToDoListItem

class ToDoListTestCase(TestCase):
	"""Tests for the todo list models"""

	def test_todo_list(self):
		"""Test creating a todo list with no items"""
		ToDoList.objects.create(title="Test List")

		# verify the object was saved
		todo_list = ToDoList.objects.get(title="Test List")
		# verify the data is accurate and exists
		self.assertEqual(todo_list.title, "Test List")

		# delete the list
		todo_list.delete()

		# try to retrieve the todo list
		try:
			retrieved_list = ToDoList.objects.get(title="Test List")
		except ToDoList.DoesNotExist:
			retrieved_list = None

		self.assertEqual(retrieved_list, None)

	def test_todo_list_items(self):
		"""
		This test creates a todo list, adds an item to it, and verifies
		that item is accessible through the 'items' related name.
		Then, it deletes everything.
		"""
		todo_list = ToDoList.objects.create(title="Test")
		todo_list_item = ToDoListItem.objects.create(
			todo_list=todo_list,
			title="Test Item",
			description="This is a test todo list item")

		# verify that the related name returns the todo_list item
		self.assertEqual(todo_list.items.count(), 1)
		self.assertEqual(todo_list.items.first(), todo_list_item)

		todo_list.delete()

		# verify the todo list item was deleted with the list
		# due to the CASCADE attribute we gave our model
		try:
			retrieved_item = ToDoListItem.objects.get(title="Test Item")
		except ToDoListItem.DoesNotExist:
			retrieved_item = None
		self.assertEqual(retrieved_item, None)

