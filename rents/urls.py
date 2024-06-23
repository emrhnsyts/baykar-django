from django.urls import path
from rents import views

urlpatterns = [
    # URL pattern for listing all rent objects and creating new ones
    path("", views.RentListCreateView.as_view()),
    # URL pattern for retrieving, updating, and deleting a specific rent object
    path("<int:pk>", views.RentRetrieveUpdateDestroyView.as_view()),
]
