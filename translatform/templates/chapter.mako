<!doctype html>
<html>
<head>
  <link rel="stylesheet" href="/static/css/bootstrap.min.css" />
  <link rel="stylesheet" href="/static/css/chapter.css" />
  <link rel="stylesheet" href="/static/css/sphinx/pygments.css" />
  <link rel="stylesheet" href="/static/css/sphinx/style.css" />
  <script src="/static/js/LAB.min.js"></script>
  <script>
    $LAB
    .setGlobalDefaults({Debug:true})
    .script(["/static/js/encoder.js",
    "/static/js/jquery.min.js",
    "/static/js/md5-min.js"])
    .wait()
    .script(["/static/js/bootstrap.min.js",
    "/static/js/jquery.caret.js"])
    .wait()
    .script("/static/js/chapter.js");
  </script>
  <title>
    ${content.title |n}
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
          <ul class="nav pull-right">
            <li>
              <a href="${request.route_url('toc')}">Content</a>
            </li>
            <li>
              <a href="#">Index</a>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div class="content">
      ${content.body |n}
    </div>

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
              <input type="hidden" name="chap_id" value="${content.id}" />
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
