from django.conf.urls import include, url
from django.contrib import admin
#from testsite.home import views #agregada esta linea

urlpatterns = [
    # Examples:
    #url(r'^$', 'rodrigogutierrezk.views.home', name='home'),#descomentada esta linea
    # url(r'^blog/', include('blog.urls')),

    url(r'^home/', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
