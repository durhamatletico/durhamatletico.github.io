---
library: jquery-2.1.3.min.js
---

{% include_relative _lib/{{page.library}} %}

$(document).ready(function() {
  var menuToggle = $('#js-centered-navigation-mobile-menu').unbind();
  $('#js-centered-navigation-menu').removeClass("show");

  menuToggle.on('click', function(e) {
    e.preventDefault();
    $('#js-centered-navigation-menu').slideToggle(function(){
      if($('#js-centered-navigation-menu').is(':hidden')) {
        $('#js-centered-navigation-menu').removeAttr('style');
      }
    });
  });
});
