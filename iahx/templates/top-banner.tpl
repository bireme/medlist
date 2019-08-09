<header>
    <div class="tituloPrincial">
        <div class="container" style="position: relative">
            <div id="idioma">
                 <ul id="menu-idioma-language-en" class="nav-item">

                     {foreach key=langcode item=language from=$texts.AVAILABLE_LANGUAGES}
                          {if $langcode|lower neq $lang }
                              <li>
                                 <a href="#" onclick="changeFormParameter('lang','{$langcode|lower}');" {$class}>{$language}</a>
                              </li>
                          {/if}
                     {/foreach}
                 </ul>
             </div>
	         <h3 class="tituloPrincial text-center">{$texts.TITLE}</h3>
        </div>
    </div>
	<div class="container">
		<div class="row">
			<div class="col-md-12 text-center">
				<img src="./image/{$lang}/prais_top.png" alt="" class="img-fluid">
			</div>
		</div>
		<hr>
	</div>
</header>
