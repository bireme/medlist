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
    
        {assign var="setted" value=false}
        {foreach from=$doc->name item=name}
            {assign var="newname" value="^"|explode:$name}
            
            {if $setted == false}
                {if $newname[0] eq $lang}
                    <h3><a href="#">{$newname[1]|capitalize}</a></h3>
                    {assign var="setted" value=true}
                {/if}
            {/if}
        {/foreach}

        {if $setted == false}
            <h3><a href="#">{$newname[1]|capitalize}</a></h3>
        {/if}
		
        <!-- pharmaceutical forms -->
        <div class="pharmaceutical_forms">
            <h4>{$texts.LABEL_PHARMACEUTICAL_FORMS}</h4>
            <ul>
            {foreach from=$doc->pharmaceutical_form item=item}
                <li class="pharmaceutical_form">
                    <p>
                        {assign var="lines" value="\";"|explode:$item}
                        {foreach from=$lines item=line}
                            {assign var="values" value=":"|explode:$line}
                            
                            {assign var="key" value=$values[0]|trim}
                            {assign var="value" value=$values[1]|trim|replace:"\"":""}
                            
                            {if $key eq 'type'}
                                <strong>{$value}:</strong>
                                
                            {elseif $key eq 'observation'}
                                <strong>Observation:</strong>{$value}<br>
                            
                            {elseif $key eq 'value'}
                                {$value}<br>
                            
                            {else}
                                else
                                <strong>{$value}:</strong>
                            {/if}               
                            
                        {/foreach}
                    </p>
                </li>
            {/foreach}
            </ul>
        </div>
        
        <!-- Lists -->
        <div class="in_lists">
			<h4>{$texts.LABEL_IN_LIST}</h4>
			{foreach from=$doc->list item=list}
				{if $list eq "EML"}
					{assign var="EML" value=true }
				{elseif $list eq "EMLc"}
					{assign var="EMLc" value=true }
				{elseif $list eq "High Cost"}
					{assign var="HighCost" value=true }
				{elseif $list eq "Strategic Fund"}
					{assign var="StrategicFund" value=true }
				{/if}
			{/foreach}
			
			<ul>			
				<li><strong>EML:</strong> {if $EML} YES {else} NO {/if} </li>
				<li><strong>EMLc:</strong> {if $EMLc} YES {else} NO {/if} </li>
				<li><strong>High Cost:</strong> {if $HighCost} YES {else} NO {/if} </li>
				<li><strong>Strategic Fund:</strong> {if $StrategicFund} YES {else} NO {/if} </li>
			</ul>
		</div>


    </div>
    <div class="spacer"></div>

    <div class="user-actions">
        {include file="doc-actions-bar.tpl"}
    </div>

</div>
{/foreach}
