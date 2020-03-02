from django.urls import path

from crud import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create'),
    path('search/', views.search, name='search'),
    path('detail/<slug:slug>/', views.post_detail, name='detail'),
    path('update/<slug:slug>/', views.update_post, name='update'),
    path('delete/<slug:slug>/', views.delete_post, name='delete'),
]