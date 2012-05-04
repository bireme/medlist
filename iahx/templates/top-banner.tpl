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

<div class="top">
	<div class="topMenu">
		<ul>
			<li><a href="{$config->prais_url}">{$texts.HOME}</a></li>
			<!--
			<li><a href="#">{$texts.ABOUT_US}</a></li>
			<li><a href="#">{$texts.SEND_COMMENT}</a></li>
			<li><a href="#">{$texts.CONTACT}</a></li>
			-->
		</ul>
	</div>
	<div class="spacer"></div>

	<div class="banner">
		<div id="logo" class="logo-{$lang}"><span>Regional Platform for Innovation and Access for Health</span></div>
		<div class="identification">
			{$texts.TITLE}
		</div>

		<div class="top-rightBlock">
			<div class="separator">
			</div>
			<div id="top-pahoLogo">
				<img src="image/common/logo-paho.png" title="Pan American Health Organization - PAHO/WHO">
			</div>
			<div class="langSelector">
				<div class="currentLang">
					<a href="#">
						<span>							
							{if $lang != 'en' }
								{$texts.AVAILABLE_LANGUAGES[$lang]}
							{else}
								{$texts.AVAILABLE_LANGUAGES.en}
							{/if}
						</span>
						<div class="arrow-bottom-wht"></div>
					</a>
				</div>
				<div class="availableLangs" id="langs">
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
		</div>
	</div>	
</div>

