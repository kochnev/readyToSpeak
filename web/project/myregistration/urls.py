from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    #url(r'^profiles/$', login_required(views.UserProfileListView.as_view()), name='list_profiles'),
    #url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
]
