from projects.views import ProjectListView
from django.urls import path

urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),
]
