<%inherit file="layout.mako" />

<%block name="blk_css">
<link rel="stylesheet" href="/static/css/bootstrap.min.css" />
<link rel="stylesheet" href="/static/css/sphinx/pygments.css" />
<link rel="stylesheet" href="/static/css/sphinx/style.css" />
</%block>


<%block name="title">
${content.title |n}
</%block>

<%block name="blk_content">
${content.body |n}
</%block>
