from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from blog.models import BlogPost
from django.urls import reverse_lazy, reverse



class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)

class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save(update_fields=["views_count"])
        return obj

class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]
    def get_success_url(self):
        return reverse("blog:blogpost_detail", kwargs={"pk": self.object.pk})

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]
    def get_success_url(self):
        return reverse("blog:blogpost_detail", kwargs={"pk": self.object.pk})

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    def get_success_url(self):
        return reverse("blog:blogpost_list", kwargs={"pk": self.object.pk})






