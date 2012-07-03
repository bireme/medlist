{assign var="facetBrowse" value=$smarty.post.fb|substring_before:":"}

<div class="bContent" id="refine_facet">
{foreach from=$result->facet_counts item=cluster}

  {foreach key=key item=item from=$cluster}

	{assign var="label" value="REFINE_$key"}
	{assign var="totalItems" value=$item|@count}

	{if $totalItems gt 0}

      	<div id="{$key}">
      	{if $key == 'has_evidence'}
			<strong onclick="showHideBox('{$key}')">{$texts.$label}</strong>
			(<a href="#" onclick="javascript:applyFilter('{$item[0][0]}','has_evidence')">{$item[0][1]}</a>)
      	{else}      	
			<strong>{$texts.$label}</strong>
			<a href="#" onclick="showChart(this,'{$texts.$label}','{$key}')" class="thickbox"><img src="image/common/chart.gif" border="0"></a>
			<ul id="{$key}_set">
		
			{if $key == 'observation'}
				{foreach key=clusterKey item=clusterItem from=$item}

					{capture name=obs}{translate text=$clusterItem[0] suffix=OBSERVATION_ translation=$texts}{/capture}
					{if $smarty.capture.obs ne ''}
						<li>
							<a href="#" onclick="javascript:applyFilter('{$clusterItem[0]}','{$key}')">{$smarty.capture.obs}</a> ({$clusterItem[1]})
						</li>
					{/if}
				{/foreach}
			{else}			
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
				
			{/if}
				
			{if $totalItems gt 0 AND $totalItems%$colectionData->cluster_items_limit eq 0}
				<li><a href="#" onclick="javascript:showMoreClusterItems('{$key}','{$totalItems+$colectionData->cluster_items_limit}'); return false"><b>{$texts.SHOW_MORE_ITEMS}...</b></a></li>
			{/if}
		</ul>
		{/if}
	</div>

	{/if}
  {/foreach}
{/foreach}
</div>
