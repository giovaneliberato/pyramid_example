var postAnswer = function(){
	var answer = $('#answer-field').val();
	var params = {'answer': answer,
				  'question_id': $(this).attr('data-id')};

	$.post('/answer', params, function(data){
		$('#answers').append('<p>'+ answer +'</p>');
		$('#answer-field').val('');
	});
}


var upVote = function(){
	$.post('/vote_answer', {'answer_id': $(this).attr('data-id'), 'vote_type': $(this).attr('data-vote')}, function(data){
		alert(data)
	});
}

$(document).ready(function(){
	$('#answer-btn').click(postAnswer);
	$('.up-vote').click(upVote)
})