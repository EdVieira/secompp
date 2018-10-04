from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
	title = models.CharField(max_length=200) #varchar 200
	text = models.TextField(verbose_name='texto do blog ') #text
	created_date = models.DateTimeField(default=timezone.now) #passa a referencia
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		# publicar atualizando data de publicação
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		# sobrescrita da instância
		return '{} - {}'.format(self.title,self.author)