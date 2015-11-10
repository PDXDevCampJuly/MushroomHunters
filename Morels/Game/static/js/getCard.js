/**
 * Created by Chelsea on 10/27/15.
 */

var cards = [];
var forest = [];
var decay = [];
var sellingCards = [];
var sellingCrdsVal = [];

(function create_post() {
    $('#hand').each(function () {

        $(this).find('li').each(function () {
            var classNumber = $(this).children('img').attr('id');
            console.log(classNumber);
            cards.push(classNumber);
        });
        console.log(cards);
    });
}());



$('.forest').sortable({
    items: ':not(.forest)',
    start: function(){
        $('#forest', this).each(function(){
            var $this = $(this);
            $this.data('pos', $this.index());
        });
    },
    change: function(){
        $sortable = $(this);
        $statics = $('.static', this).detach();
        $helper = $('<li></li>').prependTo(this);
        $statics.each(function(){
            var $this = $(this);
            var target = $this.data('pos');

            $this.insertAfter($('li', $sortable).eq(target));
        });
        $helper.remove();
    }
});

(function(){
    //console.log(cards.length);
    if (cards.length < 8){
        console.log("boop");
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
        console.log("whoa");
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
        console.log(cardClass);
        console.log(stick);
        console.log("yooo");
        $(e).mouseover(function() {
            //console.log(this);
            $(e).attr('class', 'test');
            console.log(e)
        });
        //$(this).mouseover(function() {
        //    console.log(this);
        //    $(this).attr('class', 'test');
        //});
    }
    else{
        console.log("bruh");
        $(e).mouseover(function() {
            console.log(this);
            $(e).attr('class', 'test');
            console.log(e)
        });
    }
});


function sendSellAjax() {
    $.ajax({
        url: '/game/' + $game_id + '/sell_cards/', // the endpoint
        method: "POST", // http method
        data: {sellingCards: sellingCards, sellingCrdsVal: sellingCrdsVal},
        success: function (json) {
            $('#post-sell').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            console.log(errmsg, err);
        }
    });
}


