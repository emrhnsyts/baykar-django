from django.contrib import admin
from django.urls import include, path
from ihas import views

urlpatterns = [
    path("api/v1/ihas/", include("ihas.urls")),
    path("api/v1/rents/", include("rents.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt"))
]
