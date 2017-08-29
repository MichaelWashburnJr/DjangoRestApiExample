from django.test import TestCase
from todo import serializers

class ToDoListTestCase(TestCase):
    """Tests for the todo list models"""

    def test_todo_list_create(self):
        """
        Define some json data we expect to receive and use the 
        serializer to parse it into models. Test the models
        to make sure they're correct.
        """
        # define data that resembles what would come through the API.
        # A Python dictionary is often what JSON data is parsed into initially.
        data = {
            'title': 'Test List',
            'items': [
                {
                    'title': 'Test Item 1',
                    'description': 'This is test item 1'
                },
                {
                    'title': 'Test Item 2',
                    'description': 'This is test item 2'
                }
            ]
        }

        # pass the data into the serializer to try and parse it
        serializer = serializers.ToDoList(data=data)
        # verify that the serializer thinks the data is valid
        self.assertTrue(serializer.is_valid())

        # get the object parsed from the serializer
        todo_list = serializer.save()

        # verify the title is correct
        self.assertEqual(todo_list.title, 'Test List')
        # verify it has two items
        self.assertEqual(todo_list.items.count(), 2)
