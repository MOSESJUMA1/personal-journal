from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from journal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.journal_home, name='journal_home'),
    path('signup/', views.signup, name='signup'),
    path('new/', views.new_entry, name='new_entry'),
    path('login/', auth_views.LoginView.as_view(template_name='journal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]