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
