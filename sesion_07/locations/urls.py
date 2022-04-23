"""Locations app URL config"""

from django.urls import path

from . import views


app_name = "locations"
urlpatterns = [
    path("create/", views.CreateAddressView.as_view(), name="create"),
    path("me/", views.ShowUserAddressView.as_view(), name="show"),
    path("delete/", views.DeleteAddressView.as_view(), name="delete"),
]
