from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

class HashTag(models.Model):
    hashtag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.hashtag_name

class Publication(models.Model):
    hashtag = models.ManyToManyField(HashTag)
    title = models.CharField(max_length=20)
    title_kg = models.CharField(max_length=20)
    text = models.TextField()
    text_kg = models.TextField()
    short_text = models.CharField(max_length=255)
    short_text_kg = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    publication = models.ForeignKey(Publication, related_name='comments', on_delete=models.CASCADE)
