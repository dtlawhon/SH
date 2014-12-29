from django.conf.urls import patterns, include, url
from django.contrib import admin
from SH import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SH.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/$', include(admin.site.urls)),
    url(r'^$', views.home, name='index'),
    url(r'^register/$', views.register, name='register'), 
    url(r'^login/$', views.user_login, name='login'),
    url(r'^about/$', views.about, name='about'),
    url(r'^careers/$', views.careers, name='careers'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^chefregister/$', views.chef_register, name='chefregister'),
    
)
