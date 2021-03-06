from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^dashboard$', views.dashboard, name="dashboard"),
    url(r'^login$', views.login_user, name="login_user"),
    url(r'^logout$', views.logout_user, name="logout_user"),
]