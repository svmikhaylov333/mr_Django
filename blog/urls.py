from django.urls import include, path

from blog.apps import BlogConfig
from blog.views import (BlogPostCreateView, BlogPostDeleteView,
                        BlogPostDetailView, BlogPostListView,
                        BlogPostUpdateView)

app_name = BlogConfig.name


urlpatterns = [
    path("", BlogPostListView.as_view(), name="blogpost_list"),
    path("<int:pk>/", BlogPostDetailView.as_view(), name="blogpost_detail"),
    path("create/", BlogPostCreateView.as_view(), name="blogpost_form"),
    path("<int:pk>/update/", BlogPostUpdateView.as_view(), name="blogpost_update"),
    path("<int:pk>/delete/", BlogPostDeleteView.as_view(), name="blogpost_delete"),
]
