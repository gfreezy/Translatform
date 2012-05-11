Encoder.EncodeType = "numerical";
function convertToVisibleSpace(si) {
  var s = Encoder.htmlDecode(si);
  var so = s.replace(/ /g, "␣");
  return so;
}

function convertFromVisibleSpace(si) {
  var s = Encoder.htmlDecode(si);
  var so = s.replace(/␣/g, " ");
  return so;
}

function clean_space(txt) {
  txt = txt.replace(/\s/g,'');
  return txt;
}

function tidy_text(txt) {
  txt = txt.replace(/’/g, "'");
  txt = txt.replace(/‘/g, "'");
  txt = txt.replace(/”/g, "\"");
  txt = txt.replace(/“/g, "\"");
  txt = txt.replace(/，/g, ",");
  txt = txt.replace(/。/g, ".");
  txt = txt.replace(/¶/g, "");
  txt = txt.replace(/\(\)/g, "");
  txt = clean_space(txt);
  return txt;
}

function htmlToText(html) {
   var tmp = document.createElement("DIV");
   tmp.innerHTML = html;
   return tmp.textContent||tmp.innerText;
}

function getMD5(txt) {
  var md5 = hex_md5(txt);
  return md5;
}

function getTranslationURL($target) {
  var md5 = $target.attr("rel");
  var chap_id = $("input[name='chap_id']").val();
  return "/"+chap_id+"/"+md5+"/translation/";
}

function setTranslation($target, txt) {
  if(txt) {
    $target.html(Encoder.htmlEncode(txt));
  }
  $target.prepend("<i class='icon-edit'></i>");
}

// 为每段文字加上md5的rel
$(".content, .nav .dropdown-menu").find("p, li, dt, h1, h2, h3").each(function() {
  var $this = $(this);
  var txt = tidy_text(htmlToText($this.html()));
//  console.info(txt);
  var md5 = getMD5(txt);
  $this.attr("rel", md5);
});


var $modal = $("#myModal");
var $history = $("a[href='#history']");
var $translate = $("a[href='#translate']");

$modal.modal({show:false});

$(".content").on("click", ".icon-edit", function() {
  var $source = $modal.data("source");
  if($source) {
    $source.removeClass("highlight");
  }
  $source = $(this).parent();
  $source.addClass("highlight");
  $modal.data("source", $source);

  var url = getTranslationURL($source);
  $trans = $modal.find("textarea.translation")
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
  var url = getTranslationURL($source);
  var text = $modal.find("textarea.translation").val();
  text = convertFromVisibleSpace(text);
  setTranslation($source, text);
  $.post(url, {"translation": text}, function() {
    $modal.modal("hide");
  });
  return false;
});

$history.on("show", function(e) {
  var $source = $modal.data("source");
  var url = getTranslationURL($source);
  $.getJSON(url+"history/", function(data) {
    if(data["translations"].length) {
      var $history = $("#history");
      $history.empty();
      var $ol = $history.add("ol");
      $.each(data["translations"], function(index, value) {
        $ol.append("<li><pre>" + Encoder.htmlEncode(value) + "</pre></li>");
      });
    }
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
