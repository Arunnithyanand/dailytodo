from django.urls import path
from todo import views

urlpatterns=[
    path("home",views.home,name="home"),
    path("todo/create",views.create_todo,name="create"),
    path("todo/list",views.listtodo,name="todolist"),
    path("todo/view/<int:id>",views.viewtodo,name="todoview"),
    path("todo/delete/<int:id>",views.removetodo,name="deletetodo"),
    path("todo/update/<int:id>",views.updatetodo,name="updatetodo"),
    path("accounts/registration",views.registration_user,name="signup"),
    path("accounts/login",views.signin,name="signin"),
    path("accounts/logout",views.signout,name="signout")
]