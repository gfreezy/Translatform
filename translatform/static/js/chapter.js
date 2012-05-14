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

function getCommentURL($target) {
  var md5 = $target.attr("rel");
  var chap_id = $("input[name='chap_id']").val();
  return "/"+chap_id+"/"+md5+"/comment/";
}

function setTranslation($target, txt) {
  if(txt) {
    $target.html(Encoder.htmlEncode(txt));
  }
  $target.prepend("<i class='icon-edit'></i>");
  $target.append("<i class='icon-comment'></i>");

}

function getChapterURL() {
  return window.location.pathname;
}

// 为每段文字加上md5的rel
$(".content, .nav .dropdown-menu").find("p, li, dt, h1, h2, h3").each(function() {
  var $this = $(this);
  var txt = tidy_text(htmlToText($this.html()));
  //  console.info(txt);
  var md5 = getMD5(txt);
  $this.attr("rel", md5);
});

// 加载并显示最新翻译
var chapterURL = getChapterURL();
$.getJSON(chapterURL+'translated/', function(data) {
  if(data['status'] === 'ok') {
    var paragraphs = data['paragraphs'];
    $(".content [rel]").each(function() {
      var $this = $(this);
      var md5 = $this.attr("rel");
      var txt = paragraphs[md5];
      if(txt != undefined) {
        setTranslation($this, txt);
      }
    });

    $(".nav .dropdown-menu [rel]").each(function() {
      var $this = $(this);
      var md5 = $this.attr("rel");
      var txt = paragraphs[md5];
      if(txt) {
        $this.find("a").html(Encoder.htmlEncode(txt));
      }
    });
  }
});


(function($modal) {
  var $history = $modal.find("a[href='#history']");
  var $translate = $modal.find("a[href='#translate']");

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
    var $ol = $modal.find("#history ol");
    $ol.empty();
    var $warn = $modal.find("#history .alert");
    $warn.hide();
    $.getJSON(url+"history/", function(data) {
      if(data["translations"].length) {
        $.each(data["translations"], function(index, value) {
          $ol.append("<li><pre>" + Encoder.htmlEncode(value) + "</pre></li>");
        });
      } else {
        $warn.show();
      }
    });
  });

  watchTextareaChange($modal.find("textarea.translation"), function($t) {
    var pos = $t.caret();
    var before = $t.val();
    var after = convertToVisibleSpace(before);
    $t.val(after);
    $t.caret(pos);
  });

})($("#translateModal"));


(function($modal) {
  var $allCommentLink = $modal.find("a[href='#all-comment']");
  var $newCommentLink = $modal.find("a[href='#new-comment']");

  $(".content").on("click", ".icon-comment", function() {
    var $source = $(this).parent();
    $modal.data("source", $source);
    $newCommentLink.tab("show");
    $modal.modal("show");
  });


  $modal.on("click", "a.btn-primary", function() {
    var $source = $modal.data("source");
    var url = getCommentURL($source);
    var $comment = $modal.find("textarea[name='comment']");
    var comment = $comment.val();
    $comment.val("");
    var $author = $modal.find("input[name='author']");
    var author = $author.val();
    $author.val("");
    $.post(url, {"comment": comment, "author": author}, function() {
      $modal.modal("hide");
    });
    return false;
  });


  $allCommentLink.on("show", function(e) {
    var $source = $modal.data("source");
    var url = getCommentURL($source);
    var $ol = $modal.find("#all-comment ol");
    $ol.empty();
    var $warn = $modal.find("#all-comment .alert");
    $warn.hide();
    $.getJSON(url+"all/", function(data) {
      if(data["comments"] && data["comments"].length) {
        $.each(data["comments"], function(index, value) {
          $ol.append("<li><p>" + value[1] + "</p></li>");
        });
      } else {
        $warn.show();
      }
    });
  });

})($("#commentModal"));
