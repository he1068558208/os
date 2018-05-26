from django.urls import path, re_path

from hrs import views

urlpatterns = {
    path('depts', views.depts,name='depts'),
    path('emp/', views.emps,name='empsindept'),
    path('deldept/', views.deldept,name='del'),
    re_path(r'^add1/',views.add1)
}