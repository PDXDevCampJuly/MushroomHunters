/*
 * Created by Chelsea on 10/13/15.
 */


//$("#sortable1").fixedsortable({
//        fixed: "> .static", //you can use css selector
//        sort: function() {  //you can add events as well, without getting confused. for example:
//            $(".static").css("background",randomColor());  //change the fixed items background
//        },
//        change: function(event,ui) {
//            $(ui.item[0]).css("border","2px solid "+randomColor());  //change the captured border color
//        },
//        stop: function(event,ui) {
//            $(ui.item[0]).css("border","2px solid #777"); //change the back the css modifications
//            $("#forest > li.static").css("background","#aaa");
//        }
//    });



$(function  () {
  $("ul.example").sortable();
});



$("ul.simple_with_no_drop").sortable({
  //  isValidTarget: function  ($item, container) {
  //  if($item.is(".highlight"))
  //    return true;
  //  else
  //    return $item.parent("ul")[0] == container.el[0];
  //},
  group: 'no-drop',
  drop: false

});

$("ul.simple_with_drop").sortable({
    group: 'no-drop',
    handle: 'i.icon-move',
    onDragStart: function ($item, container, _super) {

    if(!container.options.drop)
        $item.clone().insertAfter($item);
    _super($item, container);
  }
});

$("ul.simple_with_no_drag").sortable({
  group: 'no-drop',
  drag: false
});