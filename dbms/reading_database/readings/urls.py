from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(r'^adddata', views.add_data),
    url(r'^addreadingdata', views.add_reading_data)
    # url('', views.index)   
]

urlpatterns = format_suffix_patterns(urlpatterns)


'''urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^poc/(?P<cr_num>cr-[a-z,A-Z]{3}-[0-9]{3})/$', views.PoCList.as_view()),
    #url(r'^ccpusers/',include('cr_app.urls')),
    url(r'^venues/(?P<cr_num>cr-[a-z,A-Z]{3}-[0-9]{3})/$', views.SuggestVenueList.as_view()),
    #url(r'^venues/(?P<cr_num>cr-[a-z,A-Z]{3}-[0-9]{3})/(?P<venue_id>[0-9]+)/$', views.SuggestVenueList.as_view()),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)'''