from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'learnkit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^motorapp/', include('motorapp.urls', namespace='motorapp')),
    url(r'^accounts/', include('django.contrib.auth.urls',
                           namespace='accounts')),
]

