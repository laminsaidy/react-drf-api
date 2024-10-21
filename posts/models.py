from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        ('_sunshine', 'Sunshine'),
        ('moonwalk', 'Moonwalk'),
        ('beauty', 'Beauty'),
        ('relaxing', 'Relaxing'),
        ('cocktail', 'Cocktail'),
        ('nerdy', 'Nerdy'),
        ('berlin', 'Berlin'),
        ('pretty', 'Pretty'),
        ('metime', 'Metime'),
        ('holidays', 'Holidays'),
        ('rome', 'Rome'),
        ('miami', 'Miami'),
        ('breakfast', 'Breakfast'),
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

