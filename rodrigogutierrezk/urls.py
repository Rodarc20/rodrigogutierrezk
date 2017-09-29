from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #url(r'^$', 'rodrigogutierrezk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('home.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
