from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calendar', views.calendar, name='calendar'),
    path('signup', views.signup, name='signup'),
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('entry/add', views.add, name='add'),
    path('entry/delete/<int:pk>', views.delete, name='delete'),
    path('entry/<int:pk>', views.details, name='details'),
    path('admin/', admin.site.urls),

]
