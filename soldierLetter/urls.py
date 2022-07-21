from django.urls import path
from soldierLetter import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notice/', views.notice, name='notice'),
    path('review/', views.review, name='review'),
]