from django.urls import path, include

from marketplace.views import ProjectListView, ProjectDetailView, ProjectCreateView

urlpatterns = [
    path("", ProjectListView.as_view(), name="project_list"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("project/create/", ProjectCreateView.as_view(), name="project_create"),
]

app_name = "marketplace"