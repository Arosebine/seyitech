from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Message(models.Model):
    username = models.CharField( max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=15)
    messages = models.TextField()

    def __str__(self):
        return self.username












class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age =models.IntegerField()
    website = models.URLField(blank=True, null=True)
    your_cv = models.FileField(blank=True, null=True, upload_to='uploads/pdf')
    

    def __str__(self):
        return self.user.username


class Category(models.Model):
    product_name = models.CharField(verbose_name='Category Name', max_length=100)
    description = models.TextField(verbose_name='Description', blank=True, null=True)

    def __str__(self):
        return self.product_name



class Post(models.Model):
    post_title = models.CharField(verbose_name='Post Title', max_length=100)
    category = models.ManyToManyField(Category, verbose_name='Categories of post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    post_image = models.ImageField(blank=True, null=True, upload_to='upload/post_image', verbose_name='Post image')
    create_date = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)
    content = models.TextField()

    def publish(self):
        return self.published_date
        self.save

    def approve_comment(self):
        return self.comments.filter(approve_comment=True)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_poster = models.CharField(max_length=200)
    comments = models.TextField()
    create_date = models.DateTimeField()
    approve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def __str__(self):
        return self.comments
