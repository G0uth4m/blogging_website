from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
    path('',views.main,name="main"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('blog/',views.blog,name="blog"),
    path('blog/createblog',views.createblog,name="createblog"),
    path('blog/allblogs',views.allblogs,name="allblogs"),
    url(r'^blog/allblogs/(?P<pk>\d+)/$',views.viewpost,name="edit_profile"),
    path('blog/myblog',views.myblog,name="myblog"),
    path('blog/contact',views.contact,name="contact"),
    url(r'^blog/allblogs/(?P<pk>\d+)/comments',views.comments,name="comments"),
]