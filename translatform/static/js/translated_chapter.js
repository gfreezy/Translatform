function getChapterURL() {
  return window.location.pathname;
}

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
