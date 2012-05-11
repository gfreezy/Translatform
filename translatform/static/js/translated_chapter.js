function getChapterURL() {
  return window.location.pathname;
}

var chapterURL = getChapterURL();
$.getJSON(chapterURL+'translated/', function(data) {
  if(data['status'] === 'ok') {
    var paragraphs = data['paragraphs'];
    $("p, li, dt, h1, h2, h3").each(function() {
      var $this = $(this);
      var md5 = $this.attr("rel");
      var txt = paragraphs[md5];
      if(txt != undefined) {
        setTranslation($this, txt);
      }
    });
  }
});
