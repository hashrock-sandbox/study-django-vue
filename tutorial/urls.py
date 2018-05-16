from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views
from django.views.generic import TemplateView
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', serve,
        kwargs={'path': 'index.html'}),
    url(r'^(?!/static/.*)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/%(path)s')),        
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]