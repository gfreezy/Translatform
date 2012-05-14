<%inherit file="base.mako" />

<%block name="blk_css">
<link rel="stylesheet" href="/static/css/bootstrap.min.css" />
<link rel="stylesheet" href="/static/css/site.css" />
</%block>

<%block name="blk_js">
<script src="/static/js/LAB.min.js"></script>
</%block>


<div class="container">

  <%block name="blk_navbar">
  ${self.def_navbar()}
  </%block>

<div class="content">
  <%block name="blk_content" />
</div>

${next.body()}

</div>

<%block name="footer">
<div class="footer">
  <div class="container">
  By gfreezy <a href="mailto:gfreezy+translatform@gmail.com">gfreezy+translatform@gmail.com</a>
  </div>
</div>
</%block>


<%def name="def_navbar(active='', toc=None)">
<div class="navbar navbar-fixed-top">
  <div class="navbar-inner">
    <div class="container">
      <a class="brand" href="/">
        Translatform
      </a>

      <ul class="nav pull-right">
        %if toc:
        <li class="dropdown" id="dropdown-toc">
          <a href="#dropdown-toc"
             class="dropdown-toggle"
             data-toggle="dropdown">
            目录
            <b class="caret"></b>
          </a>
          <ul class="dropdown-menu">
            ${toc.replace('<ul>', '').replace('</ul>', '')|n}
          </ul>
        </li>
        %endif
        <li class="dropdown" id="dropdown-read">
          <a href="#dropdown-read"
             class="dropdown-toggle"
             data-toggle="dropdown">
            阅读
            <b class="caret"></b>
          </a>
          <ul class="dropdown-menu">
            <li>
              <a href="/docs/html_en/index.html" target="_blank">原文</a>
            </li>
            <li>
              <a href="/docs/html_cn/index.html" target="_blank">翻译</a>
            </li>
            <li>
              <a href="/regenerate/" target="_blank">重新生成文档</a>
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</div>
</%def>
