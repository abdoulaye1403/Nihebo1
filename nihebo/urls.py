"""nihebo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,reverse
from hebogoundo.views import (detail_article_alimentaire, home,vetement,alimentaire,
                              electronique,electromenager,propos_nous,contact,produit,detail_article_vetement,detail_article_electronique,detail_article_electromenager,search)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('alimentaire/article/recherche/',search,name="search"),
    path('alimentaire/article/<int:id_article>/',detail_article_alimentaire,name='detail_alimentaire'),
    path('vetement/article/<int:id_article>/',detail_article_vetement,name='detail_vetement'),
    path('electronique/article/<int:id_article>/',detail_article_electronique,name='detail_electronique'),
    path('electromenager/article/<int:id_article>/',detail_article_electromenager,name='detail_electromenager'),
    path('alimentaire/',alimentaire, name="alimentaire"),
    path('vetement/',vetement,name="vetement"),
    path('electronique/',electronique,name="electronique"),
    path('electromenager/',electromenager,name="electromenager"),
    path('propos_nous/',propos_nous,name="propos_nous"),
    path('contact/',contact,name="contact"),
    path('produit/',produit,name="produit"),
    
   
    
    
    
]



if settings.DEBUG:
    #import debug_toolbar
    #urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)