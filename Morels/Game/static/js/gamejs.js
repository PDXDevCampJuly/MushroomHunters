/**
 * Created by Chelsea on 10/13/15.
 */
//nd = $(" .nightdeck ");

console.log("Look I did a thing");

$(function  () {
  $("ol.example").sortable();
});
 //Editable list
//var editableList = Sortable.create(editable, {
//  filter: '.js-remove',
//  onFilter: function (evt) {
//    var el = editableList.closest(evt.item); // get dragged item
//    el && el.parentNode.removeChild(el);
//  }
//});

// Or
//var container = document.getElementById("multi");
//var sort = Sortable.create(container, {
//  animation: 150, // ms, animation speed moving items when sorting, `0` — without animation
//  handle: ".tile__title", // Restricts sort start click/touch to the specified element
//  draggable: ".tile", // Specifies which items inside the element should be sortable
//  onUpdate: function (evt/**Event*/){
//     var item = evt.item; // the current dragged HTMLElement
//  }
//});

// ..
//sort.destroy();