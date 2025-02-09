from django.db import models
from django.conf import settings

# Create your models here.

class categories(models.Model):
    title = models.CharField(max_length = 100)
    keywords = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'

class post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length = 200)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateField()
    published = models.BooleanField(default=1)
    main_image = models.ImageField()
    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)
    image4 = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)
        
    def get_short_content(self):
        if len(self.content) > 500:
            short_content = self.content[:500]
            short_content += "..."
            return short_content
        return self.content

class comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    date = models.DateField()
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text

    def get_username(self):
        username = self.user.username
        return username

    def get_profileimage(self):
        profileimage = 'http://placehold.it/50x50'
        return profileimage

class like(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 

















