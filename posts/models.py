from django.db import models

choice = (
    ('Development', "Development"),
    ('Startup', "Startup"),
    ('News', "News"),
)

class Post(models.Model):
    heading = models.CharField(max_length=150)
    categories= models.CharField(choices=choice,max_length=150)
    tags = models.ManyToManyField('Tag', blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.heading

class Tag(models.Model):
    heading = models.CharField(max_length=150)

    def __str__(self):
        return self.heading

        

