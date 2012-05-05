Encoder.EncodeType = "numerical";
function convertToVisibleSpace(si) {
  s = Encoder.htmlDecode(si);
  so = s.replace(/ /g, "␣");
  return so;
}

function convertFromVisibleSpace(si) {
  s = Encoder.htmlDecode(si);
  so = s.replace(/␣/g, " ");
  return so;
}

var $modal = $("#myModal");
var $history = $("a[href='#history']");
var $translate = $("a[href='#translate']");

$modal.modal({show:false});

$("div.content~ul").on("click", "a", function() {
  var $prev = $modal.data("source");
  if($prev) {
    $prev.removeClass("highlight");
  }
  $(this).toggleClass("highlight");
  $modal.data("source", $(this));

  $trans = $modal.find("textarea.translation")
  var url = $(this).attr("href");
  $.getJSON(url, function(data) {
    $trans.val(Encoder.htmlDecode(data['translation']));
    $modal.find("textarea.origin").val(convertToVisibleSpace(data['english']));
  });

  $translate.tab("show");
  $modal.modal("show");

  // textarea must be visible when invoking caret
  $trans.caretToEnd();

  return false;
});

$modal.on("click", "a.btn-primary", function() {
  var $source = $modal.data("source");
  var text = $modal.find("textarea.translation").val();
  text = convertFromVisibleSpace(text);
  $source.html(text);
  var url = $source.attr("href");
  $.post(url, {"translation": text}, function() {
    $modal.modal("hide");
  });
  return false;
});

$history.on("show", function(e) {
  var url = $modal.data("source").attr("href");
  $ol = $("#history ol");
  $ol.empty();
  $.getJSON(url+"history/", function(data) {
    $.each(data["translations"], function(index, value) {
      $ol.append("<li><pre>" + Encoder.htmlEncode(value) + "</pre></li>");
    });
  });
});

function watchTextareaChange($ts, f) {
  $ts.each(function() {
    $t = $(this);
    $t.data("lastValue", $t.val());
    setInterval(function() {
      var currentValue = $t.val();
      var lastValue = $t.data("lastValue");
      if (currentValue != lastValue) {
        f($t);
        $t.data("lastValue", $t.val());
      }
    }, 200);
  });
}

watchTextareaChange($("textarea.translation"), function($t) {
  var pos = $t.caret();
  var before = $t.val();
  var after = convertToVisibleSpace(before);
  $t.val(after);
  $t.caret(pos);
});
