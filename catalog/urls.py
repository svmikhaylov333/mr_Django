from django.urls import include, path

from catalog.apps import CatalogConfig
from catalog.views import (ProductContactView, ProductDetailView,
                           ProductListView)

app_name = CatalogConfig.name


urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("contacts/", ProductContactView.as_view(), name="contacts"),
]
