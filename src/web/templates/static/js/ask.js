var wrapAnswer = function(answer, answer_id){
	return '<div class="row-fluid"><div class="span1">'+
			'<h1 class="vote-numbers">0</h1>'+
			'<a class="vote" href="#" data-id="'+
			answer_id +'" data-vote="UP"><span class="label label-success">'+
			'<i class="icon icon-white icon-plus"></i></span></a>'+
			'<a class="vote" href="#" data-id="'+ answer_id +'" data-vote="DOWN">'+
			'<span class="label label-important"><i class="icon icon-white icon-minus"></i></span></a>'+
			'</div>'+
			'<div class="span10">'+
			'<p>' + answer + '</p>'+
			'</div></div>';
}

var vote = function(){
	var div = $(this).parent();
	$.post('/vote_answer', {'answer_id': $(this).attr('data-id'), 'vote_type': $(this).attr('data-vote')}, function(data){
		data = $.parseJSON(data);
		div.children('h1').html(data['votes']);
	});
}


var postAnswer = function(){
	var answer = $('#answer-field').val();
	var params = {'answer': answer,
				  'question_id': $(this).attr('data-id')};

	$.post('/answer', params, function(data){
		data = $.parseJSON(data);
		$('.answers-container').append(wrapAnswer(answer, data['answer_id']));
		$('#answer-field').val('');
		$('.vote').click(vote);
	});
}



$(document).ready(function(){
	$('#answer-btn').click(postAnswer);
	$('.vote').click(vote);
})