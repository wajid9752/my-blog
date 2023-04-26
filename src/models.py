from django.db import models
from numpy import ERR_IGNORE

# Create your models here.



class blog(models.Model):
    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.date.strftime('%b %e %Y')


