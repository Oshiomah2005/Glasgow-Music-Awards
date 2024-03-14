$(document).ready(function() {
    $('.vote_btn').click(function() {
        var voteIdVar;
        var userid;
        var genre;

        voteIdVar = $(this).attr('data-artistid');
        userid = $(this).attr('data-userid');
        genre = $(this).attr('data-genre');
        alert('You have voted.')

        $.get('/awards/vote_artist/', {'artist_id': voteIdVar, 'genre' : genre, 'userid' : userid}, 
        function(data) {
            $('.voteCount').html(data);
            $('.vote_btn').hide();
        })
    });
});