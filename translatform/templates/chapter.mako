<%inherit file="layout.mako" />

<%block name="blk_title">
${content.title |n}
</%block>


<%block name="blk_css">
<link rel="stylesheet" href="/static/css/bootstrap.min.css" />
<link rel="stylesheet" href="/static/css/sphinx/pygments.css" />
<link rel="stylesheet" href="/static/css/sphinx/style.css" />
<link rel="stylesheet" href="/static/css/chapter.css" />
</%block>


<%block name="blk_js">
${parent.blk_js()}

<script>
  $LAB
  .script(["/static/js/encoder.js",
  "/static/js/jquery.min.js",
  "/static/js/md5-min.js"])
  .wait()
  .script(["/static/js/bootstrap.min.js",
  "/static/js/jquery.caret.js"])
  .wait()
  .script("/static/js/chapter.js");
</script>
</%block>


<%block name="blk_navbar">
${self.def_navbar(active='translate', toc=content.toc)}
</%block>


<%block name="blk_content">
${content.body |n}
</%block>


<div id="translateModal" class="modal hide">
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
        <div class="alert">
          <button class="close" data-dismiss="alert">×</button>
          <strong>Warning!</strong>这个段落目前为止还没有翻译！
        </div>
        <ol>
        </ol>
        <div class="modal-footer">
          <a href="#" class="btn" data-dismiss="modal">Close</a>
        </div>
      </div>
    </div>
  </div>
</div>


<div id="commentModal" class="modal hide">
  <div class="modal-header">
    <div class="close" data-dismiss="modal">x</div>
    <ul class="nav nav-tabs">
      <li class="active">
        <a href="#new-comment" data-toggle="tab">New Comment</a>
      </li>
      <li>
        <a href="#all-comment" data-toggle="tab">All Comment</a>
      </li>
    </ul>
  </div>
  <div class="modal-body">
    <div class="tab-content">
      <div class="tab-pane active" id="new-comment">
        <form class="span8">
          <label>Comment</label>
          <textarea class="span8" name="comment"></textarea>
          <label>Name</label>
          <input type="text" name="author" placeholder="Your name here" class="span4"/>
          <input type="hidden" name="chap_id" value="${content.id}" />
        </form>
        <div class="modal-footer">
          <a href="#" class="btn" data-dismiss="modal">Close</a>
          <a href="#" class="btn btn-primary">Save</a>
        </div>
      </div>
      <div class="tab-pane" id="all-comment">
        <div class="alert">
          <button class="close" data-dismiss="alert">×</button>
          这个段落目前为止还没有评论！
        </div>
        <ol>
        </ol>
        <div class="modal-footer">
          <a href="#" class="btn" data-dismiss="modal">Close</a>
        </div>
      </div>
    </div>
  </div>
</div>
