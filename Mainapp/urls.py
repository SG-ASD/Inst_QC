from django.urls import path, include
from . import views
app_name = "Mainapp"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<str:category_main>/", views.SubcategoryView.as_view(), name="subcategory"),  # <str:category_main> : category_main 값을 넘겨준다.
]
