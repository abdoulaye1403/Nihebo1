from django.contrib import admin
from django.contrib.admin.sites import site
from .models import article_alimentaire
from .models import article_electromenager
from .models import article_electronique
from .models import article_vetement
from .models import Article,Category

admin.site.register(Article)
admin.site.register(article_vetement)
admin.site.register(article_alimentaire)
admin.site.register(article_electromenager)
admin.site.register(article_electronique)
admin.site.register(Category)
# Register your models here.
