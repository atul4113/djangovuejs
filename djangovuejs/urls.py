from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from joblist.views import job_list, JobsViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'jobs', JobsViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', job_list),
    url(r'^api/', include(router.urls)),
]

