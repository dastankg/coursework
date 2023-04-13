from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=80)
    posts_text = models.TextField()
    posted = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to=f'photos/posts/%Y/%m/%d')
    visit_count = models.IntegerField(default=0)


class Comment(models.Model):
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.CharField(max_length=10)
    data = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    comment = models.TextField()
