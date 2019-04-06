$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.materialboxed').materialbox();
    $('.parallax').parallax();
    $('.tabs').tabs();
    $('.tooltipped').tooltip();
    $('.scrollspy').scrollSpy();
    $('select').formSelect();
    $('#search-button').on("click", getInfoFromDB);
    
    

    $('#postcodebutton').click(function(){
        $('.modal').modal();
    });
    $('#clickTakeAway').click(function(){
        $('#postcodes').hide();
        $('#chooseDistance').hide();
        $('#displayCriterias').show();
        
    });
    $('#clickDineOut').click(function(){
        $('#postcodes').hide();
        $('#chooseDeliveryCost').hide();
        $('#displayCriterias').show();
    });
  });

  function getInfoFromDB(){
    $.ajax({
      type: "GET",
      url: '/textFromServer.txt',
      success: postToPage
    });
  }

  function postToPage(data, status){
    $('#displayRestaurant').text(data);
  }

  $(document).ready(function () {
    $('.sidenav').sidenav();
    $('.materialboxed').materialbox();
    $('.parallax').parallax();
    $('.tabs').tabs();
    $('.datepicker').datepicker({
      disableWeekends: true
    });
    $('.tooltipped').tooltip();
    $('.scrollspy').scrollSpy();
  });
  $( "#search-button, postcode" ).click(function() {
    var cuisine = $("#cuisines :selected").val();
    var budget_range = $("#budget_range :selected").val();
    var postcode = $("#postcode").val();
    window.location.href = '/just_choose/takeaway/' + postcode + '/' + cuisine + '/' + budget_range;
  });