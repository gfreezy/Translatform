(function($modal) {
  var $btn = $("a[href='#modal']");
  var $loading = $("#loading");
  var $success = $("#success");
  var $failure = $("#failure");


  $modal.on("click", ".btn-danger", function() {
    $success.hide()
    $failure.hide();
    $modal.modal("hide");
    $btn.hide();
    $loading.show();
    var url = "/regenerate/";
    $.post(url, {action: 'regenerate'}, function(data) {
      if(data['status'] === 'ok') {
        $("#success").show();
      } else {
        $("#failure").show();
      }
      $btn.show();
      $loading.hide();
    });
    return false;
  });
})($("#modal"));


