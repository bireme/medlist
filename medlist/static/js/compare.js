$(function(){

	var checkbox = $(".list_filter");
	var form = $("#lists_filter");
	var hidden = $("#id_hidden");
	var select = $("#select_countries");
	var matches = $(".matches");

	function submit_lists_filter() {
		
		// adding all checked lists to string
		lists = "";
		checkbox.each(function(){
			if($(this).is(':checked')) {
				lists += $(this).val() + ",";
			}
		});

		// adding country list selected to string
		if(select.val() != "") {
			lists += select.val() + ",";
		}

		// changing the matches parameters to true or false
		matches.each(function(){
			current_hidden_id = "#id_hidden_" + $(this).attr('rel');
			if($(this).is(":checked")) {
				$(current_hidden_id).val('true');
			} else {
				$(current_hidden_id).val('false');
			}
		});
		

		// remove latest comma of the string
		if(lists != "") {
			lists = lists.substring(0,(lists.length - 1))
		}

		// adding string to hidden value
		hidden.val(lists);

		// submit the form
		form.submit();
	}

	// engine to storage selected lists
	var lists_selected = hidden.val().split(',');

	// check all the lists which was selected
	checkbox.each(function(){
		for(list in lists_selected) {
			if(lists_selected[list] == $(this).val()) {
				$(this).attr('checked', true);
			}
		}
	});

	// select country list which as selected
	select.find("option").each(function(){
		for(list in lists_selected) {
			if(lists_selected[list] == $(this).val()) {
				$(this).attr('selected', true);
			}
		}
	});

	// check all the matches which was selected
	var all = true
	matches.each(function(){
		current_hidden_id = "#id_hidden_" + $(this).attr('rel');
		if($(current_hidden_id).val() == "true") {
			all = false
			$(this).attr('checked', 'true');
		}
	});

	// listenning click on special lists
	checkbox.click(function(){
		submit_lists_filter();				
	});

	// listening change on country lists
	select.change(function(){
		submit_lists_filter();
	});

	matches.change(function(){
		submit_lists_filter();
	});


})