function sendAjax() {
    $.ajax({
        url: '/game/' + $game_id + '/update/', // the endpoint
        method: "POST", // http method
        data: {cards: cards, forest: forest, decay:decay},
        success: function (json) {
            $('#post-form').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            console.log(errmsg, err);
        }
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
    console.log('sup?');
    $('#placeholder').each(function () {

        $(this).find('li:gt(0)').each(function () {
            var idNumber = $(this).children('img').attr('id');
            var classNumber = $(this).children('img').attr('class');
            sellingCards.push(parseInt(idNumber));
            sellingCrdsVal.push(parseInt(classNumber));
            console.log(parseInt(classNumber));
            console.log(sellingCards)
        });
    });
}


function createPlay() {
    console.log("night vale")
}

function createDecay() {
    $('#decay').each(function () {

        $(this).find('li').each(function () {
            var classNumber = $(this).children('img').attr('id');
            decay.push(parseInt(classNumber));
        });
    });
}


$('#post-sell').on('submit', function (event) {
    event.preventDefault();
    console.log("Selling form submitted!");  // sanity check
    if (player == currentPlayer) {
        event.preventDefault();
        createSell();
        sendSellAjax();
        //location.reload().delay( 1100 );
    }
    else{
        console.log("Blaha");
        event.preventDefault();
    }
});


$('#post-play').on('submit', function (event) {
    event.preventDefault();
    console.log("Playing cards form submitted!");  // sanity check
    if (player == currentPlayer) {
        event.preventDefault();
        createPlay();
        //sendPlayAjax();
        //location.reload().delay( 1100 );
    }
    else{
        console.log("Blahb");
        event.preventDefault();
    }
});


$('#post-form').on('submit', function (event) {
    event.preventDefault();
    console.log("Takeing cards form submitted!");  // sanity check
    if (player == currentPlayer) {
        event.preventDefault();
        createDecay();
        createForest();
        sendAjax();
        //location.reload().delay( 1100 );
    }
    else{
        console.log("Bblah");
        event.preventDefault();
    }
});






//$(document).ready(function(){
//     $(".droppable").droppable({
//        drop: function(event, ui) {
//            var $list = $(this);
//            $helper = ui.helper;
//            $($helper).removeClass("selected");
//            var $selected = $(".selected");
//            if($selected.length > 1){
//                moveSelected($list,$selected);
//            }else{
//                moveItem(ui.draggable,$list);
//            }
//        }, tolerance: "touch"
//     });
//
//     $(".draggable").draggable({
//        revert: "invalid",
//        helper: "clone",
//        cursor: "move",
//        drag: function(event,ui){
//            var $helper = ui.helper;
//            $($helper).removeClass("selected");
//            var $selected = $(".selected");
//            if($selected.length > 1){
//                $($helper).html($selected.length + " items");
//            }
//        }
//     });
//
//    function moveSelected($list,$selected){
//        $($selected).each(function(){
//            $(this).fadeOut(function(){
//                $(this).appendTo($list).removeClass("selected").fadeIn();
//            });
//        });
//    }
//
//    function moveItem( $item,$list ) {
//        $item.fadeOut(function() {
//            $item.find(".item").remove();
//            $item.appendTo( $list ).fadeIn();
//        });
//    }
//
//    $(".item").click(function(){
//        $(this).toggleClass("selected");
//    });
//
//});






//$(".grouped").multiDraggable({ group: $(".grouped")});





//$(document).ready(function() {
//
//    var selectedClass = 'ui-state-highlight',
//        clickDelay = 600,
//        // click time (milliseconds)
//        lastClick, diffClick; // timestamps
//
//    $("#decay li")
//    // Script to deferentiate a click from a mousedown for drag event
//    .bind('mousedown mouseup', function(e) {
//            console.log("TO");
//            console.log($(e.target).parent().attr('class'));
//        if (e.type == "mousedown") {
//            lastClick = e.timeStamp; // get mousedown time
//        } else {
//            diffClick = e.timeStamp - lastClick;
//            if (diffClick < clickDelay) {
//                console.log("hoo");
//                // add selected class to group draggable objects
//                $(this).toggleClass(selectedClass);
//                console.log(this)
//            }
//        }
//    })
//    .draggable({
//        revertDuration: 10,
//        // grouped items animate separately, so leave this number low
//        containment: '.hand',
//        start: function(e, ui) {
//            ui.helper.addClass(selectedClass);
//        },
//        stop: function(e, ui) {
//            // reset group positions
//            $('.' + selectedClass).css({
//                top: 0,
//                left: 0
//            });
//        },
//        drag: function(e, ui) {
//            // set selected group position to main dragged object
//            // this works because the position is relative to the starting position
//            $('.' + selectedClass).css({
//                top: ui.position.top,
//                left: ui.position.left
//            });
//        }
//    });
//
//    $("#hand, #decay").sortable().droppable({
//        drop: function(e, ui) {
//            $('.' + selectedClass).appendTo($(this)).add(ui.draggable); // ui.draggable is appended by the script, so add it after
//            //.removeClass(selectedClass).css({
//            //    top: 0,
//            //    left: 0
//            //});
//        }
//    });
//
//
//});






//$("ul").on('click', 'li', function (e) {
//    if (e.ctrlKey || e.metaKey) {
//        $(this).toggleClass("selected");
//    } else {
//        $(this).addClass("selected").siblings().removeClass('selected');
//    }
//    }).sortable({
//    connectWith: "ul",
//    delay: 150, //Needed to prevent accidental drag when trying to select
//    revert: 0,
//    helper: function (e, item) {
//        var helper = $('<li/>');
//        if (!item.hasClass('selected')) {
//            item.addClass('selected').siblings().removeClass('selected');
//        }
//        var elements = item.parent().children('.selected').clone();
//        item.data('multidrag', elements).siblings('.selected').remove();
//        return helper.append(elements);
//    },
//    stop: function (e, info) {
//        info.item.after(info.item.data('multidrag')).remove();
//    }
//
//});
//
//
//angular.module('myApp', []).directive('sortable', function () {
//    return {
//        scope: {
//            collection: '=',
//            drop: '&',
//            bin: '=',
//            disableMultiple: '='
//        },
//        link: function (scope, element, attrs) {
//            var draggedEls = [];
//            var prevPosition = null;
//            var draggedElements;
//
//            DragCollection[attrs.id] = {
//                collection: scope.collection || [],
//                bin: scope.bin
//            };
//
//            var elementTagName = element.prop('tagName');
//            var helperTag = attrs.helperTag || '.card';
//
//            if (!scope.disableMultiple) {
//                element.on('click', attrs.childrenTag || '.card', function (e) {
//                    var $this = $(this);
//                    if ($(e.toElement).closest('.task-controls').length === 0) {
//                        if (e.ctrlKey || e.metaKey) {
//                            $this.toggleClass("selected");
//                        }
//                    }
//                });
//            }
//
//            element.sortable({
//                connectWith: "[sortable]",
//                delay: 150,
//                revert: 0,
//                tolerance: "pointer",
//                scrollSensitivity: 10,
//                start: function (e, ui) {
//
//                    prevPosition = ui.item.index();
//                    ui.placeholder.height(ui.item.height());
//
//                },
//                helper: function (e, item) {
//                    // Basically, if you grab an unhighlighted item to drag,
//                    // it will deselect (unhighlight) everything else
//                    if (!item.hasClass('selected')) {
//                        item.addClass('selected').siblings().removeClass('selected');
//                    }
//
//                    //////////////////////////////////////////////////////////////////////
//                    // HERE'S HOW TO PASS THE SELECTED ITEMS TO THE `stop()` FUNCTION:
//
//                    // Clone the selected items into an array
//                    var elements = item.parent().children('.selected').clone();
//
//                    // Add a property to `item` called 'multidrag` that contains the
//                    // selected items, then remove the selected items from the source list
//                    item.data('multidrag', elements);
//                    draggedElements = item.siblings('.selected').detach();
//
//                    // Now the selected items exist in memory, attached to the `item`,
//                    // so we can access them later when we get to the `stop()` callback
//
//                    //Create the helper
//                    var helper = $('<' + helperTag + '/>');
//                    return helper.append(elements);
//                },
//                stop: function (e, ui) {
//                    var elements = ui.item.data('multidrag'),
//                        destination = DragCollection[ui.item.closest(
//                        elementTagName + ':not(#' + ui.item.attr('id') + ')').attr('id')],
//                        destinationCollection = destination.collection,
//                        destinationBin = destination.bin,
//                        newPostion = ui.item.index(),
//                        i = 0;
//
//                   // For each moved element we need to update collections
//                    elements.each(function () {
//                        // find proper moved object
//                        var id = parseInt($(this).attr('id').split('_')[1]);
//
//                        var find = _.find(scope.collection, function (element) {
//                            return element.id == id;
//                        });
//
//                        draggedEls.push(find);
//                        i++;
//                    });
//
//
//                    ui.item.detach();
//
//                    //remove all dragged elements from source collection
//                    for (var j = 0; j < draggedEls.length; j++) {
//                        for (var k = 0; k < scope.collection.length; k++) {
//                            if (scope.collection[k].id == draggedEls[j].id) {
//                                scope.collection.splice(k, 1);
//                            }
//                        }
//                    }
//
//                    for (var r = 0; r < draggedEls.length; r++) {
//                        destinationCollection.splice(newPostion + r, 0, draggedEls[r]);
//                    }
//
//
//
//                    // call the passed drop function
//                    scope.$apply(function (scope) {
//                        var fn = scope.drop();
//                        if ('undefined' !== typeof fn) {
//                            fn(draggedEls,
//                            destinationBin,
//                            destinationCollection[newPostion - 1],
//                            destinationCollection[newPostion + i]);
//                        }
//                        draggedEls = [];
//                    });
//
//                    ui.item.closest(elementTagName).find('> .selected').removeClass('selected');
//
//                }
//            });
//
//         }
//    };
//});