from django.db import models
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL

class Blog(models.Model):

      STATUS_CHOICES = [
            ('draft', 'Draft'),
            ('pending', 'Pending'),
            ('published', 'Published'),
            ('rejected', 'Rejected'),
      ]

      title = models.CharField(max_length=200)
      body = models.TextField()
      author = models.ForeignKey(User, on_delete=models.CASCADE)
      status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.title

      def get_absolute_url(self):
            return reverse("blog_detail", kwargs={"pk": self.pk})


class Like(models.Model):
      blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      value = models.IntegerField()  # 1 / -1


class Comment(models.Model):
      blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      text = models.TextField()