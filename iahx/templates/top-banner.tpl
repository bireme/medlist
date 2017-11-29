<script>	
	$(function() {ldelim}
		var lang = "{$lang}";
		var box_langs = $(".availableLangs");
		var cur_lang = $(".currentLang");
		
		$("#lang_" + lang).hide();
		box_langs.hide();

		cur_lang.click(function(){ldelim}
			box_langs.toggle();
		 {rdelim});	
    {rdelim})    
</script>


<div class="header">
    <div class="logo">
        <a href="{$config->prais_url}" title="{$texts.HOME}">
            <img src="image/common/logo-prais-{$lang}.png">
        </a>
    </div>
    <div class="title">
        {$texts.TITLE} 
    </div>
    <div class="language" id="langs" style="display: block;">
		<ul>
			{foreach key=langcode item=language from=$texts.AVAILABLE_LANGUAGES}
				{if $langcode|lower eq $lang }
					{assign var="display" value="display: none"}
				{else}
					{assign var="display" value=""}
				{/if}
				<li id="lang_{$langcode|lower}" style="{$display}"><a id="lang_{$langcode|lower}" href="#" onclick="searchForm.q.value='';changeFormParameter('lang','{$langcode|lower}');" {$class}><span>{$language}</span></a></li>
			{/foreach}
		</ul>

    </div>
</div>
