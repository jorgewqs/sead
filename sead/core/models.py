from django.db import models

class Cursos(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	descricao = models.TextField('Descrição', blank=True)
	imagem = models.ImageField(upload_to='sead/images', verbose_name='Imagem')
	data_inicio = models.DateField('Data Início', null=True, blank=True)
	data_criacao = models.DateTimeField('Criado em', auto_now_add=True)
	data_atualizacao = models.DateTimeField('Atualizado em', auto_now=True)
