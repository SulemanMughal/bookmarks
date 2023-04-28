# from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    # login url
    # path('login/', views.user_login, name='login'),

    # login url
    path('login', LoginView.as_view(), name='login'),

    # logout url
    path('logout', views.logout_view, name='logout'),

    # logout_then_login url
    path('logout-then-login', logout_then_login, name='logout_then_login'),


    # Dashboard url
    path('', views.dashboard, name='dashboard'),


    # change password urls
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    # restore password urls
    path('password-reset', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete',PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # registration
    path('register', views.register, name='register'),

    # profile
    path('edit', views.edit, name='edit'),


    path('users/', views.user_list, name='user_list'),

    path('users/<str:username>/', views.user_detail, name='user_detail'),

    path('users/follow/users', views.user_follow, name='user_follow_url'),

]