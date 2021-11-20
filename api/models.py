from django.db import models
from django.utils.html import format_html
from tinymce.models import  HTMLField
# Create your models here.
class Category(models.Model):
      cat_id=models.AutoField(primary_key=True)
      name=models.CharField(max_length=90)
      title=models.CharField(max_length=90)
      description=models.TextField()
      image=models.ImageField(upload_to='Category')
      url=models.CharField(max_length=90)
      date=models.DateField(auto_now_add=True ,null=True )


      def __str__(self):
            return self.name

      def image_tag(self):
            return  format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%" />'.format(self.image))


class Post(models.Model):
      post_id=models.AutoField(primary_key=True)
      name = models.CharField(max_length=90)
      title=models.CharField(max_length=90)
      content=HTMLField()
      cat=models.ForeignKey(Category,on_delete=models.CASCADE)
      url=models.CharField(max_length=90)
      image=models.ImageField(upload_to='post/')



      def __str__(self):
            return self.name