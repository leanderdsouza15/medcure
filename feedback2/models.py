from django.db import models

#Model for Med locator
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField()

    def _str_(self):
        return self.name
    