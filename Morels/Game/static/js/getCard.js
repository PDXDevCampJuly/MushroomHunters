/**
 * Created by Chelsea on 10/27/15.
 */

var cards = [];
var forest = [];
var decay = [];
var sellingCards = [];
var sellingCrdsVal = [];
var crdSource = [];
var plsBeFale = true;
var method = ['buyCards', '2'];
var testtest = ['takefromfeet'];
var pan = [];
//var buying =false;

(function createPost() {
    $('#hand').each(function () {

        $(this).find('li').each(function () {
            var classNumber = $(this).attr('class');
            cards.push(classNumber);
        });
    });
}());

(function(){
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

$('.forest').mouseover(function(e) {
    var cardClass = ($(e.target).attr('class'));
    if (cardClass == 0){
        cardClass = 1;
    }
    var stick = sticks - parseInt(cardClass);
    if (stick >= 0){
        console.log("goo");
        $(this).mouseover(function() {
            $(this).attr('class', 'test');

        });
    }
    else{
        console.log("boop");
        $('.forest').sortable({
            items: ':not(.forest)',
        start: function(){
        $('#forest', this).each(function(){
            var $this = $(this);
            $this.data('pos', $this.index());
        });
    }
    //change: function(){
    //    $sortable = $(this);
    //    $statics = $('.static', this).detach();
    //    $helper = $('<li></li>').prependTo(this);
    //    $statics.each(function(){
    //        var $this = $(this);
    //        var target = $this.data('pos');
    //
    //        $this.insertAfter($('li', $sortable).eq(target));
    //    });
    //    $helper.remove();
    //}
});
    }
});


//$(".test").mousedown(function (e)
//{
//    e.preventDefault(); //this nullifies the click
//    if ($(this).hasClass('.test'))
//    {
//
//    }
//});

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
            console.log("gi")
        }

    });
}

function sendAjax() {
    $.ajax({
        url: '/game/' + $game_id + '/update/', // the endpoint
        method: "POST", // http method
        data: {cards: cards, forest: forest, decay:decay, testtest:testtest},
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

function createDecay() {
    $('#decay').each(function () {

        $(this).find('li').each(function () {
            var classNumber = $(this).children('img').attr('id');
            decay.push(parseInt(classNumber));
        });
    });
}

function createForest() {
    $('#forest').each(function () {

        $(this).find('li').each(function () {
            var classNumber = $(this).children('img').attr('id');
            forest.push(parseInt(classNumber));
        });
    });
}

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


function checkBuy() {
    $('#hand').each(function () {
          plsBeFale = ($(this).find('li').hasClass('test '));
          buying = true;
    });
}

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

$('#post-sell').on('submit', function (event) {
    event.preventDefault();
    console.log("Selling form submitted! Let's see if it goes through");  // sanity check
    if (player == currentPlayer) {
        checkValid();
        var chkval = crdSource.allValuesSame();
        if (chkval == true){
            console.log(crdSource.length);
            if (pan.length == 1 ) {
                if (crdSource.length >= 2) {
                    event.preventDefault();
                    createSell();
                    sendSellAjax();
                }
            }
        }
        //location.reload().delay( 1100 );
    }
    else{
        event.preventDefault();
    }
});


$('#post-play').on('submit', function (event) {
    event.preventDefault();
      // sanity check
    if (player == currentPlayer) {
        checkValid();
        var checkval = crdSource.allValuesSame();
        console.log(checkval);
        if (checkval == true){
            console.log(crdSource.length);
            if (crdSource.length >= 2) {

                console.log("Playing cards form submitted! Let's see if it goes through");
                event.preventDefault();
                createSell();
                sendPlayAjax();
                //location.reload().delay( 1100 );
            }
        }
    }
    else{
        console.log("Blahb");
        event.preventDefault();
    }
});


$('#post-form').on('submit', function (event) {
    event.preventDefault();
    console.log("Takeing cards form submitted! Let's see if it goes through");  // sanity check
    if (player == currentPlayer) {
        event.preventDefault();
        createDecay();
        createForest();
        checkBuy();
        console.log('printing sendBuyAjax');
            console.log(plsBeFale);
        if (plsBeFale === false) {
            //sendBuyAjax();
            sendAjax();
            //location.reload().delay( 1100 );
        }else{
            //sendAjax();
            sendBuyAjax();
        }
    }

    else{
        event.preventDefault();
    }
});



Array.prototype.allValuesSame = function() {

    for(var i = 1; i < this.length; i++)
    {
        if(this[i] !== this[0])
            return false;
    }

    return true;
};
