from django.db import models

class Article(models.Model):

    ARTICLES_TYPES = (
        (1, 'Type 1'),
        (2, 'Type 2'),
    )

    title = models.CharField(max_length=50)
    body = models.TextField()
    type = models.IntegerField(choices=ARTICLES_TYPES)
    pub_date = models.DateTimeField(auto_now_add=True)


