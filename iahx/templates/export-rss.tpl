<?xml version="1.0" encoding="UTF-8"?>

<rss version="2.0">
	<channel>
		<title>{$texts.TITLE}: {$smarty.request.q}</title>
		<link>{$url}</link>
		<description>{$texts.DESCRIPTION}</description>

		{foreach from=$result->response->docs item=doc}

			{capture name=scieloLinks}
				{iahlinks scielo=$links->response->docs document=$doc->ur id=$doc->id lang=$lang}
			{/capture}

			<item>
				<guid>{$doc->id}</guid>
				{foreach from=$doc->name item=name}
					{assign var="newname" value="^"|explode:$name}
					
					{if $newname[0] eq $lang}
						<title>{$newname[1]|capitalize}</title>
					{/if}
				{/foreach}

				<author>{$texts.TITLE}</author>
            	<source>PRAIS</source>

				{if $doc->ur|@count > 0}
					<link>{$doc->ur[0]|replace:"&":"&amp;"}</link>
				{else}
					<link>{$url}?detail=1&amp;q=id:{$doc->id}</link>
				{/if}
				<description/>
                <keywords/>
			</item>
		{/foreach}
	</channel>
</rss>
