from django.db import models

# Create your models here.
class CadastroFilme(models.Model):
    titulo = models.CharField(max_length=50)
    sinopse = models.TextField()
    
    def __str__(self):
        return self.titulo