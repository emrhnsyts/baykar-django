from django.urls import path
from ihas import views


urlpatterns = [
    # URL pattern for listing all IHA objects and creating new ones
    path("", views.IHAListCreateView.as_view()),
    # URL pattern for retrieving, updating, and deleting a specific IHA object
    path("<int:pk>", views.IHARetrieveUpdateDestroyView.as_view()),
    # URL pattern for creating a rent object for a specific IHA object
    path("<int:pk>/rent", views.IHARentView.as_view()),
]
