from django.db import models

class AdminLog(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)

    
class Meta:
    db_table = 'adminlogin_adminlog'