from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import os.path
p = os.path.join(os.path.dirname(__file__), 'media_files/')

urlpatterns = patterns('',
        (r'^$', 'plotserver.app.views.index'),
        (r'^media_files/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': p}),
)
