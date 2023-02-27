from django.urls import path
from .views import Top50View

urlpatterns = [
    path('top-50/', Top50View.as_view(), name='top-50'),
]
