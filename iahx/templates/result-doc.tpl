{if isset($smarty.request.debug)}
    {debug}
{/if}

{foreach from=$result->response->docs item=doc name=doclist}

	<div id="{$doc->id}" class="record">

    <div class="yourSelectionCheck">
        <a onclick="markUnmark(this.firstChild,'{$doc->id}');"><img src="./image/common/box_unselected.gif" state="u" alt="{$texts.MARK_DOCUMENT}" title="{$texts.MARK_DOCUMENT}" /></a>
    </div>
    <div class="position">
        {$smarty.foreach.doclist.index+$pagination.from}.
    </div>
    <div class="data">
		<h3>
			<a href="{$config->medlist_url}medicine/{$doc->id}/">
				{extractdata element=$doc->name part=$lang default="en"}
			</a>
		</h3>
		
        <!-- pharmaceutical forms -->
        {if $doc->pharmaceutical_form}
			<div class="pharmaceutical_forms">
				<h4>{$texts.LABEL_PHARMACEUTICAL_FORMS}</h4>
				<ul>
				{foreach from=$doc->pharmaceutical_form item=item}
					<li class="pharmaceutical_form">
						{extractdata element=$item part=$lang}: {extractdata element=$item part=comp}
					</li>	
				{/foreach}
				</ul>
			</div>
		{/if}
        
        <!-- Lists -->
        {if $doc->list OR $doc->country}
			<div class="in_lists">
				<h4>{$texts.LABEL_IN_LIST}</h4>
				<ul>
					{foreach from=$doc->list item=list}
						<li>{extractdata element=$list part=$lang}</li>
					{/foreach}
					{foreach from=$doc->country item=list}
						<li>{extractdata element=$list part=$lang}</li>
					{/foreach}				
				</ul>
			</div>
		{/if}
		<div class="spacer"></div>
    </div>

    <div class="user-actions">
        {include file="doc-actions-bar.tpl"}
    </div>

</div>
{/foreach}
