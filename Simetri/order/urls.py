from django.urls import path
from . import views

app_name="order"
urlpatterns = [
    path("", views.index, name="home"),
    path("search/",views.search, name ="search")
]