from django.shortcuts import HttpResponse, get_object_or_404, render_to_response, render
from django.views.decorators.cache import cache_page
from django.core.urlresolvers import reverse
from django.template import RequestContext
from medlist.list.models import *
from django.conf import settings
from django.template import loader, Context
from django.template.loader import render_to_string
from datetime import datetime
from models import *


# @cache_page(settings.CACHE_TIMEOUT)
def save_history(request, id):

    list = get_object_or_404(List, pk=id)

    # just shows the list that not have been published yet if have 'preview' parameter
    if not list.published:
        # if not have preview parameter, returns 404 error
        if not 'preview' in request.GET.keys():
            raise Http404

    sections = Section.tree.filter(list=list)
    sections_has_complementary = []
    for section in sections:
        if SectionPharmForm.objects.filter(section=section).filter(complementary_list=True).count() > 0:
            sections_has_complementary.append(section.id)

    pharm_section = {}
    for section in sections:
        query = SectionPharmForm.objects.filter(section=section)
        pharm_section[section.id] = query
        

    output = {'list': list}
    output['nodes'] = sections
    output['pharm_section'] = pharm_section
    output['sections_has_complementary'] = sections_has_complementary
    
    # saving the default list
    content = render_to_string('history/show_list.html', output, context_instance=RequestContext(request))

    history = History(name=list.name, abbreviation=list.abbreviation, year=list.year, edition=list.edition, 
        type=list.type, subtype=list.subtype, published=list.published, obs=list.obs, created=datetime.now())
    history.content = content
    history.save()

    try:
        request.META['LANGUAGE_CODE'] = 'pt-br'

        content = render_to_string('history/show_list.html', output, context_instance=RequestContext(request))
        local = ListLocal.objects.get(list=list, language=request.META['LANGUAGE_CODE'])
        
        history = HistoryLocal(list=list, language=request.META['LANGUAGE_CODE'], name=local.name, obs=local.obs)
        history.content = content
        history.save()

    except:
        print 'not saved local %s to list %s' % (request.META['LANGUAGE_CODE'], list.id)

    try:
        request.META['LANGUAGE_CODE'] = 'es'

        content = render_to_string('history/show_list.html', output, context_instance=RequestContext(request))
        local = ListLocal.objects.get(list=list, language=request.META['LANGUAGE_CODE'])
        
        history = HistoryLocal(list=list, language=request.META['LANGUAGE_CODE'], name=local.name, obs=local.obs)
        history.content = content
        history.save()

    except:
        print 'not saved local %s to list %s' % (request.META['LANGUAGE_CODE'], list.id)

    return HttpResponse('Saved list %s.' % list.id)


def show_history(request, id):

    output = {}
    language = request.LANGUAGE_CODE

    history = get_object_or_404(History, pk=id)
    history_local = HistoryLocal.objects.filter(history=history).get(language=language)

    if not history_local:
        history_local = history

    output['history'] = history
    output['history_local'] = history_local

    return render_to_response('history/show_history.html', output, context_instance=RequestContext(request))
   
