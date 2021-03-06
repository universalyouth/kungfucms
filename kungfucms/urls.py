"""kungfu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from kungfucms.apps.exception.views import exception_handler400, \
    exception_handler403, \
    exception_handler404
    # exception_handler500
from kungfucms.utils import get_theme_static_dir


urlpatterns = [
    path('account/', include('kungfucms.apps.account.urls')),
    path('captcha/', include('decaptcha.urls')),
    path('admin/', admin.site.urls),
]

handler400 = exception_handler400
handler403 = exception_handler403
handler404 = exception_handler404
# handler500 = exception_handler500

if settings.DEBUG:
    import debug_toolbar
    static_dir = get_theme_static_dir()
    urlpatterns += static(settings.STATIC_URL, document_root=static_dir)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]