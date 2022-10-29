# pages/urls.py
from django.urls import path
from .views import MainView as MV

main_page = MV()

urlpatterns = [
    path("", main_page.index, name="home"),
    path("update", main_page.update, name="update"),
]