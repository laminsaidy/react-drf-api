from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
    ('_2000', '2000'), ('selfie', 'Selfie'),
    ('holidays', 'Holidays'), ('summer', 'Summer'),
    ('hiking', 'Hiking'), ('dinner', 'Dinner'),
    ('happiness', 'Happiness'), ('winter', 'Winter'),
    ('family', 'Family'), ('sunshine', 'Sunshine'),
    ('wild', 'Wild'), ('rome', 'Rome'),
    ('beauty', 'Beauty'), ('work', 'Work')
]
  
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../cat_h31tct', blank=True
    )

    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'