from django.db import models

# Create your models here.
class Member(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    profile = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    count = models.IntegerField(default=0)  # 조회수
    writer = models.CharField(max_length=30, default='anonymous')  # 작성자
    passwd = models.CharField(max_length=30)  # 비밀번호

    def __str__(self):
        return self.title