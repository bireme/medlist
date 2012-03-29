<div class="top">
	<div class="topMenu">
		<ul>
			<li><a href="{$config->prais_url}">{$texts.HOME}</a></li>
			<li><a href="#">{$texts.ABOUT_US}</a></li>
			<li><a href="#">{$texts.SEND_COMMENT}</a></li>
			<li><a href="#">{$texts.CONTACT}</a></li>
		</ul>
	</div>
	<div class="loginBox">
		
			<input type="text" class="textEntry" />
			<input type="password" class="textEntry" />
			<input type="submit" class="submit" value="" />
		
		<div id="forgotPass"><a href="#">{$texts.FORGOT_LOGIN}</a></div>
	</div>
	<div class="spacer"></div>
	<div class="banner">
		<div id="logo"><span>Regional Platform for Innovation and Access for Health</span></div>
		<div class="identification">
			{$texts.TITLE}
		</div>
		<div class="langSelector">
			<ul>
			{foreach key=langcode item=language from=$texts.AVAILABLE_LANGUAGES}
				{if $langcode|lower eq $lang }
					{assign var="class" value=" class='selected'"}
				{else}
					{assign var="class" value=""}
				{/if}
				<li><a id="lang_{$langcode|lower}" href="#" onclick="searchForm.q.value='';changeFormParameter('lang','{$langcode|lower}');" {$class}><span>{$language}</span></a></li>
			{/foreach}
			</ul>
		</div>
	</div>
</div>

