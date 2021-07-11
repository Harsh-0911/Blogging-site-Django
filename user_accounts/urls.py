from django.urls import path

from . import views

app_name = 'user_accounts'

urlpatterns = [
	path('', views.get_started, name='get_started'),
	path('login/', views.login_, name='login'),
	path('register/', views.register, name='register'),
	path('logout/', views.logout_, name='logout')
]