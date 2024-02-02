from django.db import models

class FormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobileno = models.CharField(max_length=15)
    message = models.TextField(max_length=400)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
