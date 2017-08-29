from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views

urlpatterns = [
	# Maps to ToDoList.get and ToDoList.post
	url(r'^todo_lists$', views.ToDoList.as_view()),
	# Maps to ToDoList.delete
	url(r'^todo_lists/(?P<todo_list_id>[0-9]+)$', views.ToDoList.as_view()),
	# maps to ToDoListItem.post
	url(r'^todo_lists/(?P<todo_list_id>[0-9]+)/items$', views.ToDoListItem.as_view()),
	# maps to ToDoListItem.delete
	url(r'^todo_lists/items/(?P<todo_list_item_id>[0-9]+)$', views.ToDoListItem.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
