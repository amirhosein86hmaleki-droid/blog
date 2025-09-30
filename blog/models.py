from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
#article to user
#ManyTOMany
#ManyToOne
#OneToOne
#cascade
#set null

#protect
#set default

class  Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(status=True)



class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='articles')
    category = models.ManyToManyField(Category,related_name='articles')
    title = models.CharField(max_length=100)
    body = models.TextField()
    views = models.IntegerField(null=True)
    image = models.ImageField(upload_to='images/articles/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    myfile = models.FileField(upload_to='test',null=True)
    status = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True,blank=True)
    objects = models.Manager()
    custom_manager = ArticleManager()




    def save(self,force_insert=False,force_update=False,using=None,update_fields=None):
        self.slug = slugify(self.title)
        super(Article,self).save()


    def get_absolute_url(self):
        return reverse('blog:article_detail',kwargs={'slug':self.slug})

    def __str__(self):
        return f"{self.title}-{self.body[:30]}"

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name='replies',null=True,blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.body[:50]