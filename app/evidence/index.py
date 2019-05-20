import os
from solr import SolrConnection
from django.db.models import signals
from django.conf import settings

from evidence.models import *

def update_index(sender, instance, created, **kwargs):

    if isinstance(instance, MedicineEvidenceSummary):
        #print "Atualizando desde o medicamento"
        evidence = EvidenceSummary.objects.get(pk=instance.evidence.id)
    else:
        #print "Atualizando desde a Evidencia"
        evidence = instance

    index_evidence(evidence)

def delete_evidence_from_medicine(sender, instance, using, **kwargs):
    evidence = EvidenceSummary.objects.get(pk=instance.evidence.id)

    index_evidence(evidence)


def index_evidence(evidence):
    evidence_medicine_list = []

    evidence_medicine = MedicineEvidenceSummary.objects.filter(evidence=evidence.id)
    for evimed in evidence_medicine:
        if evimed.medicine.name not in evidence_medicine_list:
                evidence_medicine_list.append(evimed.medicine.name)

    # try to create a connection to a solr server and send medicine
    try:
        solr = SolrConnection(settings.SOLR_URL)
        solr.add(
            id = "evidence-%s-%s" % (evidence.language, evidence.id),
            type = "evidence",
            title = evidence.title,
            description = evidence.description,
            context = evidence.context,
            question = evidence.question,
            link = evidence.link,
            file = evidence.file,
            language = evidence.language,
            evidence_medicine = evidence_medicine_list,
        )
        response = solr.commit()
    except Exception as ex:
        return False

    return True



signals.post_save.connect(update_index, sender=EvidenceSummary)
#signals.post_save.connect(update_index, sender=EvidenceSummaryLocal)
signals.post_save.connect(update_index, sender=MedicineEvidenceSummary)

signals.post_delete.connect(delete_evidence_from_medicine, sender=MedicineEvidenceSummary)
