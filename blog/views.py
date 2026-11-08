from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
#from django.core.mail  import send_mail

from blog.models import BlogPost


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

        # to do отправка писем- доделать
        # if obj.views_count == 100:
        #     send_mail(
        #         subject=f"Статья '{obj.title}' набрала 100 просмотров!",
        #         message ="круто",
        #         from_email="xxx@xxx.ru",
        #         recipient_list=["xxx@xxx.ru"],
        #         fail_silently=False,
        #     )
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]

    def get_success_url(self):
        return reverse("blog:blogpost_detail", kwargs={"pk": self.object.pk})


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]
    success_url = reverse_lazy("blog:blogpost_list")
    def get_success_url(self):
        return reverse("blog:blogpost_detail", kwargs={"pk": self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost

    def get_success_url(self):
        return reverse("blog:blogpost_list")