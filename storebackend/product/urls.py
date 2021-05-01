from django.urls import path, include

from product import views

urlpatterns = [
  path('latest-products/', views.LatestProductsList.as_view()),
  path('products/<category_slug>/<product_slug>', views.ProductDetail.as_view()),
  path('products/<category_slug>', views.CategoryDetail.as_view()),
]