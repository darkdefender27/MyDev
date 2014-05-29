from django.db import models

# Create your models here.

class Blog (models.Model):
	title = models.CharField(max_length=100, unique=True)
	body = models.TextField()

	def __unicode__(self):
		return self.title

		
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title


class Customer (models.Model):
	tab_id = models.IntegerField()
	email_id = models.EmailField(max_length = 75)
	location = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	repassword = models.CharField(max_length = 100)
	
	def __unicode__(self):
		return self.tab_id
	
	
