
{if $doc->db eq 'DECS'}
    <div class="text_abstract">
        <a href="#" onclick="javascript:refineByIndex('{$doc->ti_pt[0]}','mh')"><img src="./image/common/viewFullText.gif"/></a>
        <a href="#" onclick="javascript:refineByIndex('{$doc->ti_pt[0]}','mh')">{$texts.SEARCH_USING_TERMINOLOGY}</a>
    </div>

{else}

    {capture name=fulltextlinks}
         {iahlinks scielo=$links->response->docs document=$doc->ur id=$doc->id lang=$lang la_text=$doc->la la_abstract=$doc->la_ab}
    {/capture}

    <div style="display: none;" class="linkBox boxContent" id="linkBox_{$doc->id}">
        <div class="showBox">
            {$smarty.capture.fulltextlinks}
        </div>
        <span class="arrowBox"></span>
    </div>

    {* mostra linha com links para resumo e texto completo disponiveis para scielo *}
    {if $scieloLinkList|@count > 0}
        <div class="text_abstract">           
            {$abstractFulltextList}
        </div>
    {/if}

    {* mostra linha com resumo e texto completo informadas no documento *}
    {if  $scieloLinkList|@count == 0 AND ($doc->ab|@count > 0 OR $fulltextLinkList|@count > 0)}
        <div class="text_abstract">
            
            {if  $doc->ab|@count > 0}
                <a name="abs"></a>
                <span>
                    <a href="resources/{$doc->id}">{$texts.ABSTRACT}</a>
                </span>
            {/if}
            
            {if $fulltextLinkList|@count > 1}
                <a name="abs"><img src="./image/common/viewFullText.gif"/></a>
                <span>
                    <a href="#" onclick="showhideLayers('linkBox_{$doc->id}'); return false;">
                        &#160;{$texts.FULLTEXT}                        
                    </a>
                </span>
            {elseif $fulltextLinkList|@count > 0}
                <a name="abs"><img src="./image/common/viewFullText.gif"/></a>
                <span>
                    <a href="{$fulltextLinkList[0]}" target="_blank">
                    &#160;{$texts.FULLTEXT}                        
                    </a>
                </span>
            {/if}
        </div>
    {/if}

    {if $doc->ur_AUDIO|@count > 0}
        <div class="action">
            {if $doc->ur_AUDIO|@count > 1}
                <a href="#" onclick="showhideLayers('linkMid_{$doc->id}'); return false;">
                    <img src="./image/common/icon_audio.gif"/>
                    &#160;<span>Áudio</span>                        
                </a>
                <div style="display: none; float: none;" class="linkBox boxContent" id="linkMid_{$doc->id}">
                    <div class="showBox">
                        <ul>
                            {foreach from=$doc->ur_AUDIO item=media}
                                <li><a href="{$media}">{$media}</a></li>
                            {/foreach}
                        </ul>
                    </div>
                    <span class="arrowBox"></span>
                </div>
            {else}
                <a href="{$doc->ur_AUDIO[0]}">
                    <img src="./image/common/icon_audio.gif"/>
                    &#160;<span>Áudio</span>
                </a>
            {/if}
        </div>
    {/if}

    {if $doc->ur_MULTIMIDIA|@count > 0}
        <div class="action">
            {if $doc->ur_MULTIMIDIA|@count > 1}
                <a href="#" onclick="showhideLayers('linkMid_{$doc->id}'); return false;">
                    <img src="./image/common/icon_video.gif"/>
                    &#160;<span>Vídeo</span>                        
                </a>
                <div style="display: none; float: none;" class="linkBox boxContent" id="linkMid_{$doc->id}">
                    <div class="showBox">
                        <ul>
                            {foreach from=$doc->ur_MULTIMIDIA item=media}
                                <li><a href="{$media}">{$media}</a></li>
                            {/foreach}
                        </ul>
                    </div>
                    <span class="arrowBox"></span>
                </div>
            {else}
                <a href="{$doc->ur_MULTIMIDIA[0]}">
                    <img src="./image/common/icon_video.gif"/>
                    &#160;<span>Vídeo</span>
                </a>
            {/if}
        </div>
    {/if}

    <div class="print">
        <a href="index.php?q=%2Bid:(%22{$doc->id}%22)&amp;lang={$lang}&amp;printMode=true">
            <img src="./image/common/icon_print.gif"/>
            &#160;<span>{$texts.PRINT}</span>
        </a>
    </div>
    {if $doc->db|contains:"MEDLINE" or $doc->services|@contains:"SCAD"}
        <div class="scad">
            <a href="{$config->photocopy_url}&lang={$lang}&db={$doc->db|upper}&ident={$refID}">
                <img src="./image/common/icon_scad.gif"/>
                &#160;<span>{$texts.PHOTOCOPY}</span>
            </a>
        </div>
    {/if}

    {if isset($smarty.cookies.userTK)}
        <div class="scielo">
                <a href="#">
                    <img src="./image/common/icon_addToFolder.gif"/>
                    &#160;<span>{$texts.ADD_TO_COLLECTION}</span>
                </a>
        </div>
    {/if}

{/if}
