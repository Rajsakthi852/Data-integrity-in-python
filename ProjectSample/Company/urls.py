from django.urls import path
from . import views

urlpatterns=[
    path("",views.registerpage),
    path("userlog/",views.userlog),
    path("adminlog/",views.adminlog),
    path("adminhome/",views.adminhome),
    path("pending/",views.pending),
    path("approve/<int:id>/",views.approve),
    path("approved/",views.approved),
    path("edit/<int:id>/",views.edit),
    path("delete/<int:id>/",views.delete)
]