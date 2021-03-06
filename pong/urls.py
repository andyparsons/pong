from django.conf.urls import patterns, include, url, include
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from rest_framework import viewsets, routers

import help.views 

from django.contrib import admin
admin.autodiscover()

# API ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

# API Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = patterns('',
	# admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='home.haml')),
    url(r'asks/', help.views.ListContactView.as_view(),
		name='asks-list',),

    # Wire up our API using automatic URL routing.
	# Additionally, we include login URLs for the browseable API.
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)




   