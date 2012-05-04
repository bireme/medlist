{assign var="facetBrowse" value=$smarty.post.fb|substring_before:":"}

<div class="bContent" id="refine_facet">
{foreach from=$result->facet_counts item=cluster}

  {foreach key=key item=item from=$cluster}

	{assign var="label" value="REFINE_$key"}
	{assign var="totalItems" value=$item|@count}

	{if $totalItems gt 0}

      	<div id="{$key}">
		<strong>{$texts.$label}</strong>
		<a href="#" onclick="showChart(this,'{$texts.$label}','{$key}')" class="thickbox"><img src="image/common/chart.gif" border="0"></a>
		<ul id="{$key}_set">
			{foreach key=clusterKey item=clusterItem from=$item}
				<li>				
					<a href="#" onclick="javascript:applyFilter('{$clusterItem[0]}','{$key}')">
					{if $clusterItem[0]|contains:"^"}
						{extractdata element=$clusterItem[0] part=$lang}
					{else}
						{$clusterItem[0]|truncate:35}
					{/if}	
					</a> ({$clusterItem[1]})
				</li>
			{/foreach}
			{if $totalItems gt 0 AND $totalItems%$colectionData->cluster_items_limit eq 0}
				<li><a href="#" onclick="javascript:showMoreClusterItems('{$key}','{$totalItems+$colectionData->cluster_items_limit}'); return false"><b>{$texts.SHOW_MORE_ITEMS}...</b></a></li>
			{/if}
		</ul>
	</div>

	{/if}
  {/foreach}
{/foreach}
</div>
