from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieListView.as_view(), name='index'),
    path('<int:pk>/', MovieDetailView.as_view(), name='detail'),
    path('create/', MovieCreateView.as_view(), name='create'),
    path('update/<int:pk>/', MovieUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', MovieDeleteView.as_view(), name='delete')
    ]