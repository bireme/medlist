from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from directory.models import *

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

    def file_is_pdf(self):
        if "pdf" in self.file:
            return True
        return False

    def link_is_pdf(self):
        if "pdf" in self.link:
            return True
        return False

    created = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated = models.DateTimeField(_("Updated at"), auto_now=True, editable=False)

    language = models.CharField(_("language"), max_length=10, choices=LANGUAGES_CHOICES, default='en')
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    context = models.TextField(_("Context"), blank=True, null=True)
    question = models.CharField(_("Question"), max_length=255, blank=True, null=True)
    link = models.URLField(_("link"), blank=True)
    file = models.FileField(_("File"), upload_to=new_filename, blank=True)

    def __str__(self):
        return str(self.title)

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

    evidence = models.ForeignKey(EvidenceSummary, on_delete=models.PROTECT)
    language = models.CharField(_("language"), max_length=10, choices=LANGUAGES_CHOICES)

    created = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated = models.DateTimeField(_("Updated at"), auto_now=True, editable=False)

    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    context = models.TextField(_("Context"), blank=True, null=True)
    question = models.CharField(_("Question"), max_length=255, blank=True, null=True)
    link = models.URLField(_("link"), blank=True)
    file = models.FileField(_("File"), upload_to=new_filename, blank=True)

    def file_is_pdf(self):
        if "pdf" in self.file:
            return True
        return False

    def link_is_pdf(self):
        if "pdf" in self.link:
            return True
        return False

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        super(EvidenceSummaryLocal, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.title)

class MedicineEvidenceSummary(models.Model):

    class Meta:
        verbose_name = "Evidence Summary in Medicine"
        verbose_name_plural = "Evidence Summaries in Medicine"

    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
    evidence = models.ForeignKey(EvidenceSummary, on_delete=models.PROTECT)

    def __unicode__(self):
        return str(self.evidence.title)
