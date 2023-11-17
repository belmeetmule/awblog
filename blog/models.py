from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
            return super(PublishedManager,self).get_queryset().filter(status='published')

# post medel
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # title field
    title = models.CharField(max_length=250)
    # slug field
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # author field 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # body field
    # body = models.TextField()
    body = RichTextUploadingField()
    # publish field
    publish = models.DateTimeField(default=timezone.now)
    # created field
    created = models.DateTimeField(auto_now_add=True)
    # updated field
    updated = models.DateTimeField(auto_now=True)
    # status field
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    # image field
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/', blank=True)

    # class meta
    class Meta:
        ordering = ('-publish',)
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() 

    def get_absolute_url(self):
         return reverse('blog:post_detail', args=[self.slug])
    
    def get_comments(self):
         return self.comments.filter(parent=None).filter(active=True)
    
    # __str__ method
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

    def get_comments(self):
        return self.comments.filter(active=True)
    

