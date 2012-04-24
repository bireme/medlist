				
				{literal}
				<script language="JavaScript" type="text/javascript">
					if(!cookiesEnabled()){
						document.getElementById('yourSelection').style.display = 'none';
						document.getElementById('searchHistory').style.display = 'none';
						document.getElementById('mailSend').style.display = 'none';
						hideClass('div','yourSelectionCheck');
						alertBookmarkUnavailable();
					}
				</script>
				{/literal}
			</div>
			<div class="spacer"></div>
		</div> <!-- div content -->

		<div class="footer">
		</div>

        {if $config->google_analytics_code != ''}
			<script type="text/javascript">
			  var _gaq = _gaq || [];
			  _gaq.push(['_setAccount', '{$config->google_analytics_code}']);
			  _gaq.push(['_trackPageview']);
			{literal}
			  (function() {
				var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
				ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
				var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
			  })();
			{/literal}
			</script>
		{/if}
	</body>
</html>
