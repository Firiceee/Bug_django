from . import views
from django.urls import path

urlpatterns = [
    path("<str:name>", views.greet, name="greet"),
    path("",views.index, name ="hello"),
    path("essai/", views.check_template),
    path("tests/", views.testttt)
]