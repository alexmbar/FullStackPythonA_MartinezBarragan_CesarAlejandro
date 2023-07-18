from django.urls import path
from . import views
from .views import APIRootView

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('reportes/', views.ReportesListCreateView.as_view(), name='reportes-list-create'),
    path('reportes/<int:pk>/', views.ReportesRetrieveUpdateDestroyView.as_view(), name='reportes-retrieve-update-destroy'),
]