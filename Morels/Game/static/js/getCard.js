/**
 * Created by Chelsea on 10/27/15.
 */

var cards = [];
var forest = [];
var decay = [];
var sellingCards = [];
var sellingCrdsVal = [];
var crdSource = [];
var hasClass = true;
var method = ['1', '2'];
var lengthlist = ['1'];
var pan = [];

(function createPost() {
    $('#hand').each(function () {

        $(this).find('li').each(function () {
            var classNumber = $(this).attr('class');
            cards.push(classNumber);
        });
    });
}());

(function(){
    //makes decay and forest only connect to hand and hand only connect to placeholder
    if (cards.length < 8){
        $(function () {
	    $("#decay,#forest").sortable({
		    connectWith: "#hand",
		start: function (event, ui) {
			ui.item.toggleClass("highlight");
		},
		stop: function (event, ui) {
			ui.item.toggleClass("highlight");
		}
	});
        $(" #hand ").sortable({
		    connectWith: "#placeholder",
		start: function (event, ui) {
			ui.item.toggleClass("highlight");
		},
		stop: function (event, ui) {
			ui.item.toggleClass("highlight");
		}
	});
    });
    }
    //If users hand is full decay and forest are diconected
    else{
        $(function () {
	    $(" #hand ").sortable({
		    connectWith: "#placeholder",
		start: function (event, ui) {
			ui.item.toggleClass("highlight");
		},
		stop: function (event, ui) {
			ui.item.toggleClass("highlight");
		}
	});

    });
    }
}());

// If cards in forest(that aren't at users feet) stickValue is less than users sticks - 1 change class to make it movable
$('.forest').mouseover(function(e) {
    var cardClass = ($(e.target).attr('class'));
    if (cardClass == 0){
        cardClass = 1;
    }
    var stick = sticks - parseInt(cardClass);
    if (stick >= 0){
        $(this).mouseover(function() {
            $(this).attr('class', 'test');

        });
    }
    else{
        $('.forest').sortable({
            items: ':not(.forest)',
        start: function(){
        $('#forest', this).each(function(){
            var $this = $(this);
            $this.data('pos', $this.index());
        });
    }
});
    }
});

// Send ajax to view that will play cards
// TODO: swap sell with play
function sendSellAjax() {
    $.ajax({
        url: '/game/' + $game_id + '/sell_cards/', // the endpoint
        method: "POST", // http method
        data: {sellingCards: sellingCards, sellingCrdsVal: sellingCrdsVal},
        success: function (json) {
            $('#post-sell').val(''); // remove the value from the input
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            console.log(errmsg, err);
        }
    });
}

// Send ajax to view that will sell cards
// TODO: swap sell with play
function sendPlayAjax() {
    $.ajax({
        url: '/game/' + $game_id + '/play_cards/', // the endpoint
        method: "POST", // http method
        data: {sellingCards: sellingCards, sellingCrdsVal: sellingCrdsVal},
        success: function (json) {
            $('#post-sell').val(''); // remove the value from the input
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            console.log(errmsg, err);
        }

    });
}

// Send ajax to view that will add card from forest
function sendAjax() {
    $.ajax({
        url: '/game/' + $game_id + '/update/', // the endpoint
        method: "POST", // http method
        data: {cards: cards, forest: forest, decay:decay, lengthlist:lengthlist},
        success: function (json) {
            $('#post-form').val(''); // remove the value from the input
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            console.log(errmsg, err);
        }
    });
}

// Appends cards in list decay to array
function createDecay() {
    $('#decay').each(function () {

        $(this).find('li').each(function () {
            var classNumber = $(this).children('img').attr('id');
            decay.push(parseInt(classNumber));
        });
    });
}

// Appends cards in list decay to array
function createForest() {
    $('#forest').each(function () {

        $(this).find('li').each(function () {
            var classNumber = $(this).children('img').attr('id');
            forest.push(parseInt(classNumber));
        });
    });
}

// Appends cards in list decay to array
function createSell() {
    $('#placeholder').each(function () {

        $(this).find('li:gt(0)').each(function () {
            var idNumber = $(this).children('img').attr('id');
            var classNumber = $(this).children('img').attr('class');
            sellingCards.push(parseInt(idNumber));
            sellingCrdsVal.push(parseInt(classNumber));
        });
    });
}


// Checks cards to see if card in hand has class test
function checkBuy() {
    $('#hand').each(function () {
          hasClass = ($(this).find('li').hasClass('test '));
          buying = true;
    });
}

// Send ajax to view that will add card to hand and remove sticks from user
function sendBuyAjax(){
    $.ajax({
        url: '/game/' + $game_id + '/buy_cards/', // the endpoint
        method: "POST", // http method
        data: {cards: cards, forest: forest, method:method},
        success: function (json) {
            $('#post-form').val(''); // remove the value from the input
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            console.log(errmsg, err);
        }
    });
}

// Checks to see if A) there's more than 1 card and B) if there's a pan
function checkValid() {
    $('#placeholder').each(function () {

        $(this).find('li:gt(0)').each(function () {
            var classsrc = $(this).children('img').attr('src');
            crdSource.push(classsrc);
            if (classsrc == '/static/pan.png'){
                pan = '1';
                crdSource.pop(crdSource)
            }
        });
    });
}

// Calls ajax if A)user is current player, B)if cards are matching, C) there's a pan, D)there's two or more cards
$('#post-sell').on('submit', function (event) {
    event.preventDefault();
    console.log("Selling form submitted! Let's see if it goes through");  // sanity check
    if (player == currentPlayer) {
        checkValid();
        var chkval = crdSource.allValuesSame();
        if (chkval == true){
            if (pan.length == 1 ) {
                if (crdSource.length >= 2) {
                    event.preventDefault();
                    createSell();
                    sendSellAjax();
                }
            }
        }
    }
    else{
        event.preventDefault();
    }
});


// Calls ajax if A)user is current player, B)is cards are matching, C)if there's more than 1 card
$('#post-play').on('submit', function (event) {
    event.preventDefault();
      // sanity check
    if (player == currentPlayer) {
        checkValid();
        var checkval = crdSource.allValuesSame();
        if (checkval == true){
            console.log(crdSource.length);
            if (crdSource.length >= 2) {

                console.log("Playing cards form submitted! Let's see if it goes through");
                event.preventDefault();
                createSell();
                sendPlayAjax();
            }
        }
    }
    else{
        event.preventDefault();
    }
});


// Calls ajax if A)user is current player, B) class is test
$('#post-form').on('submit', function (event) {
    event.preventDefault();
    console.log("Takeing cards form submitted! Let's see if it goes through");  // sanity check
    if (player == currentPlayer) {
        event.preventDefault();
        createDecay();
        createForest();
        checkBuy();
        console.log('printing sendBuyAjax');
        if (hasClass === false) {
            sendAjax();
        }else{
            sendBuyAjax();
        }
    }

    else{
        event.preventDefault();
    }
});


// see's if everything matches
Array.prototype.allValuesSame = function() {

    for(var i = 1; i < this.length; i++)
    {
        if(this[i] !== this[0])
            return false;
    }

    return true;
};
