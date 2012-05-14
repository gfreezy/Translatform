<%inherit file="layout.mako" />

<%block name="blk_title">
Translatform
</%block>

<%block name="blk_js">
${parent.blk_js()}

<script>
  $LAB
  .script("/static/js/jquery.min.js")
  .wait()
  .script("/static/js/bootstrap.min.js");
</script>
</%block>


<h2>Getting Started</h2>
<ul>
  <li>
    <a href="installation">installation</a>
  </li>
  <li>
    <a href="transition">transition</a>
  </li>
  <li>
    <a href="tutorial">tutorial</a>
  </li>
  <li>
    <a href="levels">levels</a>
  </li>
  <li>
    <a href="quickstart">quickstart</a>
  </li>
</ul>

<h2>Serving and Testing</h2>
<ul>
  <li>
    <a href="serving">serving</a>
  </li>
  <li>
    <a href="test">test</a>
  </li>
  <li>
    <a href="debug">debug</a>
  </li>
</ul>

<h2>Reference</h2>
<ul>
  <li>
    <a href="wrappers">wrappers</a>
  </li>
  <li>
    <a href="routing">routing</a>
  </li>
  <li>
    <a href="wsgi">wsgi</a>
  </li>
  <li>
    <a href="http">http</a>
  </li>
  <li>
    <a href="datastructures">datastructures</a>
  </li>
  <li>
    <a href="utils">utils</a>
  </li>
  <li>
    <a href="local">local</a>
  </li>
  <li>
    <a href="middlewares">middlewares</a>
  </li>
  <li>
    <a href="exceptions">exceptions</a>
  </li>
</ul>

<h2>Deprecated Modules</h2>
<ul>
  <li>
    <a href="script">script</a>
  </li>
  <li>
    <a href="templates">templates</a>
  </li>
</ul>

<h2>Additional Information</h2>
<ul>
  <li>
    <a href="terms">terms</a>
  </li>
  <li>
    <a href="unicode">unicode</a>
  </li>
  <li>
    <a href="request_request_data">data</a>
  </li>
  <li>
    <a href="changes">changes</a>
  </li>
</ul>
