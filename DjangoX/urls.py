from django.urls import path
from .views import DjangoXListView, DjangoXDetailView, DjangoXCreateView, DjangoXUpdateView, DjangoXDeleteView

urlpatterns = [
    path('', DjangoXListView.as_view(), name='DjangoX_list'),
    path('<int:pk>/', DjangoXDetailView.as_view(), name='DjangoX_detail'),
    path('create/', DjangoXCreateView.as_view(), name='DjangoX_create'),
    path('<int:pk>/update/', DjangoXUpdateView.as_view(), name='DjangoX_update'),

    path('<int:pk>/delete/', DjangoXDeleteView.as_view(), name='DjangoX_delete'),
]
