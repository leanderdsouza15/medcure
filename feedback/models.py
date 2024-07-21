from django.db import models

#Model for lab locator
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    rating = models.IntegerField()

    def _str_(self):
        return f"{self.name} - {self.rating} stars"