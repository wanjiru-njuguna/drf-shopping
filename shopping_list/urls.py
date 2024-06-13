from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from shopping_list.api.viewsets import ShoppingItemViewSet
from shopping_list.api.views import (ListAddShoppingItem,
    ListAddShoppingList,
    ShoppingItemDetail,
    ShoppingListAddMembers,
    ShoppingListRemoveMembers,
    SearchShoppingItems,
    ShoppingListDetail,)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("api/shopping-lists/", ListAddShoppingList.as_view(), name="all-shopping-lists"),
    path("api/shopping-lists/<uuid:pk>/", ShoppingListDetail.as_view(), name="shopping_list_detail"),
    path('api/shopping-lists/<uuid:pk>/add-members/', ShoppingListAddMembers.as_view(), name="shopping-list-add-members"),
    path("api/shopping-lists/<uuid:pk>/remove-members/", ShoppingListRemoveMembers.  as_view(), name="shopping-list-remove-members"),
    path("api/shopping-lists/<uuid:pk>/shopping-items/", ListAddShoppingItem.as_view(), name="list-add-shopping-item"),
    path("api/shopping-lists/<uuid:pk>/shopping-items/<uuid:item_pk>/", ShoppingItemDetail.as_view(), name="shopping-item-detail"),
    path('api/search-shopping-items/', SearchShoppingItems.as_view(), name="search-shopping-items"),

]