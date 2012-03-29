{if $result eq ''}
    <div class="noResults">
        {$texts.COLLECTION_UNAVAILABLE}
    </div>
{elseif isset($result->response->connection_problem)}
    <div class="noResults">
        {$texts.CONNECTION_ERROR}
    </div>
{elseif $numFound eq '0'}
    <div class="noResults">
        {$texts.NO_RESULTS}
    </div>
{else}

<div class="results">

    <div class="resultServices">
		<div class="refineSearch" id="refineSearch">
			{include file="result-clusters.tpl"}
		</div>
    <div></div>


</div>
{if $numFound > 0}
    <div class="resultOptions">
                <div class="resultNavigation">{include file="result-navigation.tpl"}</div>
                <div class="resultsBar">
                        <div class="selectAll" id="selectAll">
                            <input type="button" value="{$texts.SELECT_PAGE}" onclick="markAll(); showhideLayers('selectAll');showhideLayers('clearAll')" />
                        </div>
                        <div class="clearAll" id="clearAll" style="display: none">
                            <input type="button" value="{$texts.UNSELECT_PAGE}" onclick="unmarkAll();showhideLayers('clearAll');showhideLayers('selectAll')" />
                        </div>
                        <div class="orderBy">
                            
                            <select name="sortBy" class="inputText" onchange="javascript:changeOrderBy(this);">
                                <option value="">{$texts.SORT_OPTIONS}</option>
                                {foreach from=$colectionData->sort_list->sort item=sortItem}
                                    {assign var=sortName value=$sortItem->name|upper}
                                    {assign var=sortValue value=$sortItem->value}
    
                                    {if $sortName neq ''}
                                        {if $sortName == $smarty.request.sort}
                                            <option value="{$sortName}" selected="1">{$texts.SORT.$sortName}</option>
                                        {else}
                                            <option value="{$sortName}">{$texts.SORT.$sortName}</option>
                                        {/if}
                                    {/if}
                                {/foreach}
                            </select>
                        </div>
    
                        {if $colectionData->format_list->format|@count > 0}
                            <div class="format">
                                
                                <!--<select name="fmt" class="inputText" onchange="javascript:changeDisplayFormat(this);">
                                    <option value="">{$texts.FORMAT_OPTIONS}</option>                               
                                    {foreach from=$colectionData->format_list->format item=formatItem}
                                        {assign var=formatName value=$formatItem->name|strip}
                                        {assign var=textsDisplay value=$texts.DISPLAY}
    
                                        {if $formatName neq ''}
                                            {if $formatName == $smarty.request.fmt}
                                                <option value="{$formatName}" selected="1">{$texts.DISPLAY.$formatName}</option>
                                            {else}
                                                <option value="{$formatName}">{$texts.DISPLAY.$formatName}</option>
                                            {/if}
                                        {/if}
                                    {/foreach}
                                </select>-->
                            </div>
                        {/if}
    
                        <div class="feed">
                            <a class="RSS" href="index.php?output=rss&site={$site}&col={$col}&lang={$lang}{$getParams}"><span>RSS</span></a>
                            <a class="XML" href="index.php?output=xml&site={$site}&col={$col}&lang={$lang}{$getParams}"><span>XML</span></a>
                        </div>


            </div>
			<div class="totalResults">
				{$texts.RESULTS}&#160;
				<strong>{$pagination.from}-{$pagination.to}</strong> de <strong>{$pagination.total|number_format:0:",":"."}</strong>
			</div>
    </div>
{/if}
<div class="resultSet">
    {if $fmt eq ''}
        {include file="result-doc.tpl"}
    {else}
        {include file="result-doc-$fmt.tpl"}
    {/if}

    {include file="result-navigation.tpl"}
</div>


<script language="JavaScript" type="text/javascript">recoverBookmarks();</script>
</div>

{/if}
