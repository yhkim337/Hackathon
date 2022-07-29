from django.urls import path
from soldierLetter import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notice/', views.notice, name='notice'),
    path('review/', views.ReviewView.review_read, name='review'),
    path('review/new/', views.ReviewView.review_new, name='new_review'),
    path('review/<int:rid>/', views.ReviewView.review_edit, name='edit_review'),
    path('review/<int:rid>/delete', views.ReviewView.review_delete, name='delete_review')
]