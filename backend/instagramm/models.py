from django.db import models

# from account.models import User
from django.contrib.auth import get_user_model #2й вариант
User = get_user_model()


class AbstractPost(models.Model):
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # user = models.ForeignKey('account.User', on_delete=models.CASCADE) #2й вариант
    #
    # from django.contrib.auth.models import User #3й вариант
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Post(AbstractPost):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Comment(AbstractPost):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'comment - {self.post.title}'





