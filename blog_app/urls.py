from django.urls import path
from . import views
app_name='blog_app'


urlpatterns=[
    path('',views.home,name='home'),
    path('add/',views.add_blog,name='add'),
    path('update/<int:id>/',views.update_blog,name='update'),
    path('delete/<int:id>/',views.delete_blog,name='delete'),

]