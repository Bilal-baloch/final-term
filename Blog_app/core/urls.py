from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('authorposts/<str:author>',views.post_of_an_author,name='authorposts'),
    path('details/<int:pk>',views.blog_details,name='details'),
    path('addblog/',views.add_blog,name='addblog')
]
