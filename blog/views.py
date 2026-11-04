from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from blog.models import BlogPost
from django.urls import reverse_lazy



class BlogPostListView(ListView):
    model = BlogPost

class BlogPostDetailView(DetailView):
    model = BlogPost

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blog_post_create.html'
    fields = ["title", "content", "preview", "is_published"]
    success_url = reverse_lazy("blog:blog_post_list")

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "blog/blog_post_form.html"
    fields = ["title", "content", "preview", "is_published"]
    success_url = reverse_lazy("blog:blog_post_list")

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/blog_post_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_post_list")






