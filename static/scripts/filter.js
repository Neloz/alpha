$(window).on("load", function(){
  $("#pendientes").on("click", function(){
    $("#todos").removeClass("active");
    $("#autoriz").removeClass("active");
    $("#pendientes").addClass("active");
  });
  $("#todos").on("click", function(){
    $("#pendientes").removeClass("active");
    $("#todos").addClass("active");
    $("#autoriz").removeClass("active");
  });
  $("#autoriz").on("click", function(){
    $("#pendientes").removeClass("active");
    $("#todos").removeClass("active");
    $("#autoriz").addClass("active");
  });
});

$(document).ready(function () {
   $('#pendientes').click(function () {
      var rex = new RegExp($(this).val(), 'i');
        $('.contenidobusqueda tr').hide();
        $('.contenidobusqueda tr').filter(function () {
            return rex.test($(this).text());
        }).show();

        })
   $('#autoriz').click(function () {
      var rex = new RegExp($(this).val(), 'i');
        $('.contenidobusqueda tr').hide();
        $('.contenidobusqueda tr').filter(function () {
           return rex.test($(this).text());
        }).show();

        })
   $('#todos').click(function () {
      var rex = new RegExp($(this).val(), 'i');
        $('.contenidobusqueda tr').show();

        })

});
