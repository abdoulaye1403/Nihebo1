from django.db.models import query
from django.shortcuts import render
from .models import Article, article_alimentaire, article_electromenager, article_electronique, article_vetement

def home(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request,"hebogoundo/home.html",context)

def alimentaire(request):
    alimentaire = article_alimentaire.objects.all()
    context = {'alimentaire':alimentaire}
    return render(request,"hebogoundo/alimentaire.html",context)

def vetement(request):
    vetement = article_vetement.objects.all()
    context = {'vetement':vetement}
    return render(request,"hebogoundo/vêtements.html",context)

def electronique(request):
    electronique = article_electronique.objects.all()
    context = {'electronique':electronique}
    return render(request,"hebogoundo/electronique.html",context)

def electromenager(request):
    electromenager = article_electromenager.objects.all()
    context = {'electromenager':electromenager}
    return render(request,"hebogoundo/electromenager.html",context)

def propos_nous(request):
    return render(request,"hebogoundo/about.html")

def contact(request):
    return render(request,"hebogoundo/contact.html")

def produit(request):
    return render(request,"hebogoundo/produits.html")

def detail_article_alimentaire(request,id_article):
    article = article_alimentaire.objects.get(id=id_article)
    category = article.category
    articles_en_relation = article_alimentaire.objects.filter(category=category)
    
    return render(request,"hebogoundo/detailAlimentaire.html",({'article':article,'aer':articles_en_relation}))

def detail_article_vetement(request,id_article):
    article = article_vetement.objects.get(id=id_article)
    category = article.category
    articles_en_relation = article_vetement.objects.filter(category=category)
    
    return render(request,"hebogoundo/detailVetement.html",({'article':article,'aer':articles_en_relation}))

def detail_article_electronique(request,id_article):
    article = article_electronique.objects.get(id=id_article)
    category = article.category
    articles_en_relation = article_electronique.objects.filter(category=category)
    
    return render(request,"hebogoundo/detailElectronique.html",({'article':article,'aer':articles_en_relation}))

def detail_article_electromenager(request,id_article):
    article = article_electromenager.objects.get(id=id_article)
    category = article.category
    articles_en_relation = article_electromenager.objects.filter(category=category)
    
    return render(request,"hebogoundo/detailElectromenager.html",({'article':article,'aer':articles_en_relation}))

def search(request):
    query = request.GET["art"] 
    liste_article = article_alimentaire.objects.filter(title__icontains=query)
    return render(request,"hebogoundo/search.html",{'liste_article':liste_article})

  
# Create your views here.
