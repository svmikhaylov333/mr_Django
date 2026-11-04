from django.urls import include, path

from blog.apps import BlogConfig
from blog.views import Blog, ProductDetailView, ProductListView

app_name = CatalogConfig.name


urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("contacts/", ProductContactView.as_view(), name="contacts"),
]
