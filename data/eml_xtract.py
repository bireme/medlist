#!/usr/bin/env python
# coding: utf-8

from itertools import dropwhile
from pprint import pprint
import re
import json

EML_FILENAME = 'eml17-copypaste.txt'

def get_index():
    excludes = [
        'Essential Medicines', 'WHO Model List', 
        'EML 17 (March 2011)', '17th edition',
        ]
    entries = []
    with open(EML_FILENAME) as eml:
        tudo = ((i+1, lin.strip()) for i, lin in enumerate(eml))
        index = dropwhile((lambda t: not t[1].startswith('Index')), tudo)
        index.next()
        for nl, lin in index:
            lin = lin.replace('‐', '-')
            if any([not lin,
                   lin.startswith('page - '),
                   lin in excludes]):
                continue
            if '...' not in lin: # read next line to complete entry
                head = lin # eg: "sodium stibogluconate or"...
                nl, lin = index.next() # "meglumine antimoniate"
                if '-2H20' in head:
                    head = head.replace('-2H20','- 2H₂O')
                lin = head + ' ' + lin
                #print '{0} "{1}"'.format(nl, lin)
            parts = lin.split('...')
            term = parts[0].strip()
            pages = parts[-1].replace('.',' ').strip()
            pages = [int(p) for p in pages.split(',')]
            entries.append((term, pages))
    return entries

def get_sections():
    excecoes = ['13.5 g/L']
    re_section = re.compile(r'^\d+\.')
    re_page = re.compile(r'^page - (\d+)')
    page = prev_page = 0
    sec_ant = (0,)
    sections = []
    with open(EML_FILENAME) as eml:
        tudo = ((i+1, lin.rstrip()) for i, lin in enumerate(eml))
        for nl, lin in tudo:
            if lin in excecoes:
                continue
            if re_section.match(lin):
                #print lin
                sec_num, sec_title = lin.split(' ', 1)
                sec_num = sec_num.rstrip('.')
                # convert to check sequence
                sec_num = tuple( (int(s) for s in sec_num.split('.')) )
                sec_num
                #print nl, sec_page, sec_num, sec_title
                sec_dif = sec_num[0] - sec_ant[0] 
                assert sec_dif in [0, 1]
                assert sec_ant != sec_num
                # assert that section 1. is followed by 1.1. or 2.
                assert sum( (b-a for a, b in zip(sec_ant+(0,), sec_num)) ) == 1
                #sec_str = '.'.join(str(n) for n in sec_num)
                # page numbers appear after the page content
                sections.append( (sec_num, sec_title, page+1) )
                sec_ant = sec_num
            if sec_ant[0] and 'complementary list' in lin.lower():
                sections.append( (sec_ant+('complementary',), lin.strip(), page+1) )                
            else:
                page_match = re_page.match(lin)
                if page_match is not None:
                    #print lin
                    page = int(page_match.group(1))
                    assert (page - prev_page) == 1
                    prev_page = page
    return sections

def index_sort_key(entry):
    return entry[0].lower().replace('-','')

def list_medicines(index):
    from base28 import reprbase
    for i, entry in enumerate(index):
        pages = ','.join(str(x) for x in entry[1])
        print '{0}\t{1}\t{2}'.format(reprbase(i+28), entry[0], pages)

if __name__=='__main__':
    index = get_index()
    index.sort(key=index_sort_key) 
    print json.dumps(index, indent=2)
    #list_medicines(index)
    sections = get_sections()
    #print json.dumps(sections, indent=2)

"""
Termos avulsos (sem num de pagina):
2132 "estradiol cypionate + medroxyprogesterone"
2136 "ethambutol + isoniazid + pyrazinamide +"
2145 "factor IX complex (coagulation factors, II, VII,"
2191 "intraperitoneal dialysis solution"
2293 "potassium ferric hexacyano‐ferrate(II)- 2H₂0"
2371 "sodium stibogluconate or"


"""