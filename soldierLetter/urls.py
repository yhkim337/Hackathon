from django.urls import path
from soldierLetter import views

urlpatterns = [
    path('', views.base, name='base'),
    path('notice/', views.notice, name='notice'),
    path('review/', views.review, name='review'),
]