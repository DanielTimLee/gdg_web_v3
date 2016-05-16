var clear = function () {
  $('.nag').nag('hide');
};

$('.dropdown').dropdown();
$('.nag').nag('show');
$('.close.icon').click(clear);
$(document).ready(function () {
  setTimeout(clear, 5000);
});
