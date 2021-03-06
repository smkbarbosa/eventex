from django.conf.urls import include, url
from django.contrib import admin

from eventex.core.views import home, speaker_detail, talk_list
from eventex.certificate.views import certificate

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^inscricao/', include('eventex.subscriptions.urls',
                                namespace='subscriptions')),
    url(r'^palestras/$', talk_list, name='talk_list'),
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', speaker_detail, name='speaker_detail'), ## qualquer componente de palavra que ocorre 1 ou mais vezes
    url(r'^certificate/$', certificate, name='certificate'),
    url(r'^admin/', include(admin.site.urls)),

]
