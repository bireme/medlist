{if isset($smarty.request.debug)}
    {debug}
{/if}

{foreach from=$result->response->docs item=doc name=doclist}

    {* assign var=refID value=$doc->id|regex_replace:"/.*-/":"" *}
    {assign var=refID value=$doc->id|substring_after:"-"}

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
            <h4>Pharmaceutical Forms</h4>
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

        <strong>EML:</strong> {if $EML} YES {else} NO {/if} <br>
        <strong>EMLc:</strong> {if $EMLc} YES {else} NO {/if} <br>
        <strong>High Cost:</strong> {if $HighCost} YES {else} NO {/if} <br>
        <strong>Strategic Fund:</strong> {if $StrategicFund} YES {else} NO {/if} <br>

        <!-- countries -->
        {if $doc->country|@count > 0}
            <h4>{$texts.LABEL_IN_COUNTRIES}</h4>
            <ul>
                {foreach from=$doc->country item=country}
                    <li>{$country}</li>
                {/foreach}
            </ul>
        {/if}
        
        <!--
        {if $doc->list|@count > 0}
            <br><strong>{$texts.LABEL_IN_LIST}:</strong>
            {assign var="count" value=1}
            {foreach from=$doc->list item=list}
                {if $count < $doc->list|@count}
                    {$list},
                {else}
                    {$list}.
                {/if}
                {assign var="count" value=$count+1}
            {/foreach}
        {/if}
        
        {if $scieloLinkList|@count > 0}
            <div class="abstractFulltextList">
                
            </div>
        {/if}
        -->

    </div>
    <div class="spacer"></div>

    <div class="user-actions">
        {include file="doc-actions-bar.tpl"}
        
        {if $doc->db|contains:"MEDLINE"}
            <div class="pubmed">
                <a href="{$doc->id}">
                <img src="./image/common/icon_PubMed.gif"/>
                <span>PubMed LinkOut</span>
                </a>
            </div>
        {/if}
        
    </div>

</div>
{/foreach}
