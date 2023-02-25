# from todo import models
# from rest_framework import generics
# from .serializers import TodoSerializer

# class ListTodo(generics.ListCreateAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = TodoSerializer    #these variable names must be what they are supposed to be and not random

# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = TodoSerializer


# instead of creating logic to handle each type of crud operation, drf provides us viewset which allows us to handle all these
# different types request handling 

from todo import models
from rest_framework import viewsets

from .serializers import TodoSerializer

class TodoViewset(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()    
    serializer_class = TodoSerializer