from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('profiles/', views.ProfileListView.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery_list'),
    path('documents/', views.DocumentListView.as_view(), name='document_list'),
]
