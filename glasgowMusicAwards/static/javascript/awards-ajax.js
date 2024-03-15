$(document).ready(function() {
    $('.vote_btn').click(function() {

        var voteIdVar;
        var username;
        var genre;


        voteIdVar = $(this).attr('data-artistid');
        username = $(this).attr('data-username');
        genre = $(this).attr('data-genre');

        alert("You have voted for " + voteIdVar)

        $.get('/awards/vote_artist/', {'artistName': voteIdVar, 'genre' : genre, 'username' : username}, 
        function(data) {
            $('.vote_btn').hide();
            $('.voteCount').html(data);
        })
    });
});