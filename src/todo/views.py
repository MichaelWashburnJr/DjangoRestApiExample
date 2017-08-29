from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo import serializers, models

class ToDoList(APIView):
	"""
	List all todo lists when the GET method is called. 
	Add new ToDo lists when the POST method is called.
	Delete a ToDo list when the DELETE method is called.
	"""

	def get(self, request, format=None):
		"""
		Return a list of all the ToDoList objects in the database.
		"""
		# query the database for all instances of the ToDoList model
		todo_lists = models.ToDoList.objects.all()

		# serialize the data into a returnable format
		serializer = serializers.ToDoList(todo_lists, many=True)

		return Response(serializer.data)

	def post(self, request, format=None):
		"""
		Creates a new ToDoList with the given request data.
		"""
		# deserialize the data from the request
		serializer = serializers.ToDoList(data=request.data)
		# if the data validation done by the serialize passes
		if serializer.is_valid():
			# then save the ToDoList to the database and return the resulting ToDoList
			serializer.save()
			return Response(serializer.data)
		else:
			# Throw a 400 error if the serializer detected the data wasn't valid
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, todo_list_id, format=None):
		"""Deletes a ToDoList from the database"""
		# do this in a try block to catch errors if todo_list_id isn't real
		try:
			# if the list is real then delete it
			todo_list = models.ToDoList.objects.get(id=todo_list_id)
			todo_list.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		# catch the DoesNotExist error and return an Http error
		except models.ToDoList.DoesNotExist:
			raise Http404

class ToDoListItem(APIView):
	"""
	Endpoints for adding/deleting individual ToDoListItems.
	"""

	def post(self, request, todo_list_id, format=None):
		"""Add new ToDoList items to an existing ToDoList"""
		# do this in a try block in case the todo_list_id is not real
		try:
			# Query the db for the existing list
			todo_list = models.ToDoList.objects.get(id=todo_list_id)
			# deserialize the data from the request
			serializer = serializers.ToDoListItem(data=request.data)

			# if the ToDoListItem is valid then add the list id and save it
			if serializer.is_valid():
				serializer.validated_data['todo_list_id'] = todo_list_id
				serializer.save()
				return Response(serializer.data)

			else:
				# return an HTTP 400 error if the data was not correct
				return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

		# ALWAYS catch your DoesNotExist errors :)
		except models.ToDoList.DoesNotExist:
			raise Http404

	def delete(self, request, todo_list_item_id, format=None):
		"""Deletes a ToDoListItem from the database"""
		# try to find the ToDoListItem with the id
		try:
			item = models.ToDoListItem.objects.get(id=todo_list_item_id)
			# if the item exists then delete it
			item.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		# return the 404 error if it doesn't exist
		except models.ToDoListItem.DoesNotExist:
			raise Http404
