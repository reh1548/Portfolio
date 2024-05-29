from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Existing models...

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    main_image = models.ImageField(upload_to='blog_images/')
    additional_images = models.ManyToManyField('BlogImage', blank=True)
    content = HTMLField()
    
    def __str__(self):
        return self.title
    

class BlogImage(models.Model):
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return f'Image {self.id}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog.title}'
