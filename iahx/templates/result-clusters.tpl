{assign var="facetBrowse" value=$smarty.post.fb|substring_before:":"}

<div class="bContent" id="refine_facet">
{foreach from=$result->facet_counts item=cluster}

  {foreach key=key item=item from=$cluster}

	{assign var="label" value="REFINE_$key"}
	{assign var="totalItems" value=$item|@count}

	{if $totalItems gt 0}

      	<div id="{$key}">
		{if $key == 'fulltext'}
			<strong>{$texts.$label}</strong>
			(<a href="#" onclick="javascript:applyFilter('{$item[0][0]}','fulltext')">{$item[0][1]}</a>)
		{else}
			<strong>{$texts.$label}</strong>
			<a href="#" onclick="showChart(this,'{$texts.$label}','{$key}')" class="thickbox"><img src="image/common/chart.gif"></a>
			<ul id="{$key}_set">
			{if $key == 'pharmaceutical_form_type'}
				<strong>{$texts.CLUSTER_PHARM_FORM_TYPE}</strong>
			{elseif $key == 'section'}
				<strong>{$texts.CLUSTER_SECTION}</strong>
			{elseif $key == 'subsection'}
				<strong>{$texts.CLUSTER_SUBSECTION}</strong>
			{elseif $key == 'squarebox'}
				<strong>Square Box</strong>
			{elseif $key == 'list'}
				<strong>{$texts.CLUSTER_LIST}</strong>
			{elseif $key == 'country'}
				<strong>{$texts.CLUSTER_COUNTRY}</strong>
			{/if}
			
			{foreach key=clusterKey item=clusterItem from=$item}
				<li>
					<a href="#" onclick="javascript:applyFilter('{$clusterItem[0]}','{$key}')" title="{$clusterItem[0]|lower|capitalize}">{$clusterItem[0]|lower|capitalize|truncate:35}</a> ({$clusterItem[1]})
				</li>
			{/foreach}
			

		{/if}

		{if $totalItems gt 0 AND $totalItems%$colectionData->cluster_items_limit eq 0}
			<li><a href="#" onclick="javascript:showMoreClusterItems('{$key}','{$totalItems+$colectionData->cluster_items_limit}'); return false"><b>{$texts.SHOW_MORE_ITEMS}...</b></a></li>
		{/if}
		</ul>
	</div>

	{/if}
  {/foreach}
{/foreach}
</div>
