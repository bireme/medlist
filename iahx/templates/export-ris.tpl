{foreach from=$result->response->docs item=doc}
{if $doc->db|@contains:"MEDLINE"}
	{assign var=refDB value=MEDLINE}
	{assign var=refID value=$doc->id|substring_after:"-"}
{else}
    {assign var=refDB value=$doc->db}	
	{assign var=refID value=$doc->id}
{/if}

{if $doc->type[0] eq 'article'}
TY  - JOUR
{/if}
{if $doc->type[0] eq 'non-conventional'}
TY  - GEN
{/if}
{if $doc->type[0] eq 'book'}
TY  - BOOK
{/if}
{foreach item=au from=$doc->au}
AU  - {$au}
{/foreach}
{foreach item=ti from=$doc->ti}
T1  - {$ti}
{/foreach}
{if $doc->ta}
JO  - {$doc->ta[0]}
{/if}
{if $doc->vi neq ''}
VL  - {$doc->vi[0]}
{/if}
{if $doc->ip neq ''}
IS  - {$doc->ip[0]}
{/if}
DB  - {$refDB}
DP  - http://www.bvsalud.org
ID  - {$refID}
LA  - {$doc->la[0]}
{if $doc->pg > 0}
{if $doc->pg[0]|contains:"-"}
SP  - {$doc->pg[0]|substring_before:"-"}
EP  - {$doc->pg[0]|substring_after:"-"}
{else}
SP  - {$doc->pg[0]}
EP  - {$doc->pg[0]}
{/if}
{if $doc->da > 0}
DA  - {$doc->da[0]|substr:0:4}/{$doc->da[0]|substr:4:2}/{$doc->da[0]|substr:6:2}
{/if}
{/if}
{if $doc->da > 0}
PY  - {$doc->da[0]|substr:0:4}
{/if}
{foreach item=mh from=$doc->mh}
KW  - {$mh}
{/foreach}
{foreach item=ab from=$doc->ab}
N2  - {$ab}
{/foreach}
{foreach item=ur from=$doc->ur}
UR  - {$ur}
{/foreach}
ER  - 

{/foreach}
