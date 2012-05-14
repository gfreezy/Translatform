<%inherit file="layout.mako" />

<%block name="blk_title">
Regenerate Document
</%block>

<%block name="blk_js">
${parent.blk_js()}

<script>
  $LAB
  .script("/static/js/jquery.min.js")
  .wait()
  .script("/static/js/bootstrap.min.js")
  .wait()
  .script("/static/js/regenerate.js");
</script>
</%block>

<div id="loading" class="hide">
<h3>正在生成......</h3>
<img src="/static/img/loading.gif" />
</div>

<div id="success" class="alert alert-success hide">
  <h3>生成成功!</h3>
</div>

<div id="failure" class="alert alert-error hide">
  <h3>生成失败！</h3>
</div>

<a href="#modal" data-toggle="modal" class="btn btn-primary btn-large">
  重新生成文档
</a>


<div class="modal hide" id="modal">
  <div class="modal-header">
    <h3>Warning</h3>
  </div>
  <div class="modal-body">
    <p>你确定要重新生成文档吗?</p>
  </div>
  <div class="modal-footer">
    <a href="#" class="btn btn-primary" data-dismiss="modal">Close</a>
    <a href="#" class="btn btn-danger">Yes</a>
  </div>
</div>

