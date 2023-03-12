from django.db import models

# Create your models here.
class blog(models.Model):
    #title
    #publication date
    #body
    #image

    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='image/')