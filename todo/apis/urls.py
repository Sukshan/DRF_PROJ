# from django.urls import path

# from .views import ListTodo, DetailTodo

# urlpatterns = [
#     path('', ListTodo.as_view()),
#     path('<int:pk>/', DetailTodo.as_view()),
# ]

# since we are using viewset now, we have to write default router code

from rest_framework.routers import DefaultRouter
from .views import TodoViewset

from django.urls import path

router = DefaultRouter()
router.register('', TodoViewset, basename = 'todo')

urlpatterns = router.urls