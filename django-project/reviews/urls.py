from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='index'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:artilce_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:review_pk>/comments/',views.comment_create, name='comment_create'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.comments_delete,name='comments_delete'),
]