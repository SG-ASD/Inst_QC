from django.urls import path
from . import views
app_name = "Mainapp"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<str:category_main>/", views.SubcategoryView.as_view(), name="subcategory"),  # <int:review_id> : id 값을 넘겨준다.
]
