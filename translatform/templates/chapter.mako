<!doctype html>
<html>
<head>
  <link rel="stylesheet" href="/static/css/bootstrap.min.css" />
  <link rel="stylesheet" href="/static/css/document.css" />
  <script src="/static/js/LAB.min.js"></script>
  <script>
    $LAB
    .setGlobalDefaults({Debug:true})
    .script(["/static/js/encoder.js",
    "/static/js/jquery.min.js"]).wait()
    .script(["/static/js/bootstrap.min.js",
    "/static/js/jquery.caret.js"]).wait()
    .script("/static/js/chapter.js");
  </script>
  <title>
    Chapter${chap_id} - Translatform
  </title>
</head>
<body>
  <div class="container">
    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="brand" href="#">
            Translatform
          </a>
          <ul class="nav">
            <li class="active">
              <a href="#">Translate</a>
            </li>
            <li>
              <a href="#">Read</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="content">
    </div>

    <ul class="unstyled">
      %for paragraph in paragraphs:
      <li>
        <pre><a href="${request.route_url('translation', chap_id=chap_id, para_id=paragraph.para_number)}">${paragraph.latest_translation()}</a></pre>
      </li>
      %endfor
    </ul>
    <div id="myModal" class="modal hide">
      <div class="modal-header">
        <div class="close" data-dismiss="modal">x</div>
        <ul class="nav nav-tabs">
          <li class="active">
            <a href="#translate" data-toggle="tab">Translate</a>
          </li>
          <li>
            <a href="#history" data-toggle="tab">History</a>
          </li>
        </ul>
      </div>
      <div class="modal-body">
        <div class="tab-content">
          <div class="tab-pane active" id="translate">
            <form class="span8">
              <label>Original Text</label>
              <textarea class="span8 origin" disabled></textarea>
              <label>Translation</label>
              <textarea class="span8 translation"></textarea>
            </form>
            <div class="modal-footer">
              <a href="#" class="btn" data-dismiss="modal">Close</a>
              <a href="#" class="btn btn-primary">Save</a>
            </div>
          </div>
          <div class="tab-pane" id="history">
            <ol>
            </ol>
            <div class="modal-footer">
              <a href="#" class="btn" data-dismiss="modal">Close</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
