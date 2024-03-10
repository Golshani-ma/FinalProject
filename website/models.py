from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} -> {}'.format(self.name, self.subject)

    class Meta:
        ordering = ['-created_at']
        db_table_comment = "Contact Table"


class NewsLetter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email