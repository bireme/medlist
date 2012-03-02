{foreach from=$result->response->docs item=doc}

{occ element=$doc->au separator=;}. - {occ element=$doc->ti separator=" - "}. {occ  element=$doc->fo separator=;}

{/foreach}
