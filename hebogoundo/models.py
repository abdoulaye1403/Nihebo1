from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class article_alimentaire(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/images")
    prix = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class article_vetement(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/images")
    prix = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title  

class article_electromenager(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/images")
    prix = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class article_electronique(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/images")
    prix = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    

class Article(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/images")
    desc = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


# Create your models here.
