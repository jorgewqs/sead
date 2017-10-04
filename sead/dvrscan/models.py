from django.db import models

class Dvr(models.Model):

	name_dvr = models.CharField('Nome', max_length=100)
	ip_dvr = models.GenericIPAddressField('IPv4 address', max_length=15, null=True)
	unidade_dvr = models.TextField('Descrição', blank=True)
	status_dvr = models.BooleanField('Status', blank=True)
	data_atualizacao_dvr = models.DateTimeField('Atualizado em', auto_now=True)