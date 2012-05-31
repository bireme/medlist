from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from medlist.directory.models import *

class EvidenceSummary(models.Model):

    class Meta:
        verbose_name = _("Evidence Summary")
        verbose_name_plural = _("Evidence Summaries")

    def new_filename(instance, filename):
        path = 'evidences_files'
        
        fname, dot, extension = filename.rpartition('.')
        fname = slugify(fname)[:60]
        file = "%s.%s" % (fname, extension)

        return os.path.join(path, file)

    medicine = models.ForeignKey(Medicine, related_name="+")

    created = models.DateTimeField(_("Created at"), default=datetime.now(), editable=False)
    updated = models.DateTimeField(_("Updated at"), default=datetime.now(), editable=False)

    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    context = models.TextField(_("Context"), blank=True, null=True)
    question = models.CharField(_("Question"), max_length=255, blank=True, null=True)
    file = models.FileField(_("File"), upload_to=new_filename, blank=True)

    def __unicode__(self):
        return unicode(self.title)

    def get_translation(self, lang_code):
        translation = EvidenceSummaryLocal.objects.filter(evidence=self.id, language=lang_code)
        if translation:
            return translation[0].__unicode__()
        else:
            return self.__unicode__()

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        super(EvidenceSummary, self).save(*args, **kwargs) 

class EvidenceSummaryLocal(models.Model):   

    class Meta:
        verbose_name = _("Evidence Summary Translate")
        verbose_name_plural = _("Evidence Summary Translations")

    def new_filename(instance, filename):
        path = 'evidences_files'
        
        fname, dot, extension = filename.rpartition('.')
        fname = slugify(fname)[:60]
        file = "%s.%s" % (fname, extension)

        return os.path.join(path, file)

    evidence = models.ForeignKey(EvidenceSummary)
    language = models.CharField(_("language"), max_length=10, choices=LANGUAGES_CHOICES[1:])

    created = models.DateTimeField(_("Created at"), default=datetime.now(), editable=False)
    updated = models.DateTimeField(_("Updated at"), default=datetime.now(), editable=False)

    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    context = models.TextField(_("Context"), blank=True, null=True)
    question = models.CharField(_("Question"), max_length=255, blank=True, null=True)
    file = models.FileField(_("File"), upload_to=new_filename, blank=True)

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        super(EvidenceSummary, self).save(*args, **kwargs) 

    def __unicode__(self):
        return unicode(self.title)