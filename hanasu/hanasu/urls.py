"""hanasu URL Configuration


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from mysite import views
import authentication.views
import lexique.views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index', views.index, name ='index'),
    path('hanasu_register', authentication.views.signup_page, name='signup'),
    path('hanasu_home', views.hanasuhome, name ='home'),
    path('hanasu_maneki_neko', views.hanasugame, name ='maneki_neko'),
    path('hanasu_user', views.user_page, name='user_page'),
    # chemin url de la page connection.
    path('hanasu_login', authentication.views.login_page, name ='login'),
    path('logout', authentication.views.logout_user, name ='logout'),
    # chemin vers l'appli lexique
    path('hanasu_lexique', lexique.views.lexique, name ='lexique'),
    path('hanasu_lexique/upload/', lexique.views.lexique_upload, name='lexique_upload'),
    path('hanasu_lexique_update/<int:id>/', lexique.views.lexique_update, name='lexique_update'),
    path('hanasu_lexique_delete/<int:id>/', lexique.views.lexique_delete, name='lexique_delete'),
    # chemin vers le blog post
    path('hanasu_blog', lexique.views.blog, name = 'blog'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
