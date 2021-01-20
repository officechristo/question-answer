from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Question(models.Model):
    Q_text = models.TextField(max_length=500, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    attachment = models.FileField(blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return f"{self.Q_text}  {self.user}"


class Answer(models.Model):
    A_text = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ans')
    Q_id = models.ForeignKey(Question, on_delete=models.CASCADE, )
    objects = models.Manager()

    def __str__(self):
        return f"{self.A_text}"
