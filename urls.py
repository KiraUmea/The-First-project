from django.urls import path, include
from . import views
from . import admin


admin.site.site_header = 'Админка'


urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('', views.blogs, name='blogs'),
    path('/about/', views.about, name='about'),
    path('/', views.slash, name='slash'),
    path('/<slug>/', views.slug, name='slug'),
    path('/<slug>/comment/', views.slug_comment, name='slug_comment'),
    path('/create/', views.create, name='create'),
    path('/<slug>/update/', views.slug_update, name='slug_update'),
    path('/<slug>/delete/', views.slug_delete, name='slug_delete'),
    path('/profile/<username>/', views.profile_username, name='profile_username'),
    path('/change_password/', views.change_password, name='change_password'),
    path('/registration/', views.registration, name='registration'),
    path('/login/', views.login, name='login'),
    path('/logout/', views.logout, name='logout'),
    path('main', views.main, name='main'),
    path('create blog', views.create_blog, name='create blog')
]
