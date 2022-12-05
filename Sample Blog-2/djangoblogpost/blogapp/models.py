from django.db import models
from django.utils import timezone
from django.core.files.base import ContentFile
#from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# Create your models here.
class Posts(models.Model):
    class Meta:
        verbose_name_plural="Posts" #This will handle the extra "s" (singular or plural in models)

    title=models.CharField(max_length=120)
    content=models.TextField()
    author=models.TextField()
    image=models.FileField(upload_to="images/", blank=True, null=True,default = 'images/default no pic image.jpg')
    posted_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['posted_on']

    def __str__(self): 
        return(self.title)
    
         
class Comments(models.Model):
    post = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=120)
    comment_body=models.CharField(max_length=256,null=True)
    posted_on=models.DateTimeField(default=timezone.now)
    #status=models.BooleanField()

    #class Meta:
     #   ordering = ['posted_on',]

    #def __str__(self):
     #   return('Comment: {} by {} '.format(self.comment_body, self.name))

    def __str__(self):
        return "%s -%s" % (self.post.title,self.name)

