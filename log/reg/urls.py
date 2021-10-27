from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('user',views.user,name='user'),
    path('user_del/<int:id>',views.user_del,name="user_del"),
    path('edit/<int:id>',views.edit,name="edit"),
    # path('update/<int:id>',views.update,name="update")

]