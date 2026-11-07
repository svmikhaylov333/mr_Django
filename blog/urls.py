from django.urls import include, path

from blog.apps import BlogConfig
from blog.views import BlogPostCreateView, BlogPostListView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView

app_name = BlogConfig.name


urlpatterns = [
    path("", BlogPostListView.as_view(), name="blog_post_list"),
    path("<int:pk>/", BlogPostDetailView.as_view(), name="blog_post_detail"),
    path("create/", BlogPostCreateView.as_view(), name="blog_post_create"),
    path("<int:pk>/update/", BlogPostUpdateView.as_view(), name="blog_post_update"),
    path("<int:pk>/delete/", BlogPostDeleteView.as_view(), name="blog_post_delete"),
]
