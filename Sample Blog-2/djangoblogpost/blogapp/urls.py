from django.urls import path
from.import views 

urlpatterns=[
    path("",views.home,name="home"),
    path("posts/",views.posts,name="posts"),
    path("about/",views.about,name="about"),
    path("posts/newpost/",views.newpost,name="newpost"),
    path("posts/newpost/newpostrecord/",views.newpostrecord,name="newpostrecord"),
    path("posts/update/<int:id>",views.update,name="update"),
    path("posts/update/updaterecord/<int:id>",views.updaterecord,name="updaterecord"),
    path("posts/delete/<int:id>",views.delete),
    path("posts/login_user/",views.login_user,name="login_user"),
    path("search/",views.search,name="search"),

    #Comments
    path("posts/comments/<int:pk>",views.comments,name="comments"),
    path("posts/delete_comments/<int:pk>",views.delete_comments,name="delete_comments"),

   #user authentication
    path("register/", views.Register, name="register"),
    path("login/",views.Login,name="login"),
    path("logout/", views.Logout, name="logout"),
]