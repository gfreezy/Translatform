<%inherit file="base.mako" />

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
  footer
</div>
</%block>


<%def name="def_navbar(active='', toc=None)">
<div class="navbar navbar-fixed-top">
  <div class="navbar-inner">
    <div class="container">
      <a class="brand" href="/">
        Translatform
      </a>
      <ul class="nav">
        <li ${'class=active' if active=='translate' else ''}>
          <a href="#">Translate</a>
        </li>
        <li ${'class=active' if active=='english' else ''}>
          <a href="#">English</a>
        </li>
      </ul>
      <ul class="nav pull-right">
        <li>
          <a href="${request.route_url('toc')}">Content</a>
        </li>
        %if toc:
        <li class="dropdown">
          <a href="#"
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
      </ul>
    </div>
  </div>
</div>
</%def>
