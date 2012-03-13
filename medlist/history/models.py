from django.utils.translation import ugettext_lazy as _
from django.db import models
from datetime import datetime
from list.models import *

class History(models.Model):

	LIST_TYPES = (
			('c', _('Country List')),
			('p', _('PAHO List')),
			('w', _('WHO List')),
		)
	LIST_SUBTYPES = (
			('e', _('EML')),
			('c', _('EML Children')),
			('h', _('High Cost')),
			('s', _('Strategic Fund')),
		)

	class Meta:
		verbose_name = _("history")
		verbose_name_plural = _("histories")

	name = models.CharField(_("list name"), max_length=255)
	content = models.TextField(_("content serialized"))
	year = models.CharField(_("list year"), max_length=4)
	type = models.CharField(_("list type"), max_length=255, choices=LIST_TYPES)
	subtype = models.CharField(_("list subtype"), max_length=255, choices=LIST_SUBTYPES)
	created = models.DateTimeField(_("date creation"), default=datetime.now, editable=False)

	def __unicode__(self):
		return unicode(self.name)

