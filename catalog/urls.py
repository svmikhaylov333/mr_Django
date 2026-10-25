from django.urls import include, path

from catalog.apps import CatalogConfig
from catalog.views import contacts, products_list

app_name = CatalogConfig.name


urlpatterns = [
    path("", products_list, name="products_list"),
    path("contacts/", contacts, name="contacts"),
]
