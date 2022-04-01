from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("Main/<str:category_main>/", views.SubcategoryView.as_view(), name="subcategory"),  # <int:review_id> : id 값을 넘겨준다.
    # path("Instrument/", include('Instrumentapp.urls')),
]
