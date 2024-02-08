from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
     path('', views.home, name='home'),
     path('signup/',views.signup,name='signup'),
      path('login/',views.login,name='login'),
      path('dashboard/',views.dashboard,name='dashboard'),
      path('logout/', views.dashboard_logout,name='logout'),
      path('update/<int:id>',views.update,name='update'),
      path('delete/<int:id>',views.delete,name='delete'),
      path('dashboard/search/', views.search,name='dashboard/search')
]