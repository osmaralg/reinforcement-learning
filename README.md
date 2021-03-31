# reinforcement-learning

<a href="dds-pandemic-control.com">
<img  src="/static/assets/img/capture.JPG" alt="My cool logo"/>
</a>

Install
========

Install the virtualenv package

`pip install virtualenv`

Create virtual environment called env, myenv, etc. 

`virtualenv env`

Activate the virtualenvironmnent (LInux)

`source env/bin/activate`

Go the path of the project and install the required libraries 

`pip install -r requirements.txt`

Testing
-----------------
To run the server in the localhost run 

`python manage.py runserver`

Open your browser in the address localhost:8000 


File Description
-----------------
`project_emec2.py`: Takes input from the reinforcement learning model and creates the necessary JSON files for further visualization.

`manage.py`: Contains all the commands required to run the server

`requirements.txt`: Contains all library requirements to run the server

`articles\functions.py`: Contains general functions used by other scripts in the repository.

`articles\templates\welcome.html`: Contains Javascript and HTML scripts required for creating the dashboard

`static\data\RL Model`: Contains scripts for the reinfocement learning model



<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>RL_Corona_30032021</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[75]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># !pip install tensorflow==2.3.0</span>
<span class="c1"># !pip install keras</span>
<span class="c1"># !pip install keras-rl2</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[98]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Inputs</span>
<span class="n">s</span> <span class="o">=</span> <span class="mi">200</span> <span class="c1">#size of the grid</span>
<span class="n">N</span> <span class="o">=</span> <span class="mi">1000</span> <span class="c1">#size of population</span>
<span class="n">M</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(</span><span class="n">N</span> <span class="o">*</span> <span class="mf">0.007</span><span class="p">)</span> <span class="c1">#Number of infectious population</span>
<span class="n">Et</span> <span class="o">=</span> <span class="mi">2</span> <span class="c1">#Number of days staying exposed</span>
<span class="n">It</span> <span class="o">=</span> <span class="mi">21</span> <span class="c1">#Number of days staying infectious</span>
<span class="n">Mt</span> <span class="o">=</span> <span class="mi">8</span> <span class="c1">#Number of daily movements</span>
<span class="n">D</span> <span class="o">=</span> <span class="mi">100</span> <span class="c1">#Number of days</span>
<span class="n">death_rate</span> <span class="o">=</span> <span class="mi">100</span>
<span class="n">expose_rate</span> <span class="o">=</span> <span class="mi">10</span>

<span class="c1">#Initialization</span>
<span class="n">S</span> <span class="o">=</span> <span class="n">N</span> <span class="o">-</span> <span class="n">M</span> <span class="c1">#Susceptible population</span>
<span class="n">E</span> <span class="o">=</span> <span class="mi">0</span> <span class="c1">#Exposed population</span>
<span class="n">I</span> <span class="o">=</span> <span class="n">M</span> <span class="c1">#Number of infectious population </span>
<span class="n">R</span> <span class="o">=</span> <span class="mi">0</span> <span class="c1">#Recovered population</span>
<span class="n">P</span> <span class="o">=</span> <span class="n">S</span> <span class="o">+</span> <span class="n">E</span> <span class="o">+</span> <span class="n">I</span> <span class="o">+</span> <span class="n">R</span> <span class="c1">#Total population</span>
<span class="n">economy</span> <span class="o">=</span> <span class="mi">0</span> <span class="c1">#Daily economic transaction</span>

<span class="n">policy_match</span> <span class="o">=</span> <span class="p">{</span><span class="mi">0</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">:</span><span class="mf">0.75</span><span class="p">,</span> <span class="mi">2</span><span class="p">:</span><span class="mf">0.25</span><span class="p">}</span> <span class="c1"># assign action to policy</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[99]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">gym</span> <span class="k">import</span> <span class="n">Env</span>
<span class="kn">from</span> <span class="nn">gym.spaces</span> <span class="k">import</span> <span class="n">Discrete</span><span class="p">,</span> <span class="n">Box</span><span class="p">,</span> <span class="n">Dict</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">random</span> 
<span class="kn">import</span> <span class="nn">time</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[108]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Create a virtual environment actions</span>
<span class="k">def</span> <span class="nf">reset</span><span class="p">():</span>
    <span class="k">global</span> <span class="n">P</span><span class="p">,</span> <span class="n">M</span><span class="p">,</span> <span class="n">It</span><span class="p">,</span> <span class="n">s</span>
    <span class="n">dummy_array</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="n">shape</span><span class="o">=</span><span class="p">(</span><span class="n">P</span><span class="p">,</span><span class="mi">8</span><span class="p">))</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">dummy_array</span><span class="p">,</span><span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">,</span><span class="s1">&#39;y&#39;</span><span class="p">,</span><span class="s1">&#39;Day&#39;</span><span class="p">,</span><span class="s1">&#39;Susceptible&#39;</span><span class="p">,</span><span class="s1">&#39;Exposed&#39;</span><span class="p">,</span><span class="s1">&#39;Infectious&#39;</span><span class="p">,</span><span class="s1">&#39;Recovered&#39;</span><span class="p">,</span><span class="s1">&#39;GG&#39;</span><span class="p">])</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">astype</span><span class="p">({</span><span class="s1">&#39;x&#39;</span><span class="p">:</span><span class="nb">int</span><span class="p">,</span><span class="s1">&#39;y&#39;</span><span class="p">:</span><span class="nb">int</span><span class="p">,</span><span class="s1">&#39;Day&#39;</span><span class="p">:</span><span class="nb">int</span><span class="p">,</span><span class="s1">&#39;Susceptible&#39;</span><span class="p">:</span><span class="nb">bool</span><span class="p">,</span><span class="s1">&#39;Exposed&#39;</span><span class="p">:</span><span class="nb">int</span><span class="p">,</span><span class="s1">&#39;Infectious&#39;</span><span class="p">:</span><span class="nb">int</span><span class="p">,</span><span class="s1">&#39;Recovered&#39;</span><span class="p">:</span><span class="nb">bool</span><span class="p">,</span><span class="s1">&#39;GG&#39;</span><span class="p">:</span><span class="nb">bool</span><span class="p">})</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">&#39;Susceptible&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="c1">#Appending infectious population in </span>
    <span class="n">dfupdate</span><span class="o">=</span><span class="n">df</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="n">M</span><span class="p">)</span>
    <span class="n">dfupdate</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="n">It</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">dfupdate</span><span class="p">))</span>
    <span class="n">dfupdate</span><span class="p">[</span><span class="s1">&#39;Susceptible&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="n">df</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">dfupdate</span><span class="p">)</span>
    <span class="n">update_list</span> <span class="o">=</span> <span class="n">dfupdate</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span> 
    <span class="c1">#Dispersing people randomly among grid</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">s</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">))</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">&#39;y&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">s</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">))</span>

    <span class="k">return</span> <span class="n">df</span>

<span class="k">def</span> <span class="nf">update_pos</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="n">df</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">S</span>
    <span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">p</span><span class="p">,</span><span class="s1">&#39;x&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">p</span><span class="p">,</span><span class="s1">&#39;x&#39;</span><span class="p">]</span><span class="o">+</span><span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">)),</span><span class="n">s</span><span class="p">),</span><span class="mi">0</span><span class="p">)</span> <span class="c1">#make valid movements in the grid</span>
    <span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">p</span><span class="p">,</span><span class="s1">&#39;y&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">p</span><span class="p">,</span><span class="s1">&#39;y&#39;</span><span class="p">]</span><span class="o">+</span><span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">)),</span><span class="n">s</span><span class="p">),</span><span class="mi">0</span><span class="p">)</span> 
    
<span class="k">def</span> <span class="nf">coor_around</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="n">df</span><span class="p">):</span>
    <span class="k">return</span> <span class="p">[(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">p</span><span class="p">,</span> <span class="s1">&#39;x&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="n">a</span><span class="p">,</span> <span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">p</span><span class="p">,</span> <span class="s1">&#39;y&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="n">b</span><span class="p">)</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">)</span> <span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">)]</span>

<span class="k">def</span> <span class="nf">one_day</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
    <span class="c1"># start_time = time.time()</span>
    <span class="k">global</span> <span class="n">P</span><span class="p">,</span> <span class="n">M</span><span class="p">,</span> <span class="n">It</span><span class="p">,</span> <span class="n">S</span><span class="p">,</span> <span class="n">death_rate</span><span class="p">,</span> <span class="n">expose_rate</span>
    <span class="n">policy_match</span> <span class="o">=</span> <span class="p">{</span><span class="mi">0</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">:</span> <span class="mf">0.75</span><span class="p">,</span> <span class="mi">2</span><span class="p">:</span> <span class="mf">0.25</span><span class="p">}</span>  <span class="c1"># assign action to policy</span>
    <span class="n">moves_under_policy</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">Mt</span> <span class="o">*</span> <span class="n">policy_match</span><span class="p">[</span><span class="n">action</span><span class="p">],</span> <span class="mi">0</span><span class="p">))</span>

    <span class="n">df_infectious</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[(</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)]</span>
    <span class="n">df_infectious</span> <span class="o">=</span> <span class="n">df_infectious</span><span class="p">[[</span><span class="s1">&#39;x&#39;</span><span class="p">,</span> <span class="s1">&#39;y&#39;</span><span class="p">]]</span>

    <span class="k">for</span> <span class="n">mt</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">moves_under_policy</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">person</span> <span class="ow">in</span> <span class="n">df</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>

            <span class="k">if</span> <span class="ow">not</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;GG&#39;</span><span class="p">]:</span>  <span class="c1"># If the person is not dead</span>

                <span class="n">new_move_x</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>
                <span class="n">new_move_y</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>

                <span class="n">person</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="n">new_move_x</span><span class="p">,</span> <span class="n">s</span><span class="p">),</span> <span class="mi">0</span><span class="p">)</span>
                <span class="n">person</span><span class="p">[</span><span class="s1">&#39;y&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;y&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="n">new_move_y</span><span class="p">,</span> <span class="n">s</span><span class="p">),</span> <span class="mi">0</span><span class="p">)</span>

                <span class="n">df</span><span class="o">.</span><span class="n">iat</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">])</span>
                <span class="n">df</span><span class="o">.</span><span class="n">iat</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;y&#39;</span><span class="p">])</span>

                <span class="k">if</span> <span class="n">index</span> <span class="ow">in</span> <span class="n">df_infectious</span><span class="o">.</span><span class="n">index</span><span class="p">:</span>  <span class="c1"># assigning whats in person (row) to df_infectious at the correct index</span>
                    <span class="n">df_infectious</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;x&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">]</span>
                    <span class="n">df_infectious</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;y&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;y&#39;</span><span class="p">]</span>

                <span class="k">if</span> <span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;Recovered&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="kc">False</span><span class="p">):</span>  <span class="c1"># If a person is in infectious state</span>
                    <span class="k">if</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">-</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">7</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">It</span><span class="p">:</span>  <span class="c1"># If the infectious days are completed</span>
                        <span class="k">if</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">death_rate</span><span class="p">))</span> <span class="o">&gt;</span> <span class="p">(</span>
                                <span class="n">death_rate</span> <span class="o">-</span> <span class="mi">2</span><span class="p">):</span>  <span class="c1"># If the person dies(with probability distribution 1:4)</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
                            <span class="k">if</span> <span class="n">index</span> <span class="ow">in</span> <span class="n">df_infectious</span><span class="o">.</span><span class="n">index</span><span class="p">:</span>
                                <span class="n">df_infectious</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="n">index</span><span class="p">])</span>

                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;GG&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>  <span class="c1"># Kill the person</span>
                        <span class="k">else</span><span class="p">:</span>  <span class="c1"># If the person survives</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
                            <span class="k">if</span> <span class="n">index</span> <span class="ow">in</span> <span class="n">df_infectious</span><span class="o">.</span><span class="n">index</span><span class="p">:</span>
                                <span class="n">df_infectious</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="n">index</span><span class="p">])</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Recovered&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>  <span class="c1"># Recover the person</span>
                    <span class="k">elif</span> <span class="n">mt</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">moves_under_policy</span><span class="p">:</span>
                        <span class="k">if</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="mf">0.5</span><span class="p">:</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
                        <span class="k">else</span><span class="p">:</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span>  <span class="c1"># Increase the infectious day counter   </span>
        
                
                <span class="k">elif</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>  <span class="c1"># If a person is in exposed state</span>
                    
                    <span class="k">if</span> <span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">-</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">)))</span> <span class="o">&gt;=</span> <span class="n">Et</span><span class="p">:</span>  <span class="c1"># If the person has reached the exposed day limit?  7</span>
                        
                        <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
                        <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mf">0.5</span> <span class="k">if</span> <span class="n">mt</span><span class="o">+</span><span class="mi">1</span> <span class="o">!=</span> <span class="n">moves_under_policy</span> <span class="k">else</span> <span class="mi">1</span>  <span class="c1"># Increase the infectious day counter, now the person is infectious</span>
                        <span class="n">df_infectious</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">person</span><span class="p">)</span>
                    <span class="k">elif</span> <span class="n">mt</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">moves_under_policy</span><span class="p">:</span> <span class="c1"># At the end of the day</span>
                        <span class="k">if</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="mf">0.5</span><span class="p">:</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
                        <span class="k">else</span><span class="p">:</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span>  <span class="c1"># Increase the exposed day counter</span>
                        
                <span class="k">elif</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Susceptible&#39;</span><span class="p">]:</span>  <span class="c1"># If the person is in susceptible state</span>

                    <span class="n">x_temp</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">])</span>
                    <span class="n">df_xtemp</span> <span class="o">=</span> <span class="n">df_infectious</span><span class="p">[[</span><span class="s1">&#39;x&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">to_numpy</span><span class="p">()</span>

                    <span class="k">if</span> <span class="p">(</span><span class="n">x_temp</span> <span class="ow">in</span> <span class="n">df_xtemp</span><span class="p">)</span> <span class="ow">or</span> <span class="p">((</span><span class="n">x_temp</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span> <span class="ow">in</span> <span class="n">df_xtemp</span><span class="p">)</span> <span class="ow">or</span> <span class="p">((</span><span class="n">x_temp</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="ow">in</span> <span class="n">df_xtemp</span><span class="p">):</span>

                        <span class="n">y_temp</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;y&#39;</span><span class="p">])</span>
                        <span class="n">df_ytemp</span> <span class="o">=</span> <span class="n">df_infectious</span><span class="p">[[</span><span class="s1">&#39;y&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">to_numpy</span><span class="p">()</span>
                        <span class="k">if</span> <span class="p">(</span><span class="n">y_temp</span> <span class="ow">in</span> <span class="n">df_ytemp</span><span class="p">)</span> <span class="ow">or</span> <span class="p">((</span><span class="n">y_temp</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span> <span class="ow">in</span> <span class="n">df_ytemp</span><span class="p">)</span> <span class="ow">or</span> <span class="p">((</span><span class="n">y_temp</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="ow">in</span> <span class="n">df_ytemp</span><span class="p">):</span>
                            <span class="k">if</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">expose_rate</span><span class="p">))</span> <span class="o">&gt;</span> <span class="p">(</span><span class="n">expose_rate</span> <span class="o">-</span> <span class="mi">2</span><span class="p">):</span>
                                <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mf">0.5</span> <span class="k">if</span> <span class="n">mt</span><span class="o">+</span><span class="mi">1</span> <span class="o">!=</span> <span class="n">moves_under_policy</span> <span class="k">else</span> <span class="mi">1</span>
                                <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Susceptible&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>
                                
                    
    <span class="c1"># print(&quot;--- %s seconds ---&quot; % (time.time() - start_time))</span>

    <span class="k">return</span> <span class="n">df</span>  <span class="c1"># time.time() - start_time #</span>

<span class="k">def</span> <span class="nf">economy_gain</span><span class="p">(</span><span class="n">df</span><span class="p">):</span>
    <span class="n">economy_gain</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">[(</span><span class="n">df</span><span class="o">.</span><span class="n">GG</span> <span class="o">==</span> <span class="kc">False</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">Infectious</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)])</span> <span class="o">*</span> <span class="nb">round</span><span class="p">(</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">0.8</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span> <span class="mi">2</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">economy_gain</span>

<span class="k">def</span> <span class="nf">current_state</span><span class="p">(</span><span class="n">df</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">economy</span>
    <span class="n">active_cases</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">])</span>
    <span class="n">new_inf</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span><span class="p">])</span>
    <span class="n">recovered</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Recovered&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="kc">True</span><span class="p">])</span>
    <span class="n">gg</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;GG&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="kc">True</span><span class="p">])</span>
    <span class="n">reproduction_rate</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span><span class="p">])</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">])</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">])</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="k">else</span> <span class="mi">0</span>
    <span class="n">economy</span> <span class="o">=</span> <span class="n">economy</span> <span class="o">+</span> <span class="n">economy_gain</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
        
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">active_cases</span><span class="p">,</span> <span class="n">new_inf</span><span class="p">,</span> <span class="n">recovered</span><span class="p">,</span> <span class="n">gg</span><span class="p">,</span> <span class="n">reproduction_rate</span><span class="p">,</span> <span class="n">economy</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[109]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">simulation</span><span class="p">():</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">reset</span><span class="p">()</span>
    <span class="n">states</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">df_collect</span> <span class="o">=</span> <span class="n">df</span>
    <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">one_day</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
        <span class="n">df</span><span class="o">.</span><span class="n">Day</span> <span class="o">=</span> <span class="n">d</span><span class="o">+</span><span class="mi">1</span>
        <span class="n">df_collect</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">df_collect</span><span class="p">,</span> <span class="n">df</span><span class="p">])</span>
        <span class="n">states</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_state</span><span class="p">(</span><span class="n">df</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">df_collect</span><span class="p">,</span> <span class="n">states</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[110]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">def_observation_space</span> <span class="o">=</span> <span class="n">Box</span><span class="p">(</span><span class="n">low</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">]),</span> <span class="n">high</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">P</span><span class="p">,</span><span class="n">P</span><span class="p">,</span><span class="n">P</span><span class="p">,</span><span class="n">P</span><span class="p">,</span><span class="mi">10</span><span class="p">,</span><span class="n">P</span><span class="o">*</span><span class="n">D</span><span class="o">*</span><span class="n">Mt</span><span class="p">],</span> <span class="n">dtype</span> <span class="o">=</span> <span class="nb">int</span><span class="p">))</span>
<span class="c1">##[active_cases, new_inf, recovered, gg, reproduction_rate, economy]</span>

<span class="c1"># Create the virtual environment for RL</span>
<span class="k">class</span> <span class="nc">CoronaPolicy</span><span class="p">(</span><span class="n">Env</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">action_space</span> <span class="o">=</span> <span class="n">Discrete</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">observation_space</span> <span class="o">=</span> <span class="n">def_observation_space</span> <span class="c1"># Box(low = 0, high = P, shape = (5,1), dtype = int )</span>
        <span class="c1"># Dict(recovered=Discrete(P+1), sus=Discrete(P+1), exposed=Discrete(P+1),inf=Discrete(P+1),gg=Discrete(P+1))</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">df</span> <span class="o">=</span> <span class="n">reset</span><span class="p">()</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">current_state</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">df</span><span class="p">))</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">day</span> <span class="o">=</span> <span class="mi">0</span>
        
        
        
    <span class="k">def</span> <span class="nf">step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">df</span> <span class="o">=</span> <span class="n">one_day</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">df</span><span class="p">,</span> <span class="n">action</span><span class="p">)</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">current_state</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">df</span><span class="p">)</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">day</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">day</span> <span class="o">+</span> <span class="mi">1</span>
        
        <span class="n">reward</span> <span class="o">=</span> <span class="n">economy_gain</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">df</span><span class="p">)</span>
        
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">day</span> <span class="o">&lt;=</span> <span class="n">D</span><span class="p">:</span>
            <span class="n">done</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">done</span> <span class="o">=</span> <span class="kc">True</span>
            
        <span class="n">info</span> <span class="o">=</span> <span class="p">{}</span>
        
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="p">,</span> <span class="n">reward</span><span class="p">,</span> <span class="n">done</span><span class="p">,</span> <span class="n">info</span>
    
    <span class="k">def</span> <span class="nf">render</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>
    
    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">observation_space</span> <span class="o">=</span> <span class="n">def_observation_space</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">df</span> <span class="o">=</span> <span class="n">reset</span><span class="p">()</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">current_state</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">df</span><span class="p">)</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">day</span> <span class="o">=</span> <span class="mi">0</span>
        
        
        
        
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span>
        
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>/Users/yi/opt/anaconda3/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: <span class="ansi-yellow-fg">WARN: Box bound precision lowered by casting to float32</span>
  warnings.warn(colorize(&#39;%s: %s&#39;%(&#39;WARN&#39;, msg % args), &#39;yellow&#39;))
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[111]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">env</span> <span class="o">=</span> <span class="n">CoronaPolicy</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[112]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># episodes = 10</span>
<span class="c1"># for episode in range(1, episodes+1):</span>
<span class="c1">#     state = env.reset()</span>
<span class="c1">#     done = False</span>
<span class="c1">#     economy = 0</span>
    
<span class="c1">#     while not done:</span>
<span class="c1">#         action = env.action_space.sample()</span>
<span class="c1">#         n_state, reward, done, info = env.step(action)</span>
<span class="c1">#         economy += reward</span>
        
<span class="c1">#     print(f&#39;Episode: {episode} Score: {economy}&#39;)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Deep-Learning-Model-with-Keras">Deep Learning Model with Keras<a class="anchor-link" href="#Deep-Learning-Model-with-Keras">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[113]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">tensorflow.keras.models</span> <span class="k">import</span> <span class="n">Sequential</span>
<span class="kn">from</span> <span class="nn">tensorflow.keras.layers</span> <span class="k">import</span> <span class="n">Dense</span><span class="p">,</span> <span class="n">Flatten</span>
<span class="kn">from</span> <span class="nn">tensorflow.keras.optimizers</span> <span class="k">import</span> <span class="n">Adam</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[114]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">build_model</span><span class="p">(</span><span class="n">states</span><span class="p">,</span> <span class="n">actions</span><span class="p">):</span>
    <span class="n">model</span> <span class="o">=</span> <span class="n">Sequential</span><span class="p">()</span>
    <span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Dense</span><span class="p">(</span><span class="mi">32</span><span class="p">,</span> <span class="n">activation</span> <span class="o">=</span> <span class="s1">&#39;relu&#39;</span><span class="p">,</span><span class="n">input_shape</span> <span class="o">=</span> <span class="n">states</span><span class="p">))</span>
    <span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Dense</span><span class="p">(</span><span class="mi">64</span><span class="p">,</span> <span class="n">activation</span> <span class="o">=</span> <span class="s1">&#39;relu&#39;</span><span class="p">))</span>
    <span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Dense</span><span class="p">(</span><span class="n">actions</span><span class="p">,</span> <span class="n">activation</span> <span class="o">=</span> <span class="s1">&#39;linear&#39;</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">model</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[120]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># del model</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[121]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">states</span> <span class="o">=</span> <span class="n">env</span><span class="o">.</span><span class="n">observation_space</span><span class="o">.</span><span class="n">shape</span>
<span class="n">actions</span> <span class="o">=</span> <span class="n">env</span><span class="o">.</span><span class="n">action_space</span><span class="o">.</span><span class="n">n</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">build_model</span><span class="p">(</span><span class="n">states</span><span class="p">,</span> <span class="n">actions</span><span class="p">)</span>
<span class="n">model</span><span class="o">.</span><span class="n">summary</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Model: &#34;sequential_1&#34;
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_3 (Dense)              (None, 32)                224       
_________________________________________________________________
dense_4 (Dense)              (None, 64)                2112      
_________________________________________________________________
dense_5 (Dense)              (None, 3)                 195       
=================================================================
Total params: 2,531
Trainable params: 2,531
Non-trainable params: 0
_________________________________________________________________
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Build-Agent-with-Keras-RL">Build Agent with Keras-RL<a class="anchor-link" href="#Build-Agent-with-Keras-RL">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[117]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">rl.agents</span> <span class="k">import</span> <span class="n">DQNAgent</span>
<span class="kn">from</span> <span class="nn">rl.policy</span> <span class="k">import</span> <span class="n">BoltzmannQPolicy</span>
<span class="kn">from</span> <span class="nn">rl.memory</span> <span class="k">import</span> <span class="n">SequentialMemory</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[122]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">build_agent</span><span class="p">(</span><span class="n">model</span><span class="p">,</span> <span class="n">actions</span><span class="p">):</span>
    <span class="n">policy</span> <span class="o">=</span> <span class="n">BoltzmannQPolicy</span><span class="p">()</span> <span class="c1"># ?</span>
    <span class="n">memory</span> <span class="o">=</span> <span class="n">SequentialMemory</span><span class="p">(</span><span class="n">limit</span> <span class="o">=</span> <span class="mi">1000</span><span class="p">,</span> <span class="n">window_length</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
    <span class="n">dqn</span> <span class="o">=</span> <span class="n">DQNAgent</span><span class="p">(</span><span class="n">model</span> <span class="o">=</span> <span class="n">model</span><span class="p">,</span> <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span><span class="p">,</span> <span class="n">policy</span> <span class="o">=</span> <span class="n">policy</span><span class="p">,</span> 
                   <span class="n">nb_actions</span> <span class="o">=</span> <span class="n">actions</span><span class="p">,</span> <span class="n">nb_steps_warmup</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span> <span class="n">target_model_update</span> <span class="o">=</span> <span class="mi">1000</span><span class="p">)</span> <span class="c1"># target_model_update</span>
                  
    <span class="k">return</span> <span class="n">dqn</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dqn</span> <span class="o">=</span> <span class="n">build_agent</span><span class="p">(</span><span class="n">model</span><span class="p">,</span> <span class="n">actions</span><span class="p">)</span>
<span class="n">dqn</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="n">Adam</span><span class="p">(</span><span class="n">lr</span> <span class="o">=</span> <span class="mf">1e-3</span><span class="p">),</span> <span class="n">metrics</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;mae&#39;</span><span class="p">])</span>
<span class="n">dqn</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">env</span><span class="p">,</span> <span class="n">nb_steps</span> <span class="o">=</span> <span class="mi">2000</span><span class="p">,</span> <span class="n">visualize</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">verbose</span> <span class="o">=</span> <span class="mi">1</span>  <span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Training for 2000 steps ...
Interval 1 (0 steps performed)
WARNING:tensorflow:From /Users/yi/opt/anaconda3/lib/python3.7/site-packages/tensorflow/python/keras/engine/training_v1.py:2070: Model.state_updates (from tensorflow.python.keras.engine.training) is deprecated and will be removed in a future version.
Instructions for updating:
This property should not be used in TensorFlow 2.0, as updates are applied automatically.
No. 28 exposure increased to 1.0 in day 4 at 5
    1/10000 [..............................] - ETA: 53:06:12 - reward: 993.0000No. 28 exposure increased to 2.0 in day 4 at 1
No. 111 exposure increased to 1.0 in day 4 at 1
    2/10000 [..............................] - ETA: 35:03:16 - reward: 938.3850*When No. 28 infected, Exposure is 2.0 in day 4 at move 1
No. 111 exposure increased to 2.0 in day 4 at 5
No. 169 exposure increased to 1.0 in day 4 at 5
No. 558 exposure increased to 2.0 in day 4 at 5
No. 890 exposure increased to 1.0 in day 4 at 5
No. 937 exposure increased to 1.0 in day 4 at 5
    3/10000 [..............................] - ETA: 37:39:48 - reward: 946.6600No. 111 exposure increased to 3.0 in day 4 at 1
No. 169 exposure increased to 2.0 in day 4 at 1
No. 303 exposure increased to 2.0 in day 4 at 1
No. 442 exposure increased to 2.0 in day 4 at 1
No. 558 exposure increased to 3.0 in day 4 at 1
No. 890 exposure increased to 2.0 in day 4 at 1
No. 937 exposure increased to 2.0 in day 4 at 1
    4/10000 [..............................] - ETA: 31:40:00 - reward: 943.3500*When No. 890 infected, Exposure is 2.0 in day 4 at move 0
*When No. 303 infected, Exposure is 2.0 in day 4 at move 1
*When No. 558 infected, Exposure is 3.0 in day 4 at move 1
*When No. 442 infected, Exposure is 2.0 in day 4 at move 2
*When No. 169 infected, Exposure is 2.0 in day 4 at move 3
No. 61 exposure increased to 1.0 in day 4 at 5
No. 111 exposure increased to 4.0 in day 4 at 5
No. 872 exposure increased to 1.0 in day 4 at 5
No. 937 exposure increased to 3.0 in day 4 at 5
    5/10000 [..............................] - ETA: 34:32:29 - reward: 924.7880*When No. 111 infected, Exposure is 4.0 in day 4 at move 0
No. 61 exposure increased to 2.0 in day 4 at 1
No. 594 exposure increased to 1.0 in day 4 at 1
No. 608 exposure increased to 1.0 in day 4 at 1
No. 872 exposure increased to 2.0 in day 4 at 1
No. 937 exposure increased to 4.0 in day 4 at 1
    6/10000 [..............................] - ETA: 30:51:12 - reward: 904.0367*When No. 937 infected, Exposure is 4.0 in day 4 at move 0
No. 61 exposure increased to 3.0 in day 4 at 5
No. 110 exposure increased to 1.0 in day 4 at 5
No. 153 exposure increased to 1.0 in day 4 at 5
No. 259 exposure increased to 1.0 in day 4 at 5
No. 594 exposure increased to 2.0 in day 4 at 5
No. 608 exposure increased to 2.0 in day 4 at 5
No. 872 exposure increased to 3.0 in day 4 at 5
    7/10000 [..............................] - ETA: 32:32:10 - reward: 898.9686No. 61 exposure increased to 4.0 in day 4 at 5
No. 110 exposure increased to 2.0 in day 4 at 5
No. 153 exposure increased to 2.0 in day 4 at 5
No. 209 exposure increased to 1.0 in day 4 at 5
No. 259 exposure increased to 2.0 in day 4 at 5
No. 552 exposure increased to 1.0 in day 4 at 5
No. 594 exposure increased to 3.0 in day 4 at 5
No. 608 exposure increased to 3.0 in day 4 at 5
No. 627 exposure increased to 1.0 in day 4 at 5
No. 687 exposure increased to 2.0 in day 4 at 5
No. 872 exposure increased to 4.0 in day 4 at 5
    8/10000 [..............................] - ETA: 33:50:52 - reward: 899.0963*When No. 259 infected, Exposure is 2.0 in day 4 at move 0
*When No. 594 infected, Exposure is 3.0 in day 4 at move 0
*When No. 872 infected, Exposure is 4.0 in day 4 at move 0
*When No. 153 infected, Exposure is 2.0 in day 4 at move 2
No. 61 exposure increased to 5.0 in day 4 at 5
No. 92 exposure increased to 1.0 in day 4 at 5
No. 110 exposure increased to 3.0 in day 4 at 5
No. 122 exposure increased to 1.0 in day 4 at 5
No. 209 exposure increased to 2.0 in day 4 at 5
No. 298 exposure increased to 1.0 in day 4 at 5
No. 327 exposure increased to 1.0 in day 4 at 5
No. 527 exposure increased to 1.0 in day 4 at 5
No. 552 exposure increased to 2.0 in day 4 at 5
No. 608 exposure increased to 4.0 in day 4 at 5
No. 627 exposure increased to 2.0 in day 4 at 5
*When No. 687 infected, Exposure is 2.0 in day 4 at move 5
No. 725 exposure increased to 1.0 in day 4 at 5
    9/10000 [..............................] - ETA: 34:41:01 - reward: 893.2233*When No. 61 infected, Exposure is 5.0 in day 4 at move 0
No. 70 exposure increased to 1.0 in day 4 at 1
No. 92 exposure increased to 2.0 in day 4 at 1
No. 110 exposure increased to 4.0 in day 4 at 1
No. 122 exposure increased to 2.0 in day 4 at 1
No. 207 exposure increased to 2.0 in day 4 at 1
No. 209 exposure increased to 3.0 in day 4 at 1
No. 248 exposure increased to 2.0 in day 4 at 1
No. 298 exposure increased to 2.0 in day 4 at 1
No. 327 exposure increased to 2.0 in day 4 at 1
No. 411 exposure increased to 2.0 in day 4 at 1
No. 527 exposure increased to 2.0 in day 4 at 1
No. 552 exposure increased to 3.0 in day 4 at 1
No. 608 exposure increased to 5.0 in day 4 at 1
No. 627 exposure increased to 3.0 in day 4 at 1
No. 725 exposure increased to 2.0 in day 4 at 1
No. 846 exposure increased to 1.0 in day 4 at 1
No. 946 exposure increased to 2.0 in day 4 at 1
   10/10000 [..............................] - ETA: 32:36:29 - reward: 902.2010*When No. 608 infected, Exposure is 5.0 in day 4 at move 0
No. 19 exposure increased to 1.0 in day 4 at 1
No. 70 exposure increased to 2.0 in day 4 at 1
No. 92 exposure increased to 3.0 in day 4 at 1
No. 110 exposure increased to 5.0 in day 4 at 1
*When No. 122 infected, Exposure is 2.0 in day 4 at move 1
No. 207 exposure increased to 3.0 in day 4 at 1
No. 209 exposure increased to 4.0 in day 4 at 1
No. 210 exposure increased to 1.0 in day 4 at 1
No. 248 exposure increased to 3.0 in day 4 at 1
No. 298 exposure increased to 3.0 in day 4 at 1
No. 327 exposure increased to 3.0 in day 4 at 1
No. 411 exposure increased to 3.0 in day 4 at 1
No. 527 exposure increased to 3.0 in day 4 at 1
No. 550 exposure increased to 1.0 in day 4 at 1
No. 552 exposure increased to 4.0 in day 4 at 1
*When No. 627 infected, Exposure is 3.0 in day 4 at move 1
No. 725 exposure increased to 3.0 in day 4 at 1
No. 782 exposure increased to 1.0 in day 4 at 1
No. 846 exposure increased to 2.0 in day 4 at 1
No. 946 exposure increased to 3.0 in day 4 at 1
No. 985 exposure increased to 2.0 in day 4 at 1
   11/10000 [..............................] - ETA: 30:54:14 - reward: 903.9282*When No. 209 infected, Exposure is 4.0 in day 4 at move 0
*When No. 298 infected, Exposure is 3.0 in day 4 at move 0
*When No. 411 infected, Exposure is 3.0 in day 4 at move 0
No. 6 exposure increased to 1.0 in day 4 at 1
No. 19 exposure increased to 2.0 in day 4 at 1
No. 70 exposure increased to 3.0 in day 4 at 1
No. 92 exposure increased to 4.0 in day 4 at 1
*When No. 110 infected, Exposure is 5.0 in day 4 at move 1
No. 207 exposure increased to 4.0 in day 4 at 1
No. 210 exposure increased to 2.0 in day 4 at 1
No. 248 exposure increased to 4.0 in day 4 at 1
No. 327 exposure increased to 4.0 in day 4 at 1
No. 432 exposure increased to 1.0 in day 4 at 1
No. 527 exposure increased to 4.0 in day 4 at 1
No. 550 exposure increased to 2.0 in day 4 at 1
*When No. 552 infected, Exposure is 4.0 in day 4 at move 1
No. 620 exposure increased to 2.0 in day 4 at 1
*When No. 725 infected, Exposure is 3.0 in day 4 at move 1
No. 726 exposure increased to 2.0 in day 4 at 1
No. 747 exposure increased to 2.0 in day 4 at 1
No. 782 exposure increased to 2.0 in day 4 at 1
No. 812 exposure increased to 1.0 in day 4 at 1
No. 846 exposure increased to 3.0 in day 4 at 1
No. 946 exposure increased to 4.0 in day 4 at 1
No. 960 exposure increased to 1.0 in day 4 at 1
No. 985 exposure increased to 3.0 in day 4 at 1
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>/Users/yi/opt/anaconda3/lib/python3.7/site-packages/rl/memory.py:40: UserWarning: Not enough entries to sample without replacement. Consider increasing your warm-up phase to avoid oversampling!
  warnings.warn(&#39;Not enough entries to sample without replacement. Consider increasing your warm-up phase to avoid oversampling!&#39;)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>   12/10000 [..............................] - ETA: 29:35:13 - reward: 907.3325*When No. 19 infected, Exposure is 2.0 in day 4 at move 0
No. 6 exposure increased to 2.0 in day 4 at 1
*When No. 70 infected, Exposure is 3.0 in day 4 at move 1
No. 92 exposure increased to 5.0 in day 4 at 1
No. 142 exposure increased to 2.0 in day 4 at 1
*When No. 207 infected, Exposure is 4.0 in day 4 at move 1
No. 210 exposure increased to 3.0 in day 4 at 1
No. 248 exposure increased to 5.0 in day 4 at 1
No. 327 exposure increased to 5.0 in day 4 at 1
No. 432 exposure increased to 2.0 in day 4 at 1
*When No. 527 infected, Exposure is 4.0 in day 4 at move 1
No. 550 exposure increased to 3.0 in day 4 at 1
No. 620 exposure increased to 3.0 in day 4 at 1
No. 623 exposure increased to 2.0 in day 4 at 1
No. 726 exposure increased to 3.0 in day 4 at 1
No. 747 exposure increased to 3.0 in day 4 at 1
No. 782 exposure increased to 3.0 in day 4 at 1
No. 812 exposure increased to 2.0 in day 4 at 1
No. 829 exposure increased to 1.0 in day 4 at 1
No. 846 exposure increased to 4.0 in day 4 at 1
No. 946 exposure increased to 5.0 in day 4 at 1
No. 960 exposure increased to 2.0 in day 4 at 1
No. 985 exposure increased to 4.0 in day 4 at 1
   13/10000 [..............................] - ETA: 28:31:17 - reward: 909.9146*When No. 248 infected, Exposure is 5.0 in day 4 at move 0
*When No. 620 infected, Exposure is 3.0 in day 4 at move 0
No. 6 exposure increased to 3.0 in day 4 at 1
No. 92 exposure increased to 6.0 in day 4 at 1
No. 107 exposure increased to 2.0 in day 4 at 1
No. 142 exposure increased to 3.0 in day 4 at 1
No. 144 exposure increased to 2.0 in day 4 at 1
No. 210 exposure increased to 4.0 in day 4 at 1
*When No. 327 infected, Exposure is 5.0 in day 4 at move 1
No. 371 exposure increased to 1.0 in day 4 at 1
No. 416 exposure increased to 1.0 in day 4 at 1
No. 432 exposure increased to 3.0 in day 4 at 1
No. 440 exposure increased to 2.0 in day 4 at 1
*When No. 550 infected, Exposure is 3.0 in day 4 at move 1
No. 576 exposure increased to 1.0 in day 4 at 1
No. 623 exposure increased to 3.0 in day 4 at 1
No. 726 exposure increased to 4.0 in day 4 at 1
No. 744 exposure increased to 2.0 in day 4 at 1
No. 747 exposure increased to 4.0 in day 4 at 1
No. 782 exposure increased to 4.0 in day 4 at 1
No. 810 exposure increased to 2.0 in day 4 at 1
No. 812 exposure increased to 3.0 in day 4 at 1
No. 829 exposure increased to 2.0 in day 4 at 1
No. 846 exposure increased to 5.0 in day 4 at 1
No. 946 exposure increased to 6.0 in day 4 at 1
No. 960 exposure increased to 3.0 in day 4 at 1
No. 971 exposure increased to 2.0 in day 4 at 1
No. 985 exposure increased to 5.0 in day 4 at 1
   14/10000 [..............................] - ETA: 27:38:21 - reward: 903.5707*When No. 210 infected, Exposure is 4.0 in day 4 at move 0
*When No. 623 infected, Exposure is 3.0 in day 4 at move 0
*When No. 782 infected, Exposure is 4.0 in day 4 at move 0
*When No. 846 infected, Exposure is 5.0 in day 4 at move 0
No. 6 exposure increased to 4.0 in day 4 at 1
No. 69 exposure increased to 1.0 in day 4 at 1
*When No. 92 infected, Exposure is 6.0 in day 4 at move 1
No. 107 exposure increased to 3.0 in day 4 at 1
No. 142 exposure increased to 4.0 in day 4 at 1
No. 144 exposure increased to 3.0 in day 4 at 1
No. 159 exposure increased to 2.0 in day 4 at 1
No. 225 exposure increased to 1.0 in day 4 at 1
No. 348 exposure increased to 2.0 in day 4 at 1
No. 371 exposure increased to 2.0 in day 4 at 1
No. 416 exposure increased to 2.0 in day 4 at 1
*When No. 432 infected, Exposure is 3.0 in day 4 at move 1
No. 440 exposure increased to 3.0 in day 4 at 1
No. 576 exposure increased to 2.0 in day 4 at 1
*When No. 726 infected, Exposure is 4.0 in day 4 at move 1
No. 744 exposure increased to 3.0 in day 4 at 1
No. 747 exposure increased to 5.0 in day 4 at 1
No. 748 exposure increased to 1.0 in day 4 at 1
No. 810 exposure increased to 3.0 in day 4 at 1
No. 812 exposure increased to 4.0 in day 4 at 1
*When No. 829 infected, Exposure is 2.0 in day 4 at move 1
No. 844 exposure increased to 2.0 in day 4 at 1
No. 914 exposure increased to 2.0 in day 4 at 1
*When No. 946 infected, Exposure is 6.0 in day 4 at move 1
*When No. 960 infected, Exposure is 3.0 in day 4 at move 1
No. 971 exposure increased to 3.0 in day 4 at 1
No. 985 exposure increased to 6.0 in day 4 at 1
   15/10000 [..............................] - ETA: 26:50:52 - reward: 899.4767*When No. 144 infected, Exposure is 3.0 in day 4 at move 0
*When No. 159 infected, Exposure is 2.0 in day 4 at move 0
*When No. 416 infected, Exposure is 2.0 in day 4 at move 0
*When No. 744 infected, Exposure is 3.0 in day 4 at move 0
*When No. 747 infected, Exposure is 5.0 in day 4 at move 0
*When No. 844 infected, Exposure is 2.0 in day 4 at move 0
*When No. 440 infected, Exposure is 3.0 in day 4 at move 1
*When No. 810 infected, Exposure is 3.0 in day 4 at move 1
*When No. 985 infected, Exposure is 6.0 in day 4 at move 2
*When No. 348 infected, Exposure is 2.0 in day 4 at move 4
*When No. 812 infected, Exposure is 4.0 in day 4 at move 4
No. 6 exposure increased to 5.0 in day 4 at 5
No. 69 exposure increased to 2.0 in day 4 at 5
No. 77 exposure increased to 1.0 in day 4 at 5
No. 107 exposure increased to 4.0 in day 4 at 5
No. 113 exposure increased to 1.0 in day 4 at 5
No. 142 exposure increased to 5.0 in day 4 at 5
No. 160 exposure increased to 1.0 in day 4 at 5
No. 171 exposure increased to 1.0 in day 4 at 5
No. 172 exposure increased to 2.0 in day 4 at 5
No. 225 exposure increased to 2.0 in day 4 at 5
No. 247 exposure increased to 1.0 in day 4 at 5
No. 282 exposure increased to 1.0 in day 4 at 5
No. 286 exposure increased to 1.0 in day 4 at 5
No. 313 exposure increased to 1.0 in day 4 at 5
No. 356 exposure increased to 1.0 in day 4 at 5
No. 371 exposure increased to 3.0 in day 4 at 5
No. 413 exposure increased to 2.0 in day 4 at 5
*When No. 576 infected, Exposure is 2.0 in day 4 at move 5
No. 622 exposure increased to 1.0 in day 4 at 5
No. 625 exposure increased to 1.0 in day 4 at 5
No. 748 exposure increased to 2.0 in day 4 at 5
No. 753 exposure increased to 1.0 in day 4 at 5
No. 775 exposure increased to 1.0 in day 4 at 5
No. 783 exposure increased to 1.0 in day 4 at 5
No. 792 exposure increased to 1.0 in day 4 at 5
No. 793 exposure increased to 1.0 in day 4 at 5
No. 808 exposure increased to 1.0 in day 4 at 5
No. 813 exposure increased to 1.0 in day 4 at 5
No. 864 exposure increased to 2.0 in day 4 at 5
No. 871 exposure increased to 1.0 in day 4 at 5
No. 900 exposure increased to 1.0 in day 4 at 5
No. 914 exposure increased to 3.0 in day 4 at 5
No. 971 exposure increased to 4.0 in day 4 at 5
No. 980 exposure increased to 1.0 in day 4 at 5
No. 988 exposure increased to 1.0 in day 4 at 5
No. 995 exposure increased to 1.0 in day 4 at 5
   16/10000 [..............................] - ETA: 28:01:56 - reward: 891.6906*When No. 6 infected, Exposure is 5.0 in day 4 at move 0
*When No. 142 infected, Exposure is 5.0 in day 4 at move 0
*When No. 69 infected, Exposure is 2.0 in day 4 at move 1
No. 77 exposure increased to 2.0 in day 4 at 1
No. 107 exposure increased to 5.0 in day 4 at 1
No. 108 exposure increased to 1.0 in day 4 at 1
No. 113 exposure increased to 2.0 in day 4 at 1
No. 160 exposure increased to 2.0 in day 4 at 1
No. 171 exposure increased to 2.0 in day 4 at 1
No. 172 exposure increased to 3.0 in day 4 at 1
*When No. 225 infected, Exposure is 2.0 in day 4 at move 1
No. 247 exposure increased to 2.0 in day 4 at 1
No. 282 exposure increased to 2.0 in day 4 at 1
No. 286 exposure increased to 2.0 in day 4 at 1
No. 313 exposure increased to 2.0 in day 4 at 1
No. 356 exposure increased to 2.0 in day 4 at 1
No. 371 exposure increased to 4.0 in day 4 at 1
No. 398 exposure increased to 2.0 in day 4 at 1
No. 403 exposure increased to 2.0 in day 4 at 1
No. 413 exposure increased to 3.0 in day 4 at 1
No. 486 exposure increased to 1.0 in day 4 at 1
No. 555 exposure increased to 1.0 in day 4 at 1
No. 593 exposure increased to 2.0 in day 4 at 1
No. 596 exposure increased to 2.0 in day 4 at 1
No. 622 exposure increased to 2.0 in day 4 at 1
No. 625 exposure increased to 2.0 in day 4 at 1
No. 693 exposure increased to 1.0 in day 4 at 1
No. 748 exposure increased to 3.0 in day 4 at 1
No. 753 exposure increased to 2.0 in day 4 at 1
No. 775 exposure increased to 2.0 in day 4 at 1
No. 783 exposure increased to 2.0 in day 4 at 1
No. 792 exposure increased to 2.0 in day 4 at 1
No. 793 exposure increased to 2.0 in day 4 at 1
No. 794 exposure increased to 1.0 in day 4 at 1
No. 808 exposure increased to 2.0 in day 4 at 1
No. 813 exposure increased to 2.0 in day 4 at 1
*When No. 864 infected, Exposure is 2.0 in day 4 at move 1
No. 871 exposure increased to 2.0 in day 4 at 1
No. 878 exposure increased to 1.0 in day 4 at 1
No. 900 exposure increased to 2.0 in day 4 at 1
No. 914 exposure increased to 4.0 in day 4 at 1
No. 941 exposure increased to 1.0 in day 4 at 1
*When No. 971 infected, Exposure is 4.0 in day 4 at move 1
No. 980 exposure increased to 2.0 in day 4 at 1
No. 987 exposure increased to 1.0 in day 4 at 1
No. 988 exposure increased to 2.0 in day 4 at 1
No. 995 exposure increased to 2.0 in day 4 at 1
   17/10000 [..............................] - ETA: 27:21:24 - reward: 890.6071*When No. 398 infected, Exposure is 2.0 in day 4 at move 0
No. 50 exposure increased to 2.0 in day 4 at 1
No. 77 exposure increased to 3.0 in day 4 at 1
No. 88 exposure increased to 2.0 in day 4 at 1
No. 100 exposure increased to 2.0 in day 4 at 1
No. 107 exposure increased to 6.0 in day 4 at 1
No. 108 exposure increased to 2.0 in day 4 at 1
No. 113 exposure increased to 3.0 in day 4 at 1
No. 118 exposure increased to 1.0 in day 4 at 1
No. 131 exposure increased to 2.0 in day 4 at 1
No. 145 exposure increased to 1.0 in day 4 at 1
No. 160 exposure increased to 3.0 in day 4 at 1
No. 171 exposure increased to 3.0 in day 4 at 1
No. 172 exposure increased to 4.0 in day 4 at 1
No. 218 exposure increased to 2.0 in day 4 at 1
No. 247 exposure increased to 3.0 in day 4 at 1
No. 282 exposure increased to 3.0 in day 4 at 1
No. 286 exposure increased to 3.0 in day 4 at 1
No. 304 exposure increased to 1.0 in day 4 at 1
No. 313 exposure increased to 3.0 in day 4 at 1
No. 356 exposure increased to 3.0 in day 4 at 1
No. 371 exposure increased to 5.0 in day 4 at 1
No. 403 exposure increased to 3.0 in day 4 at 1
No. 413 exposure increased to 4.0 in day 4 at 1
No. 449 exposure increased to 2.0 in day 4 at 1
No. 486 exposure increased to 2.0 in day 4 at 1
No. 491 exposure increased to 2.0 in day 4 at 1
No. 523 exposure increased to 1.0 in day 4 at 1
No. 528 exposure increased to 2.0 in day 4 at 1
No. 555 exposure increased to 2.0 in day 4 at 1
No. 574 exposure increased to 2.0 in day 4 at 1
No. 593 exposure increased to 3.0 in day 4 at 1
No. 596 exposure increased to 3.0 in day 4 at 1
No. 622 exposure increased to 3.0 in day 4 at 1
No. 625 exposure increased to 3.0 in day 4 at 1
No. 626 exposure increased to 2.0 in day 4 at 1
No. 657 exposure increased to 1.0 in day 4 at 1
No. 693 exposure increased to 2.0 in day 4 at 1
No. 695 exposure increased to 2.0 in day 4 at 1
*When No. 748 infected, Exposure is 3.0 in day 4 at move 1
No. 753 exposure increased to 3.0 in day 4 at 1
No. 775 exposure increased to 3.0 in day 4 at 1
No. 783 exposure increased to 3.0 in day 4 at 1
No. 792 exposure increased to 3.0 in day 4 at 1
No. 793 exposure increased to 3.0 in day 4 at 1
No. 794 exposure increased to 2.0 in day 4 at 1
No. 808 exposure increased to 3.0 in day 4 at 1
No. 813 exposure increased to 3.0 in day 4 at 1
No. 871 exposure increased to 3.0 in day 4 at 1
No. 876 exposure increased to 1.0 in day 4 at 1
No. 878 exposure increased to 2.0 in day 4 at 1
No. 900 exposure increased to 3.0 in day 4 at 1
*When No. 914 infected, Exposure is 4.0 in day 4 at move 1
No. 941 exposure increased to 2.0 in day 4 at 1
No. 980 exposure increased to 3.0 in day 4 at 1
No. 983 exposure increased to 2.0 in day 4 at 1
No. 987 exposure increased to 2.0 in day 4 at 1
No. 988 exposure increased to 3.0 in day 4 at 1
No. 995 exposure increased to 3.0 in day 4 at 1
   18/10000 [..............................] - ETA: 27:26:52 - reward: 884.8089*When No. 107 infected, Exposure is 6.0 in day 4 at move 0
*When No. 171 infected, Exposure is 3.0 in day 4 at move 0
*When No. 356 infected, Exposure is 3.0 in day 4 at move 0
*When No. 413 infected, Exposure is 4.0 in day 4 at move 0
*When No. 449 infected, Exposure is 2.0 in day 4 at move 0
*When No. 693 infected, Exposure is 2.0 in day 4 at move 0
*When No. 753 infected, Exposure is 3.0 in day 4 at move 0
*When No. 813 infected, Exposure is 3.0 in day 4 at move 0
*When No. 108 infected, Exposure is 2.0 in day 4 at move 1
*When No. 113 infected, Exposure is 3.0 in day 4 at move 1
*When No. 218 infected, Exposure is 2.0 in day 4 at move 1
*When No. 313 infected, Exposure is 3.0 in day 4 at move 1
*When No. 593 infected, Exposure is 3.0 in day 4 at move 1
*When No. 622 infected, Exposure is 3.0 in day 4 at move 1
*When No. 626 infected, Exposure is 2.0 in day 4 at move 1
*When No. 695 infected, Exposure is 2.0 in day 4 at move 1
*When No. 808 infected, Exposure is 3.0 in day 4 at move 1
*When No. 878 infected, Exposure is 2.0 in day 4 at move 1
*When No. 988 infected, Exposure is 3.0 in day 4 at move 1
*When No. 100 infected, Exposure is 2.0 in day 4 at move 2
*When No. 160 infected, Exposure is 3.0 in day 4 at move 2
*When No. 783 infected, Exposure is 3.0 in day 4 at move 2
*When No. 900 infected, Exposure is 3.0 in day 4 at move 2
*When No. 50 infected, Exposure is 2.0 in day 4 at move 3
*When No. 172 infected, Exposure is 4.0 in day 4 at move 3
*When No. 247 infected, Exposure is 3.0 in day 4 at move 3
*When No. 596 infected, Exposure is 3.0 in day 4 at move 3
*When No. 775 infected, Exposure is 3.0 in day 4 at move 3
*When No. 980 infected, Exposure is 3.0 in day 4 at move 3
*When No. 88 infected, Exposure is 2.0 in day 4 at move 4
*When No. 871 infected, Exposure is 3.0 in day 4 at move 4
No. 13 exposure increased to 1.0 in day 4 at 5
No. 16 exposure increased to 2.0 in day 4 at 5
No. 67 exposure increased to 1.0 in day 4 at 5
No. 77 exposure increased to 4.0 in day 4 at 5
No. 85 exposure increased to 1.0 in day 4 at 5
No. 102 exposure increased to 1.0 in day 4 at 5
No. 118 exposure increased to 2.0 in day 4 at 5
No. 131 exposure increased to 3.0 in day 4 at 5
No. 145 exposure increased to 2.0 in day 4 at 5
No. 163 exposure increased to 1.0 in day 4 at 5
No. 170 exposure increased to 1.0 in day 4 at 5
No. 194 exposure increased to 2.0 in day 4 at 5
No. 212 exposure increased to 1.0 in day 4 at 5
No. 215 exposure increased to 1.0 in day 4 at 5
No. 216 exposure increased to 2.0 in day 4 at 5
No. 243 exposure increased to 1.0 in day 4 at 5
No. 251 exposure increased to 1.0 in day 4 at 5
No. 255 exposure increased to 2.0 in day 4 at 5
No. 282 exposure increased to 4.0 in day 4 at 5
No. 286 exposure increased to 4.0 in day 4 at 5
No. 289 exposure increased to 1.0 in day 4 at 5
No. 304 exposure increased to 2.0 in day 4 at 5
No. 342 exposure increased to 1.0 in day 4 at 5
No. 371 exposure increased to 6.0 in day 4 at 5
No. 372 exposure increased to 2.0 in day 4 at 5
No. 403 exposure increased to 4.0 in day 4 at 5
No. 426 exposure increased to 2.0 in day 4 at 5
No. 486 exposure increased to 3.0 in day 4 at 5
No. 487 exposure increased to 1.0 in day 4 at 5
No. 491 exposure increased to 3.0 in day 4 at 5
No. 498 exposure increased to 1.0 in day 4 at 5
No. 500 exposure increased to 2.0 in day 4 at 5
No. 501 exposure increased to 1.0 in day 4 at 5
No. 523 exposure increased to 2.0 in day 4 at 5
No. 528 exposure increased to 3.0 in day 4 at 5
No. 547 exposure increased to 1.0 in day 4 at 5
No. 555 exposure increased to 3.0 in day 4 at 5
No. 574 exposure increased to 3.0 in day 4 at 5
No. 591 exposure increased to 1.0 in day 4 at 5
No. 625 exposure increased to 4.0 in day 4 at 5
No. 637 exposure increased to 1.0 in day 4 at 5
No. 651 exposure increased to 1.0 in day 4 at 5
No. 657 exposure increased to 2.0 in day 4 at 5
No. 660 exposure increased to 1.0 in day 4 at 5
No. 666 exposure increased to 1.0 in day 4 at 5
No. 670 exposure increased to 1.0 in day 4 at 5
No. 674 exposure increased to 1.0 in day 4 at 5
No. 751 exposure increased to 1.0 in day 4 at 5
No. 787 exposure increased to 1.0 in day 4 at 5
No. 792 exposure increased to 4.0 in day 4 at 5
No. 793 exposure increased to 4.0 in day 4 at 5
No. 794 exposure increased to 3.0 in day 4 at 5
No. 876 exposure increased to 2.0 in day 4 at 5
No. 881 exposure increased to 1.0 in day 4 at 5
No. 892 exposure increased to 1.0 in day 4 at 5
No. 906 exposure increased to 1.0 in day 4 at 5
No. 915 exposure increased to 1.0 in day 4 at 5
No. 924 exposure increased to 1.0 in day 4 at 5
*When No. 941 infected, Exposure is 2.0 in day 4 at move 5
No. 942 exposure increased to 1.0 in day 4 at 5
No. 968 exposure increased to 1.0 in day 4 at 5
No. 976 exposure increased to 1.0 in day 4 at 5
No. 977 exposure increased to 1.0 in day 4 at 5
No. 983 exposure increased to 3.0 in day 4 at 5
No. 987 exposure increased to 3.0 in day 4 at 5
No. 995 exposure increased to 4.0 in day 4 at 5
   19/10000 [..............................] - ETA: 29:34:02 - reward: 878.2063*When No. 145 infected, Exposure is 2.0 in day 4 at move 0
*When No. 282 infected, Exposure is 4.0 in day 4 at move 0
*When No. 491 infected, Exposure is 3.0 in day 4 at move 0
*When No. 625 infected, Exposure is 4.0 in day 4 at move 0
*When No. 794 infected, Exposure is 3.0 in day 4 at move 0
*When No. 987 infected, Exposure is 3.0 in day 4 at move 0
*When No. 371 infected, Exposure is 6.0 in day 4 at move 1
*When No. 792 infected, Exposure is 4.0 in day 4 at move 1
*When No. 16 infected, Exposure is 2.0 in day 4 at move 2
*When No. 216 infected, Exposure is 2.0 in day 4 at move 2
*When No. 995 infected, Exposure is 4.0 in day 4 at move 2
*When No. 77 infected, Exposure is 4.0 in day 4 at move 3
*When No. 131 infected, Exposure is 3.0 in day 4 at move 3
*When No. 255 infected, Exposure is 2.0 in day 4 at move 3
*When No. 286 infected, Exposure is 4.0 in day 4 at move 3
*When No. 426 infected, Exposure is 2.0 in day 4 at move 3
*When No. 574 infected, Exposure is 3.0 in day 4 at move 3
*When No. 486 infected, Exposure is 3.0 in day 4 at move 4
No. 12 exposure increased to 1.0 in day 4 at 5
No. 13 exposure increased to 2.0 in day 4 at 5
No. 22 exposure increased to 1.0 in day 4 at 5
No. 25 exposure increased to 1.0 in day 4 at 5
No. 51 exposure increased to 1.0 in day 4 at 5
No. 57 exposure increased to 1.0 in day 4 at 5
No. 67 exposure increased to 2.0 in day 4 at 5
No. 82 exposure increased to 1.0 in day 4 at 5
No. 85 exposure increased to 2.0 in day 4 at 5
No. 102 exposure increased to 2.0 in day 4 at 5
No. 118 exposure increased to 3.0 in day 4 at 5
No. 123 exposure increased to 2.0 in day 4 at 5
No. 127 exposure increased to 1.0 in day 4 at 5
No. 163 exposure increased to 2.0 in day 4 at 5
No. 170 exposure increased to 2.0 in day 4 at 5
No. 182 exposure increased to 1.0 in day 4 at 5
No. 194 exposure increased to 3.0 in day 4 at 5
No. 205 exposure increased to 1.0 in day 4 at 5
No. 208 exposure increased to 2.0 in day 4 at 5
No. 211 exposure increased to 1.0 in day 4 at 5
No. 212 exposure increased to 2.0 in day 4 at 5
No. 215 exposure increased to 2.0 in day 4 at 5
No. 229 exposure increased to 1.0 in day 4 at 5
No. 231 exposure increased to 1.0 in day 4 at 5
No. 243 exposure increased to 2.0 in day 4 at 5
No. 249 exposure increased to 1.0 in day 4 at 5
No. 251 exposure increased to 2.0 in day 4 at 5
No. 254 exposure increased to 1.0 in day 4 at 5
No. 257 exposure increased to 2.0 in day 4 at 5
No. 275 exposure increased to 1.0 in day 4 at 5
No. 289 exposure increased to 2.0 in day 4 at 5
No. 304 exposure increased to 3.0 in day 4 at 5
No. 308 exposure increased to 2.0 in day 4 at 5
No. 309 exposure increased to 1.0 in day 4 at 5
No. 314 exposure increased to 1.0 in day 4 at 5
No. 319 exposure increased to 1.0 in day 4 at 5
No. 333 exposure increased to 1.0 in day 4 at 5
No. 337 exposure increased to 1.0 in day 4 at 5
No. 342 exposure increased to 2.0 in day 4 at 5
No. 360 exposure increased to 1.0 in day 4 at 5
No. 372 exposure increased to 3.0 in day 4 at 5
No. 375 exposure increased to 2.0 in day 4 at 5
No. 382 exposure increased to 1.0 in day 4 at 5
No. 401 exposure increased to 1.0 in day 4 at 5
No. 403 exposure increased to 5.0 in day 4 at 5
No. 409 exposure increased to 1.0 in day 4 at 5
No. 424 exposure increased to 1.0 in day 4 at 5
No. 438 exposure increased to 1.0 in day 4 at 5
No. 454 exposure increased to 1.0 in day 4 at 5
No. 456 exposure increased to 1.0 in day 4 at 5
No. 475 exposure increased to 2.0 in day 4 at 5
No. 487 exposure increased to 2.0 in day 4 at 5
No. 488 exposure increased to 1.0 in day 4 at 5
No. 498 exposure increased to 2.0 in day 4 at 5
No. 500 exposure increased to 3.0 in day 4 at 5
No. 501 exposure increased to 2.0 in day 4 at 5
No. 510 exposure increased to 2.0 in day 4 at 5
No. 511 exposure increased to 1.0 in day 4 at 5
No. 523 exposure increased to 3.0 in day 4 at 5
No. 525 exposure increased to 1.0 in day 4 at 5
No. 528 exposure increased to 4.0 in day 4 at 5
No. 547 exposure increased to 2.0 in day 4 at 5
No. 549 exposure increased to 1.0 in day 4 at 5
No. 555 exposure increased to 4.0 in day 4 at 5
No. 578 exposure increased to 1.0 in day 4 at 5
No. 591 exposure increased to 2.0 in day 4 at 5
No. 597 exposure increased to 1.0 in day 4 at 5
No. 609 exposure increased to 1.0 in day 4 at 5
No. 613 exposure increased to 1.0 in day 4 at 5
No. 637 exposure increased to 2.0 in day 4 at 5
No. 651 exposure increased to 2.0 in day 4 at 5
No. 657 exposure increased to 3.0 in day 4 at 5
No. 660 exposure increased to 2.0 in day 4 at 5
No. 664 exposure increased to 1.0 in day 4 at 5
No. 666 exposure increased to 2.0 in day 4 at 5
No. 670 exposure increased to 2.0 in day 4 at 5
No. 674 exposure increased to 2.0 in day 4 at 5
No. 679 exposure increased to 1.0 in day 4 at 5
No. 689 exposure increased to 1.0 in day 4 at 5
No. 713 exposure increased to 1.0 in day 4 at 5
No. 718 exposure increased to 1.0 in day 4 at 5
No. 733 exposure increased to 1.0 in day 4 at 5
No. 741 exposure increased to 1.0 in day 4 at 5
No. 745 exposure increased to 1.0 in day 4 at 5
No. 751 exposure increased to 2.0 in day 4 at 5
No. 754 exposure increased to 1.0 in day 4 at 5
No. 761 exposure increased to 2.0 in day 4 at 5
No. 770 exposure increased to 1.0 in day 4 at 5
No. 787 exposure increased to 2.0 in day 4 at 5
No. 793 exposure increased to 5.0 in day 4 at 5
No. 876 exposure increased to 3.0 in day 4 at 5
No. 880 exposure increased to 1.0 in day 4 at 5
No. 881 exposure increased to 2.0 in day 4 at 5
No. 892 exposure increased to 2.0 in day 4 at 5
No. 903 exposure increased to 1.0 in day 4 at 5
No. 906 exposure increased to 2.0 in day 4 at 5
No. 913 exposure increased to 1.0 in day 4 at 5
No. 915 exposure increased to 2.0 in day 4 at 5
No. 924 exposure increased to 2.0 in day 4 at 5
No. 936 exposure increased to 2.0 in day 4 at 5
No. 942 exposure increased to 2.0 in day 4 at 5
No. 968 exposure increased to 2.0 in day 4 at 5
No. 972 exposure increased to 1.0 in day 4 at 5
No. 974 exposure increased to 1.0 in day 4 at 5
No. 976 exposure increased to 2.0 in day 4 at 5
No. 977 exposure increased to 2.0 in day 4 at 5
*When No. 983 infected, Exposure is 3.0 in day 4 at move 5
   20/10000 [..............................] - ETA: 30:28:08 - reward: 875.8910*When No. 251 infected, Exposure is 2.0 in day 4 at move 0
*When No. 257 infected, Exposure is 2.0 in day 4 at move 0
*When No. 500 infected, Exposure is 3.0 in day 4 at move 0
*When No. 501 infected, Exposure is 2.0 in day 4 at move 0
*When No. 528 infected, Exposure is 4.0 in day 4 at move 0
*When No. 555 infected, Exposure is 4.0 in day 4 at move 0
*When No. 670 infected, Exposure is 2.0 in day 4 at move 0
*When No. 793 infected, Exposure is 5.0 in day 4 at move 0
*When No. 212 infected, Exposure is 2.0 in day 4 at move 1
*When No. 243 infected, Exposure is 2.0 in day 4 at move 1
*When No. 403 infected, Exposure is 5.0 in day 4 at move 1
*When No. 651 infected, Exposure is 2.0 in day 4 at move 1
*When No. 906 infected, Exposure is 2.0 in day 4 at move 1
*When No. 123 infected, Exposure is 2.0 in day 4 at move 2
*When No. 523 infected, Exposure is 3.0 in day 4 at move 2
*When No. 194 infected, Exposure is 3.0 in day 4 at move 3
*When No. 475 infected, Exposure is 2.0 in day 4 at move 3
*When No. 751 infected, Exposure is 2.0 in day 4 at move 3
*When No. 85 infected, Exposure is 2.0 in day 4 at move 4
*When No. 118 infected, Exposure is 3.0 in day 4 at move 4
*When No. 170 infected, Exposure is 2.0 in day 4 at move 4
*When No. 208 infected, Exposure is 2.0 in day 4 at move 4
*When No. 342 infected, Exposure is 2.0 in day 4 at move 4
*When No. 547 infected, Exposure is 2.0 in day 4 at move 4
*When No. 876 infected, Exposure is 3.0 in day 4 at move 4
*When No. 968 infected, Exposure is 2.0 in day 4 at move 4
No. 5 exposure increased to 1.0 in day 4 at 5
No. 12 exposure increased to 2.0 in day 4 at 5
No. 13 exposure increased to 3.0 in day 4 at 5
No. 22 exposure increased to 2.0 in day 4 at 5
No. 25 exposure increased to 2.0 in day 4 at 5
No. 51 exposure increased to 2.0 in day 4 at 5
No. 54 exposure increased to 2.0 in day 4 at 5
No. 57 exposure increased to 2.0 in day 4 at 5
No. 62 exposure increased to 1.0 in day 4 at 5
No. 67 exposure increased to 3.0 in day 4 at 5
No. 80 exposure increased to 1.0 in day 4 at 5
No. 82 exposure increased to 2.0 in day 4 at 5
No. 90 exposure increased to 1.0 in day 4 at 5
*When No. 102 infected, Exposure is 2.0 in day 4 at move 5
No. 127 exposure increased to 2.0 in day 4 at 5
No. 136 exposure increased to 1.0 in day 4 at 5
*When No. 163 infected, Exposure is 2.0 in day 4 at move 5
No. 164 exposure increased to 1.0 in day 4 at 5
No. 182 exposure increased to 2.0 in day 4 at 5
No. 189 exposure increased to 1.0 in day 4 at 5
No. 195 exposure increased to 1.0 in day 4 at 5
No. 205 exposure increased to 2.0 in day 4 at 5
No. 211 exposure increased to 2.0 in day 4 at 5
No. 215 exposure increased to 3.0 in day 4 at 5
No. 229 exposure increased to 2.0 in day 4 at 5
No. 231 exposure increased to 2.0 in day 4 at 5
No. 249 exposure increased to 2.0 in day 4 at 5
No. 254 exposure increased to 2.0 in day 4 at 5
No. 258 exposure increased to 1.0 in day 4 at 5
No. 275 exposure increased to 2.0 in day 4 at 5
No. 283 exposure increased to 1.0 in day 4 at 5
*When No. 289 infected, Exposure is 2.0 in day 4 at move 5
No. 304 exposure increased to 4.0 in day 4 at 5
No. 308 exposure increased to 3.0 in day 4 at 5
No. 309 exposure increased to 2.0 in day 4 at 5
No. 314 exposure increased to 2.0 in day 4 at 5
No. 319 exposure increased to 2.0 in day 4 at 5
No. 333 exposure increased to 2.0 in day 4 at 5
No. 337 exposure increased to 2.0 in day 4 at 5
No. 360 exposure increased to 2.0 in day 4 at 5
No. 365 exposure increased to 1.0 in day 4 at 5
No. 370 exposure increased to 1.0 in day 4 at 5
No. 372 exposure increased to 4.0 in day 4 at 5
No. 375 exposure increased to 3.0 in day 4 at 5
No. 382 exposure increased to 2.0 in day 4 at 5
No. 401 exposure increased to 2.0 in day 4 at 5
No. 409 exposure increased to 2.0 in day 4 at 5
No. 424 exposure increased to 2.0 in day 4 at 5
No. 438 exposure increased to 2.0 in day 4 at 5
No. 454 exposure increased to 2.0 in day 4 at 5
No. 455 exposure increased to 1.0 in day 4 at 5
No. 456 exposure increased to 2.0 in day 4 at 5
No. 487 exposure increased to 3.0 in day 4 at 5
No. 488 exposure increased to 2.0 in day 4 at 5
No. 498 exposure increased to 3.0 in day 4 at 5
No. 503 exposure increased to 1.0 in day 4 at 5
No. 504 exposure increased to 1.0 in day 4 at 5
No. 510 exposure increased to 3.0 in day 4 at 5
No. 511 exposure increased to 2.0 in day 4 at 5
No. 524 exposure increased to 1.0 in day 4 at 5
No. 525 exposure increased to 2.0 in day 4 at 5
No. 549 exposure increased to 2.0 in day 4 at 5
No. 571 exposure increased to 1.0 in day 4 at 5
No. 578 exposure increased to 2.0 in day 4 at 5
No. 582 exposure increased to 1.0 in day 4 at 5
No. 591 exposure increased to 3.0 in day 4 at 5
No. 597 exposure increased to 2.0 in day 4 at 5
No. 609 exposure increased to 2.0 in day 4 at 5
No. 613 exposure increased to 2.0 in day 4 at 5
No. 637 exposure increased to 3.0 in day 4 at 5
No. 648 exposure increased to 2.0 in day 4 at 5
No. 657 exposure increased to 4.0 in day 4 at 5
No. 660 exposure increased to 3.0 in day 4 at 5
No. 664 exposure increased to 2.0 in day 4 at 5
No. 666 exposure increased to 3.0 in day 4 at 5
No. 671 exposure increased to 1.0 in day 4 at 5
No. 674 exposure increased to 3.0 in day 4 at 5
No. 679 exposure increased to 2.0 in day 4 at 5
No. 689 exposure increased to 2.0 in day 4 at 5
No. 713 exposure increased to 2.0 in day 4 at 5
No. 718 exposure increased to 2.0 in day 4 at 5
No. 733 exposure increased to 2.0 in day 4 at 5
No. 734 exposure increased to 1.0 in day 4 at 5
No. 741 exposure increased to 2.0 in day 4 at 5
No. 745 exposure increased to 2.0 in day 4 at 5
No. 754 exposure increased to 2.0 in day 4 at 5
No. 755 exposure increased to 1.0 in day 4 at 5
No. 761 exposure increased to 3.0 in day 4 at 5
No. 770 exposure increased to 2.0 in day 4 at 5
No. 787 exposure increased to 3.0 in day 4 at 5
No. 791 exposure increased to 2.0 in day 4 at 5
No. 799 exposure increased to 1.0 in day 4 at 5
No. 811 exposure increased to 1.0 in day 4 at 5
No. 822 exposure increased to 1.0 in day 4 at 5
No. 835 exposure increased to 1.0 in day 4 at 5
No. 848 exposure increased to 1.0 in day 4 at 5
No. 850 exposure increased to 1.0 in day 4 at 5
No. 879 exposure increased to 1.0 in day 4 at 5
No. 880 exposure increased to 2.0 in day 4 at 5
No. 881 exposure increased to 3.0 in day 4 at 5
No. 892 exposure increased to 3.0 in day 4 at 5
No. 903 exposure increased to 2.0 in day 4 at 5
No. 913 exposure increased to 2.0 in day 4 at 5
No. 915 exposure increased to 3.0 in day 4 at 5
No. 919 exposure increased to 1.0 in day 4 at 5
No. 923 exposure increased to 1.0 in day 4 at 5
No. 924 exposure increased to 3.0 in day 4 at 5
No. 927 exposure increased to 1.0 in day 4 at 5
No. 936 exposure increased to 3.0 in day 4 at 5
No. 942 exposure increased to 3.0 in day 4 at 5
No. 952 exposure increased to 1.0 in day 4 at 5
No. 972 exposure increased to 2.0 in day 4 at 5
No. 974 exposure increased to 2.0 in day 4 at 5
No. 976 exposure increased to 3.0 in day 4 at 5
No. 977 exposure increased to 3.0 in day 4 at 5
No. 981 exposure increased to 1.0 in day 4 at 5
   21/10000 [..............................] - ETA: 31:11:20 - reward: 869.2781*When No. 12 infected, Exposure is 2.0 in day 4 at move 0
*When No. 22 infected, Exposure is 2.0 in day 4 at move 0
*When No. 215 infected, Exposure is 3.0 in day 4 at move 0
*When No. 375 infected, Exposure is 3.0 in day 4 at move 0
*When No. 498 infected, Exposure is 3.0 in day 4 at move 0
*When No. 578 infected, Exposure is 2.0 in day 4 at move 0
*When No. 613 infected, Exposure is 2.0 in day 4 at move 0
*When No. 689 infected, Exposure is 2.0 in day 4 at move 0
*When No. 787 infected, Exposure is 3.0 in day 4 at move 0
*When No. 881 infected, Exposure is 3.0 in day 4 at move 0
*When No. 903 infected, Exposure is 2.0 in day 4 at move 0
*When No. 915 infected, Exposure is 3.0 in day 4 at move 0
*When No. 977 infected, Exposure is 3.0 in day 4 at move 0
*When No. 127 infected, Exposure is 2.0 in day 4 at move 1
*When No. 275 infected, Exposure is 2.0 in day 4 at move 1
*When No. 308 infected, Exposure is 3.0 in day 4 at move 1
*When No. 314 infected, Exposure is 2.0 in day 4 at move 1
*When No. 337 infected, Exposure is 2.0 in day 4 at move 1
*When No. 657 infected, Exposure is 4.0 in day 4 at move 1
*When No. 660 infected, Exposure is 3.0 in day 4 at move 1
*When No. 674 infected, Exposure is 3.0 in day 4 at move 1
*When No. 679 infected, Exposure is 2.0 in day 4 at move 1
*When No. 761 infected, Exposure is 3.0 in day 4 at move 1
*When No. 972 infected, Exposure is 2.0 in day 4 at move 1
*When No. 13 infected, Exposure is 3.0 in day 4 at move 2
*When No. 609 infected, Exposure is 2.0 in day 4 at move 2
*When No. 745 infected, Exposure is 2.0 in day 4 at move 2
*When No. 924 infected, Exposure is 3.0 in day 4 at move 2
*When No. 372 infected, Exposure is 4.0 in day 4 at move 3
*When No. 424 infected, Exposure is 2.0 in day 4 at move 3
*When No. 637 infected, Exposure is 3.0 in day 4 at move 3
*When No. 229 infected, Exposure is 2.0 in day 4 at move 4
*When No. 231 infected, Exposure is 2.0 in day 4 at move 4
*When No. 304 infected, Exposure is 4.0 in day 4 at move 4
*When No. 488 infected, Exposure is 2.0 in day 4 at move 4
*When No. 648 infected, Exposure is 2.0 in day 4 at move 4
*When No. 754 infected, Exposure is 2.0 in day 4 at move 4
*When No. 976 infected, Exposure is 3.0 in day 4 at move 4
No. 5 exposure increased to 2.0 in day 4 at 5
No. 14 exposure increased to 1.0 in day 4 at 5
No. 21 exposure increased to 1.0 in day 4 at 5
No. 25 exposure increased to 3.0 in day 4 at 5
No. 51 exposure increased to 3.0 in day 4 at 5
No. 54 exposure increased to 3.0 in day 4 at 5
No. 57 exposure increased to 3.0 in day 4 at 5
No. 62 exposure increased to 2.0 in day 4 at 5
No. 67 exposure increased to 4.0 in day 4 at 5
No. 80 exposure increased to 2.0 in day 4 at 5
No. 82 exposure increased to 3.0 in day 4 at 5
No. 90 exposure increased to 2.0 in day 4 at 5
No. 99 exposure increased to 1.0 in day 4 at 5
No. 126 exposure increased to 1.0 in day 4 at 5
No. 136 exposure increased to 2.0 in day 4 at 5
No. 140 exposure increased to 1.0 in day 4 at 5
No. 149 exposure increased to 1.0 in day 4 at 5
No. 152 exposure increased to 1.0 in day 4 at 5
No. 158 exposure increased to 1.0 in day 4 at 5
No. 164 exposure increased to 2.0 in day 4 at 5
No. 182 exposure increased to 3.0 in day 4 at 5
No. 186 exposure increased to 1.0 in day 4 at 5
No. 189 exposure increased to 2.0 in day 4 at 5
No. 190 exposure increased to 1.0 in day 4 at 5
No. 195 exposure increased to 2.0 in day 4 at 5
No. 205 exposure increased to 3.0 in day 4 at 5
No. 211 exposure increased to 3.0 in day 4 at 5
*When No. 249 infected, Exposure is 2.0 in day 4 at move 5
No. 254 exposure increased to 3.0 in day 4 at 5
No. 258 exposure increased to 2.0 in day 4 at 5
No. 263 exposure increased to 1.0 in day 4 at 5
No. 283 exposure increased to 2.0 in day 4 at 5
No. 300 exposure increased to 1.0 in day 4 at 5
No. 306 exposure increased to 1.0 in day 4 at 5
No. 309 exposure increased to 3.0 in day 4 at 5
No. 315 exposure increased to 1.0 in day 4 at 5
No. 319 exposure increased to 3.0 in day 4 at 5
No. 333 exposure increased to 3.0 in day 4 at 5
No. 360 exposure increased to 3.0 in day 4 at 5
No. 365 exposure increased to 2.0 in day 4 at 5
No. 370 exposure increased to 2.0 in day 4 at 5
No. 373 exposure increased to 1.0 in day 4 at 5
No. 382 exposure increased to 3.0 in day 4 at 5
No. 383 exposure increased to 1.0 in day 4 at 5
No. 392 exposure increased to 1.0 in day 4 at 5
No. 401 exposure increased to 3.0 in day 4 at 5
No. 409 exposure increased to 3.0 in day 4 at 5
No. 419 exposure increased to 1.0 in day 4 at 5
No. 423 exposure increased to 1.0 in day 4 at 5
No. 425 exposure increased to 1.0 in day 4 at 5
No. 429 exposure increased to 1.0 in day 4 at 5
No. 437 exposure increased to 1.0 in day 4 at 5
No. 438 exposure increased to 3.0 in day 4 at 5
No. 445 exposure increased to 1.0 in day 4 at 5
No. 454 exposure increased to 3.0 in day 4 at 5
No. 455 exposure increased to 2.0 in day 4 at 5
No. 456 exposure increased to 3.0 in day 4 at 5
No. 467 exposure increased to 1.0 in day 4 at 5
No. 478 exposure increased to 1.0 in day 4 at 5
No. 487 exposure increased to 4.0 in day 4 at 5
No. 494 exposure increased to 1.0 in day 4 at 5
No. 496 exposure increased to 1.0 in day 4 at 5
No. 503 exposure increased to 2.0 in day 4 at 5
No. 504 exposure increased to 2.0 in day 4 at 5
No. 509 exposure increased to 1.0 in day 4 at 5
No. 510 exposure increased to 4.0 in day 4 at 5
No. 511 exposure increased to 3.0 in day 4 at 5
No. 517 exposure increased to 1.0 in day 4 at 5
No. 524 exposure increased to 2.0 in day 4 at 5
No. 525 exposure increased to 3.0 in day 4 at 5
*When No. 549 infected, Exposure is 2.0 in day 4 at move 5
No. 553 exposure increased to 1.0 in day 4 at 5
No. 557 exposure increased to 1.0 in day 4 at 5
No. 562 exposure increased to 1.0 in day 4 at 5
No. 571 exposure increased to 2.0 in day 4 at 5
No. 579 exposure increased to 2.0 in day 4 at 5
No. 582 exposure increased to 2.0 in day 4 at 5
No. 589 exposure increased to 1.0 in day 4 at 5
No. 591 exposure increased to 4.0 in day 4 at 5
*When No. 597 infected, Exposure is 2.0 in day 4 at move 5
No. 629 exposure increased to 1.0 in day 4 at 5
No. 650 exposure increased to 1.0 in day 4 at 5
No. 659 exposure increased to 1.0 in day 4 at 5
No. 661 exposure increased to 1.0 in day 4 at 5
No. 664 exposure increased to 3.0 in day 4 at 5
No. 666 exposure increased to 4.0 in day 4 at 5
No. 671 exposure increased to 2.0 in day 4 at 5
No. 675 exposure increased to 1.0 in day 4 at 5
No. 698 exposure increased to 1.0 in day 4 at 5
No. 702 exposure increased to 1.0 in day 4 at 5
No. 713 exposure increased to 3.0 in day 4 at 5
No. 716 exposure increased to 1.0 in day 4 at 5
*When No. 718 infected, Exposure is 2.0 in day 4 at move 5
No. 732 exposure increased to 1.0 in day 4 at 5
*When No. 733 infected, Exposure is 2.0 in day 4 at move 5
No. 734 exposure increased to 2.0 in day 4 at 5
No. 741 exposure increased to 3.0 in day 4 at 5
No. 743 exposure increased to 2.0 in day 4 at 5
No. 755 exposure increased to 2.0 in day 4 at 5
No. 765 exposure increased to 1.0 in day 4 at 5
No. 770 exposure increased to 3.0 in day 4 at 5
No. 777 exposure increased to 1.0 in day 4 at 5
No. 791 exposure increased to 3.0 in day 4 at 5
No. 799 exposure increased to 2.0 in day 4 at 5
No. 811 exposure increased to 2.0 in day 4 at 5
No. 822 exposure increased to 2.0 in day 4 at 5
No. 835 exposure increased to 2.0 in day 4 at 5
No. 837 exposure increased to 1.0 in day 4 at 5
No. 848 exposure increased to 2.0 in day 4 at 5
No. 850 exposure increased to 2.0 in day 4 at 5
No. 879 exposure increased to 2.0 in day 4 at 5
No. 880 exposure increased to 3.0 in day 4 at 5
No. 892 exposure increased to 4.0 in day 4 at 5
No. 897 exposure increased to 1.0 in day 4 at 5
*When No. 913 infected, Exposure is 2.0 in day 4 at move 5
No. 918 exposure increased to 2.0 in day 4 at 5
No. 919 exposure increased to 2.0 in day 4 at 5
No. 923 exposure increased to 2.0 in day 4 at 5
No. 927 exposure increased to 2.0 in day 4 at 5
No. 936 exposure increased to 4.0 in day 4 at 5
No. 942 exposure increased to 4.0 in day 4 at 5
No. 944 exposure increased to 1.0 in day 4 at 5
No. 947 exposure increased to 1.0 in day 4 at 5
No. 952 exposure increased to 2.0 in day 4 at 5
*When No. 974 infected, Exposure is 2.0 in day 4 at move 5
No. 981 exposure increased to 2.0 in day 4 at 5
No. 991 exposure increased to 1.0 in day 4 at 5
   22/10000 [..............................] - ETA: 31:44:17 - reward: 862.2855*When No. 62 infected, Exposure is 2.0 in day 4 at move 0
*When No. 195 infected, Exposure is 2.0 in day 4 at move 0
*When No. 319 infected, Exposure is 3.0 in day 4 at move 0
*When No. 333 infected, Exposure is 3.0 in day 4 at move 0
*When No. 360 infected, Exposure is 3.0 in day 4 at move 0
*When No. 409 infected, Exposure is 3.0 in day 4 at move 0
*When No. 510 infected, Exposure is 4.0 in day 4 at move 0
*When No. 511 infected, Exposure is 3.0 in day 4 at move 0
*When No. 591 infected, Exposure is 4.0 in day 4 at move 0
*When No. 666 infected, Exposure is 4.0 in day 4 at move 0
*When No. 734 infected, Exposure is 2.0 in day 4 at move 0
*When No. 791 infected, Exposure is 3.0 in day 4 at move 0
*When No. 880 infected, Exposure is 3.0 in day 4 at move 0
*When No. 892 infected, Exposure is 4.0 in day 4 at move 0
*When No. 923 infected, Exposure is 2.0 in day 4 at move 0
No. 5 exposure increased to 3.0 in day 4 at 1
No. 14 exposure increased to 2.0 in day 4 at 1
No. 21 exposure increased to 2.0 in day 4 at 1
No. 25 exposure increased to 4.0 in day 4 at 1
No. 34 exposure increased to 1.0 in day 4 at 1
*When No. 51 infected, Exposure is 3.0 in day 4 at move 1
No. 54 exposure increased to 4.0 in day 4 at 1
*When No. 57 infected, Exposure is 3.0 in day 4 at move 1
No. 58 exposure increased to 1.0 in day 4 at 1
No. 67 exposure increased to 5.0 in day 4 at 1
No. 78 exposure increased to 1.0 in day 4 at 1
No. 80 exposure increased to 3.0 in day 4 at 1
*When No. 82 infected, Exposure is 3.0 in day 4 at move 1
No. 90 exposure increased to 3.0 in day 4 at 1
No. 99 exposure increased to 2.0 in day 4 at 1
No. 126 exposure increased to 2.0 in day 4 at 1
*When No. 136 infected, Exposure is 2.0 in day 4 at move 1
No. 140 exposure increased to 2.0 in day 4 at 1
No. 148 exposure increased to 2.0 in day 4 at 1
No. 149 exposure increased to 2.0 in day 4 at 1
No. 150 exposure increased to 2.0 in day 4 at 1
No. 152 exposure increased to 2.0 in day 4 at 1
No. 158 exposure increased to 2.0 in day 4 at 1
No. 164 exposure increased to 3.0 in day 4 at 1
No. 180 exposure increased to 1.0 in day 4 at 1
No. 182 exposure increased to 4.0 in day 4 at 1
No. 186 exposure increased to 2.0 in day 4 at 1
No. 189 exposure increased to 3.0 in day 4 at 1
No. 190 exposure increased to 2.0 in day 4 at 1
No. 205 exposure increased to 4.0 in day 4 at 1
No. 211 exposure increased to 4.0 in day 4 at 1
No. 254 exposure increased to 4.0 in day 4 at 1
No. 258 exposure increased to 3.0 in day 4 at 1
No. 262 exposure increased to 1.0 in day 4 at 1
No. 263 exposure increased to 2.0 in day 4 at 1
No. 283 exposure increased to 3.0 in day 4 at 1
No. 300 exposure increased to 2.0 in day 4 at 1
No. 306 exposure increased to 2.0 in day 4 at 1
*When No. 309 infected, Exposure is 3.0 in day 4 at move 1
No. 315 exposure increased to 2.0 in day 4 at 1
No. 349 exposure increased to 1.0 in day 4 at 1
No. 365 exposure increased to 3.0 in day 4 at 1
No. 370 exposure increased to 3.0 in day 4 at 1
No. 373 exposure increased to 2.0 in day 4 at 1
No. 377 exposure increased to 1.0 in day 4 at 1
No. 380 exposure increased to 1.0 in day 4 at 1
No. 382 exposure increased to 4.0 in day 4 at 1
No. 383 exposure increased to 2.0 in day 4 at 1
No. 392 exposure increased to 2.0 in day 4 at 1
No. 401 exposure increased to 4.0 in day 4 at 1
No. 419 exposure increased to 2.0 in day 4 at 1
No. 423 exposure increased to 2.0 in day 4 at 1
No. 425 exposure increased to 2.0 in day 4 at 1
No. 429 exposure increased to 2.0 in day 4 at 1
No. 430 exposure increased to 1.0 in day 4 at 1
No. 437 exposure increased to 2.0 in day 4 at 1
No. 438 exposure increased to 4.0 in day 4 at 1
No. 445 exposure increased to 2.0 in day 4 at 1
No. 453 exposure increased to 2.0 in day 4 at 1
No. 454 exposure increased to 4.0 in day 4 at 1
No. 455 exposure increased to 3.0 in day 4 at 1
No. 456 exposure increased to 4.0 in day 4 at 1
No. 467 exposure increased to 2.0 in day 4 at 1
No. 478 exposure increased to 2.0 in day 4 at 1
*When No. 487 infected, Exposure is 4.0 in day 4 at move 1
No. 490 exposure increased to 2.0 in day 4 at 1
No. 494 exposure increased to 2.0 in day 4 at 1
No. 496 exposure increased to 2.0 in day 4 at 1
No. 499 exposure increased to 1.0 in day 4 at 1
No. 503 exposure increased to 3.0 in day 4 at 1
*When No. 504 infected, Exposure is 2.0 in day 4 at move 1
No. 509 exposure increased to 2.0 in day 4 at 1
No. 517 exposure increased to 2.0 in day 4 at 1
No. 524 exposure increased to 3.0 in day 4 at 1
No. 525 exposure increased to 4.0 in day 4 at 1
No. 536 exposure increased to 2.0 in day 4 at 1
No. 553 exposure increased to 2.0 in day 4 at 1
No. 554 exposure increased to 1.0 in day 4 at 1
No. 557 exposure increased to 2.0 in day 4 at 1
No. 562 exposure increased to 2.0 in day 4 at 1
*When No. 571 infected, Exposure is 2.0 in day 4 at move 1
No. 579 exposure increased to 3.0 in day 4 at 1
No. 582 exposure increased to 3.0 in day 4 at 1
No. 589 exposure increased to 2.0 in day 4 at 1
No. 618 exposure increased to 1.0 in day 4 at 1
No. 629 exposure increased to 2.0 in day 4 at 1
No. 647 exposure increased to 1.0 in day 4 at 1
No. 650 exposure increased to 2.0 in day 4 at 1
No. 659 exposure increased to 2.0 in day 4 at 1
No. 661 exposure increased to 2.0 in day 4 at 1
No. 662 exposure increased to 2.0 in day 4 at 1
No. 664 exposure increased to 4.0 in day 4 at 1
*When No. 671 infected, Exposure is 2.0 in day 4 at move 1
No. 675 exposure increased to 2.0 in day 4 at 1
No. 698 exposure increased to 2.0 in day 4 at 1
No. 701 exposure increased to 2.0 in day 4 at 1
No. 702 exposure increased to 2.0 in day 4 at 1
*When No. 713 infected, Exposure is 3.0 in day 4 at move 1
No. 716 exposure increased to 2.0 in day 4 at 1
No. 732 exposure increased to 2.0 in day 4 at 1
No. 741 exposure increased to 4.0 in day 4 at 1
No. 743 exposure increased to 3.0 in day 4 at 1
No. 755 exposure increased to 3.0 in day 4 at 1
No. 765 exposure increased to 2.0 in day 4 at 1
No. 770 exposure increased to 4.0 in day 4 at 1
No. 777 exposure increased to 2.0 in day 4 at 1
No. 799 exposure increased to 3.0 in day 4 at 1
No. 800 exposure increased to 1.0 in day 4 at 1
No. 811 exposure increased to 3.0 in day 4 at 1
No. 822 exposure increased to 3.0 in day 4 at 1
No. 824 exposure increased to 1.0 in day 4 at 1
No. 835 exposure increased to 3.0 in day 4 at 1
No. 837 exposure increased to 2.0 in day 4 at 1
No. 848 exposure increased to 3.0 in day 4 at 1
No. 850 exposure increased to 3.0 in day 4 at 1
No. 870 exposure increased to 1.0 in day 4 at 1
No. 879 exposure increased to 3.0 in day 4 at 1
No. 885 exposure increased to 2.0 in day 4 at 1
No. 897 exposure increased to 2.0 in day 4 at 1
No. 901 exposure increased to 2.0 in day 4 at 1
No. 918 exposure increased to 3.0 in day 4 at 1
No. 919 exposure increased to 3.0 in day 4 at 1
No. 927 exposure increased to 3.0 in day 4 at 1
*When No. 936 infected, Exposure is 4.0 in day 4 at move 1
*When No. 942 infected, Exposure is 4.0 in day 4 at move 1
No. 944 exposure increased to 2.0 in day 4 at 1
No. 947 exposure increased to 2.0 in day 4 at 1
No. 952 exposure increased to 3.0 in day 4 at 1
No. 954 exposure increased to 1.0 in day 4 at 1
No. 981 exposure increased to 3.0 in day 4 at 1
No. 991 exposure increased to 2.0 in day 4 at 1
   23/10000 [..............................] - ETA: 30:59:11 - reward: 854.5261*When No. 25 infected, Exposure is 4.0 in day 4 at move 0
*When No. 182 infected, Exposure is 4.0 in day 4 at move 0
*When No. 254 infected, Exposure is 4.0 in day 4 at move 0
*When No. 306 infected, Exposure is 2.0 in day 4 at move 0
*When No. 383 infected, Exposure is 2.0 in day 4 at move 0
*When No. 401 infected, Exposure is 4.0 in day 4 at move 0
*When No. 453 infected, Exposure is 2.0 in day 4 at move 0
*When No. 454 infected, Exposure is 4.0 in day 4 at move 0
*When No. 455 infected, Exposure is 3.0 in day 4 at move 0
*When No. 467 infected, Exposure is 2.0 in day 4 at move 0
*When No. 524 infected, Exposure is 3.0 in day 4 at move 0
*When No. 664 infected, Exposure is 4.0 in day 4 at move 0
*When No. 770 infected, Exposure is 4.0 in day 4 at move 0
*When No. 850 infected, Exposure is 3.0 in day 4 at move 0
*When No. 901 infected, Exposure is 2.0 in day 4 at move 0
*When No. 944 infected, Exposure is 2.0 in day 4 at move 0
*When No. 67 infected, Exposure is 5.0 in day 4 at move 1
*When No. 189 infected, Exposure is 3.0 in day 4 at move 1
*When No. 211 infected, Exposure is 4.0 in day 4 at move 1
*When No. 300 infected, Exposure is 2.0 in day 4 at move 1
*When No. 438 infected, Exposure is 4.0 in day 4 at move 1
*When No. 525 infected, Exposure is 4.0 in day 4 at move 1
*When No. 659 infected, Exposure is 2.0 in day 4 at move 1
*When No. 799 infected, Exposure is 3.0 in day 4 at move 1
*When No. 848 infected, Exposure is 3.0 in day 4 at move 1
*When No. 919 infected, Exposure is 3.0 in day 4 at move 1
*When No. 927 infected, Exposure is 3.0 in day 4 at move 1
*When No. 952 infected, Exposure is 3.0 in day 4 at move 1
*When No. 5 infected, Exposure is 3.0 in day 4 at move 2
*When No. 14 infected, Exposure is 2.0 in day 4 at move 2
*When No. 54 infected, Exposure is 4.0 in day 4 at move 2
*When No. 152 infected, Exposure is 2.0 in day 4 at move 2
*When No. 258 infected, Exposure is 3.0 in day 4 at move 2
*When No. 370 infected, Exposure is 3.0 in day 4 at move 2
*When No. 456 infected, Exposure is 4.0 in day 4 at move 2
*When No. 536 infected, Exposure is 2.0 in day 4 at move 2
*When No. 716 infected, Exposure is 2.0 in day 4 at move 2
*When No. 741 infected, Exposure is 4.0 in day 4 at move 2
*When No. 777 infected, Exposure is 2.0 in day 4 at move 2
*When No. 811 infected, Exposure is 3.0 in day 4 at move 2
*When No. 835 infected, Exposure is 3.0 in day 4 at move 2
*When No. 981 infected, Exposure is 3.0 in day 4 at move 2
*When No. 126 infected, Exposure is 2.0 in day 4 at move 3
*When No. 150 infected, Exposure is 2.0 in day 4 at move 3
*When No. 205 infected, Exposure is 4.0 in day 4 at move 3
*When No. 365 infected, Exposure is 3.0 in day 4 at move 3
*When No. 419 infected, Exposure is 2.0 in day 4 at move 3
*When No. 478 infected, Exposure is 2.0 in day 4 at move 3
*When No. 743 infected, Exposure is 3.0 in day 4 at move 3
*When No. 755 infected, Exposure is 3.0 in day 4 at move 3
*When No. 149 infected, Exposure is 2.0 in day 4 at move 4
*When No. 283 infected, Exposure is 3.0 in day 4 at move 4
*When No. 382 infected, Exposure is 4.0 in day 4 at move 4
*When No. 490 infected, Exposure is 2.0 in day 4 at move 4
*When No. 662 infected, Exposure is 2.0 in day 4 at move 4
*When No. 991 infected, Exposure is 2.0 in day 4 at move 4
No. 15 exposure increased to 1.0 in day 4 at 5
No. 21 exposure increased to 3.0 in day 4 at 5
No. 31 exposure increased to 1.0 in day 4 at 5
No. 34 exposure increased to 2.0 in day 4 at 5
No. 38 exposure increased to 2.0 in day 4 at 5
No. 46 exposure increased to 1.0 in day 4 at 5
No. 49 exposure increased to 1.0 in day 4 at 5
No. 56 exposure increased to 1.0 in day 4 at 5
No. 58 exposure increased to 2.0 in day 4 at 5
No. 65 exposure increased to 1.0 in day 4 at 5
No. 72 exposure increased to 1.0 in day 4 at 5
No. 75 exposure increased to 1.0 in day 4 at 5
No. 78 exposure increased to 2.0 in day 4 at 5
No. 80 exposure increased to 4.0 in day 4 at 5
No. 86 exposure increased to 2.0 in day 4 at 5
No. 90 exposure increased to 4.0 in day 4 at 5
No. 97 exposure increased to 1.0 in day 4 at 5
No. 98 exposure increased to 1.0 in day 4 at 5
No. 99 exposure increased to 3.0 in day 4 at 5
No. 120 exposure increased to 1.0 in day 4 at 5
No. 124 exposure increased to 1.0 in day 4 at 5
No. 129 exposure increased to 1.0 in day 4 at 5
No. 140 exposure increased to 3.0 in day 4 at 5
No. 148 exposure increased to 3.0 in day 4 at 5
No. 158 exposure increased to 3.0 in day 4 at 5
No. 162 exposure increased to 2.0 in day 4 at 5
*When No. 164 infected, Exposure is 3.0 in day 4 at move 5
No. 175 exposure increased to 1.0 in day 4 at 5
No. 180 exposure increased to 2.0 in day 4 at 5
No. 186 exposure increased to 3.0 in day 4 at 5
No. 190 exposure increased to 3.0 in day 4 at 5
No. 213 exposure increased to 2.0 in day 4 at 5
No. 219 exposure increased to 1.0 in day 4 at 5
No. 223 exposure increased to 1.0 in day 4 at 5
No. 232 exposure increased to 1.0 in day 4 at 5
No. 236 exposure increased to 1.0 in day 4 at 5
No. 244 exposure increased to 1.0 in day 4 at 5
No. 262 exposure increased to 2.0 in day 4 at 5
No. 263 exposure increased to 3.0 in day 4 at 5
No. 285 exposure increased to 2.0 in day 4 at 5
No. 288 exposure increased to 2.0 in day 4 at 5
No. 305 exposure increased to 2.0 in day 4 at 5
No. 307 exposure increased to 1.0 in day 4 at 5
No. 315 exposure increased to 3.0 in day 4 at 5
No. 322 exposure increased to 1.0 in day 4 at 5
No. 329 exposure increased to 1.0 in day 4 at 5
No. 349 exposure increased to 2.0 in day 4 at 5
No. 351 exposure increased to 2.0 in day 4 at 5
No. 358 exposure increased to 2.0 in day 4 at 5
No. 366 exposure increased to 1.0 in day 4 at 5
No. 368 exposure increased to 2.0 in day 4 at 5
No. 373 exposure increased to 3.0 in day 4 at 5
No. 377 exposure increased to 2.0 in day 4 at 5
No. 380 exposure increased to 2.0 in day 4 at 5
No. 381 exposure increased to 2.0 in day 4 at 5
No. 392 exposure increased to 3.0 in day 4 at 5
No. 415 exposure increased to 1.0 in day 4 at 5
No. 417 exposure increased to 1.0 in day 4 at 5
No. 423 exposure increased to 3.0 in day 4 at 5
No. 425 exposure increased to 3.0 in day 4 at 5
No. 429 exposure increased to 3.0 in day 4 at 5
No. 430 exposure increased to 2.0 in day 4 at 5
No. 437 exposure increased to 3.0 in day 4 at 5
No. 439 exposure increased to 1.0 in day 4 at 5
No. 445 exposure increased to 3.0 in day 4 at 5
No. 463 exposure increased to 1.0 in day 4 at 5
No. 471 exposure increased to 1.0 in day 4 at 5
No. 494 exposure increased to 3.0 in day 4 at 5
No. 495 exposure increased to 1.0 in day 4 at 5
No. 496 exposure increased to 3.0 in day 4 at 5
No. 497 exposure increased to 1.0 in day 4 at 5
No. 499 exposure increased to 2.0 in day 4 at 5
No. 503 exposure increased to 4.0 in day 4 at 5
No. 509 exposure increased to 3.0 in day 4 at 5
No. 515 exposure increased to 1.0 in day 4 at 5
No. 516 exposure increased to 1.0 in day 4 at 5
No. 517 exposure increased to 3.0 in day 4 at 5
No. 539 exposure increased to 2.0 in day 4 at 5
No. 541 exposure increased to 1.0 in day 4 at 5
No. 553 exposure increased to 3.0 in day 4 at 5
No. 554 exposure increased to 2.0 in day 4 at 5
No. 557 exposure increased to 3.0 in day 4 at 5
No. 562 exposure increased to 3.0 in day 4 at 5
No. 566 exposure increased to 1.0 in day 4 at 5
No. 573 exposure increased to 1.0 in day 4 at 5
No. 579 exposure increased to 4.0 in day 4 at 5
*When No. 582 infected, Exposure is 3.0 in day 4 at move 5
No. 585 exposure increased to 1.0 in day 4 at 5
No. 586 exposure increased to 1.0 in day 4 at 5
No. 589 exposure increased to 3.0 in day 4 at 5
No. 592 exposure increased to 1.0 in day 4 at 5
No. 601 exposure increased to 1.0 in day 4 at 5
No. 610 exposure increased to 1.0 in day 4 at 5
No. 618 exposure increased to 2.0 in day 4 at 5
No. 629 exposure increased to 3.0 in day 4 at 5
No. 632 exposure increased to 1.0 in day 4 at 5
No. 634 exposure increased to 2.0 in day 4 at 5
No. 640 exposure increased to 1.0 in day 4 at 5
No. 646 exposure increased to 1.0 in day 4 at 5
No. 647 exposure increased to 2.0 in day 4 at 5
No. 649 exposure increased to 1.0 in day 4 at 5
No. 650 exposure increased to 3.0 in day 4 at 5
No. 653 exposure increased to 1.0 in day 4 at 5
No. 658 exposure increased to 1.0 in day 4 at 5
No. 661 exposure increased to 3.0 in day 4 at 5
No. 675 exposure increased to 3.0 in day 4 at 5
No. 684 exposure increased to 1.0 in day 4 at 5
No. 698 exposure increased to 3.0 in day 4 at 5
No. 701 exposure increased to 3.0 in day 4 at 5
No. 702 exposure increased to 3.0 in day 4 at 5
No. 719 exposure increased to 1.0 in day 4 at 5
No. 723 exposure increased to 1.0 in day 4 at 5
No. 727 exposure increased to 1.0 in day 4 at 5
No. 732 exposure increased to 3.0 in day 4 at 5
No. 736 exposure increased to 2.0 in day 4 at 5
No. 742 exposure increased to 2.0 in day 4 at 5
No. 765 exposure increased to 3.0 in day 4 at 5
No. 768 exposure increased to 1.0 in day 4 at 5
No. 771 exposure increased to 2.0 in day 4 at 5
No. 800 exposure increased to 2.0 in day 4 at 5
No. 804 exposure increased to 1.0 in day 4 at 5
No. 805 exposure increased to 1.0 in day 4 at 5
No. 815 exposure increased to 1.0 in day 4 at 5
No. 820 exposure increased to 2.0 in day 4 at 5
*When No. 822 infected, Exposure is 3.0 in day 4 at move 5
No. 824 exposure increased to 2.0 in day 4 at 5
No. 831 exposure increased to 1.0 in day 4 at 5
No. 836 exposure increased to 1.0 in day 4 at 5
No. 837 exposure increased to 3.0 in day 4 at 5
No. 840 exposure increased to 1.0 in day 4 at 5
No. 853 exposure increased to 1.0 in day 4 at 5
No. 859 exposure increased to 1.0 in day 4 at 5
No. 863 exposure increased to 1.0 in day 4 at 5
No. 870 exposure increased to 2.0 in day 4 at 5
No. 879 exposure increased to 4.0 in day 4 at 5
No. 885 exposure increased to 3.0 in day 4 at 5
No. 897 exposure increased to 3.0 in day 4 at 5
No. 916 exposure increased to 1.0 in day 4 at 5
No. 918 exposure increased to 4.0 in day 4 at 5
No. 940 exposure increased to 1.0 in day 4 at 5
No. 947 exposure increased to 3.0 in day 4 at 5
No. 949 exposure increased to 1.0 in day 4 at 5
No. 954 exposure increased to 2.0 in day 4 at 5
No. 961 exposure increased to 1.0 in day 4 at 5
No. 996 exposure increased to 1.0 in day 4 at 5
No. 997 exposure increased to 2.0 in day 4 at 5
   24/10000 [..............................] - ETA: 31:24:01 - reward: 845.6142*When No. 90 infected, Exposure is 4.0 in day 4 at move 0
*When No. 148 infected, Exposure is 3.0 in day 4 at move 0
*When No. 186 infected, Exposure is 3.0 in day 4 at move 0
*When No. 381 infected, Exposure is 2.0 in day 4 at move 0
*When No. 392 infected, Exposure is 3.0 in day 4 at move 0
*When No. 496 infected, Exposure is 3.0 in day 4 at move 0
*When No. 499 infected, Exposure is 2.0 in day 4 at move 0
*When No. 503 infected, Exposure is 4.0 in day 4 at move 0
*When No. 557 infected, Exposure is 3.0 in day 4 at move 0
*When No. 765 infected, Exposure is 3.0 in day 4 at move 0
*When No. 21 infected, Exposure is 3.0 in day 4 at move 1
*When No. 58 infected, Exposure is 2.0 in day 4 at move 1
*When No. 445 infected, Exposure is 3.0 in day 4 at move 1
*When No. 554 infected, Exposure is 2.0 in day 4 at move 1
*When No. 562 infected, Exposure is 3.0 in day 4 at move 1
*When No. 589 infected, Exposure is 3.0 in day 4 at move 1
*When No. 837 infected, Exposure is 3.0 in day 4 at move 1
*When No. 954 infected, Exposure is 2.0 in day 4 at move 1
*When No. 140 infected, Exposure is 3.0 in day 4 at move 2
*When No. 349 infected, Exposure is 2.0 in day 4 at move 2
*When No. 425 infected, Exposure is 3.0 in day 4 at move 2
*When No. 539 infected, Exposure is 2.0 in day 4 at move 2
*When No. 579 infected, Exposure is 4.0 in day 4 at move 2
*When No. 634 infected, Exposure is 2.0 in day 4 at move 2
*When No. 650 infected, Exposure is 3.0 in day 4 at move 2
*When No. 675 infected, Exposure is 3.0 in day 4 at move 2
*When No. 879 infected, Exposure is 4.0 in day 4 at move 2
*When No. 34 infected, Exposure is 2.0 in day 4 at move 3
*When No. 80 infected, Exposure is 4.0 in day 4 at move 3
*When No. 430 infected, Exposure is 2.0 in day 4 at move 3
*When No. 702 infected, Exposure is 3.0 in day 4 at move 3
*When No. 800 infected, Exposure is 2.0 in day 4 at move 3
*When No. 824 infected, Exposure is 2.0 in day 4 at move 3
*When No. 870 infected, Exposure is 2.0 in day 4 at move 3
*When No. 947 infected, Exposure is 3.0 in day 4 at move 3
*When No. 263 infected, Exposure is 3.0 in day 4 at move 4
*When No. 429 infected, Exposure is 3.0 in day 4 at move 4
*When No. 517 infected, Exposure is 3.0 in day 4 at move 4
*When No. 629 infected, Exposure is 3.0 in day 4 at move 4
*When No. 661 infected, Exposure is 3.0 in day 4 at move 4
*When No. 701 infected, Exposure is 3.0 in day 4 at move 4
*When No. 918 infected, Exposure is 4.0 in day 4 at move 4
No. 1 exposure increased to 2.0 in day 4 at 5
No. 7 exposure increased to 1.0 in day 4 at 5
No. 11 exposure increased to 2.0 in day 4 at 5
No. 15 exposure increased to 2.0 in day 4 at 5
No. 17 exposure increased to 1.0 in day 4 at 5
No. 31 exposure increased to 2.0 in day 4 at 5
No. 38 exposure increased to 3.0 in day 4 at 5
No. 43 exposure increased to 2.0 in day 4 at 5
No. 46 exposure increased to 2.0 in day 4 at 5
No. 47 exposure increased to 2.0 in day 4 at 5
No. 49 exposure increased to 2.0 in day 4 at 5
No. 56 exposure increased to 2.0 in day 4 at 5
No. 60 exposure increased to 1.0 in day 4 at 5
No. 65 exposure increased to 2.0 in day 4 at 5
No. 72 exposure increased to 2.0 in day 4 at 5
No. 75 exposure increased to 2.0 in day 4 at 5
No. 78 exposure increased to 3.0 in day 4 at 5
No. 86 exposure increased to 3.0 in day 4 at 5
No. 97 exposure increased to 2.0 in day 4 at 5
No. 98 exposure increased to 2.0 in day 4 at 5
No. 99 exposure increased to 4.0 in day 4 at 5
No. 120 exposure increased to 2.0 in day 4 at 5
No. 124 exposure increased to 2.0 in day 4 at 5
No. 129 exposure increased to 2.0 in day 4 at 5
No. 147 exposure increased to 1.0 in day 4 at 5
No. 154 exposure increased to 1.0 in day 4 at 5
No. 158 exposure increased to 4.0 in day 4 at 5
No. 162 exposure increased to 3.0 in day 4 at 5
No. 175 exposure increased to 2.0 in day 4 at 5
No. 178 exposure increased to 1.0 in day 4 at 5
No. 180 exposure increased to 3.0 in day 4 at 5
No. 184 exposure increased to 1.0 in day 4 at 5
*When No. 190 infected, Exposure is 3.0 in day 4 at move 5
No. 199 exposure increased to 1.0 in day 4 at 5
No. 213 exposure increased to 3.0 in day 4 at 5
No. 219 exposure increased to 2.0 in day 4 at 5
No. 221 exposure increased to 1.0 in day 4 at 5
No. 223 exposure increased to 2.0 in day 4 at 5
No. 232 exposure increased to 2.0 in day 4 at 5
No. 236 exposure increased to 2.0 in day 4 at 5
No. 244 exposure increased to 2.0 in day 4 at 5
No. 262 exposure increased to 3.0 in day 4 at 5
No. 269 exposure increased to 1.0 in day 4 at 5
No. 271 exposure increased to 1.0 in day 4 at 5
No. 285 exposure increased to 3.0 in day 4 at 5
*When No. 288 infected, Exposure is 2.0 in day 4 at move 5
No. 302 exposure increased to 1.0 in day 4 at 5
No. 305 exposure increased to 3.0 in day 4 at 5
No. 307 exposure increased to 2.0 in day 4 at 5
No. 315 exposure increased to 4.0 in day 4 at 5
No. 321 exposure increased to 1.0 in day 4 at 5
No. 322 exposure increased to 2.0 in day 4 at 5
No. 328 exposure increased to 1.0 in day 4 at 5
No. 329 exposure increased to 2.0 in day 4 at 5
No. 351 exposure increased to 3.0 in day 4 at 5
No. 358 exposure increased to 3.0 in day 4 at 5
No. 366 exposure increased to 2.0 in day 4 at 5
No. 368 exposure increased to 3.0 in day 4 at 5
*When No. 373 infected, Exposure is 3.0 in day 4 at move 5
No. 377 exposure increased to 3.0 in day 4 at 5
No. 380 exposure increased to 3.0 in day 4 at 5
No. 404 exposure increased to 1.0 in day 4 at 5
No. 408 exposure increased to 1.0 in day 4 at 5
No. 415 exposure increased to 2.0 in day 4 at 5
No. 417 exposure increased to 2.0 in day 4 at 5
No. 423 exposure increased to 4.0 in day 4 at 5
No. 427 exposure increased to 1.0 in day 4 at 5
No. 437 exposure increased to 4.0 in day 4 at 5
No. 439 exposure increased to 2.0 in day 4 at 5
No. 447 exposure increased to 2.0 in day 4 at 5
No. 463 exposure increased to 2.0 in day 4 at 5
No. 464 exposure increased to 1.0 in day 4 at 5
No. 471 exposure increased to 2.0 in day 4 at 5
No. 484 exposure increased to 1.0 in day 4 at 5
No. 494 exposure increased to 4.0 in day 4 at 5
No. 495 exposure increased to 2.0 in day 4 at 5
No. 497 exposure increased to 2.0 in day 4 at 5
No. 509 exposure increased to 4.0 in day 4 at 5
No. 512 exposure increased to 1.0 in day 4 at 5
No. 515 exposure increased to 2.0 in day 4 at 5
No. 516 exposure increased to 2.0 in day 4 at 5
No. 541 exposure increased to 2.0 in day 4 at 5
No. 546 exposure increased to 1.0 in day 4 at 5
No. 553 exposure increased to 4.0 in day 4 at 5
No. 556 exposure increased to 1.0 in day 4 at 5
No. 559 exposure increased to 1.0 in day 4 at 5
No. 566 exposure increased to 2.0 in day 4 at 5
No. 573 exposure increased to 2.0 in day 4 at 5
No. 583 exposure increased to 2.0 in day 4 at 5
No. 585 exposure increased to 2.0 in day 4 at 5
No. 586 exposure increased to 2.0 in day 4 at 5
No. 592 exposure increased to 2.0 in day 4 at 5
No. 601 exposure increased to 2.0 in day 4 at 5
No. 606 exposure increased to 1.0 in day 4 at 5
No. 610 exposure increased to 2.0 in day 4 at 5
No. 618 exposure increased to 3.0 in day 4 at 5
No. 632 exposure increased to 2.0 in day 4 at 5
No. 640 exposure increased to 2.0 in day 4 at 5
No. 645 exposure increased to 2.0 in day 4 at 5
No. 646 exposure increased to 2.0 in day 4 at 5
No. 647 exposure increased to 3.0 in day 4 at 5
No. 649 exposure increased to 2.0 in day 4 at 5
No. 653 exposure increased to 2.0 in day 4 at 5
No. 658 exposure increased to 2.0 in day 4 at 5
No. 667 exposure increased to 1.0 in day 4 at 5
No. 684 exposure increased to 2.0 in day 4 at 5
No. 698 exposure increased to 4.0 in day 4 at 5
No. 714 exposure increased to 1.0 in day 4 at 5
No. 719 exposure increased to 2.0 in day 4 at 5
No. 723 exposure increased to 2.0 in day 4 at 5
No. 727 exposure increased to 2.0 in day 4 at 5
*When No. 732 infected, Exposure is 3.0 in day 4 at move 5
No. 736 exposure increased to 3.0 in day 4 at 5
No. 742 exposure increased to 3.0 in day 4 at 5
No. 757 exposure increased to 1.0 in day 4 at 5
No. 762 exposure increased to 1.0 in day 4 at 5
No. 766 exposure increased to 1.0 in day 4 at 5
No. 768 exposure increased to 2.0 in day 4 at 5
No. 771 exposure increased to 3.0 in day 4 at 5
No. 774 exposure increased to 1.0 in day 4 at 5
No. 781 exposure increased to 1.0 in day 4 at 5
No. 786 exposure increased to 1.0 in day 4 at 5
No. 796 exposure increased to 1.0 in day 4 at 5
No. 801 exposure increased to 1.0 in day 4 at 5
No. 804 exposure increased to 2.0 in day 4 at 5
No. 805 exposure increased to 2.0 in day 4 at 5
No. 815 exposure increased to 2.0 in day 4 at 5
No. 820 exposure increased to 3.0 in day 4 at 5
No. 831 exposure increased to 2.0 in day 4 at 5
No. 836 exposure increased to 2.0 in day 4 at 5
No. 840 exposure increased to 2.0 in day 4 at 5
No. 853 exposure increased to 2.0 in day 4 at 5
No. 859 exposure increased to 2.0 in day 4 at 5
No. 862 exposure increased to 1.0 in day 4 at 5
No. 863 exposure increased to 2.0 in day 4 at 5
No. 885 exposure increased to 4.0 in day 4 at 5
No. 897 exposure increased to 4.0 in day 4 at 5
No. 902 exposure increased to 1.0 in day 4 at 5
No. 916 exposure increased to 2.0 in day 4 at 5
No. 925 exposure increased to 1.0 in day 4 at 5
No. 928 exposure increased to 1.0 in day 4 at 5
No. 930 exposure increased to 1.0 in day 4 at 5
No. 940 exposure increased to 2.0 in day 4 at 5
No. 949 exposure increased to 2.0 in day 4 at 5
No. 950 exposure increased to 1.0 in day 4 at 5
No. 961 exposure increased to 2.0 in day 4 at 5
No. 963 exposure increased to 1.0 in day 4 at 5
No. 970 exposure increased to 1.0 in day 4 at 5
No. 994 exposure increased to 1.0 in day 4 at 5
No. 996 exposure increased to 2.0 in day 4 at 5
No. 997 exposure increased to 3.0 in day 4 at 5
No. 998 exposure increased to 1.0 in day 4 at 5
   25/10000 [..............................] - ETA: 31:42:32 - reward: 837.4328*When No. 46 infected, Exposure is 2.0 in day 4 at move 0
*When No. 56 infected, Exposure is 2.0 in day 4 at move 0
*When No. 99 infected, Exposure is 4.0 in day 4 at move 0
*When No. 158 infected, Exposure is 4.0 in day 4 at move 0
*When No. 232 infected, Exposure is 2.0 in day 4 at move 0
*When No. 423 infected, Exposure is 4.0 in day 4 at move 0
*When No. 437 infected, Exposure is 4.0 in day 4 at move 0
*When No. 494 infected, Exposure is 4.0 in day 4 at move 0
*When No. 647 infected, Exposure is 3.0 in day 4 at move 0
*When No. 698 infected, Exposure is 4.0 in day 4 at move 0
*When No. 804 infected, Exposure is 2.0 in day 4 at move 0
*When No. 1 infected, Exposure is 2.0 in day 4 at move 1
*When No. 49 infected, Exposure is 2.0 in day 4 at move 1
*When No. 72 infected, Exposure is 2.0 in day 4 at move 1
*When No. 78 infected, Exposure is 3.0 in day 4 at move 1
*When No. 129 infected, Exposure is 2.0 in day 4 at move 1
*When No. 180 infected, Exposure is 3.0 in day 4 at move 1
*When No. 219 infected, Exposure is 2.0 in day 4 at move 1
*When No. 285 infected, Exposure is 3.0 in day 4 at move 1
*When No. 315 infected, Exposure is 4.0 in day 4 at move 1
*When No. 322 infected, Exposure is 2.0 in day 4 at move 1
*When No. 351 infected, Exposure is 3.0 in day 4 at move 1
*When No. 380 infected, Exposure is 3.0 in day 4 at move 1
*When No. 463 infected, Exposure is 2.0 in day 4 at move 1
*When No. 509 infected, Exposure is 4.0 in day 4 at move 1
*When No. 553 infected, Exposure is 4.0 in day 4 at move 1
*When No. 719 infected, Exposure is 2.0 in day 4 at move 1
*When No. 723 infected, Exposure is 2.0 in day 4 at move 1
*When No. 771 infected, Exposure is 3.0 in day 4 at move 1
*When No. 820 infected, Exposure is 3.0 in day 4 at move 1
*When No. 885 infected, Exposure is 4.0 in day 4 at move 1
*When No. 996 infected, Exposure is 2.0 in day 4 at move 1
*When No. 997 infected, Exposure is 3.0 in day 4 at move 1
*When No. 97 infected, Exposure is 2.0 in day 4 at move 2
*When No. 262 infected, Exposure is 3.0 in day 4 at move 2
*When No. 541 infected, Exposure is 2.0 in day 4 at move 2
*When No. 742 infected, Exposure is 3.0 in day 4 at move 2
*When No. 831 infected, Exposure is 2.0 in day 4 at move 2
*When No. 236 infected, Exposure is 2.0 in day 4 at move 3
*When No. 586 infected, Exposure is 2.0 in day 4 at move 3
*When No. 618 infected, Exposure is 3.0 in day 4 at move 3
*When No. 646 infected, Exposure is 2.0 in day 4 at move 3
*When No. 897 infected, Exposure is 4.0 in day 4 at move 3
*When No. 75 infected, Exposure is 2.0 in day 4 at move 4
*When No. 98 infected, Exposure is 2.0 in day 4 at move 4
*When No. 213 infected, Exposure is 3.0 in day 4 at move 4
*When No. 307 infected, Exposure is 2.0 in day 4 at move 4
*When No. 417 infected, Exposure is 2.0 in day 4 at move 4
*When No. 585 infected, Exposure is 2.0 in day 4 at move 4
*When No. 601 infected, Exposure is 2.0 in day 4 at move 4
*When No. 632 infected, Exposure is 2.0 in day 4 at move 4
*When No. 653 infected, Exposure is 2.0 in day 4 at move 4
*When No. 805 infected, Exposure is 2.0 in day 4 at move 4
No. 2 exposure increased to 1.0 in day 4 at 5
No. 4 exposure increased to 1.0 in day 4 at 5
No. 7 exposure increased to 2.0 in day 4 at 5
No. 11 exposure increased to 3.0 in day 4 at 5
No. 15 exposure increased to 3.0 in day 4 at 5
No. 17 exposure increased to 2.0 in day 4 at 5
No. 27 exposure increased to 1.0 in day 4 at 5
No. 31 exposure increased to 3.0 in day 4 at 5
No. 38 exposure increased to 4.0 in day 4 at 5
No. 43 exposure increased to 3.0 in day 4 at 5
No. 47 exposure increased to 3.0 in day 4 at 5
No. 60 exposure increased to 2.0 in day 4 at 5
No. 65 exposure increased to 3.0 in day 4 at 5
No. 73 exposure increased to 1.0 in day 4 at 5
No. 79 exposure increased to 1.0 in day 4 at 5
No. 84 exposure increased to 1.0 in day 4 at 5
No. 86 exposure increased to 4.0 in day 4 at 5
No. 104 exposure increased to 1.0 in day 4 at 5
No. 115 exposure increased to 1.0 in day 4 at 5
No. 116 exposure increased to 1.0 in day 4 at 5
*When No. 120 infected, Exposure is 2.0 in day 4 at move 5
*When No. 124 infected, Exposure is 2.0 in day 4 at move 5
No. 130 exposure increased to 1.0 in day 4 at 5
No. 147 exposure increased to 2.0 in day 4 at 5
No. 154 exposure increased to 2.0 in day 4 at 5
No. 162 exposure increased to 4.0 in day 4 at 5
No. 175 exposure increased to 3.0 in day 4 at 5
No. 178 exposure increased to 2.0 in day 4 at 5
No. 184 exposure increased to 2.0 in day 4 at 5
No. 197 exposure increased to 1.0 in day 4 at 5
No. 199 exposure increased to 2.0 in day 4 at 5
No. 214 exposure increased to 1.0 in day 4 at 5
No. 217 exposure increased to 1.0 in day 4 at 5
No. 221 exposure increased to 2.0 in day 4 at 5
No. 223 exposure increased to 3.0 in day 4 at 5
No. 227 exposure increased to 1.0 in day 4 at 5
No. 244 exposure increased to 3.0 in day 4 at 5
No. 269 exposure increased to 2.0 in day 4 at 5
No. 271 exposure increased to 2.0 in day 4 at 5
No. 295 exposure increased to 1.0 in day 4 at 5
No. 296 exposure increased to 1.0 in day 4 at 5
No. 302 exposure increased to 2.0 in day 4 at 5
*When No. 305 infected, Exposure is 3.0 in day 4 at move 5
No. 311 exposure increased to 1.0 in day 4 at 5
No. 321 exposure increased to 2.0 in day 4 at 5
No. 328 exposure increased to 2.0 in day 4 at 5
No. 329 exposure increased to 3.0 in day 4 at 5
No. 358 exposure increased to 4.0 in day 4 at 5
No. 359 exposure increased to 1.0 in day 4 at 5
No. 361 exposure increased to 2.0 in day 4 at 5
No. 364 exposure increased to 1.0 in day 4 at 5
No. 366 exposure increased to 3.0 in day 4 at 5
No. 368 exposure increased to 4.0 in day 4 at 5
No. 376 exposure increased to 2.0 in day 4 at 5
No. 377 exposure increased to 4.0 in day 4 at 5
No. 394 exposure increased to 1.0 in day 4 at 5
No. 396 exposure increased to 1.0 in day 4 at 5
No. 404 exposure increased to 2.0 in day 4 at 5
No. 405 exposure increased to 1.0 in day 4 at 5
No. 408 exposure increased to 2.0 in day 4 at 5
No. 415 exposure increased to 3.0 in day 4 at 5
No. 427 exposure increased to 2.0 in day 4 at 5
No. 439 exposure increased to 3.0 in day 4 at 5
No. 447 exposure increased to 3.0 in day 4 at 5
No. 464 exposure increased to 2.0 in day 4 at 5
No. 471 exposure increased to 3.0 in day 4 at 5
No. 473 exposure increased to 1.0 in day 4 at 5
No. 476 exposure increased to 1.0 in day 4 at 5
No. 481 exposure increased to 1.0 in day 4 at 5
No. 484 exposure increased to 2.0 in day 4 at 5
No. 485 exposure increased to 1.0 in day 4 at 5
No. 495 exposure increased to 3.0 in day 4 at 5
No. 497 exposure increased to 3.0 in day 4 at 5
No. 512 exposure increased to 2.0 in day 4 at 5
No. 513 exposure increased to 1.0 in day 4 at 5
No. 515 exposure increased to 3.0 in day 4 at 5
No. 516 exposure increased to 3.0 in day 4 at 5
No. 546 exposure increased to 2.0 in day 4 at 5
No. 556 exposure increased to 2.0 in day 4 at 5
No. 559 exposure increased to 2.0 in day 4 at 5
No. 566 exposure increased to 3.0 in day 4 at 5
No. 568 exposure increased to 1.0 in day 4 at 5
No. 570 exposure increased to 2.0 in day 4 at 5
No. 573 exposure increased to 3.0 in day 4 at 5
No. 577 exposure increased to 1.0 in day 4 at 5
No. 580 exposure increased to 1.0 in day 4 at 5
No. 583 exposure increased to 3.0 in day 4 at 5
No. 592 exposure increased to 3.0 in day 4 at 5
No. 598 exposure increased to 1.0 in day 4 at 5
No. 600 exposure increased to 1.0 in day 4 at 5
No. 606 exposure increased to 2.0 in day 4 at 5
No. 610 exposure increased to 3.0 in day 4 at 5
No. 616 exposure increased to 1.0 in day 4 at 5
No. 630 exposure increased to 1.0 in day 4 at 5
No. 640 exposure increased to 3.0 in day 4 at 5
No. 642 exposure increased to 1.0 in day 4 at 5
No. 645 exposure increased to 3.0 in day 4 at 5
No. 649 exposure increased to 3.0 in day 4 at 5
*When No. 658 infected, Exposure is 2.0 in day 4 at move 5
No. 667 exposure increased to 2.0 in day 4 at 5
No. 669 exposure increased to 1.0 in day 4 at 5
No. 678 exposure increased to 1.0 in day 4 at 5
No. 682 exposure increased to 1.0 in day 4 at 5
No. 684 exposure increased to 3.0 in day 4 at 5
No. 685 exposure increased to 1.0 in day 4 at 5
No. 714 exposure increased to 2.0 in day 4 at 5
No. 727 exposure increased to 3.0 in day 4 at 5
No. 730 exposure increased to 1.0 in day 4 at 5
No. 736 exposure increased to 4.0 in day 4 at 5
No. 739 exposure increased to 1.0 in day 4 at 5
No. 757 exposure increased to 2.0 in day 4 at 5
No. 762 exposure increased to 2.0 in day 4 at 5
No. 763 exposure increased to 2.0 in day 4 at 5
No. 766 exposure increased to 2.0 in day 4 at 5
No. 768 exposure increased to 3.0 in day 4 at 5
No. 769 exposure increased to 1.0 in day 4 at 5
No. 772 exposure increased to 1.0 in day 4 at 5
No. 774 exposure increased to 2.0 in day 4 at 5
No. 779 exposure increased to 1.0 in day 4 at 5
No. 781 exposure increased to 2.0 in day 4 at 5
No. 786 exposure increased to 2.0 in day 4 at 5
No. 789 exposure increased to 1.0 in day 4 at 5
No. 796 exposure increased to 2.0 in day 4 at 5
No. 801 exposure increased to 2.0 in day 4 at 5
No. 802 exposure increased to 1.0 in day 4 at 5
No. 807 exposure increased to 1.0 in day 4 at 5
No. 815 exposure increased to 3.0 in day 4 at 5
No. 821 exposure increased to 1.0 in day 4 at 5
No. 827 exposure increased to 1.0 in day 4 at 5
No. 828 exposure increased to 1.0 in day 4 at 5
No. 836 exposure increased to 3.0 in day 4 at 5
No. 840 exposure increased to 3.0 in day 4 at 5
No. 853 exposure increased to 3.0 in day 4 at 5
No. 859 exposure increased to 3.0 in day 4 at 5
No. 862 exposure increased to 2.0 in day 4 at 5
*When No. 863 infected, Exposure is 2.0 in day 4 at move 5
No. 865 exposure increased to 1.0 in day 4 at 5
No. 869 exposure increased to 1.0 in day 4 at 5
No. 873 exposure increased to 1.0 in day 4 at 5
No. 877 exposure increased to 1.0 in day 4 at 5
No. 888 exposure increased to 1.0 in day 4 at 5
No. 898 exposure increased to 1.0 in day 4 at 5
No. 902 exposure increased to 2.0 in day 4 at 5
No. 912 exposure increased to 1.0 in day 4 at 5
No. 916 exposure increased to 3.0 in day 4 at 5
No. 925 exposure increased to 2.0 in day 4 at 5
No. 928 exposure increased to 2.0 in day 4 at 5
No. 930 exposure increased to 2.0 in day 4 at 5
No. 933 exposure increased to 1.0 in day 4 at 5
No. 939 exposure increased to 1.0 in day 4 at 5
No. 940 exposure increased to 3.0 in day 4 at 5
No. 943 exposure increased to 1.0 in day 4 at 5
No. 949 exposure increased to 3.0 in day 4 at 5
No. 950 exposure increased to 2.0 in day 4 at 5
No. 958 exposure increased to 1.0 in day 4 at 5
No. 961 exposure increased to 3.0 in day 4 at 5
No. 963 exposure increased to 2.0 in day 4 at 5
No. 964 exposure increased to 1.0 in day 4 at 5
No. 970 exposure increased to 2.0 in day 4 at 5
No. 973 exposure increased to 2.0 in day 4 at 5
No. 984 exposure increased to 1.0 in day 4 at 5
No. 994 exposure increased to 2.0 in day 4 at 5
No. 998 exposure increased to 2.0 in day 4 at 5
   26/10000 [..............................] - ETA: 31:54:57 - reward: 824.5162*When No. 15 infected, Exposure is 3.0 in day 4 at move 0
*When No. 31 infected, Exposure is 3.0 in day 4 at move 0
*When No. 162 infected, Exposure is 4.0 in day 4 at move 0
*When No. 221 infected, Exposure is 2.0 in day 4 at move 0
*When No. 377 infected, Exposure is 4.0 in day 4 at move 0
*When No. 404 infected, Exposure is 2.0 in day 4 at move 0
*When No. 471 infected, Exposure is 3.0 in day 4 at move 0
*When No. 495 infected, Exposure is 3.0 in day 4 at move 0
*When No. 556 infected, Exposure is 2.0 in day 4 at move 0
*When No. 566 infected, Exposure is 3.0 in day 4 at move 0
*When No. 573 infected, Exposure is 3.0 in day 4 at move 0
*When No. 606 infected, Exposure is 2.0 in day 4 at move 0
*When No. 640 infected, Exposure is 3.0 in day 4 at move 0
*When No. 684 infected, Exposure is 3.0 in day 4 at move 0
*When No. 714 infected, Exposure is 2.0 in day 4 at move 0
*When No. 801 infected, Exposure is 2.0 in day 4 at move 0
*When No. 940 infected, Exposure is 3.0 in day 4 at move 0
*When No. 949 infected, Exposure is 3.0 in day 4 at move 0
*When No. 184 infected, Exposure is 2.0 in day 4 at move 1
*When No. 358 infected, Exposure is 4.0 in day 4 at move 1
*When No. 439 infected, Exposure is 3.0 in day 4 at move 1
*When No. 516 infected, Exposure is 3.0 in day 4 at move 1
*When No. 570 infected, Exposure is 2.0 in day 4 at move 1
*When No. 727 infected, Exposure is 3.0 in day 4 at move 1
*When No. 766 infected, Exposure is 2.0 in day 4 at move 1
*When No. 950 infected, Exposure is 2.0 in day 4 at move 1
*When No. 970 infected, Exposure is 2.0 in day 4 at move 1
*When No. 328 infected, Exposure is 2.0 in day 4 at move 2
*When No. 515 infected, Exposure is 3.0 in day 4 at move 2
*When No. 768 infected, Exposure is 3.0 in day 4 at move 2
*When No. 916 infected, Exposure is 3.0 in day 4 at move 2
*When No. 47 infected, Exposure is 3.0 in day 4 at move 3
*When No. 60 infected, Exposure is 2.0 in day 4 at move 3
*When No. 65 infected, Exposure is 3.0 in day 4 at move 3
*When No. 178 infected, Exposure is 2.0 in day 4 at move 3
*When No. 321 infected, Exposure is 2.0 in day 4 at move 3
*When No. 366 infected, Exposure is 3.0 in day 4 at move 3
*When No. 376 infected, Exposure is 2.0 in day 4 at move 3
*When No. 649 infected, Exposure is 3.0 in day 4 at move 3
*When No. 840 infected, Exposure is 3.0 in day 4 at move 3
*When No. 43 infected, Exposure is 3.0 in day 4 at move 4
*When No. 86 infected, Exposure is 4.0 in day 4 at move 4
*When No. 368 infected, Exposure is 4.0 in day 4 at move 4
*When No. 408 infected, Exposure is 2.0 in day 4 at move 4
*When No. 415 infected, Exposure is 3.0 in day 4 at move 4
*When No. 484 infected, Exposure is 2.0 in day 4 at move 4
*When No. 610 infected, Exposure is 3.0 in day 4 at move 4
*When No. 763 infected, Exposure is 2.0 in day 4 at move 4
*When No. 836 infected, Exposure is 3.0 in day 4 at move 4
*When No. 853 infected, Exposure is 3.0 in day 4 at move 4
*When No. 859 infected, Exposure is 3.0 in day 4 at move 4
*When No. 994 infected, Exposure is 2.0 in day 4 at move 4
No. 2 exposure increased to 2.0 in day 4 at 5
No. 4 exposure increased to 2.0 in day 4 at 5
No. 7 exposure increased to 3.0 in day 4 at 5
*When No. 11 infected, Exposure is 3.0 in day 4 at move 5
No. 17 exposure increased to 3.0 in day 4 at 5
No. 20 exposure increased to 2.0 in day 4 at 5
No. 27 exposure increased to 2.0 in day 4 at 5
No. 38 exposure increased to 5.0 in day 4 at 5
No. 40 exposure increased to 1.0 in day 4 at 5
No. 63 exposure increased to 1.0 in day 4 at 5
No. 73 exposure increased to 2.0 in day 4 at 5
No. 79 exposure increased to 2.0 in day 4 at 5
No. 84 exposure increased to 2.0 in day 4 at 5
No. 93 exposure increased to 1.0 in day 4 at 5
No. 104 exposure increased to 2.0 in day 4 at 5
No. 109 exposure increased to 1.0 in day 4 at 5
No. 115 exposure increased to 2.0 in day 4 at 5
No. 116 exposure increased to 2.0 in day 4 at 5
No. 117 exposure increased to 2.0 in day 4 at 5
No. 130 exposure increased to 2.0 in day 4 at 5
No. 132 exposure increased to 1.0 in day 4 at 5
No. 133 exposure increased to 1.0 in day 4 at 5
No. 147 exposure increased to 3.0 in day 4 at 5
No. 151 exposure increased to 1.0 in day 4 at 5
No. 154 exposure increased to 3.0 in day 4 at 5
No. 156 exposure increased to 2.0 in day 4 at 5
No. 175 exposure increased to 4.0 in day 4 at 5
No. 179 exposure increased to 1.0 in day 4 at 5
No. 197 exposure increased to 2.0 in day 4 at 5
No. 198 exposure increased to 1.0 in day 4 at 5
No. 199 exposure increased to 3.0 in day 4 at 5
No. 203 exposure increased to 2.0 in day 4 at 5
No. 214 exposure increased to 2.0 in day 4 at 5
No. 217 exposure increased to 2.0 in day 4 at 5
*When No. 223 infected, Exposure is 3.0 in day 4 at move 5
No. 227 exposure increased to 2.0 in day 4 at 5
No. 233 exposure increased to 1.0 in day 4 at 5
No. 241 exposure increased to 1.0 in day 4 at 5
No. 244 exposure increased to 4.0 in day 4 at 5
No. 245 exposure increased to 1.0 in day 4 at 5
No. 265 exposure increased to 1.0 in day 4 at 5
No. 266 exposure increased to 1.0 in day 4 at 5
No. 268 exposure increased to 1.0 in day 4 at 5
No. 269 exposure increased to 3.0 in day 4 at 5
No. 271 exposure increased to 3.0 in day 4 at 5
No. 281 exposure increased to 1.0 in day 4 at 5
No. 284 exposure increased to 1.0 in day 4 at 5
No. 294 exposure increased to 1.0 in day 4 at 5
No. 295 exposure increased to 2.0 in day 4 at 5
No. 296 exposure increased to 2.0 in day 4 at 5
No. 297 exposure increased to 1.0 in day 4 at 5
No. 302 exposure increased to 3.0 in day 4 at 5
No. 310 exposure increased to 2.0 in day 4 at 5
No. 311 exposure increased to 2.0 in day 4 at 5
No. 316 exposure increased to 2.0 in day 4 at 5
No. 325 exposure increased to 2.0 in day 4 at 5
No. 329 exposure increased to 4.0 in day 4 at 5
No. 359 exposure increased to 2.0 in day 4 at 5
No. 361 exposure increased to 3.0 in day 4 at 5
No. 364 exposure increased to 2.0 in day 4 at 5
No. 394 exposure increased to 2.0 in day 4 at 5
No. 395 exposure increased to 1.0 in day 4 at 5
No. 396 exposure increased to 2.0 in day 4 at 5
No. 405 exposure increased to 2.0 in day 4 at 5
No. 420 exposure increased to 1.0 in day 4 at 5
No. 427 exposure increased to 3.0 in day 4 at 5
No. 436 exposure increased to 1.0 in day 4 at 5
No. 447 exposure increased to 4.0 in day 4 at 5
No. 459 exposure increased to 1.0 in day 4 at 5
No. 464 exposure increased to 3.0 in day 4 at 5
No. 473 exposure increased to 2.0 in day 4 at 5
No. 476 exposure increased to 2.0 in day 4 at 5
No. 481 exposure increased to 2.0 in day 4 at 5
No. 485 exposure increased to 2.0 in day 4 at 5
No. 489 exposure increased to 2.0 in day 4 at 5
*When No. 497 infected, Exposure is 3.0 in day 4 at move 5
No. 512 exposure increased to 3.0 in day 4 at 5
No. 513 exposure increased to 2.0 in day 4 at 5
No. 518 exposure increased to 1.0 in day 4 at 5
No. 526 exposure increased to 1.0 in day 4 at 5
No. 529 exposure increased to 1.0 in day 4 at 5
No. 535 exposure increased to 1.0 in day 4 at 5
No. 545 exposure increased to 2.0 in day 4 at 5
No. 546 exposure increased to 3.0 in day 4 at 5
No. 559 exposure increased to 3.0 in day 4 at 5
No. 567 exposure increased to 1.0 in day 4 at 5
No. 568 exposure increased to 2.0 in day 4 at 5
No. 569 exposure increased to 1.0 in day 4 at 5
No. 577 exposure increased to 2.0 in day 4 at 5
No. 580 exposure increased to 2.0 in day 4 at 5
No. 583 exposure increased to 4.0 in day 4 at 5
*When No. 592 infected, Exposure is 3.0 in day 4 at move 5
No. 598 exposure increased to 2.0 in day 4 at 5
No. 600 exposure increased to 2.0 in day 4 at 5
No. 604 exposure increased to 2.0 in day 4 at 5
No. 605 exposure increased to 1.0 in day 4 at 5
No. 616 exposure increased to 2.0 in day 4 at 5
No. 619 exposure increased to 1.0 in day 4 at 5
No. 630 exposure increased to 2.0 in day 4 at 5
No. 641 exposure increased to 1.0 in day 4 at 5
No. 642 exposure increased to 2.0 in day 4 at 5
No. 645 exposure increased to 4.0 in day 4 at 5
No. 655 exposure increased to 1.0 in day 4 at 5
No. 667 exposure increased to 3.0 in day 4 at 5
No. 669 exposure increased to 2.0 in day 4 at 5
No. 678 exposure increased to 2.0 in day 4 at 5
No. 680 exposure increased to 1.0 in day 4 at 5
No. 682 exposure increased to 2.0 in day 4 at 5
No. 685 exposure increased to 2.0 in day 4 at 5
No. 703 exposure increased to 2.0 in day 4 at 5
No. 712 exposure increased to 1.0 in day 4 at 5
No. 730 exposure increased to 2.0 in day 4 at 5
No. 736 exposure increased to 5.0 in day 4 at 5
No. 738 exposure increased to 1.0 in day 4 at 5
No. 739 exposure increased to 2.0 in day 4 at 5
No. 757 exposure increased to 3.0 in day 4 at 5
No. 762 exposure increased to 3.0 in day 4 at 5
No. 769 exposure increased to 2.0 in day 4 at 5
No. 772 exposure increased to 2.0 in day 4 at 5
No. 774 exposure increased to 3.0 in day 4 at 5
No. 776 exposure increased to 1.0 in day 4 at 5
No. 779 exposure increased to 2.0 in day 4 at 5
No. 781 exposure increased to 3.0 in day 4 at 5
No. 785 exposure increased to 1.0 in day 4 at 5
*When No. 786 infected, Exposure is 2.0 in day 4 at move 5
No. 789 exposure increased to 2.0 in day 4 at 5
No. 796 exposure increased to 3.0 in day 4 at 5
No. 802 exposure increased to 2.0 in day 4 at 5
No. 807 exposure increased to 2.0 in day 4 at 5
No. 815 exposure increased to 4.0 in day 4 at 5
No. 816 exposure increased to 1.0 in day 4 at 5
No. 821 exposure increased to 2.0 in day 4 at 5
No. 827 exposure increased to 2.0 in day 4 at 5
No. 828 exposure increased to 2.0 in day 4 at 5
No. 834 exposure increased to 1.0 in day 4 at 5
No. 851 exposure increased to 1.0 in day 4 at 5
No. 852 exposure increased to 1.0 in day 4 at 5
No. 858 exposure increased to 1.0 in day 4 at 5
No. 861 exposure increased to 1.0 in day 4 at 5
No. 862 exposure increased to 3.0 in day 4 at 5
No. 865 exposure increased to 2.0 in day 4 at 5
No. 866 exposure increased to 2.0 in day 4 at 5
No. 869 exposure increased to 2.0 in day 4 at 5
No. 873 exposure increased to 2.0 in day 4 at 5
No. 875 exposure increased to 1.0 in day 4 at 5
No. 877 exposure increased to 2.0 in day 4 at 5
No. 886 exposure increased to 1.0 in day 4 at 5
No. 888 exposure increased to 2.0 in day 4 at 5
No. 889 exposure increased to 1.0 in day 4 at 5
No. 898 exposure increased to 2.0 in day 4 at 5
No. 902 exposure increased to 3.0 in day 4 at 5
No. 912 exposure increased to 2.0 in day 4 at 5
No. 925 exposure increased to 3.0 in day 4 at 5
No. 928 exposure increased to 3.0 in day 4 at 5
No. 930 exposure increased to 3.0 in day 4 at 5
No. 933 exposure increased to 2.0 in day 4 at 5
No. 934 exposure increased to 1.0 in day 4 at 5
No. 935 exposure increased to 1.0 in day 4 at 5
No. 939 exposure increased to 2.0 in day 4 at 5
No. 943 exposure increased to 2.0 in day 4 at 5
No. 948 exposure increased to 2.0 in day 4 at 5
No. 951 exposure increased to 1.0 in day 4 at 5
No. 957 exposure increased to 2.0 in day 4 at 5
No. 958 exposure increased to 2.0 in day 4 at 5
No. 961 exposure increased to 4.0 in day 4 at 5
No. 963 exposure increased to 3.0 in day 4 at 5
No. 964 exposure increased to 2.0 in day 4 at 5
No. 973 exposure increased to 3.0 in day 4 at 5
No. 984 exposure increased to 2.0 in day 4 at 5
No. 998 exposure increased to 3.0 in day 4 at 5
No. 999 exposure increased to 1.0 in day 4 at 5
   27/10000 [..............................] - ETA: 31:55:33 - reward: 812.2296*When No. 130 infected, Exposure is 2.0 in day 4 at move 0
*When No. 227 infected, Exposure is 2.0 in day 4 at move 0
*When No. 244 infected, Exposure is 4.0 in day 4 at move 0
*When No. 271 infected, Exposure is 3.0 in day 4 at move 0
*When No. 302 infected, Exposure is 3.0 in day 4 at move 0
*When No. 364 infected, Exposure is 2.0 in day 4 at move 0
*When No. 481 infected, Exposure is 2.0 in day 4 at move 0
*When No. 739 infected, Exposure is 2.0 in day 4 at move 0
*When No. 802 infected, Exposure is 2.0 in day 4 at move 0
*When No. 815 infected, Exposure is 4.0 in day 4 at move 0
*When No. 957 infected, Exposure is 2.0 in day 4 at move 0
No. 2 exposure increased to 3.0 in day 4 at 1
No. 4 exposure increased to 3.0 in day 4 at 1
No. 7 exposure increased to 4.0 in day 4 at 1
No. 17 exposure increased to 4.0 in day 4 at 1
No. 20 exposure increased to 3.0 in day 4 at 1
No. 24 exposure increased to 1.0 in day 4 at 1
No. 27 exposure increased to 3.0 in day 4 at 1
No. 33 exposure increased to 2.0 in day 4 at 1
No. 38 exposure increased to 6.0 in day 4 at 1
No. 40 exposure increased to 2.0 in day 4 at 1
No. 41 exposure increased to 2.0 in day 4 at 1
No. 63 exposure increased to 2.0 in day 4 at 1
No. 73 exposure increased to 3.0 in day 4 at 1
No. 79 exposure increased to 3.0 in day 4 at 1
No. 84 exposure increased to 3.0 in day 4 at 1
No. 89 exposure increased to 1.0 in day 4 at 1
No. 93 exposure increased to 2.0 in day 4 at 1
No. 104 exposure increased to 3.0 in day 4 at 1
No. 109 exposure increased to 2.0 in day 4 at 1
No. 115 exposure increased to 3.0 in day 4 at 1
No. 116 exposure increased to 3.0 in day 4 at 1
No. 117 exposure increased to 3.0 in day 4 at 1
No. 132 exposure increased to 2.0 in day 4 at 1
No. 133 exposure increased to 2.0 in day 4 at 1
No. 147 exposure increased to 4.0 in day 4 at 1
No. 151 exposure increased to 2.0 in day 4 at 1
No. 154 exposure increased to 4.0 in day 4 at 1
No. 156 exposure increased to 3.0 in day 4 at 1
No. 175 exposure increased to 5.0 in day 4 at 1
No. 179 exposure increased to 2.0 in day 4 at 1
No. 197 exposure increased to 3.0 in day 4 at 1
No. 198 exposure increased to 2.0 in day 4 at 1
No. 199 exposure increased to 4.0 in day 4 at 1
No. 200 exposure increased to 1.0 in day 4 at 1
No. 203 exposure increased to 3.0 in day 4 at 1
No. 214 exposure increased to 3.0 in day 4 at 1
*When No. 217 infected, Exposure is 2.0 in day 4 at move 1
No. 220 exposure increased to 1.0 in day 4 at 1
No. 233 exposure increased to 2.0 in day 4 at 1
No. 241 exposure increased to 2.0 in day 4 at 1
No. 245 exposure increased to 2.0 in day 4 at 1
No. 265 exposure increased to 2.0 in day 4 at 1
No. 266 exposure increased to 2.0 in day 4 at 1
No. 267 exposure increased to 1.0 in day 4 at 1
No. 268 exposure increased to 2.0 in day 4 at 1
No. 269 exposure increased to 4.0 in day 4 at 1
No. 281 exposure increased to 2.0 in day 4 at 1
No. 284 exposure increased to 2.0 in day 4 at 1
No. 294 exposure increased to 2.0 in day 4 at 1
No. 295 exposure increased to 3.0 in day 4 at 1
No. 296 exposure increased to 3.0 in day 4 at 1
No. 297 exposure increased to 2.0 in day 4 at 1
No. 310 exposure increased to 3.0 in day 4 at 1
No. 311 exposure increased to 3.0 in day 4 at 1
No. 316 exposure increased to 3.0 in day 4 at 1
No. 325 exposure increased to 3.0 in day 4 at 1
No. 329 exposure increased to 5.0 in day 4 at 1
No. 359 exposure increased to 3.0 in day 4 at 1
No. 361 exposure increased to 4.0 in day 4 at 1
No. 362 exposure increased to 1.0 in day 4 at 1
No. 389 exposure increased to 2.0 in day 4 at 1
*When No. 394 infected, Exposure is 2.0 in day 4 at move 1
No. 395 exposure increased to 2.0 in day 4 at 1
No. 396 exposure increased to 3.0 in day 4 at 1
No. 405 exposure increased to 3.0 in day 4 at 1
No. 420 exposure increased to 2.0 in day 4 at 1
*When No. 427 infected, Exposure is 3.0 in day 4 at move 1
No. 436 exposure increased to 2.0 in day 4 at 1
No. 441 exposure increased to 2.0 in day 4 at 1
No. 447 exposure increased to 5.0 in day 4 at 1
No. 459 exposure increased to 2.0 in day 4 at 1
*When No. 464 infected, Exposure is 3.0 in day 4 at move 1
No. 473 exposure increased to 3.0 in day 4 at 1
No. 476 exposure increased to 3.0 in day 4 at 1
No. 482 exposure increased to 2.0 in day 4 at 1
No. 485 exposure increased to 3.0 in day 4 at 1
No. 489 exposure increased to 3.0 in day 4 at 1
No. 507 exposure increased to 1.0 in day 4 at 1
*When No. 512 infected, Exposure is 3.0 in day 4 at move 1
No. 513 exposure increased to 3.0 in day 4 at 1
No. 518 exposure increased to 2.0 in day 4 at 1
No. 526 exposure increased to 2.0 in day 4 at 1
No. 529 exposure increased to 2.0 in day 4 at 1
No. 535 exposure increased to 2.0 in day 4 at 1
*When No. 545 infected, Exposure is 2.0 in day 4 at move 1
No. 546 exposure increased to 4.0 in day 4 at 1
No. 551 exposure increased to 2.0 in day 4 at 1
No. 559 exposure increased to 4.0 in day 4 at 1
No. 567 exposure increased to 2.0 in day 4 at 1
No. 568 exposure increased to 3.0 in day 4 at 1
No. 569 exposure increased to 2.0 in day 4 at 1
No. 577 exposure increased to 3.0 in day 4 at 1
No. 580 exposure increased to 3.0 in day 4 at 1
*When No. 583 infected, Exposure is 4.0 in day 4 at move 1
No. 587 exposure increased to 2.0 in day 4 at 1
No. 598 exposure increased to 3.0 in day 4 at 1
No. 600 exposure increased to 3.0 in day 4 at 1
No. 604 exposure increased to 3.0 in day 4 at 1
No. 605 exposure increased to 2.0 in day 4 at 1
No. 616 exposure increased to 3.0 in day 4 at 1
No. 619 exposure increased to 2.0 in day 4 at 1
No. 624 exposure increased to 1.0 in day 4 at 1
*When No. 630 infected, Exposure is 2.0 in day 4 at move 1
No. 633 exposure increased to 1.0 in day 4 at 1
No. 641 exposure increased to 2.0 in day 4 at 1
*When No. 642 infected, Exposure is 2.0 in day 4 at move 1
No. 645 exposure increased to 5.0 in day 4 at 1
No. 655 exposure increased to 2.0 in day 4 at 1
*When No. 667 infected, Exposure is 3.0 in day 4 at move 1
*When No. 669 infected, Exposure is 2.0 in day 4 at move 1
No. 673 exposure increased to 2.0 in day 4 at 1
No. 677 exposure increased to 1.0 in day 4 at 1
No. 678 exposure increased to 3.0 in day 4 at 1
No. 680 exposure increased to 2.0 in day 4 at 1
No. 682 exposure increased to 3.0 in day 4 at 1
No. 685 exposure increased to 3.0 in day 4 at 1
No. 691 exposure increased to 2.0 in day 4 at 1
No. 703 exposure increased to 3.0 in day 4 at 1
No. 710 exposure increased to 2.0 in day 4 at 1
No. 712 exposure increased to 2.0 in day 4 at 1
No. 730 exposure increased to 3.0 in day 4 at 1
No. 731 exposure increased to 2.0 in day 4 at 1
*When No. 736 infected, Exposure is 5.0 in day 4 at move 1
No. 738 exposure increased to 2.0 in day 4 at 1
No. 746 exposure increased to 2.0 in day 4 at 1
No. 757 exposure increased to 4.0 in day 4 at 1
No. 762 exposure increased to 4.0 in day 4 at 1
No. 769 exposure increased to 3.0 in day 4 at 1
No. 772 exposure increased to 3.0 in day 4 at 1
No. 774 exposure increased to 4.0 in day 4 at 1
No. 776 exposure increased to 2.0 in day 4 at 1
*When No. 779 infected, Exposure is 2.0 in day 4 at move 1
No. 781 exposure increased to 4.0 in day 4 at 1
No. 785 exposure increased to 2.0 in day 4 at 1
No. 789 exposure increased to 3.0 in day 4 at 1
*When No. 796 infected, Exposure is 3.0 in day 4 at move 1
No. 803 exposure increased to 1.0 in day 4 at 1
No. 807 exposure increased to 3.0 in day 4 at 1
No. 816 exposure increased to 2.0 in day 4 at 1
No. 821 exposure increased to 3.0 in day 4 at 1
No. 827 exposure increased to 3.0 in day 4 at 1
No. 828 exposure increased to 3.0 in day 4 at 1
No. 834 exposure increased to 2.0 in day 4 at 1
No. 851 exposure increased to 2.0 in day 4 at 1
No. 852 exposure increased to 2.0 in day 4 at 1
No. 856 exposure increased to 2.0 in day 4 at 1
No. 858 exposure increased to 2.0 in day 4 at 1
No. 861 exposure increased to 2.0 in day 4 at 1
No. 862 exposure increased to 4.0 in day 4 at 1
No. 865 exposure increased to 3.0 in day 4 at 1
No. 866 exposure increased to 3.0 in day 4 at 1
No. 869 exposure increased to 3.0 in day 4 at 1
No. 873 exposure increased to 3.0 in day 4 at 1
No. 875 exposure increased to 2.0 in day 4 at 1
No. 877 exposure increased to 3.0 in day 4 at 1
No. 886 exposure increased to 2.0 in day 4 at 1
No. 888 exposure increased to 3.0 in day 4 at 1
No. 889 exposure increased to 2.0 in day 4 at 1
No. 898 exposure increased to 3.0 in day 4 at 1
No. 902 exposure increased to 4.0 in day 4 at 1
No. 908 exposure increased to 1.0 in day 4 at 1
*When No. 912 infected, Exposure is 2.0 in day 4 at move 1
No. 925 exposure increased to 4.0 in day 4 at 1
No. 928 exposure increased to 4.0 in day 4 at 1
*When No. 930 infected, Exposure is 3.0 in day 4 at move 1
No. 933 exposure increased to 3.0 in day 4 at 1
No. 934 exposure increased to 2.0 in day 4 at 1
No. 935 exposure increased to 2.0 in day 4 at 1
No. 939 exposure increased to 3.0 in day 4 at 1
No. 943 exposure increased to 3.0 in day 4 at 1
No. 948 exposure increased to 3.0 in day 4 at 1
No. 951 exposure increased to 2.0 in day 4 at 1
No. 958 exposure increased to 3.0 in day 4 at 1
*When No. 961 infected, Exposure is 4.0 in day 4 at move 1
No. 963 exposure increased to 4.0 in day 4 at 1
No. 964 exposure increased to 3.0 in day 4 at 1
*When No. 973 infected, Exposure is 3.0 in day 4 at move 1
No. 984 exposure increased to 3.0 in day 4 at 1
No. 998 exposure increased to 4.0 in day 4 at 1
No. 999 exposure increased to 2.0 in day 4 at 1
   28/10000 [..............................] - ETA: 31:09:48 - reward: 800.1243*When No. 7 infected, Exposure is 4.0 in day 4 at move 0
*When No. 20 infected, Exposure is 3.0 in day 4 at move 0
*When No. 38 infected, Exposure is 6.0 in day 4 at move 0
*When No. 79 infected, Exposure is 3.0 in day 4 at move 0
*When No. 245 infected, Exposure is 2.0 in day 4 at move 0
*When No. 310 infected, Exposure is 3.0 in day 4 at move 0
*When No. 311 infected, Exposure is 3.0 in day 4 at move 0
*When No. 316 infected, Exposure is 3.0 in day 4 at move 0
*When No. 489 infected, Exposure is 3.0 in day 4 at move 0
*When No. 518 infected, Exposure is 2.0 in day 4 at move 0
*When No. 529 infected, Exposure is 2.0 in day 4 at move 0
*When No. 546 infected, Exposure is 4.0 in day 4 at move 0
*When No. 645 infected, Exposure is 5.0 in day 4 at move 0
*When No. 685 infected, Exposure is 3.0 in day 4 at move 0
*When No. 757 infected, Exposure is 4.0 in day 4 at move 0
*When No. 762 infected, Exposure is 4.0 in day 4 at move 0
*When No. 781 infected, Exposure is 4.0 in day 4 at move 0
*When No. 816 infected, Exposure is 2.0 in day 4 at move 0
*When No. 865 infected, Exposure is 3.0 in day 4 at move 0
*When No. 898 infected, Exposure is 3.0 in day 4 at move 0
*When No. 902 infected, Exposure is 4.0 in day 4 at move 0
*When No. 925 infected, Exposure is 4.0 in day 4 at move 0
*When No. 928 infected, Exposure is 4.0 in day 4 at move 0
*When No. 999 infected, Exposure is 2.0 in day 4 at move 0
*When No. 2 infected, Exposure is 3.0 in day 4 at move 1
*When No. 4 infected, Exposure is 3.0 in day 4 at move 1
*When No. 27 infected, Exposure is 3.0 in day 4 at move 1
*When No. 104 infected, Exposure is 3.0 in day 4 at move 1
*When No. 154 infected, Exposure is 4.0 in day 4 at move 1
*When No. 396 infected, Exposure is 3.0 in day 4 at move 1
*When No. 447 infected, Exposure is 5.0 in day 4 at move 1
*When No. 513 infected, Exposure is 3.0 in day 4 at move 1
*When No. 551 infected, Exposure is 2.0 in day 4 at move 1
*When No. 678 infected, Exposure is 3.0 in day 4 at move 1
*When No. 682 infected, Exposure is 3.0 in day 4 at move 1
*When No. 703 infected, Exposure is 3.0 in day 4 at move 1
*When No. 712 infected, Exposure is 2.0 in day 4 at move 1
*When No. 730 infected, Exposure is 3.0 in day 4 at move 1
*When No. 774 infected, Exposure is 4.0 in day 4 at move 1
*When No. 888 infected, Exposure is 3.0 in day 4 at move 1
*When No. 939 infected, Exposure is 3.0 in day 4 at move 1
*When No. 84 infected, Exposure is 3.0 in day 4 at move 2
*When No. 115 infected, Exposure is 3.0 in day 4 at move 2
*When No. 117 infected, Exposure is 3.0 in day 4 at move 2
*When No. 132 infected, Exposure is 2.0 in day 4 at move 2
*When No. 151 infected, Exposure is 2.0 in day 4 at move 2
*When No. 197 infected, Exposure is 3.0 in day 4 at move 2
*When No. 203 infected, Exposure is 3.0 in day 4 at move 2
*When No. 214 infected, Exposure is 3.0 in day 4 at move 2
*When No. 265 infected, Exposure is 2.0 in day 4 at move 2
*When No. 297 infected, Exposure is 2.0 in day 4 at move 2
*When No. 325 infected, Exposure is 3.0 in day 4 at move 2
*When No. 395 infected, Exposure is 2.0 in day 4 at move 2
*When No. 476 infected, Exposure is 3.0 in day 4 at move 2
*When No. 482 infected, Exposure is 2.0 in day 4 at move 2
*When No. 485 infected, Exposure is 3.0 in day 4 at move 2
*When No. 587 infected, Exposure is 2.0 in day 4 at move 2
*When No. 600 infected, Exposure is 3.0 in day 4 at move 2
*When No. 769 infected, Exposure is 3.0 in day 4 at move 2
*When No. 807 infected, Exposure is 3.0 in day 4 at move 2
*When No. 866 infected, Exposure is 3.0 in day 4 at move 2
*When No. 933 infected, Exposure is 3.0 in day 4 at move 2
*When No. 948 infected, Exposure is 3.0 in day 4 at move 2
*When No. 175 infected, Exposure is 5.0 in day 4 at move 3
*When No. 199 infected, Exposure is 4.0 in day 4 at move 3
*When No. 284 infected, Exposure is 2.0 in day 4 at move 3
*When No. 294 infected, Exposure is 2.0 in day 4 at move 3
*When No. 296 infected, Exposure is 3.0 in day 4 at move 3
*When No. 329 infected, Exposure is 5.0 in day 4 at move 3
*When No. 361 infected, Exposure is 4.0 in day 4 at move 3
*When No. 776 infected, Exposure is 2.0 in day 4 at move 3
*When No. 951 infected, Exposure is 2.0 in day 4 at move 3
*When No. 17 infected, Exposure is 4.0 in day 4 at move 4
*When No. 40 infected, Exposure is 2.0 in day 4 at move 4
*When No. 41 infected, Exposure is 2.0 in day 4 at move 4
*When No. 268 infected, Exposure is 2.0 in day 4 at move 4
*When No. 295 infected, Exposure is 3.0 in day 4 at move 4
*When No. 359 infected, Exposure is 3.0 in day 4 at move 4
*When No. 420 infected, Exposure is 2.0 in day 4 at move 4
*When No. 559 infected, Exposure is 4.0 in day 4 at move 4
*When No. 568 infected, Exposure is 3.0 in day 4 at move 4
*When No. 577 infected, Exposure is 3.0 in day 4 at move 4
*When No. 604 infected, Exposure is 3.0 in day 4 at move 4
*When No. 827 infected, Exposure is 3.0 in day 4 at move 4
*When No. 861 infected, Exposure is 2.0 in day 4 at move 4
*When No. 875 infected, Exposure is 2.0 in day 4 at move 4
*When No. 877 infected, Exposure is 3.0 in day 4 at move 4
*When No. 943 infected, Exposure is 3.0 in day 4 at move 4
*When No. 984 infected, Exposure is 3.0 in day 4 at move 4
No. 10 exposure increased to 1.0 in day 4 at 5
No. 18 exposure increased to 2.0 in day 4 at 5
No. 24 exposure increased to 2.0 in day 4 at 5
No. 33 exposure increased to 3.0 in day 4 at 5
No. 37 exposure increased to 2.0 in day 4 at 5
No. 63 exposure increased to 3.0 in day 4 at 5
No. 73 exposure increased to 4.0 in day 4 at 5
No. 83 exposure increased to 1.0 in day 4 at 5
No. 89 exposure increased to 2.0 in day 4 at 5
*When No. 93 infected, Exposure is 2.0 in day 4 at move 5
No. 95 exposure increased to 1.0 in day 4 at 5
No. 106 exposure increased to 1.0 in day 4 at 5
No. 109 exposure increased to 3.0 in day 4 at 5
No. 116 exposure increased to 4.0 in day 4 at 5
No. 119 exposure increased to 1.0 in day 4 at 5
No. 133 exposure increased to 3.0 in day 4 at 5
No. 135 exposure increased to 1.0 in day 4 at 5
No. 147 exposure increased to 5.0 in day 4 at 5
No. 156 exposure increased to 4.0 in day 4 at 5
No. 173 exposure increased to 1.0 in day 4 at 5
*When No. 179 infected, Exposure is 2.0 in day 4 at move 5
No. 183 exposure increased to 1.0 in day 4 at 5
*When No. 198 infected, Exposure is 2.0 in day 4 at move 5
No. 200 exposure increased to 2.0 in day 4 at 5
No. 204 exposure increased to 1.0 in day 4 at 5
No. 220 exposure increased to 2.0 in day 4 at 5
*When No. 233 infected, Exposure is 2.0 in day 4 at move 5
No. 241 exposure increased to 3.0 in day 4 at 5
No. 266 exposure increased to 3.0 in day 4 at 5
No. 267 exposure increased to 2.0 in day 4 at 5
No. 269 exposure increased to 5.0 in day 4 at 5
No. 274 exposure increased to 1.0 in day 4 at 5
No. 281 exposure increased to 3.0 in day 4 at 5
No. 291 exposure increased to 1.0 in day 4 at 5
No. 339 exposure increased to 1.0 in day 4 at 5
No. 340 exposure increased to 1.0 in day 4 at 5
No. 341 exposure increased to 2.0 in day 4 at 5
No. 343 exposure increased to 1.0 in day 4 at 5
No. 362 exposure increased to 2.0 in day 4 at 5
No. 379 exposure increased to 1.0 in day 4 at 5
No. 387 exposure increased to 1.0 in day 4 at 5
No. 389 exposure increased to 3.0 in day 4 at 5
No. 405 exposure increased to 4.0 in day 4 at 5
No. 436 exposure increased to 3.0 in day 4 at 5
No. 441 exposure increased to 3.0 in day 4 at 5
No. 446 exposure increased to 1.0 in day 4 at 5
No. 448 exposure increased to 1.0 in day 4 at 5
No. 459 exposure increased to 3.0 in day 4 at 5
No. 473 exposure increased to 4.0 in day 4 at 5
No. 507 exposure increased to 2.0 in day 4 at 5
No. 514 exposure increased to 1.0 in day 4 at 5
No. 520 exposure increased to 1.0 in day 4 at 5
No. 526 exposure increased to 3.0 in day 4 at 5
No. 535 exposure increased to 3.0 in day 4 at 5
No. 537 exposure increased to 2.0 in day 4 at 5
No. 560 exposure increased to 2.0 in day 4 at 5
No. 567 exposure increased to 3.0 in day 4 at 5
No. 569 exposure increased to 3.0 in day 4 at 5
No. 575 exposure increased to 1.0 in day 4 at 5
No. 580 exposure increased to 4.0 in day 4 at 5
No. 581 exposure increased to 1.0 in day 4 at 5
No. 584 exposure increased to 2.0 in day 4 at 5
No. 590 exposure increased to 1.0 in day 4 at 5
*When No. 598 infected, Exposure is 3.0 in day 4 at move 5
No. 605 exposure increased to 3.0 in day 4 at 5
No. 616 exposure increased to 4.0 in day 4 at 5
No. 619 exposure increased to 3.0 in day 4 at 5
No. 624 exposure increased to 2.0 in day 4 at 5
No. 633 exposure increased to 2.0 in day 4 at 5
No. 641 exposure increased to 3.0 in day 4 at 5
No. 655 exposure increased to 3.0 in day 4 at 5
No. 672 exposure increased to 2.0 in day 4 at 5
No. 673 exposure increased to 3.0 in day 4 at 5
No. 677 exposure increased to 2.0 in day 4 at 5
No. 680 exposure increased to 3.0 in day 4 at 5
No. 686 exposure increased to 2.0 in day 4 at 5
No. 691 exposure increased to 3.0 in day 4 at 5
No. 694 exposure increased to 1.0 in day 4 at 5
No. 696 exposure increased to 1.0 in day 4 at 5
No. 710 exposure increased to 3.0 in day 4 at 5
No. 711 exposure increased to 1.0 in day 4 at 5
No. 731 exposure increased to 3.0 in day 4 at 5
No. 738 exposure increased to 3.0 in day 4 at 5
No. 746 exposure increased to 3.0 in day 4 at 5
No. 772 exposure increased to 4.0 in day 4 at 5
No. 784 exposure increased to 1.0 in day 4 at 5
No. 785 exposure increased to 3.0 in day 4 at 5
No. 789 exposure increased to 4.0 in day 4 at 5
No. 803 exposure increased to 2.0 in day 4 at 5
No. 821 exposure increased to 4.0 in day 4 at 5
*When No. 828 infected, Exposure is 3.0 in day 4 at move 5
No. 830 exposure increased to 1.0 in day 4 at 5
No. 834 exposure increased to 3.0 in day 4 at 5
No. 839 exposure increased to 1.0 in day 4 at 5
No. 842 exposure increased to 1.0 in day 4 at 5
No. 851 exposure increased to 3.0 in day 4 at 5
No. 852 exposure increased to 3.0 in day 4 at 5
No. 856 exposure increased to 3.0 in day 4 at 5
No. 858 exposure increased to 3.0 in day 4 at 5
*When No. 862 infected, Exposure is 4.0 in day 4 at move 5
No. 869 exposure increased to 4.0 in day 4 at 5
No. 873 exposure increased to 4.0 in day 4 at 5
No. 886 exposure increased to 3.0 in day 4 at 5
No. 889 exposure increased to 3.0 in day 4 at 5
No. 895 exposure increased to 1.0 in day 4 at 5
No. 899 exposure increased to 1.0 in day 4 at 5
No. 907 exposure increased to 2.0 in day 4 at 5
No. 908 exposure increased to 2.0 in day 4 at 5
No. 917 exposure increased to 2.0 in day 4 at 5
No. 934 exposure increased to 3.0 in day 4 at 5
No. 935 exposure increased to 3.0 in day 4 at 5
No. 958 exposure increased to 4.0 in day 4 at 5
No. 963 exposure increased to 5.0 in day 4 at 5
No. 964 exposure increased to 4.0 in day 4 at 5
No. 975 exposure increased to 1.0 in day 4 at 5
No. 989 exposure increased to 1.0 in day 4 at 5
*When No. 998 infected, Exposure is 4.0 in day 4 at move 5
   29/10000 [..............................] - ETA: 31:10:27 - reward: 787.3641*When No. 73 infected, Exposure is 4.0 in day 4 at move 0
*When No. 116 infected, Exposure is 4.0 in day 4 at move 0
*When No. 156 infected, Exposure is 4.0 in day 4 at move 0
*When No. 266 infected, Exposure is 3.0 in day 4 at move 0
*When No. 441 infected, Exposure is 3.0 in day 4 at move 0
*When No. 655 infected, Exposure is 3.0 in day 4 at move 0
*When No. 680 infected, Exposure is 3.0 in day 4 at move 0
*When No. 710 infected, Exposure is 3.0 in day 4 at move 0
*When No. 731 infected, Exposure is 3.0 in day 4 at move 0
*When No. 803 infected, Exposure is 2.0 in day 4 at move 0
*When No. 869 infected, Exposure is 4.0 in day 4 at move 0
*When No. 907 infected, Exposure is 2.0 in day 4 at move 0
*When No. 958 infected, Exposure is 4.0 in day 4 at move 0
No. 10 exposure increased to 2.0 in day 4 at 1
No. 18 exposure increased to 3.0 in day 4 at 1
*When No. 24 infected, Exposure is 2.0 in day 4 at move 1
No. 33 exposure increased to 4.0 in day 4 at 1
No. 37 exposure increased to 3.0 in day 4 at 1
No. 63 exposure increased to 4.0 in day 4 at 1
No. 76 exposure increased to 2.0 in day 4 at 1
No. 81 exposure increased to 2.0 in day 4 at 1
No. 83 exposure increased to 2.0 in day 4 at 1
No. 89 exposure increased to 3.0 in day 4 at 1
No. 94 exposure increased to 2.0 in day 4 at 1
No. 95 exposure increased to 2.0 in day 4 at 1
No. 106 exposure increased to 2.0 in day 4 at 1
No. 109 exposure increased to 4.0 in day 4 at 1
No. 119 exposure increased to 2.0 in day 4 at 1
No. 133 exposure increased to 4.0 in day 4 at 1
No. 135 exposure increased to 2.0 in day 4 at 1
No. 143 exposure increased to 2.0 in day 4 at 1
No. 147 exposure increased to 6.0 in day 4 at 1
No. 173 exposure increased to 2.0 in day 4 at 1
No. 183 exposure increased to 2.0 in day 4 at 1
No. 200 exposure increased to 3.0 in day 4 at 1
No. 201 exposure increased to 1.0 in day 4 at 1
No. 204 exposure increased to 2.0 in day 4 at 1
No. 206 exposure increased to 2.0 in day 4 at 1
*When No. 220 infected, Exposure is 2.0 in day 4 at move 1
No. 238 exposure increased to 1.0 in day 4 at 1
No. 241 exposure increased to 4.0 in day 4 at 1
No. 260 exposure increased to 1.0 in day 4 at 1
No. 267 exposure increased to 3.0 in day 4 at 1
*When No. 269 infected, Exposure is 5.0 in day 4 at move 1
No. 274 exposure increased to 2.0 in day 4 at 1
*When No. 281 infected, Exposure is 3.0 in day 4 at move 1
No. 291 exposure increased to 2.0 in day 4 at 1
No. 301 exposure increased to 2.0 in day 4 at 1
No. 339 exposure increased to 2.0 in day 4 at 1
No. 340 exposure increased to 2.0 in day 4 at 1
No. 341 exposure increased to 3.0 in day 4 at 1
No. 343 exposure increased to 2.0 in day 4 at 1
No. 362 exposure increased to 3.0 in day 4 at 1
No. 379 exposure increased to 2.0 in day 4 at 1
No. 387 exposure increased to 2.0 in day 4 at 1
No. 389 exposure increased to 4.0 in day 4 at 1
No. 405 exposure increased to 5.0 in day 4 at 1
No. 435 exposure increased to 2.0 in day 4 at 1
No. 436 exposure increased to 4.0 in day 4 at 1
No. 446 exposure increased to 2.0 in day 4 at 1
No. 448 exposure increased to 2.0 in day 4 at 1
No. 459 exposure increased to 4.0 in day 4 at 1
No. 461 exposure increased to 1.0 in day 4 at 1
No. 469 exposure increased to 1.0 in day 4 at 1
No. 473 exposure increased to 5.0 in day 4 at 1
No. 474 exposure increased to 2.0 in day 4 at 1
No. 483 exposure increased to 1.0 in day 4 at 1
No. 507 exposure increased to 3.0 in day 4 at 1
No. 514 exposure increased to 2.0 in day 4 at 1
No. 520 exposure increased to 2.0 in day 4 at 1
No. 526 exposure increased to 4.0 in day 4 at 1
No. 535 exposure increased to 4.0 in day 4 at 1
No. 537 exposure increased to 3.0 in day 4 at 1
No. 560 exposure increased to 3.0 in day 4 at 1
*When No. 567 infected, Exposure is 3.0 in day 4 at move 1
No. 569 exposure increased to 4.0 in day 4 at 1
No. 575 exposure increased to 2.0 in day 4 at 1
No. 580 exposure increased to 5.0 in day 4 at 1
No. 581 exposure increased to 2.0 in day 4 at 1
No. 584 exposure increased to 3.0 in day 4 at 1
No. 590 exposure increased to 2.0 in day 4 at 1
No. 605 exposure increased to 4.0 in day 4 at 1
No. 611 exposure increased to 2.0 in day 4 at 1
No. 614 exposure increased to 1.0 in day 4 at 1
*When No. 616 infected, Exposure is 4.0 in day 4 at move 1
No. 619 exposure increased to 4.0 in day 4 at 1
No. 624 exposure increased to 3.0 in day 4 at 1
No. 633 exposure increased to 3.0 in day 4 at 1
No. 641 exposure increased to 4.0 in day 4 at 1
No. 672 exposure increased to 3.0 in day 4 at 1
*When No. 673 infected, Exposure is 3.0 in day 4 at move 1
No. 677 exposure increased to 3.0 in day 4 at 1
No. 686 exposure increased to 3.0 in day 4 at 1
No. 691 exposure increased to 4.0 in day 4 at 1
No. 694 exposure increased to 2.0 in day 4 at 1
No. 696 exposure increased to 2.0 in day 4 at 1
No. 706 exposure increased to 2.0 in day 4 at 1
No. 711 exposure increased to 2.0 in day 4 at 1
No. 735 exposure increased to 1.0 in day 4 at 1
*When No. 738 infected, Exposure is 3.0 in day 4 at move 1
No. 740 exposure increased to 2.0 in day 4 at 1
No. 746 exposure increased to 4.0 in day 4 at 1
*When No. 772 infected, Exposure is 4.0 in day 4 at move 1
No. 784 exposure increased to 2.0 in day 4 at 1
No. 785 exposure increased to 4.0 in day 4 at 1
No. 789 exposure increased to 5.0 in day 4 at 1
*When No. 821 infected, Exposure is 4.0 in day 4 at move 1
No. 830 exposure increased to 2.0 in day 4 at 1
No. 832 exposure increased to 1.0 in day 4 at 1
No. 833 exposure increased to 2.0 in day 4 at 1
No. 834 exposure increased to 4.0 in day 4 at 1
No. 839 exposure increased to 2.0 in day 4 at 1
No. 842 exposure increased to 2.0 in day 4 at 1
No. 851 exposure increased to 4.0 in day 4 at 1
No. 852 exposure increased to 4.0 in day 4 at 1
No. 856 exposure increased to 4.0 in day 4 at 1
No. 858 exposure increased to 4.0 in day 4 at 1
*When No. 873 infected, Exposure is 4.0 in day 4 at move 1
No. 886 exposure increased to 4.0 in day 4 at 1
No. 889 exposure increased to 4.0 in day 4 at 1
No. 895 exposure increased to 2.0 in day 4 at 1
No. 899 exposure increased to 2.0 in day 4 at 1
No. 904 exposure increased to 2.0 in day 4 at 1
No. 908 exposure increased to 3.0 in day 4 at 1
No. 917 exposure increased to 3.0 in day 4 at 1
No. 934 exposure increased to 4.0 in day 4 at 1
No. 935 exposure increased to 4.0 in day 4 at 1
No. 962 exposure increased to 2.0 in day 4 at 1
No. 963 exposure increased to 6.0 in day 4 at 1
No. 964 exposure increased to 5.0 in day 4 at 1
No. 965 exposure increased to 2.0 in day 4 at 1
No. 969 exposure increased to 1.0 in day 4 at 1
No. 975 exposure increased to 2.0 in day 4 at 1
No. 989 exposure increased to 2.0 in day 4 at 1
   30/10000 [..............................] - ETA: 30:28:22 - reward: 775.0020*When No. 10 infected, Exposure is 2.0 in day 4 at move 0
*When No. 18 infected, Exposure is 3.0 in day 4 at move 0
*When No. 33 infected, Exposure is 4.0 in day 4 at move 0
*When No. 63 infected, Exposure is 4.0 in day 4 at move 0
*When No. 119 infected, Exposure is 2.0 in day 4 at move 0
*When No. 133 infected, Exposure is 4.0 in day 4 at move 0
*When No. 147 infected, Exposure is 6.0 in day 4 at move 0
*When No. 206 infected, Exposure is 2.0 in day 4 at move 0
*When No. 339 infected, Exposure is 2.0 in day 4 at move 0
*When No. 436 infected, Exposure is 4.0 in day 4 at move 0
*When No. 473 infected, Exposure is 5.0 in day 4 at move 0
*When No. 507 infected, Exposure is 3.0 in day 4 at move 0
*When No. 580 infected, Exposure is 5.0 in day 4 at move 0
*When No. 633 infected, Exposure is 3.0 in day 4 at move 0
*When No. 691 infected, Exposure is 4.0 in day 4 at move 0
*When No. 886 infected, Exposure is 4.0 in day 4 at move 0
*When No. 934 infected, Exposure is 4.0 in day 4 at move 0
*When No. 935 infected, Exposure is 4.0 in day 4 at move 0
*When No. 989 infected, Exposure is 2.0 in day 4 at move 0
No. 0 exposure increased to 1.0 in day 4 at 1
*When No. 37 infected, Exposure is 3.0 in day 4 at move 1
No. 76 exposure increased to 3.0 in day 4 at 1
No. 81 exposure increased to 3.0 in day 4 at 1
No. 83 exposure increased to 3.0 in day 4 at 1
No. 89 exposure increased to 4.0 in day 4 at 1
No. 91 exposure increased to 1.0 in day 4 at 1
No. 94 exposure increased to 3.0 in day 4 at 1
No. 95 exposure increased to 3.0 in day 4 at 1
No. 106 exposure increased to 3.0 in day 4 at 1
No. 109 exposure increased to 5.0 in day 4 at 1
No. 112 exposure increased to 2.0 in day 4 at 1
No. 135 exposure increased to 3.0 in day 4 at 1
No. 143 exposure increased to 3.0 in day 4 at 1
No. 167 exposure increased to 2.0 in day 4 at 1
No. 173 exposure increased to 3.0 in day 4 at 1
No. 183 exposure increased to 3.0 in day 4 at 1
No. 191 exposure increased to 2.0 in day 4 at 1
No. 193 exposure increased to 1.0 in day 4 at 1
No. 200 exposure increased to 4.0 in day 4 at 1
No. 201 exposure increased to 2.0 in day 4 at 1
No. 204 exposure increased to 3.0 in day 4 at 1
No. 234 exposure increased to 1.0 in day 4 at 1
No. 238 exposure increased to 2.0 in day 4 at 1
No. 241 exposure increased to 5.0 in day 4 at 1
No. 260 exposure increased to 2.0 in day 4 at 1
No. 267 exposure increased to 4.0 in day 4 at 1
No. 274 exposure increased to 3.0 in day 4 at 1
No. 277 exposure increased to 1.0 in day 4 at 1
No. 291 exposure increased to 3.0 in day 4 at 1
No. 301 exposure increased to 3.0 in day 4 at 1
No. 317 exposure increased to 1.0 in day 4 at 1
No. 331 exposure increased to 2.0 in day 4 at 1
No. 340 exposure increased to 3.0 in day 4 at 1
No. 341 exposure increased to 4.0 in day 4 at 1
No. 343 exposure increased to 3.0 in day 4 at 1
No. 350 exposure increased to 1.0 in day 4 at 1
No. 355 exposure increased to 2.0 in day 4 at 1
No. 362 exposure increased to 4.0 in day 4 at 1
No. 379 exposure increased to 3.0 in day 4 at 1
No. 387 exposure increased to 3.0 in day 4 at 1
No. 389 exposure increased to 5.0 in day 4 at 1
No. 397 exposure increased to 2.0 in day 4 at 1
*When No. 405 infected, Exposure is 5.0 in day 4 at move 1
No. 434 exposure increased to 2.0 in day 4 at 1
No. 435 exposure increased to 3.0 in day 4 at 1
No. 446 exposure increased to 3.0 in day 4 at 1
No. 448 exposure increased to 3.0 in day 4 at 1
No. 458 exposure increased to 1.0 in day 4 at 1
*When No. 459 infected, Exposure is 4.0 in day 4 at move 1
No. 461 exposure increased to 2.0 in day 4 at 1
No. 469 exposure increased to 2.0 in day 4 at 1
No. 474 exposure increased to 3.0 in day 4 at 1
No. 483 exposure increased to 2.0 in day 4 at 1
No. 505 exposure increased to 1.0 in day 4 at 1
No. 514 exposure increased to 3.0 in day 4 at 1
No. 520 exposure increased to 3.0 in day 4 at 1
*When No. 526 infected, Exposure is 4.0 in day 4 at move 1
*When No. 535 infected, Exposure is 4.0 in day 4 at move 1
*When No. 537 infected, Exposure is 3.0 in day 4 at move 1
No. 540 exposure increased to 1.0 in day 4 at 1
No. 560 exposure increased to 4.0 in day 4 at 1
No. 563 exposure increased to 2.0 in day 4 at 1
No. 569 exposure increased to 5.0 in day 4 at 1
No. 575 exposure increased to 3.0 in day 4 at 1
No. 581 exposure increased to 3.0 in day 4 at 1
No. 584 exposure increased to 4.0 in day 4 at 1
No. 590 exposure increased to 3.0 in day 4 at 1
No. 605 exposure increased to 5.0 in day 4 at 1
No. 611 exposure increased to 3.0 in day 4 at 1
No. 614 exposure increased to 2.0 in day 4 at 1
No. 619 exposure increased to 5.0 in day 4 at 1
*When No. 624 infected, Exposure is 3.0 in day 4 at move 1
No. 636 exposure increased to 1.0 in day 4 at 1
No. 641 exposure increased to 5.0 in day 4 at 1
No. 665 exposure increased to 1.0 in day 4 at 1
No. 668 exposure increased to 1.0 in day 4 at 1
*When No. 672 infected, Exposure is 3.0 in day 4 at move 1
No. 677 exposure increased to 4.0 in day 4 at 1
*When No. 686 infected, Exposure is 3.0 in day 4 at move 1
No. 694 exposure increased to 3.0 in day 4 at 1
No. 696 exposure increased to 3.0 in day 4 at 1
No. 706 exposure increased to 3.0 in day 4 at 1
No. 711 exposure increased to 3.0 in day 4 at 1
No. 735 exposure increased to 2.0 in day 4 at 1
No. 740 exposure increased to 3.0 in day 4 at 1
No. 746 exposure increased to 5.0 in day 4 at 1
No. 750 exposure increased to 2.0 in day 4 at 1
No. 784 exposure increased to 3.0 in day 4 at 1
No. 785 exposure increased to 5.0 in day 4 at 1
No. 789 exposure increased to 6.0 in day 4 at 1
No. 830 exposure increased to 3.0 in day 4 at 1
No. 832 exposure increased to 2.0 in day 4 at 1
No. 833 exposure increased to 3.0 in day 4 at 1
No. 834 exposure increased to 5.0 in day 4 at 1
No. 839 exposure increased to 3.0 in day 4 at 1
No. 842 exposure increased to 3.0 in day 4 at 1
No. 851 exposure increased to 5.0 in day 4 at 1
No. 852 exposure increased to 5.0 in day 4 at 1
*When No. 856 infected, Exposure is 4.0 in day 4 at move 1
No. 858 exposure increased to 5.0 in day 4 at 1
No. 889 exposure increased to 5.0 in day 4 at 1
No. 895 exposure increased to 3.0 in day 4 at 1
No. 899 exposure increased to 3.0 in day 4 at 1
No. 904 exposure increased to 3.0 in day 4 at 1
*When No. 908 infected, Exposure is 3.0 in day 4 at move 1
No. 917 exposure increased to 4.0 in day 4 at 1
No. 929 exposure increased to 1.0 in day 4 at 1
No. 962 exposure increased to 3.0 in day 4 at 1
*When No. 963 infected, Exposure is 6.0 in day 4 at move 1
No. 964 exposure increased to 6.0 in day 4 at 1
No. 965 exposure increased to 3.0 in day 4 at 1
No. 969 exposure increased to 2.0 in day 4 at 1
No. 975 exposure increased to 3.0 in day 4 at 1
No. 990 exposure increased to 1.0 in day 4 at 1
   31/10000 [..............................] - ETA: 29:47:14 - reward: 762.2961*When No. 76 infected, Exposure is 3.0 in day 4 at move 0
*When No. 135 infected, Exposure is 3.0 in day 4 at move 0
*When No. 238 infected, Exposure is 2.0 in day 4 at move 0
*When No. 267 infected, Exposure is 4.0 in day 4 at move 0
*When No. 362 infected, Exposure is 4.0 in day 4 at move 0
*When No. 389 infected, Exposure is 5.0 in day 4 at move 0
*When No. 514 infected, Exposure is 3.0 in day 4 at move 0
*When No. 560 infected, Exposure is 4.0 in day 4 at move 0
*When No. 575 infected, Exposure is 3.0 in day 4 at move 0
*When No. 584 infected, Exposure is 4.0 in day 4 at move 0
*When No. 605 infected, Exposure is 5.0 in day 4 at move 0
*When No. 677 infected, Exposure is 4.0 in day 4 at move 0
*When No. 746 infected, Exposure is 5.0 in day 4 at move 0
*When No. 785 infected, Exposure is 5.0 in day 4 at move 0
*When No. 789 infected, Exposure is 6.0 in day 4 at move 0
*When No. 834 infected, Exposure is 5.0 in day 4 at move 0
*When No. 858 infected, Exposure is 5.0 in day 4 at move 0
*When No. 889 infected, Exposure is 5.0 in day 4 at move 0
*When No. 895 infected, Exposure is 3.0 in day 4 at move 0
*When No. 962 infected, Exposure is 3.0 in day 4 at move 0
*When No. 81 infected, Exposure is 3.0 in day 4 at move 1
*When No. 89 infected, Exposure is 4.0 in day 4 at move 1
*When No. 109 infected, Exposure is 5.0 in day 4 at move 1
*When No. 341 infected, Exposure is 4.0 in day 4 at move 1
*When No. 397 infected, Exposure is 2.0 in day 4 at move 1
*When No. 474 infected, Exposure is 3.0 in day 4 at move 1
*When No. 520 infected, Exposure is 3.0 in day 4 at move 1
*When No. 619 infected, Exposure is 5.0 in day 4 at move 1
*When No. 694 infected, Exposure is 3.0 in day 4 at move 1
*When No. 696 infected, Exposure is 3.0 in day 4 at move 1
*When No. 706 infected, Exposure is 3.0 in day 4 at move 1
*When No. 740 infected, Exposure is 3.0 in day 4 at move 1
*When No. 839 infected, Exposure is 3.0 in day 4 at move 1
*When No. 904 infected, Exposure is 3.0 in day 4 at move 1
*When No. 969 infected, Exposure is 2.0 in day 4 at move 1
*When No. 95 infected, Exposure is 3.0 in day 4 at move 2
*When No. 143 infected, Exposure is 3.0 in day 4 at move 2
*When No. 191 infected, Exposure is 2.0 in day 4 at move 2
*When No. 241 infected, Exposure is 5.0 in day 4 at move 2
*When No. 274 infected, Exposure is 3.0 in day 4 at move 2
*When No. 291 infected, Exposure is 3.0 in day 4 at move 2
*When No. 340 infected, Exposure is 3.0 in day 4 at move 2
*When No. 563 infected, Exposure is 2.0 in day 4 at move 2
*When No. 569 infected, Exposure is 5.0 in day 4 at move 2
*When No. 611 infected, Exposure is 3.0 in day 4 at move 2
*When No. 641 infected, Exposure is 5.0 in day 4 at move 2
*When No. 830 infected, Exposure is 3.0 in day 4 at move 2
*When No. 964 infected, Exposure is 6.0 in day 4 at move 2
*When No. 965 infected, Exposure is 3.0 in day 4 at move 2
*When No. 200 infected, Exposure is 4.0 in day 4 at move 3
*When No. 201 infected, Exposure is 2.0 in day 4 at move 3
*When No. 301 infected, Exposure is 3.0 in day 4 at move 3
*When No. 331 infected, Exposure is 2.0 in day 4 at move 3
*When No. 343 infected, Exposure is 3.0 in day 4 at move 3
*When No. 387 infected, Exposure is 3.0 in day 4 at move 3
*When No. 448 infected, Exposure is 3.0 in day 4 at move 3
*When No. 461 infected, Exposure is 2.0 in day 4 at move 3
*When No. 851 infected, Exposure is 5.0 in day 4 at move 3
*When No. 852 infected, Exposure is 5.0 in day 4 at move 3
*When No. 975 infected, Exposure is 3.0 in day 4 at move 3
*When No. 83 infected, Exposure is 3.0 in day 4 at move 4
*When No. 173 infected, Exposure is 3.0 in day 4 at move 4
*When No. 379 infected, Exposure is 3.0 in day 4 at move 4
*When No. 784 infected, Exposure is 3.0 in day 4 at move 4
*When No. 833 infected, Exposure is 3.0 in day 4 at move 4
No. 0 exposure increased to 2.0 in day 4 at 5
No. 3 exposure increased to 1.0 in day 4 at 5
No. 29 exposure increased to 1.0 in day 4 at 5
No. 48 exposure increased to 1.0 in day 4 at 5
No. 52 exposure increased to 1.0 in day 4 at 5
No. 53 exposure increased to 1.0 in day 4 at 5
No. 68 exposure increased to 1.0 in day 4 at 5
No. 87 exposure increased to 1.0 in day 4 at 5
No. 91 exposure increased to 2.0 in day 4 at 5
No. 94 exposure increased to 4.0 in day 4 at 5
No. 96 exposure increased to 1.0 in day 4 at 5
No. 103 exposure increased to 1.0 in day 4 at 5
No. 106 exposure increased to 4.0 in day 4 at 5
No. 112 exposure increased to 3.0 in day 4 at 5
No. 125 exposure increased to 1.0 in day 4 at 5
No. 128 exposure increased to 1.0 in day 4 at 5
No. 138 exposure increased to 1.0 in day 4 at 5
No. 161 exposure increased to 1.0 in day 4 at 5
No. 166 exposure increased to 2.0 in day 4 at 5
No. 167 exposure increased to 3.0 in day 4 at 5
No. 183 exposure increased to 4.0 in day 4 at 5
No. 185 exposure increased to 1.0 in day 4 at 5
No. 187 exposure increased to 1.0 in day 4 at 5
No. 193 exposure increased to 2.0 in day 4 at 5
No. 202 exposure increased to 1.0 in day 4 at 5
No. 204 exposure increased to 4.0 in day 4 at 5
No. 226 exposure increased to 1.0 in day 4 at 5
No. 234 exposure increased to 2.0 in day 4 at 5
No. 239 exposure increased to 2.0 in day 4 at 5
No. 246 exposure increased to 1.0 in day 4 at 5
No. 260 exposure increased to 3.0 in day 4 at 5
No. 264 exposure increased to 1.0 in day 4 at 5
No. 277 exposure increased to 2.0 in day 4 at 5
No. 278 exposure increased to 1.0 in day 4 at 5
No. 287 exposure increased to 1.0 in day 4 at 5
No. 317 exposure increased to 2.0 in day 4 at 5
No. 338 exposure increased to 2.0 in day 4 at 5
No. 345 exposure increased to 1.0 in day 4 at 5
No. 347 exposure increased to 1.0 in day 4 at 5
No. 350 exposure increased to 2.0 in day 4 at 5
No. 353 exposure increased to 1.0 in day 4 at 5
No. 355 exposure increased to 3.0 in day 4 at 5
No. 386 exposure increased to 1.0 in day 4 at 5
No. 390 exposure increased to 1.0 in day 4 at 5
No. 406 exposure increased to 1.0 in day 4 at 5
No. 407 exposure increased to 1.0 in day 4 at 5
No. 410 exposure increased to 1.0 in day 4 at 5
No. 421 exposure increased to 1.0 in day 4 at 5
No. 431 exposure increased to 1.0 in day 4 at 5
No. 434 exposure increased to 3.0 in day 4 at 5
No. 435 exposure increased to 4.0 in day 4 at 5
No. 443 exposure increased to 1.0 in day 4 at 5
No. 446 exposure increased to 4.0 in day 4 at 5
No. 458 exposure increased to 2.0 in day 4 at 5
No. 469 exposure increased to 3.0 in day 4 at 5
No. 480 exposure increased to 1.0 in day 4 at 5
No. 483 exposure increased to 3.0 in day 4 at 5
No. 502 exposure increased to 2.0 in day 4 at 5
No. 505 exposure increased to 2.0 in day 4 at 5
No. 532 exposure increased to 1.0 in day 4 at 5
No. 540 exposure increased to 2.0 in day 4 at 5
No. 542 exposure increased to 1.0 in day 4 at 5
No. 544 exposure increased to 1.0 in day 4 at 5
No. 581 exposure increased to 4.0 in day 4 at 5
*When No. 590 infected, Exposure is 3.0 in day 4 at move 5
No. 595 exposure increased to 1.0 in day 4 at 5
No. 612 exposure increased to 1.0 in day 4 at 5
*When No. 614 infected, Exposure is 2.0 in day 4 at move 5
No. 615 exposure increased to 2.0 in day 4 at 5
No. 617 exposure increased to 1.0 in day 4 at 5
No. 636 exposure increased to 2.0 in day 4 at 5
No. 639 exposure increased to 1.0 in day 4 at 5
No. 656 exposure increased to 1.0 in day 4 at 5
No. 665 exposure increased to 2.0 in day 4 at 5
No. 668 exposure increased to 2.0 in day 4 at 5
No. 681 exposure increased to 1.0 in day 4 at 5
No. 697 exposure increased to 1.0 in day 4 at 5
No. 700 exposure increased to 1.0 in day 4 at 5
No. 705 exposure increased to 1.0 in day 4 at 5
No. 708 exposure increased to 1.0 in day 4 at 5
*When No. 711 infected, Exposure is 3.0 in day 4 at move 5
No. 715 exposure increased to 1.0 in day 4 at 5
No. 721 exposure increased to 1.0 in day 4 at 5
No. 735 exposure increased to 3.0 in day 4 at 5
No. 737 exposure increased to 2.0 in day 4 at 5
No. 750 exposure increased to 3.0 in day 4 at 5
No. 760 exposure increased to 1.0 in day 4 at 5
No. 795 exposure increased to 1.0 in day 4 at 5
No. 798 exposure increased to 1.0 in day 4 at 5
No. 809 exposure increased to 2.0 in day 4 at 5
No. 823 exposure increased to 1.0 in day 4 at 5
No. 832 exposure increased to 3.0 in day 4 at 5
No. 842 exposure increased to 4.0 in day 4 at 5
No. 843 exposure increased to 1.0 in day 4 at 5
No. 874 exposure increased to 1.0 in day 4 at 5
No. 899 exposure increased to 4.0 in day 4 at 5
No. 910 exposure increased to 1.0 in day 4 at 5
No. 911 exposure increased to 1.0 in day 4 at 5
No. 917 exposure increased to 5.0 in day 4 at 5
No. 922 exposure increased to 1.0 in day 4 at 5
No. 929 exposure increased to 2.0 in day 4 at 5
No. 932 exposure increased to 1.0 in day 4 at 5
No. 982 exposure increased to 1.0 in day 4 at 5
No. 990 exposure increased to 2.0 in day 4 at 5
   32/10000 [..............................] - ETA: 29:39:57 - reward: 747.5006*When No. 166 infected, Exposure is 2.0 in day 4 at move 0
*When No. 204 infected, Exposure is 4.0 in day 4 at move 0
*When No. 260 infected, Exposure is 3.0 in day 4 at move 0
*When No. 355 infected, Exposure is 3.0 in day 4 at move 0
*When No. 615 infected, Exposure is 2.0 in day 4 at move 0
*When No. 809 infected, Exposure is 2.0 in day 4 at move 0
*When No. 842 infected, Exposure is 4.0 in day 4 at move 0
*When No. 899 infected, Exposure is 4.0 in day 4 at move 0
*When No. 0 infected, Exposure is 2.0 in day 4 at move 1
No. 3 exposure increased to 2.0 in day 4 at 1
No. 29 exposure increased to 2.0 in day 4 at 1
No. 48 exposure increased to 2.0 in day 4 at 1
No. 52 exposure increased to 2.0 in day 4 at 1
No. 53 exposure increased to 2.0 in day 4 at 1
No. 68 exposure increased to 2.0 in day 4 at 1
No. 87 exposure increased to 2.0 in day 4 at 1
No. 91 exposure increased to 3.0 in day 4 at 1
No. 94 exposure increased to 5.0 in day 4 at 1
No. 96 exposure increased to 2.0 in day 4 at 1
No. 101 exposure increased to 1.0 in day 4 at 1
No. 103 exposure increased to 2.0 in day 4 at 1
No. 106 exposure increased to 5.0 in day 4 at 1
No. 112 exposure increased to 4.0 in day 4 at 1
No. 121 exposure increased to 1.0 in day 4 at 1
No. 125 exposure increased to 2.0 in day 4 at 1
No. 128 exposure increased to 2.0 in day 4 at 1
No. 138 exposure increased to 2.0 in day 4 at 1
No. 161 exposure increased to 2.0 in day 4 at 1
No. 167 exposure increased to 4.0 in day 4 at 1
No. 183 exposure increased to 5.0 in day 4 at 1
No. 185 exposure increased to 2.0 in day 4 at 1
No. 187 exposure increased to 2.0 in day 4 at 1
No. 193 exposure increased to 3.0 in day 4 at 1
No. 202 exposure increased to 2.0 in day 4 at 1
No. 226 exposure increased to 2.0 in day 4 at 1
No. 234 exposure increased to 3.0 in day 4 at 1
No. 239 exposure increased to 3.0 in day 4 at 1
No. 246 exposure increased to 2.0 in day 4 at 1
No. 264 exposure increased to 2.0 in day 4 at 1
No. 277 exposure increased to 3.0 in day 4 at 1
No. 278 exposure increased to 2.0 in day 4 at 1
No. 287 exposure increased to 2.0 in day 4 at 1
No. 312 exposure increased to 2.0 in day 4 at 1
*When No. 317 infected, Exposure is 2.0 in day 4 at move 1
No. 338 exposure increased to 3.0 in day 4 at 1
No. 345 exposure increased to 2.0 in day 4 at 1
No. 347 exposure increased to 2.0 in day 4 at 1
No. 350 exposure increased to 3.0 in day 4 at 1
No. 352 exposure increased to 1.0 in day 4 at 1
No. 353 exposure increased to 2.0 in day 4 at 1
No. 374 exposure increased to 1.0 in day 4 at 1
No. 386 exposure increased to 2.0 in day 4 at 1
No. 388 exposure increased to 2.0 in day 4 at 1
No. 390 exposure increased to 2.0 in day 4 at 1
No. 406 exposure increased to 2.0 in day 4 at 1
No. 407 exposure increased to 2.0 in day 4 at 1
No. 410 exposure increased to 2.0 in day 4 at 1
No. 421 exposure increased to 2.0 in day 4 at 1
No. 431 exposure increased to 2.0 in day 4 at 1
No. 434 exposure increased to 4.0 in day 4 at 1
No. 435 exposure increased to 5.0 in day 4 at 1
No. 443 exposure increased to 2.0 in day 4 at 1
No. 446 exposure increased to 5.0 in day 4 at 1
No. 458 exposure increased to 3.0 in day 4 at 1
No. 469 exposure increased to 4.0 in day 4 at 1
No. 480 exposure increased to 2.0 in day 4 at 1
No. 483 exposure increased to 4.0 in day 4 at 1
No. 502 exposure increased to 3.0 in day 4 at 1
No. 505 exposure increased to 3.0 in day 4 at 1
No. 506 exposure increased to 1.0 in day 4 at 1
No. 532 exposure increased to 2.0 in day 4 at 1
No. 540 exposure increased to 3.0 in day 4 at 1
No. 542 exposure increased to 2.0 in day 4 at 1
No. 544 exposure increased to 2.0 in day 4 at 1
No. 581 exposure increased to 5.0 in day 4 at 1
No. 595 exposure increased to 2.0 in day 4 at 1
No. 612 exposure increased to 2.0 in day 4 at 1
No. 617 exposure increased to 2.0 in day 4 at 1
*When No. 636 infected, Exposure is 2.0 in day 4 at move 1
No. 639 exposure increased to 2.0 in day 4 at 1
No. 656 exposure increased to 2.0 in day 4 at 1
No. 665 exposure increased to 3.0 in day 4 at 1
No. 668 exposure increased to 3.0 in day 4 at 1
No. 681 exposure increased to 2.0 in day 4 at 1
No. 697 exposure increased to 2.0 in day 4 at 1
No. 699 exposure increased to 1.0 in day 4 at 1
No. 700 exposure increased to 2.0 in day 4 at 1
No. 705 exposure increased to 2.0 in day 4 at 1
No. 708 exposure increased to 2.0 in day 4 at 1
No. 715 exposure increased to 2.0 in day 4 at 1
No. 721 exposure increased to 2.0 in day 4 at 1
No. 735 exposure increased to 4.0 in day 4 at 1
No. 737 exposure increased to 3.0 in day 4 at 1
No. 750 exposure increased to 4.0 in day 4 at 1
No. 759 exposure increased to 2.0 in day 4 at 1
No. 760 exposure increased to 2.0 in day 4 at 1
No. 795 exposure increased to 2.0 in day 4 at 1
No. 798 exposure increased to 2.0 in day 4 at 1
No. 823 exposure increased to 2.0 in day 4 at 1
*When No. 832 infected, Exposure is 3.0 in day 4 at move 1
No. 843 exposure increased to 2.0 in day 4 at 1
No. 868 exposure increased to 2.0 in day 4 at 1
No. 874 exposure increased to 2.0 in day 4 at 1
No. 910 exposure increased to 2.0 in day 4 at 1
No. 911 exposure increased to 2.0 in day 4 at 1
No. 917 exposure increased to 6.0 in day 4 at 1
No. 920 exposure increased to 2.0 in day 4 at 1
No. 922 exposure increased to 2.0 in day 4 at 1
*When No. 929 infected, Exposure is 2.0 in day 4 at move 1
No. 932 exposure increased to 2.0 in day 4 at 1
No. 978 exposure increased to 2.0 in day 4 at 1
No. 982 exposure increased to 2.0 in day 4 at 1
No. 990 exposure increased to 3.0 in day 4 at 1
No. 992 exposure increased to 1.0 in day 4 at 1
   33/10000 [..............................] - ETA: 29:00:08 - reward: 732.8255*When No. 3 infected, Exposure is 2.0 in day 4 at move 0
*When No. 68 infected, Exposure is 2.0 in day 4 at move 0
*When No. 167 infected, Exposure is 4.0 in day 4 at move 0
*When No. 239 infected, Exposure is 3.0 in day 4 at move 0
*When No. 353 infected, Exposure is 2.0 in day 4 at move 0
*When No. 390 infected, Exposure is 2.0 in day 4 at move 0
*When No. 431 infected, Exposure is 2.0 in day 4 at move 0
*When No. 505 infected, Exposure is 3.0 in day 4 at move 0
*When No. 540 infected, Exposure is 3.0 in day 4 at move 0
*When No. 639 infected, Exposure is 2.0 in day 4 at move 0
*When No. 668 infected, Exposure is 3.0 in day 4 at move 0
*When No. 705 infected, Exposure is 2.0 in day 4 at move 0
*When No. 708 infected, Exposure is 2.0 in day 4 at move 0
*When No. 750 infected, Exposure is 4.0 in day 4 at move 0
*When No. 843 infected, Exposure is 2.0 in day 4 at move 0
*When No. 911 infected, Exposure is 2.0 in day 4 at move 0
*When No. 990 infected, Exposure is 3.0 in day 4 at move 0
No. 23 exposure increased to 1.0 in day 4 at 1
No. 29 exposure increased to 3.0 in day 4 at 1
No. 48 exposure increased to 3.0 in day 4 at 1
No. 52 exposure increased to 3.0 in day 4 at 1
*When No. 53 infected, Exposure is 2.0 in day 4 at move 1
No. 87 exposure increased to 3.0 in day 4 at 1
No. 91 exposure increased to 4.0 in day 4 at 1
No. 94 exposure increased to 6.0 in day 4 at 1
*When No. 96 infected, Exposure is 2.0 in day 4 at move 1
No. 101 exposure increased to 2.0 in day 4 at 1
No. 103 exposure increased to 3.0 in day 4 at 1
No. 106 exposure increased to 6.0 in day 4 at 1
No. 112 exposure increased to 5.0 in day 4 at 1
No. 121 exposure increased to 2.0 in day 4 at 1
No. 125 exposure increased to 3.0 in day 4 at 1
No. 128 exposure increased to 3.0 in day 4 at 1
No. 138 exposure increased to 3.0 in day 4 at 1
No. 161 exposure increased to 3.0 in day 4 at 1
*When No. 183 infected, Exposure is 5.0 in day 4 at move 1
No. 185 exposure increased to 3.0 in day 4 at 1
No. 187 exposure increased to 3.0 in day 4 at 1
No. 193 exposure increased to 4.0 in day 4 at 1
No. 202 exposure increased to 3.0 in day 4 at 1
No. 226 exposure increased to 3.0 in day 4 at 1
*When No. 234 infected, Exposure is 3.0 in day 4 at move 1
No. 246 exposure increased to 3.0 in day 4 at 1
No. 253 exposure increased to 1.0 in day 4 at 1
No. 264 exposure increased to 3.0 in day 4 at 1
No. 277 exposure increased to 4.0 in day 4 at 1
No. 278 exposure increased to 3.0 in day 4 at 1
No. 280 exposure increased to 1.0 in day 4 at 1
No. 287 exposure increased to 3.0 in day 4 at 1
No. 312 exposure increased to 3.0 in day 4 at 1
No. 334 exposure increased to 1.0 in day 4 at 1
No. 338 exposure increased to 4.0 in day 4 at 1
No. 345 exposure increased to 3.0 in day 4 at 1
No. 347 exposure increased to 3.0 in day 4 at 1
No. 350 exposure increased to 4.0 in day 4 at 1
No. 352 exposure increased to 2.0 in day 4 at 1
No. 374 exposure increased to 2.0 in day 4 at 1
No. 386 exposure increased to 3.0 in day 4 at 1
No. 388 exposure increased to 3.0 in day 4 at 1
*When No. 406 infected, Exposure is 2.0 in day 4 at move 1
No. 407 exposure increased to 3.0 in day 4 at 1
No. 410 exposure increased to 3.0 in day 4 at 1
*When No. 421 infected, Exposure is 2.0 in day 4 at move 1
*When No. 434 infected, Exposure is 4.0 in day 4 at move 1
No. 435 exposure increased to 6.0 in day 4 at 1
No. 443 exposure increased to 3.0 in day 4 at 1
No. 446 exposure increased to 6.0 in day 4 at 1
No. 457 exposure increased to 1.0 in day 4 at 1
No. 458 exposure increased to 4.0 in day 4 at 1
*When No. 469 infected, Exposure is 4.0 in day 4 at move 1
No. 480 exposure increased to 3.0 in day 4 at 1
No. 483 exposure increased to 5.0 in day 4 at 1
No. 502 exposure increased to 4.0 in day 4 at 1
No. 506 exposure increased to 2.0 in day 4 at 1
No. 532 exposure increased to 3.0 in day 4 at 1
No. 542 exposure increased to 3.0 in day 4 at 1
No. 544 exposure increased to 3.0 in day 4 at 1
No. 564 exposure increased to 2.0 in day 4 at 1
*When No. 581 infected, Exposure is 5.0 in day 4 at move 1
No. 595 exposure increased to 3.0 in day 4 at 1
No. 612 exposure increased to 3.0 in day 4 at 1
No. 617 exposure increased to 3.0 in day 4 at 1
No. 656 exposure increased to 3.0 in day 4 at 1
No. 665 exposure increased to 4.0 in day 4 at 1
No. 681 exposure increased to 3.0 in day 4 at 1
No. 697 exposure increased to 3.0 in day 4 at 1
No. 699 exposure increased to 2.0 in day 4 at 1
No. 700 exposure increased to 3.0 in day 4 at 1
No. 715 exposure increased to 3.0 in day 4 at 1
No. 721 exposure increased to 3.0 in day 4 at 1
*When No. 735 infected, Exposure is 4.0 in day 4 at move 1
No. 737 exposure increased to 4.0 in day 4 at 1
No. 759 exposure increased to 3.0 in day 4 at 1
No. 760 exposure increased to 3.0 in day 4 at 1
No. 767 exposure increased to 1.0 in day 4 at 1
No. 795 exposure increased to 3.0 in day 4 at 1
No. 798 exposure increased to 3.0 in day 4 at 1
No. 814 exposure increased to 2.0 in day 4 at 1
No. 817 exposure increased to 1.0 in day 4 at 1
No. 823 exposure increased to 3.0 in day 4 at 1
No. 841 exposure increased to 1.0 in day 4 at 1
No. 868 exposure increased to 3.0 in day 4 at 1
No. 874 exposure increased to 3.0 in day 4 at 1
No. 910 exposure increased to 3.0 in day 4 at 1
No. 917 exposure increased to 7.0 in day 4 at 1
No. 920 exposure increased to 3.0 in day 4 at 1
No. 922 exposure increased to 3.0 in day 4 at 1
No. 931 exposure increased to 2.0 in day 4 at 1
No. 932 exposure increased to 3.0 in day 4 at 1
No. 978 exposure increased to 3.0 in day 4 at 1
*When No. 982 infected, Exposure is 2.0 in day 4 at move 1
No. 992 exposure increased to 2.0 in day 4 at 1
   34/10000 [..............................] - ETA: 28:21:46 - reward: 718.4976*When No. 48 infected, Exposure is 3.0 in day 4 at move 0
*When No. 91 infected, Exposure is 4.0 in day 4 at move 0
*When No. 94 infected, Exposure is 6.0 in day 4 at move 0
*When No. 106 infected, Exposure is 6.0 in day 4 at move 0
*When No. 138 infected, Exposure is 3.0 in day 4 at move 0
*When No. 185 infected, Exposure is 3.0 in day 4 at move 0
*When No. 187 infected, Exposure is 3.0 in day 4 at move 0
*When No. 277 infected, Exposure is 4.0 in day 4 at move 0
*When No. 278 infected, Exposure is 3.0 in day 4 at move 0
*When No. 350 infected, Exposure is 4.0 in day 4 at move 0
*When No. 446 infected, Exposure is 6.0 in day 4 at move 0
*When No. 483 infected, Exposure is 5.0 in day 4 at move 0
*When No. 502 infected, Exposure is 4.0 in day 4 at move 0
*When No. 542 infected, Exposure is 3.0 in day 4 at move 0
*When No. 544 infected, Exposure is 3.0 in day 4 at move 0
*When No. 617 infected, Exposure is 3.0 in day 4 at move 0
*When No. 759 infected, Exposure is 3.0 in day 4 at move 0
*When No. 760 infected, Exposure is 3.0 in day 4 at move 0
*When No. 920 infected, Exposure is 3.0 in day 4 at move 0
No. 23 exposure increased to 2.0 in day 4 at 1
No. 29 exposure increased to 4.0 in day 4 at 1
No. 52 exposure increased to 4.0 in day 4 at 1
No. 71 exposure increased to 1.0 in day 4 at 1
No. 87 exposure increased to 4.0 in day 4 at 1
No. 101 exposure increased to 3.0 in day 4 at 1
No. 103 exposure increased to 4.0 in day 4 at 1
*When No. 112 infected, Exposure is 5.0 in day 4 at move 1
No. 121 exposure increased to 3.0 in day 4 at 1
*When No. 125 infected, Exposure is 3.0 in day 4 at move 1
No. 128 exposure increased to 4.0 in day 4 at 1
No. 161 exposure increased to 4.0 in day 4 at 1
No. 174 exposure increased to 1.0 in day 4 at 1
No. 193 exposure increased to 5.0 in day 4 at 1
No. 202 exposure increased to 4.0 in day 4 at 1
No. 226 exposure increased to 4.0 in day 4 at 1
No. 240 exposure increased to 1.0 in day 4 at 1
No. 242 exposure increased to 1.0 in day 4 at 1
No. 246 exposure increased to 4.0 in day 4 at 1
No. 253 exposure increased to 2.0 in day 4 at 1
No. 264 exposure increased to 4.0 in day 4 at 1
No. 270 exposure increased to 2.0 in day 4 at 1
No. 280 exposure increased to 2.0 in day 4 at 1
No. 287 exposure increased to 4.0 in day 4 at 1
No. 312 exposure increased to 4.0 in day 4 at 1
No. 324 exposure increased to 1.0 in day 4 at 1
No. 334 exposure increased to 2.0 in day 4 at 1
No. 336 exposure increased to 2.0 in day 4 at 1
*When No. 338 infected, Exposure is 4.0 in day 4 at move 1
*When No. 345 infected, Exposure is 3.0 in day 4 at move 1
No. 347 exposure increased to 4.0 in day 4 at 1
No. 352 exposure increased to 3.0 in day 4 at 1
*When No. 374 infected, Exposure is 2.0 in day 4 at move 1
*When No. 386 infected, Exposure is 3.0 in day 4 at move 1
*When No. 388 infected, Exposure is 3.0 in day 4 at move 1
No. 399 exposure increased to 2.0 in day 4 at 1
No. 402 exposure increased to 1.0 in day 4 at 1
No. 407 exposure increased to 4.0 in day 4 at 1
No. 410 exposure increased to 4.0 in day 4 at 1
No. 418 exposure increased to 1.0 in day 4 at 1
No. 435 exposure increased to 7.0 in day 4 at 1
*When No. 443 infected, Exposure is 3.0 in day 4 at move 1
No. 457 exposure increased to 2.0 in day 4 at 1
No. 458 exposure increased to 5.0 in day 4 at 1
No. 462 exposure increased to 2.0 in day 4 at 1
No. 480 exposure increased to 4.0 in day 4 at 1
No. 506 exposure increased to 3.0 in day 4 at 1
No. 531 exposure increased to 1.0 in day 4 at 1
No. 532 exposure increased to 4.0 in day 4 at 1
No. 564 exposure increased to 3.0 in day 4 at 1
No. 595 exposure increased to 4.0 in day 4 at 1
No. 612 exposure increased to 4.0 in day 4 at 1
No. 656 exposure increased to 4.0 in day 4 at 1
No. 665 exposure increased to 5.0 in day 4 at 1
No. 681 exposure increased to 4.0 in day 4 at 1
No. 697 exposure increased to 4.0 in day 4 at 1
No. 699 exposure increased to 3.0 in day 4 at 1
No. 700 exposure increased to 4.0 in day 4 at 1
*When No. 715 infected, Exposure is 3.0 in day 4 at move 1
*When No. 721 infected, Exposure is 3.0 in day 4 at move 1
No. 737 exposure increased to 5.0 in day 4 at 1
No. 749 exposure increased to 2.0 in day 4 at 1
No. 767 exposure increased to 2.0 in day 4 at 1
*When No. 795 infected, Exposure is 3.0 in day 4 at move 1
No. 798 exposure increased to 4.0 in day 4 at 1
No. 814 exposure increased to 3.0 in day 4 at 1
No. 817 exposure increased to 2.0 in day 4 at 1
No. 818 exposure increased to 2.0 in day 4 at 1
*When No. 823 infected, Exposure is 3.0 in day 4 at move 1
No. 841 exposure increased to 2.0 in day 4 at 1
No. 857 exposure increased to 1.0 in day 4 at 1
No. 868 exposure increased to 4.0 in day 4 at 1
*When No. 874 infected, Exposure is 3.0 in day 4 at move 1
No. 910 exposure increased to 4.0 in day 4 at 1
No. 917 exposure increased to 8.0 in day 4 at 1
No. 922 exposure increased to 4.0 in day 4 at 1
No. 931 exposure increased to 3.0 in day 4 at 1
No. 932 exposure increased to 4.0 in day 4 at 1
No. 953 exposure increased to 2.0 in day 4 at 1
No. 978 exposure increased to 4.0 in day 4 at 1
No. 979 exposure increased to 2.0 in day 4 at 1
No. 992 exposure increased to 3.0 in day 4 at 1
   35/10000 [..............................] - ETA: 27:43:38 - reward: 705.6549*When No. 52 infected, Exposure is 4.0 in day 4 at move 0
*When No. 101 infected, Exposure is 3.0 in day 4 at move 0
*When No. 103 infected, Exposure is 4.0 in day 4 at move 0
*When No. 121 infected, Exposure is 3.0 in day 4 at move 0
*When No. 128 infected, Exposure is 4.0 in day 4 at move 0
*When No. 226 infected, Exposure is 4.0 in day 4 at move 0
*When No. 246 infected, Exposure is 4.0 in day 4 at move 0
*When No. 347 infected, Exposure is 4.0 in day 4 at move 0
*When No. 458 infected, Exposure is 5.0 in day 4 at move 0
*When No. 681 infected, Exposure is 4.0 in day 4 at move 0
*When No. 737 infected, Exposure is 5.0 in day 4 at move 0
*When No. 814 infected, Exposure is 3.0 in day 4 at move 0
*When No. 917 infected, Exposure is 8.0 in day 4 at move 0
*When No. 161 infected, Exposure is 4.0 in day 4 at move 1
*When No. 193 infected, Exposure is 5.0 in day 4 at move 1
*When No. 287 infected, Exposure is 4.0 in day 4 at move 1
*When No. 312 infected, Exposure is 4.0 in day 4 at move 1
*When No. 435 infected, Exposure is 7.0 in day 4 at move 1
*When No. 665 infected, Exposure is 5.0 in day 4 at move 1
*When No. 749 infected, Exposure is 2.0 in day 4 at move 1
*When No. 29 infected, Exposure is 4.0 in day 4 at move 2
*When No. 87 infected, Exposure is 4.0 in day 4 at move 2
*When No. 264 infected, Exposure is 4.0 in day 4 at move 2
*When No. 407 infected, Exposure is 4.0 in day 4 at move 2
*When No. 480 infected, Exposure is 4.0 in day 4 at move 2
*When No. 595 infected, Exposure is 4.0 in day 4 at move 2
*When No. 612 infected, Exposure is 4.0 in day 4 at move 2
*When No. 697 infected, Exposure is 4.0 in day 4 at move 2
*When No. 978 infected, Exposure is 4.0 in day 4 at move 2
*When No. 410 infected, Exposure is 4.0 in day 4 at move 3
*When No. 457 infected, Exposure is 2.0 in day 4 at move 3
*When No. 532 infected, Exposure is 4.0 in day 4 at move 3
*When No. 699 infected, Exposure is 3.0 in day 4 at move 3
*When No. 700 infected, Exposure is 4.0 in day 4 at move 3
*When No. 817 infected, Exposure is 2.0 in day 4 at move 3
*When No. 953 infected, Exposure is 2.0 in day 4 at move 3
*When No. 979 infected, Exposure is 2.0 in day 4 at move 3
*When No. 202 infected, Exposure is 4.0 in day 4 at move 4
*When No. 334 infected, Exposure is 2.0 in day 4 at move 4
*When No. 462 infected, Exposure is 2.0 in day 4 at move 4
*When No. 506 infected, Exposure is 3.0 in day 4 at move 4
*When No. 931 infected, Exposure is 3.0 in day 4 at move 4
No. 23 exposure increased to 3.0 in day 4 at 5
No. 36 exposure increased to 1.0 in day 4 at 5
No. 45 exposure increased to 1.0 in day 4 at 5
No. 71 exposure increased to 2.0 in day 4 at 5
No. 74 exposure increased to 1.0 in day 4 at 5
No. 139 exposure increased to 1.0 in day 4 at 5
No. 155 exposure increased to 1.0 in day 4 at 5
No. 174 exposure increased to 2.0 in day 4 at 5
No. 181 exposure increased to 1.0 in day 4 at 5
No. 188 exposure increased to 1.0 in day 4 at 5
No. 235 exposure increased to 1.0 in day 4 at 5
No. 240 exposure increased to 2.0 in day 4 at 5
No. 242 exposure increased to 2.0 in day 4 at 5
No. 250 exposure increased to 1.0 in day 4 at 5
*When No. 253 infected, Exposure is 2.0 in day 4 at move 5
No. 270 exposure increased to 3.0 in day 4 at 5
No. 273 exposure increased to 1.0 in day 4 at 5
No. 280 exposure increased to 3.0 in day 4 at 5
No. 290 exposure increased to 1.0 in day 4 at 5
No. 320 exposure increased to 1.0 in day 4 at 5
No. 323 exposure increased to 1.0 in day 4 at 5
No. 324 exposure increased to 2.0 in day 4 at 5
No. 332 exposure increased to 1.0 in day 4 at 5
*When No. 336 infected, Exposure is 2.0 in day 4 at move 5
No. 344 exposure increased to 1.0 in day 4 at 5
No. 352 exposure increased to 4.0 in day 4 at 5
No. 399 exposure increased to 3.0 in day 4 at 5
No. 400 exposure increased to 2.0 in day 4 at 5
No. 402 exposure increased to 2.0 in day 4 at 5
No. 412 exposure increased to 2.0 in day 4 at 5
No. 418 exposure increased to 2.0 in day 4 at 5
No. 450 exposure increased to 2.0 in day 4 at 5
No. 452 exposure increased to 2.0 in day 4 at 5
No. 466 exposure increased to 1.0 in day 4 at 5
No. 472 exposure increased to 2.0 in day 4 at 5
No. 477 exposure increased to 1.0 in day 4 at 5
No. 479 exposure increased to 1.0 in day 4 at 5
No. 492 exposure increased to 1.0 in day 4 at 5
No. 531 exposure increased to 2.0 in day 4 at 5
No. 534 exposure increased to 2.0 in day 4 at 5
No. 564 exposure increased to 4.0 in day 4 at 5
No. 603 exposure increased to 2.0 in day 4 at 5
No. 643 exposure increased to 2.0 in day 4 at 5
No. 656 exposure increased to 5.0 in day 4 at 5
No. 676 exposure increased to 2.0 in day 4 at 5
No. 692 exposure increased to 1.0 in day 4 at 5
No. 724 exposure increased to 1.0 in day 4 at 5
No. 728 exposure increased to 1.0 in day 4 at 5
No. 764 exposure increased to 1.0 in day 4 at 5
No. 767 exposure increased to 3.0 in day 4 at 5
No. 790 exposure increased to 1.0 in day 4 at 5
No. 797 exposure increased to 1.0 in day 4 at 5
No. 798 exposure increased to 5.0 in day 4 at 5
No. 818 exposure increased to 3.0 in day 4 at 5
No. 825 exposure increased to 1.0 in day 4 at 5
No. 841 exposure increased to 3.0 in day 4 at 5
No. 857 exposure increased to 2.0 in day 4 at 5
No. 868 exposure increased to 5.0 in day 4 at 5
No. 910 exposure increased to 5.0 in day 4 at 5
No. 921 exposure increased to 1.0 in day 4 at 5
No. 922 exposure increased to 5.0 in day 4 at 5
No. 926 exposure increased to 1.0 in day 4 at 5
No. 932 exposure increased to 5.0 in day 4 at 5
No. 938 exposure increased to 1.0 in day 4 at 5
No. 955 exposure increased to 1.0 in day 4 at 5
No. 956 exposure increased to 2.0 in day 4 at 5
No. 992 exposure increased to 4.0 in day 4 at 5
   36/10000 [..............................] - ETA: 27:26:05 - reward: 691.6256*When No. 23 infected, Exposure is 3.0 in day 4 at move 0
*When No. 399 infected, Exposure is 3.0 in day 4 at move 0
*When No. 676 infected, Exposure is 2.0 in day 4 at move 0
*When No. 798 infected, Exposure is 5.0 in day 4 at move 0
*When No. 868 infected, Exposure is 5.0 in day 4 at move 0
*When No. 910 infected, Exposure is 5.0 in day 4 at move 0
No. 36 exposure increased to 2.0 in day 4 at 1
No. 45 exposure increased to 2.0 in day 4 at 1
No. 71 exposure increased to 3.0 in day 4 at 1
No. 74 exposure increased to 2.0 in day 4 at 1
No. 134 exposure increased to 1.0 in day 4 at 1
No. 139 exposure increased to 2.0 in day 4 at 1
No. 155 exposure increased to 2.0 in day 4 at 1
No. 157 exposure increased to 1.0 in day 4 at 1
No. 174 exposure increased to 3.0 in day 4 at 1
No. 181 exposure increased to 2.0 in day 4 at 1
No. 188 exposure increased to 2.0 in day 4 at 1
No. 222 exposure increased to 1.0 in day 4 at 1
No. 235 exposure increased to 2.0 in day 4 at 1
No. 240 exposure increased to 3.0 in day 4 at 1
No. 242 exposure increased to 3.0 in day 4 at 1
No. 250 exposure increased to 2.0 in day 4 at 1
No. 270 exposure increased to 4.0 in day 4 at 1
No. 273 exposure increased to 2.0 in day 4 at 1
No. 280 exposure increased to 4.0 in day 4 at 1
No. 290 exposure increased to 2.0 in day 4 at 1
No. 320 exposure increased to 2.0 in day 4 at 1
No. 323 exposure increased to 2.0 in day 4 at 1
*When No. 324 infected, Exposure is 2.0 in day 4 at move 1
No. 332 exposure increased to 2.0 in day 4 at 1
No. 344 exposure increased to 2.0 in day 4 at 1
No. 352 exposure increased to 5.0 in day 4 at 1
No. 354 exposure increased to 2.0 in day 4 at 1
No. 367 exposure increased to 2.0 in day 4 at 1
No. 369 exposure increased to 1.0 in day 4 at 1
No. 400 exposure increased to 3.0 in day 4 at 1
No. 402 exposure increased to 3.0 in day 4 at 1
No. 412 exposure increased to 3.0 in day 4 at 1
No. 418 exposure increased to 3.0 in day 4 at 1
No. 450 exposure increased to 3.0 in day 4 at 1
No. 452 exposure increased to 3.0 in day 4 at 1
No. 466 exposure increased to 2.0 in day 4 at 1
No. 472 exposure increased to 3.0 in day 4 at 1
No. 477 exposure increased to 2.0 in day 4 at 1
No. 479 exposure increased to 2.0 in day 4 at 1
No. 492 exposure increased to 2.0 in day 4 at 1
No. 531 exposure increased to 3.0 in day 4 at 1
No. 534 exposure increased to 3.0 in day 4 at 1
*When No. 564 infected, Exposure is 4.0 in day 4 at move 1
No. 603 exposure increased to 3.0 in day 4 at 1
No. 621 exposure increased to 1.0 in day 4 at 1
No. 643 exposure increased to 3.0 in day 4 at 1
*When No. 656 infected, Exposure is 5.0 in day 4 at move 1
No. 692 exposure increased to 2.0 in day 4 at 1
No. 724 exposure increased to 2.0 in day 4 at 1
No. 728 exposure increased to 2.0 in day 4 at 1
No. 729 exposure increased to 1.0 in day 4 at 1
No. 764 exposure increased to 2.0 in day 4 at 1
No. 767 exposure increased to 4.0 in day 4 at 1
No. 790 exposure increased to 2.0 in day 4 at 1
No. 797 exposure increased to 2.0 in day 4 at 1
No. 818 exposure increased to 4.0 in day 4 at 1
No. 825 exposure increased to 2.0 in day 4 at 1
*When No. 841 infected, Exposure is 3.0 in day 4 at move 1
No. 857 exposure increased to 3.0 in day 4 at 1
No. 884 exposure increased to 1.0 in day 4 at 1
No. 921 exposure increased to 2.0 in day 4 at 1
No. 922 exposure increased to 6.0 in day 4 at 1
No. 926 exposure increased to 2.0 in day 4 at 1
*When No. 932 infected, Exposure is 5.0 in day 4 at move 1
No. 938 exposure increased to 2.0 in day 4 at 1
No. 955 exposure increased to 2.0 in day 4 at 1
No. 956 exposure increased to 3.0 in day 4 at 1
*When No. 992 infected, Exposure is 4.0 in day 4 at move 1
   37/10000 [..............................] - ETA: 26:50:39 - reward: 679.1043*When No. 174 infected, Exposure is 3.0 in day 4 at move 0
*When No. 402 infected, Exposure is 3.0 in day 4 at move 0
*When No. 412 infected, Exposure is 3.0 in day 4 at move 0
*When No. 767 infected, Exposure is 4.0 in day 4 at move 0
*When No. 818 infected, Exposure is 4.0 in day 4 at move 0
*When No. 921 infected, Exposure is 2.0 in day 4 at move 0
*When No. 270 infected, Exposure is 4.0 in day 4 at move 1
*When No. 290 infected, Exposure is 2.0 in day 4 at move 1
*When No. 352 infected, Exposure is 5.0 in day 4 at move 1
*When No. 400 infected, Exposure is 3.0 in day 4 at move 1
*When No. 466 infected, Exposure is 2.0 in day 4 at move 1
*When No. 477 infected, Exposure is 2.0 in day 4 at move 1
*When No. 643 infected, Exposure is 3.0 in day 4 at move 1
*When No. 857 infected, Exposure is 3.0 in day 4 at move 1
*When No. 922 infected, Exposure is 6.0 in day 4 at move 1
*When No. 955 infected, Exposure is 2.0 in day 4 at move 1
*When No. 155 infected, Exposure is 2.0 in day 4 at move 2
*When No. 323 infected, Exposure is 2.0 in day 4 at move 2
*When No. 472 infected, Exposure is 3.0 in day 4 at move 2
*When No. 531 infected, Exposure is 3.0 in day 4 at move 2
*When No. 534 infected, Exposure is 3.0 in day 4 at move 2
*When No. 240 infected, Exposure is 3.0 in day 4 at move 3
*When No. 242 infected, Exposure is 3.0 in day 4 at move 3
*When No. 790 infected, Exposure is 2.0 in day 4 at move 3
*When No. 71 infected, Exposure is 3.0 in day 4 at move 4
*When No. 74 infected, Exposure is 2.0 in day 4 at move 4
*When No. 139 infected, Exposure is 2.0 in day 4 at move 4
*When No. 188 infected, Exposure is 2.0 in day 4 at move 4
*When No. 332 infected, Exposure is 2.0 in day 4 at move 4
*When No. 479 infected, Exposure is 2.0 in day 4 at move 4
No. 8 exposure increased to 1.0 in day 4 at 5
No. 36 exposure increased to 3.0 in day 4 at 5
No. 42 exposure increased to 1.0 in day 4 at 5
No. 45 exposure increased to 3.0 in day 4 at 5
No. 134 exposure increased to 2.0 in day 4 at 5
No. 146 exposure increased to 1.0 in day 4 at 5
No. 157 exposure increased to 2.0 in day 4 at 5
No. 181 exposure increased to 3.0 in day 4 at 5
No. 222 exposure increased to 2.0 in day 4 at 5
No. 235 exposure increased to 3.0 in day 4 at 5
No. 237 exposure increased to 1.0 in day 4 at 5
No. 250 exposure increased to 3.0 in day 4 at 5
No. 252 exposure increased to 1.0 in day 4 at 5
No. 273 exposure increased to 3.0 in day 4 at 5
*When No. 280 infected, Exposure is 4.0 in day 4 at move 5
No. 320 exposure increased to 3.0 in day 4 at 5
No. 330 exposure increased to 1.0 in day 4 at 5
*When No. 344 infected, Exposure is 2.0 in day 4 at move 5
No. 354 exposure increased to 3.0 in day 4 at 5
No. 363 exposure increased to 1.0 in day 4 at 5
No. 367 exposure increased to 3.0 in day 4 at 5
No. 369 exposure increased to 2.0 in day 4 at 5
No. 385 exposure increased to 1.0 in day 4 at 5
No. 414 exposure increased to 1.0 in day 4 at 5
No. 418 exposure increased to 4.0 in day 4 at 5
No. 428 exposure increased to 1.0 in day 4 at 5
No. 444 exposure increased to 1.0 in day 4 at 5
No. 450 exposure increased to 4.0 in day 4 at 5
No. 452 exposure increased to 4.0 in day 4 at 5
No. 468 exposure increased to 1.0 in day 4 at 5
No. 492 exposure increased to 3.0 in day 4 at 5
No. 493 exposure increased to 1.0 in day 4 at 5
No. 572 exposure increased to 1.0 in day 4 at 5
No. 603 exposure increased to 4.0 in day 4 at 5
No. 621 exposure increased to 2.0 in day 4 at 5
No. 628 exposure increased to 1.0 in day 4 at 5
No. 635 exposure increased to 1.0 in day 4 at 5
No. 688 exposure increased to 2.0 in day 4 at 5
No. 692 exposure increased to 3.0 in day 4 at 5
No. 704 exposure increased to 1.0 in day 4 at 5
*When No. 724 infected, Exposure is 2.0 in day 4 at move 5
*When No. 728 infected, Exposure is 2.0 in day 4 at move 5
No. 729 exposure increased to 2.0 in day 4 at 5
No. 764 exposure increased to 3.0 in day 4 at 5
No. 773 exposure increased to 1.0 in day 4 at 5
No. 797 exposure increased to 3.0 in day 4 at 5
No. 825 exposure increased to 3.0 in day 4 at 5
No. 845 exposure increased to 2.0 in day 4 at 5
No. 882 exposure increased to 1.0 in day 4 at 5
No. 884 exposure increased to 2.0 in day 4 at 5
No. 926 exposure increased to 3.0 in day 4 at 5
*When No. 938 infected, Exposure is 2.0 in day 4 at move 5
No. 945 exposure increased to 1.0 in day 4 at 5
No. 956 exposure increased to 4.0 in day 4 at 5
   38/10000 [..............................] - ETA: 26:31:21 - reward: 665.8753*When No. 235 infected, Exposure is 3.0 in day 4 at move 0
*When No. 450 infected, Exposure is 4.0 in day 4 at move 0
*When No. 492 infected, Exposure is 3.0 in day 4 at move 0
*When No. 845 infected, Exposure is 2.0 in day 4 at move 0
*When No. 222 infected, Exposure is 2.0 in day 4 at move 1
*When No. 418 infected, Exposure is 4.0 in day 4 at move 1
*When No. 452 infected, Exposure is 4.0 in day 4 at move 1
*When No. 797 infected, Exposure is 3.0 in day 4 at move 1
*When No. 956 infected, Exposure is 4.0 in day 4 at move 1
*When No. 369 infected, Exposure is 2.0 in day 4 at move 2
*When No. 603 infected, Exposure is 4.0 in day 4 at move 2
*When No. 36 infected, Exposure is 3.0 in day 4 at move 3
*When No. 250 infected, Exposure is 3.0 in day 4 at move 3
*When No. 320 infected, Exposure is 3.0 in day 4 at move 3
*When No. 884 infected, Exposure is 2.0 in day 4 at move 3
No. 8 exposure increased to 2.0 in day 4 at 5
No. 9 exposure increased to 1.0 in day 4 at 5
No. 32 exposure increased to 2.0 in day 4 at 5
No. 42 exposure increased to 2.0 in day 4 at 5
No. 45 exposure increased to 4.0 in day 4 at 5
No. 114 exposure increased to 2.0 in day 4 at 5
No. 134 exposure increased to 3.0 in day 4 at 5
No. 146 exposure increased to 2.0 in day 4 at 5
No. 157 exposure increased to 3.0 in day 4 at 5
No. 181 exposure increased to 4.0 in day 4 at 5
No. 192 exposure increased to 1.0 in day 4 at 5
No. 237 exposure increased to 2.0 in day 4 at 5
No. 252 exposure increased to 2.0 in day 4 at 5
No. 273 exposure increased to 4.0 in day 4 at 5
No. 330 exposure increased to 2.0 in day 4 at 5
No. 354 exposure increased to 4.0 in day 4 at 5
No. 357 exposure increased to 1.0 in day 4 at 5
No. 363 exposure increased to 2.0 in day 4 at 5
No. 367 exposure increased to 4.0 in day 4 at 5
No. 378 exposure increased to 1.0 in day 4 at 5
No. 385 exposure increased to 2.0 in day 4 at 5
No. 393 exposure increased to 1.0 in day 4 at 5
No. 414 exposure increased to 2.0 in day 4 at 5
No. 428 exposure increased to 2.0 in day 4 at 5
No. 433 exposure increased to 1.0 in day 4 at 5
No. 444 exposure increased to 2.0 in day 4 at 5
No. 460 exposure increased to 1.0 in day 4 at 5
No. 468 exposure increased to 2.0 in day 4 at 5
No. 493 exposure increased to 2.0 in day 4 at 5
No. 538 exposure increased to 1.0 in day 4 at 5
No. 565 exposure increased to 1.0 in day 4 at 5
No. 572 exposure increased to 2.0 in day 4 at 5
No. 599 exposure increased to 1.0 in day 4 at 5
*When No. 621 infected, Exposure is 2.0 in day 4 at move 5
No. 628 exposure increased to 2.0 in day 4 at 5
No. 631 exposure increased to 1.0 in day 4 at 5
No. 635 exposure increased to 2.0 in day 4 at 5
No. 652 exposure increased to 1.0 in day 4 at 5
No. 688 exposure increased to 3.0 in day 4 at 5
No. 692 exposure increased to 4.0 in day 4 at 5
No. 704 exposure increased to 2.0 in day 4 at 5
No. 729 exposure increased to 3.0 in day 4 at 5
No. 752 exposure increased to 1.0 in day 4 at 5
No. 764 exposure increased to 4.0 in day 4 at 5
No. 773 exposure increased to 2.0 in day 4 at 5
No. 819 exposure increased to 2.0 in day 4 at 5
No. 825 exposure increased to 4.0 in day 4 at 5
No. 849 exposure increased to 1.0 in day 4 at 5
No. 854 exposure increased to 2.0 in day 4 at 5
No. 882 exposure increased to 2.0 in day 4 at 5
No. 887 exposure increased to 1.0 in day 4 at 5
No. 893 exposure increased to 1.0 in day 4 at 5
No. 894 exposure increased to 1.0 in day 4 at 5
No. 896 exposure increased to 2.0 in day 4 at 5
No. 905 exposure increased to 1.0 in day 4 at 5
No. 926 exposure increased to 4.0 in day 4 at 5
No. 945 exposure increased to 2.0 in day 4 at 5
No. 966 exposure increased to 1.0 in day 4 at 5
No. 993 exposure increased to 1.0 in day 4 at 5
   39/10000 [..............................] - ETA: 26:10:49 - reward: 653.8277*When No. 134 infected, Exposure is 3.0 in day 4 at move 0
*When No. 157 infected, Exposure is 3.0 in day 4 at move 0
*When No. 367 infected, Exposure is 4.0 in day 4 at move 0
*When No. 692 infected, Exposure is 4.0 in day 4 at move 0
*When No. 729 infected, Exposure is 3.0 in day 4 at move 0
*When No. 764 infected, Exposure is 4.0 in day 4 at move 0
*When No. 114 infected, Exposure is 2.0 in day 4 at move 1
*When No. 181 infected, Exposure is 4.0 in day 4 at move 1
*When No. 273 infected, Exposure is 4.0 in day 4 at move 1
*When No. 363 infected, Exposure is 2.0 in day 4 at move 1
*When No. 468 infected, Exposure is 2.0 in day 4 at move 1
*When No. 688 infected, Exposure is 3.0 in day 4 at move 1
*When No. 8 infected, Exposure is 2.0 in day 4 at move 2
*When No. 237 infected, Exposure is 2.0 in day 4 at move 2
*When No. 354 infected, Exposure is 4.0 in day 4 at move 2
*When No. 414 infected, Exposure is 2.0 in day 4 at move 2
*When No. 773 infected, Exposure is 2.0 in day 4 at move 2
*When No. 825 infected, Exposure is 4.0 in day 4 at move 2
*When No. 926 infected, Exposure is 4.0 in day 4 at move 2
*When No. 146 infected, Exposure is 2.0 in day 4 at move 4
*When No. 385 infected, Exposure is 2.0 in day 4 at move 4
*When No. 819 infected, Exposure is 2.0 in day 4 at move 4
*When No. 854 infected, Exposure is 2.0 in day 4 at move 4
No. 9 exposure increased to 2.0 in day 4 at 5
No. 26 exposure increased to 2.0 in day 4 at 5
No. 30 exposure increased to 2.0 in day 4 at 5
No. 32 exposure increased to 3.0 in day 4 at 5
No. 42 exposure increased to 3.0 in day 4 at 5
No. 45 exposure increased to 5.0 in day 4 at 5
No. 137 exposure increased to 1.0 in day 4 at 5
No. 165 exposure increased to 2.0 in day 4 at 5
No. 168 exposure increased to 1.0 in day 4 at 5
No. 176 exposure increased to 1.0 in day 4 at 5
No. 192 exposure increased to 2.0 in day 4 at 5
No. 252 exposure increased to 3.0 in day 4 at 5
No. 256 exposure increased to 1.0 in day 4 at 5
*When No. 330 infected, Exposure is 2.0 in day 4 at move 5
No. 357 exposure increased to 2.0 in day 4 at 5
No. 378 exposure increased to 2.0 in day 4 at 5
No. 393 exposure increased to 2.0 in day 4 at 5
No. 428 exposure increased to 3.0 in day 4 at 5
No. 433 exposure increased to 2.0 in day 4 at 5
No. 444 exposure increased to 3.0 in day 4 at 5
No. 460 exposure increased to 2.0 in day 4 at 5
No. 493 exposure increased to 3.0 in day 4 at 5
No. 508 exposure increased to 2.0 in day 4 at 5
No. 530 exposure increased to 1.0 in day 4 at 5
No. 538 exposure increased to 2.0 in day 4 at 5
No. 565 exposure increased to 2.0 in day 4 at 5
No. 572 exposure increased to 3.0 in day 4 at 5
No. 599 exposure increased to 2.0 in day 4 at 5
No. 607 exposure increased to 1.0 in day 4 at 5
No. 628 exposure increased to 3.0 in day 4 at 5
No. 631 exposure increased to 2.0 in day 4 at 5
*When No. 635 infected, Exposure is 2.0 in day 4 at move 5
No. 638 exposure increased to 1.0 in day 4 at 5
No. 652 exposure increased to 2.0 in day 4 at 5
No. 704 exposure increased to 3.0 in day 4 at 5
No. 722 exposure increased to 1.0 in day 4 at 5
No. 752 exposure increased to 2.0 in day 4 at 5
No. 758 exposure increased to 2.0 in day 4 at 5
No. 780 exposure increased to 1.0 in day 4 at 5
No. 806 exposure increased to 2.0 in day 4 at 5
No. 849 exposure increased to 2.0 in day 4 at 5
No. 882 exposure increased to 3.0 in day 4 at 5
No. 887 exposure increased to 2.0 in day 4 at 5
No. 893 exposure increased to 2.0 in day 4 at 5
No. 894 exposure increased to 2.0 in day 4 at 5
No. 896 exposure increased to 3.0 in day 4 at 5
No. 905 exposure increased to 2.0 in day 4 at 5
No. 945 exposure increased to 3.0 in day 4 at 5
No. 966 exposure increased to 2.0 in day 4 at 5
No. 993 exposure increased to 2.0 in day 4 at 5
   40/10000 [..............................] - ETA: 25:49:48 - reward: 642.3320*When No. 32 infected, Exposure is 3.0 in day 4 at move 0
*When No. 42 infected, Exposure is 3.0 in day 4 at move 0
*When No. 45 infected, Exposure is 5.0 in day 4 at move 0
*When No. 252 infected, Exposure is 3.0 in day 4 at move 0
*When No. 428 infected, Exposure is 3.0 in day 4 at move 0
*When No. 538 infected, Exposure is 2.0 in day 4 at move 0
*When No. 945 infected, Exposure is 3.0 in day 4 at move 0
No. 9 exposure increased to 3.0 in day 4 at 1
No. 26 exposure increased to 3.0 in day 4 at 1
No. 30 exposure increased to 3.0 in day 4 at 1
No. 44 exposure increased to 2.0 in day 4 at 1
No. 105 exposure increased to 2.0 in day 4 at 1
No. 137 exposure increased to 2.0 in day 4 at 1
No. 165 exposure increased to 3.0 in day 4 at 1
No. 168 exposure increased to 2.0 in day 4 at 1
No. 176 exposure increased to 2.0 in day 4 at 1
No. 192 exposure increased to 3.0 in day 4 at 1
No. 256 exposure increased to 2.0 in day 4 at 1
No. 357 exposure increased to 3.0 in day 4 at 1
No. 378 exposure increased to 3.0 in day 4 at 1
No. 393 exposure increased to 3.0 in day 4 at 1
No. 433 exposure increased to 3.0 in day 4 at 1
No. 444 exposure increased to 4.0 in day 4 at 1
No. 460 exposure increased to 3.0 in day 4 at 1
No. 493 exposure increased to 4.0 in day 4 at 1
No. 508 exposure increased to 3.0 in day 4 at 1
No. 530 exposure increased to 2.0 in day 4 at 1
No. 561 exposure increased to 2.0 in day 4 at 1
No. 565 exposure increased to 3.0 in day 4 at 1
*When No. 572 infected, Exposure is 3.0 in day 4 at move 1
No. 599 exposure increased to 3.0 in day 4 at 1
No. 607 exposure increased to 2.0 in day 4 at 1
No. 628 exposure increased to 4.0 in day 4 at 1
*When No. 631 infected, Exposure is 2.0 in day 4 at move 1
No. 638 exposure increased to 2.0 in day 4 at 1
No. 652 exposure increased to 3.0 in day 4 at 1
No. 663 exposure increased to 2.0 in day 4 at 1
No. 704 exposure increased to 4.0 in day 4 at 1
No. 722 exposure increased to 2.0 in day 4 at 1
No. 752 exposure increased to 3.0 in day 4 at 1
*When No. 758 infected, Exposure is 2.0 in day 4 at move 1
No. 780 exposure increased to 2.0 in day 4 at 1
No. 806 exposure increased to 3.0 in day 4 at 1
No. 849 exposure increased to 3.0 in day 4 at 1
No. 882 exposure increased to 4.0 in day 4 at 1
No. 887 exposure increased to 3.0 in day 4 at 1
*When No. 893 infected, Exposure is 2.0 in day 4 at move 1
No. 894 exposure increased to 3.0 in day 4 at 1
*When No. 896 infected, Exposure is 3.0 in day 4 at move 1
No. 905 exposure increased to 3.0 in day 4 at 1
No. 966 exposure increased to 3.0 in day 4 at 1
No. 993 exposure increased to 3.0 in day 4 at 1
   41/10000 [..............................] - ETA: 25:17:54 - reward: 631.0446*When No. 26 infected, Exposure is 3.0 in day 4 at move 0
*When No. 44 infected, Exposure is 2.0 in day 4 at move 0
*When No. 165 infected, Exposure is 3.0 in day 4 at move 0
*When No. 393 infected, Exposure is 3.0 in day 4 at move 0
*When No. 433 infected, Exposure is 3.0 in day 4 at move 0
*When No. 561 infected, Exposure is 2.0 in day 4 at move 0
*When No. 565 infected, Exposure is 3.0 in day 4 at move 0
*When No. 599 infected, Exposure is 3.0 in day 4 at move 0
No. 9 exposure increased to 4.0 in day 4 at 1
*When No. 30 infected, Exposure is 3.0 in day 4 at move 1
No. 55 exposure increased to 1.0 in day 4 at 1
No. 105 exposure increased to 3.0 in day 4 at 1
No. 137 exposure increased to 3.0 in day 4 at 1
No. 168 exposure increased to 3.0 in day 4 at 1
*When No. 176 infected, Exposure is 2.0 in day 4 at move 1
No. 192 exposure increased to 4.0 in day 4 at 1
No. 256 exposure increased to 3.0 in day 4 at 1
No. 272 exposure increased to 1.0 in day 4 at 1
No. 293 exposure increased to 2.0 in day 4 at 1
*When No. 357 infected, Exposure is 3.0 in day 4 at move 1
No. 378 exposure increased to 4.0 in day 4 at 1
No. 391 exposure increased to 1.0 in day 4 at 1
No. 444 exposure increased to 5.0 in day 4 at 1
No. 460 exposure increased to 4.0 in day 4 at 1
*When No. 493 infected, Exposure is 4.0 in day 4 at move 1
No. 508 exposure increased to 4.0 in day 4 at 1
No. 530 exposure increased to 3.0 in day 4 at 1
No. 607 exposure increased to 3.0 in day 4 at 1
*When No. 628 infected, Exposure is 4.0 in day 4 at move 1
*When No. 638 infected, Exposure is 2.0 in day 4 at move 1
No. 644 exposure increased to 1.0 in day 4 at 1
No. 652 exposure increased to 4.0 in day 4 at 1
No. 663 exposure increased to 3.0 in day 4 at 1
No. 704 exposure increased to 5.0 in day 4 at 1
No. 722 exposure increased to 3.0 in day 4 at 1
No. 752 exposure increased to 4.0 in day 4 at 1
No. 780 exposure increased to 3.0 in day 4 at 1
No. 806 exposure increased to 4.0 in day 4 at 1
No. 826 exposure increased to 2.0 in day 4 at 1
No. 849 exposure increased to 4.0 in day 4 at 1
No. 882 exposure increased to 5.0 in day 4 at 1
No. 887 exposure increased to 4.0 in day 4 at 1
No. 894 exposure increased to 4.0 in day 4 at 1
No. 905 exposure increased to 4.0 in day 4 at 1
No. 966 exposure increased to 4.0 in day 4 at 1
No. 993 exposure increased to 4.0 in day 4 at 1
   42/10000 [..............................] - ETA: 24:47:25 - reward: 619.9050*When No. 137 infected, Exposure is 3.0 in day 4 at move 0
*When No. 256 infected, Exposure is 3.0 in day 4 at move 0
*When No. 607 infected, Exposure is 3.0 in day 4 at move 0
*When No. 652 infected, Exposure is 4.0 in day 4 at move 0
*When No. 722 infected, Exposure is 3.0 in day 4 at move 0
*When No. 752 infected, Exposure is 4.0 in day 4 at move 0
*When No. 105 infected, Exposure is 3.0 in day 4 at move 1
*When No. 293 infected, Exposure is 2.0 in day 4 at move 1
*When No. 663 infected, Exposure is 3.0 in day 4 at move 1
*When No. 887 infected, Exposure is 4.0 in day 4 at move 1
*When No. 905 infected, Exposure is 4.0 in day 4 at move 1
*When No. 993 infected, Exposure is 4.0 in day 4 at move 1
*When No. 192 infected, Exposure is 4.0 in day 4 at move 2
*When No. 444 infected, Exposure is 5.0 in day 4 at move 2
*When No. 508 infected, Exposure is 4.0 in day 4 at move 2
*When No. 780 infected, Exposure is 3.0 in day 4 at move 2
*When No. 378 infected, Exposure is 4.0 in day 4 at move 3
*When No. 460 infected, Exposure is 4.0 in day 4 at move 3
*When No. 849 infected, Exposure is 4.0 in day 4 at move 3
*When No. 882 infected, Exposure is 5.0 in day 4 at move 3
*When No. 530 infected, Exposure is 3.0 in day 4 at move 4
*When No. 894 infected, Exposure is 4.0 in day 4 at move 4
*When No. 966 infected, Exposure is 4.0 in day 4 at move 4
*When No. 9 infected, Exposure is 4.0 in day 4 at move 5
No. 55 exposure increased to 2.0 in day 4 at 5
No. 66 exposure increased to 2.0 in day 4 at 5
No. 168 exposure increased to 4.0 in day 4 at 5
No. 177 exposure increased to 1.0 in day 4 at 5
No. 272 exposure increased to 2.0 in day 4 at 5
No. 335 exposure increased to 1.0 in day 4 at 5
No. 391 exposure increased to 2.0 in day 4 at 5
No. 519 exposure increased to 1.0 in day 4 at 5
No. 602 exposure increased to 1.0 in day 4 at 5
No. 644 exposure increased to 2.0 in day 4 at 5
*When No. 704 infected, Exposure is 5.0 in day 4 at move 5
No. 717 exposure increased to 1.0 in day 4 at 5
No. 720 exposure increased to 1.0 in day 4 at 5
No. 778 exposure increased to 2.0 in day 4 at 5
No. 806 exposure increased to 5.0 in day 4 at 5
No. 826 exposure increased to 3.0 in day 4 at 5
No. 860 exposure increased to 2.0 in day 4 at 5
No. 891 exposure increased to 1.0 in day 4 at 5
No. 909 exposure increased to 1.0 in day 4 at 5
   43/10000 [..............................] - ETA: 24:27:33 - reward: 610.3453*When No. 272 infected, Exposure is 2.0 in day 4 at move 0
*When No. 806 infected, Exposure is 5.0 in day 4 at move 0
*When No. 391 infected, Exposure is 2.0 in day 4 at move 1
*When No. 644 infected, Exposure is 2.0 in day 4 at move 2
*When No. 860 infected, Exposure is 2.0 in day 4 at move 2
*When No. 55 infected, Exposure is 2.0 in day 4 at move 3
No. 35 exposure increased to 1.0 in day 4 at 5
No. 39 exposure increased to 2.0 in day 4 at 5
No. 66 exposure increased to 3.0 in day 4 at 5
No. 168 exposure increased to 5.0 in day 4 at 5
No. 177 exposure increased to 2.0 in day 4 at 5
No. 228 exposure increased to 1.0 in day 4 at 5
No. 230 exposure increased to 1.0 in day 4 at 5
No. 335 exposure increased to 2.0 in day 4 at 5
No. 470 exposure increased to 1.0 in day 4 at 5
No. 519 exposure increased to 2.0 in day 4 at 5
No. 521 exposure increased to 1.0 in day 4 at 5
No. 522 exposure increased to 1.0 in day 4 at 5
No. 543 exposure increased to 1.0 in day 4 at 5
No. 548 exposure increased to 2.0 in day 4 at 5
No. 602 exposure increased to 2.0 in day 4 at 5
No. 707 exposure increased to 1.0 in day 4 at 5
No. 709 exposure increased to 1.0 in day 4 at 5
No. 717 exposure increased to 2.0 in day 4 at 5
No. 720 exposure increased to 2.0 in day 4 at 5
No. 778 exposure increased to 3.0 in day 4 at 5
No. 826 exposure increased to 4.0 in day 4 at 5
No. 847 exposure increased to 1.0 in day 4 at 5
No. 891 exposure increased to 2.0 in day 4 at 5
No. 909 exposure increased to 2.0 in day 4 at 5
No. 959 exposure increased to 1.0 in day 4 at 5
   44/10000 [..............................] - ETA: 24:06:25 - reward: 602.0866*When No. 548 infected, Exposure is 2.0 in day 4 at move 0
No. 35 exposure increased to 2.0 in day 4 at 1
No. 39 exposure increased to 3.0 in day 4 at 1
*When No. 66 infected, Exposure is 3.0 in day 4 at move 1
No. 168 exposure increased to 6.0 in day 4 at 1
No. 177 exposure increased to 3.0 in day 4 at 1
No. 228 exposure increased to 2.0 in day 4 at 1
No. 230 exposure increased to 2.0 in day 4 at 1
*When No. 335 infected, Exposure is 2.0 in day 4 at move 1
No. 346 exposure increased to 2.0 in day 4 at 1
No. 470 exposure increased to 2.0 in day 4 at 1
No. 519 exposure increased to 3.0 in day 4 at 1
No. 521 exposure increased to 2.0 in day 4 at 1
No. 522 exposure increased to 2.0 in day 4 at 1
No. 533 exposure increased to 2.0 in day 4 at 1
No. 543 exposure increased to 2.0 in day 4 at 1
No. 602 exposure increased to 3.0 in day 4 at 1
No. 654 exposure increased to 1.0 in day 4 at 1
No. 707 exposure increased to 2.0 in day 4 at 1
No. 709 exposure increased to 2.0 in day 4 at 1
No. 717 exposure increased to 3.0 in day 4 at 1
No. 720 exposure increased to 3.0 in day 4 at 1
No. 756 exposure increased to 1.0 in day 4 at 1
No. 778 exposure increased to 4.0 in day 4 at 1
*When No. 826 infected, Exposure is 4.0 in day 4 at move 1
No. 847 exposure increased to 2.0 in day 4 at 1
No. 855 exposure increased to 2.0 in day 4 at 1
No. 891 exposure increased to 3.0 in day 4 at 1
No. 909 exposure increased to 3.0 in day 4 at 1
No. 959 exposure increased to 2.0 in day 4 at 1
   45/10000 [..............................] - ETA: 23:38:38 - reward: 593.9678*When No. 346 infected, Exposure is 2.0 in day 4 at move 0
*When No. 720 infected, Exposure is 3.0 in day 4 at move 0
*When No. 891 infected, Exposure is 3.0 in day 4 at move 0
*When No. 168 infected, Exposure is 6.0 in day 4 at move 1
*When No. 778 infected, Exposure is 4.0 in day 4 at move 1
*When No. 709 infected, Exposure is 2.0 in day 4 at move 2
*When No. 177 infected, Exposure is 3.0 in day 4 at move 3
*When No. 543 infected, Exposure is 2.0 in day 4 at move 3
*When No. 602 infected, Exposure is 3.0 in day 4 at move 3
*When No. 39 infected, Exposure is 3.0 in day 4 at move 4
*When No. 855 infected, Exposure is 2.0 in day 4 at move 4
*When No. 909 infected, Exposure is 3.0 in day 4 at move 4
No. 35 exposure increased to 3.0 in day 4 at 5
No. 141 exposure increased to 1.0 in day 4 at 5
No. 196 exposure increased to 1.0 in day 4 at 5
No. 224 exposure increased to 1.0 in day 4 at 5
No. 228 exposure increased to 3.0 in day 4 at 5
No. 230 exposure increased to 3.0 in day 4 at 5
No. 326 exposure increased to 1.0 in day 4 at 5
No. 451 exposure increased to 1.0 in day 4 at 5
No. 465 exposure increased to 1.0 in day 4 at 5
No. 470 exposure increased to 3.0 in day 4 at 5
No. 519 exposure increased to 4.0 in day 4 at 5
No. 521 exposure increased to 3.0 in day 4 at 5
No. 522 exposure increased to 3.0 in day 4 at 5
No. 533 exposure increased to 3.0 in day 4 at 5
No. 654 exposure increased to 2.0 in day 4 at 5
No. 690 exposure increased to 1.0 in day 4 at 5
No. 707 exposure increased to 3.0 in day 4 at 5
No. 717 exposure increased to 4.0 in day 4 at 5
No. 756 exposure increased to 2.0 in day 4 at 5
No. 838 exposure increased to 1.0 in day 4 at 5
No. 847 exposure increased to 3.0 in day 4 at 5
No. 883 exposure increased to 1.0 in day 4 at 5
No. 959 exposure increased to 3.0 in day 4 at 5
   46/10000 [..............................] - ETA: 23:19:49 - reward: 587.8589*When No. 228 infected, Exposure is 3.0 in day 4 at move 1
*When No. 230 infected, Exposure is 3.0 in day 4 at move 1
*When No. 521 infected, Exposure is 3.0 in day 4 at move 1
*When No. 522 infected, Exposure is 3.0 in day 4 at move 1
*When No. 707 infected, Exposure is 3.0 in day 4 at move 1
*When No. 756 infected, Exposure is 2.0 in day 4 at move 1
*When No. 533 infected, Exposure is 3.0 in day 4 at move 2
*When No. 717 infected, Exposure is 4.0 in day 4 at move 2
*When No. 519 infected, Exposure is 4.0 in day 4 at move 4
*When No. 847 infected, Exposure is 3.0 in day 4 at move 4
*When No. 959 infected, Exposure is 3.0 in day 4 at move 4
No. 35 exposure increased to 4.0 in day 4 at 5
No. 59 exposure increased to 1.0 in day 4 at 5
No. 141 exposure increased to 2.0 in day 4 at 5
No. 196 exposure increased to 2.0 in day 4 at 5
No. 224 exposure increased to 2.0 in day 4 at 5
No. 279 exposure increased to 2.0 in day 4 at 5
No. 326 exposure increased to 2.0 in day 4 at 5
No. 384 exposure increased to 1.0 in day 4 at 5
No. 451 exposure increased to 2.0 in day 4 at 5
No. 465 exposure increased to 2.0 in day 4 at 5
No. 470 exposure increased to 4.0 in day 4 at 5
No. 654 exposure increased to 3.0 in day 4 at 5
No. 690 exposure increased to 2.0 in day 4 at 5
No. 838 exposure increased to 2.0 in day 4 at 5
No. 883 exposure increased to 2.0 in day 4 at 5
   47/10000 [..............................] - ETA: 23:00:28 - reward: 582.9700*When No. 279 infected, Exposure is 2.0 in day 4 at move 0
*When No. 451 infected, Exposure is 2.0 in day 4 at move 0
*When No. 654 infected, Exposure is 3.0 in day 4 at move 0
No. 35 exposure increased to 5.0 in day 4 at 1
No. 59 exposure increased to 2.0 in day 4 at 1
No. 141 exposure increased to 3.0 in day 4 at 1
No. 196 exposure increased to 3.0 in day 4 at 1
No. 224 exposure increased to 3.0 in day 4 at 1
No. 292 exposure increased to 1.0 in day 4 at 1
No. 326 exposure increased to 3.0 in day 4 at 1
No. 384 exposure increased to 2.0 in day 4 at 1
No. 465 exposure increased to 3.0 in day 4 at 1
No. 470 exposure increased to 5.0 in day 4 at 1
No. 690 exposure increased to 3.0 in day 4 at 1
No. 838 exposure increased to 3.0 in day 4 at 1
No. 883 exposure increased to 3.0 in day 4 at 1
   48/10000 [..............................] - ETA: 22:35:32 - reward: 577.4581*When No. 35 infected, Exposure is 5.0 in day 4 at move 0
*When No. 224 infected, Exposure is 3.0 in day 4 at move 0
*When No. 838 infected, Exposure is 3.0 in day 4 at move 0
No. 59 exposure increased to 3.0 in day 4 at 1
No. 141 exposure increased to 4.0 in day 4 at 1
No. 196 exposure increased to 4.0 in day 4 at 1
No. 292 exposure increased to 2.0 in day 4 at 1
No. 326 exposure increased to 4.0 in day 4 at 1
No. 384 exposure increased to 3.0 in day 4 at 1
*When No. 465 infected, Exposure is 3.0 in day 4 at move 1
No. 470 exposure increased to 6.0 in day 4 at 1
No. 588 exposure increased to 2.0 in day 4 at 1
No. 690 exposure increased to 4.0 in day 4 at 1
*When No. 883 infected, Exposure is 3.0 in day 4 at move 1
   49/10000 [..............................] - ETA: 22:11:27 - reward: 573.6080*When No. 470 infected, Exposure is 6.0 in day 4 at move 0
*When No. 326 infected, Exposure is 4.0 in day 4 at move 1
*When No. 59 infected, Exposure is 3.0 in day 4 at move 2
*When No. 141 infected, Exposure is 4.0 in day 4 at move 4
*When No. 690 infected, Exposure is 4.0 in day 4 at move 4
*When No. 196 infected, Exposure is 4.0 in day 4 at move 5
No. 276 exposure increased to 1.0 in day 4 at 5
No. 292 exposure increased to 3.0 in day 4 at 5
No. 384 exposure increased to 4.0 in day 4 at 5
No. 422 exposure increased to 2.0 in day 4 at 5
No. 588 exposure increased to 3.0 in day 4 at 5
   50/10000 [..............................] - ETA: 21:54:20 - reward: 571.7636*When No. 384 infected, Exposure is 4.0 in day 4 at move 0
*When No. 588 infected, Exposure is 3.0 in day 4 at move 0
No. 276 exposure increased to 2.0 in day 4 at 1
No. 292 exposure increased to 4.0 in day 4 at 1
No. 422 exposure increased to 3.0 in day 4 at 1
No. 867 exposure increased to 1.0 in day 4 at 1
   51/10000 [..............................] - ETA: 21:31:38 - reward: 570.1635*When No. 292 infected, Exposure is 4.0 in day 4 at move 0
*When No. 422 infected, Exposure is 3.0 in day 4 at move 3
No. 261 exposure increased to 1.0 in day 4 at 5
No. 276 exposure increased to 3.0 in day 4 at 5
No. 867 exposure increased to 2.0 in day 4 at 5
   52/10000 [..............................] - ETA: 21:14:17 - reward: 568.6540*When No. 276 infected, Exposure is 3.0 in day 4 at move 2
No. 261 exposure increased to 2.0 in day 4 at 5
No. 867 exposure increased to 3.0 in day 4 at 5
   53/10000 [..............................] - ETA: 20:57:21 - reward: 569.8432*When No. 867 infected, Exposure is 3.0 in day 4 at move 2
No. 261 exposure increased to 3.0 in day 4 at 5
   54/10000 [..............................] - ETA: 20:41:24 - reward: 570.1202*When No. 261 infected, Exposure is 3.0 in day 4 at move 2
  101/10000 [..............................] - ETA: 13:10:39 - reward: 702.3737No. 65 exposure increased to 1.0 in day 4 at 5
No. 97 exposure increased to 1.0 in day 4 at 5
No. 158 exposure increased to 1.0 in day 4 at 5
No. 203 exposure increased to 1.0 in day 4 at 5
No. 386 exposure increased to 1.0 in day 4 at 5
No. 430 exposure increased to 1.0 in day 4 at 5
No. 607 exposure increased to 1.0 in day 4 at 5
No. 648 exposure increased to 1.0 in day 4 at 5
No. 675 exposure increased to 1.0 in day 4 at 5
No. 843 exposure increased to 1.0 in day 4 at 5
No. 852 exposure increased to 1.0 in day 4 at 5
  102/10000 [..............................] - ETA: 13:26:30 - reward: 703.9574No. 8 exposure increased to 1.0 in day 4 at 5
No. 25 exposure increased to 1.0 in day 4 at 5
No. 65 exposure increased to 2.0 in day 4 at 5
No. 97 exposure increased to 2.0 in day 4 at 5
No. 136 exposure increased to 1.0 in day 4 at 5
No. 158 exposure increased to 2.0 in day 4 at 5
No. 203 exposure increased to 2.0 in day 4 at 5
No. 386 exposure increased to 2.0 in day 4 at 5
No. 430 exposure increased to 2.0 in day 4 at 5
No. 607 exposure increased to 2.0 in day 4 at 5
No. 648 exposure increased to 2.0 in day 4 at 5
No. 675 exposure increased to 2.0 in day 4 at 5
No. 843 exposure increased to 2.0 in day 4 at 5
No. 852 exposure increased to 2.0 in day 4 at 5
No. 890 exposure increased to 2.0 in day 4 at 5
No. 897 exposure increased to 1.0 in day 4 at 5
  103/10000 [..............................] - ETA: 13:41:45 - reward: 705.6067*When No. 203 infected, Exposure is 2.0 in day 4 at move 0
No. 8 exposure increased to 2.0 in day 4 at 1
No. 25 exposure increased to 2.0 in day 4 at 1
No. 65 exposure increased to 3.0 in day 4 at 1
No. 97 exposure increased to 3.0 in day 4 at 1
No. 136 exposure increased to 2.0 in day 4 at 1
No. 158 exposure increased to 3.0 in day 4 at 1
No. 386 exposure increased to 3.0 in day 4 at 1
No. 430 exposure increased to 3.0 in day 4 at 1
*When No. 607 infected, Exposure is 2.0 in day 4 at move 1
No. 648 exposure increased to 3.0 in day 4 at 1
*When No. 675 infected, Exposure is 2.0 in day 4 at move 1
No. 755 exposure increased to 1.0 in day 4 at 1
*When No. 843 infected, Exposure is 2.0 in day 4 at move 1
*When No. 852 infected, Exposure is 2.0 in day 4 at move 1
No. 890 exposure increased to 3.0 in day 4 at 1
No. 897 exposure increased to 2.0 in day 4 at 1
  104/10000 [..............................] - ETA: 13:41:17 - reward: 707.5620*When No. 8 infected, Exposure is 2.0 in day 4 at move 0
*When No. 97 infected, Exposure is 3.0 in day 4 at move 0
*When No. 430 infected, Exposure is 3.0 in day 4 at move 0
*When No. 648 infected, Exposure is 3.0 in day 4 at move 0
*When No. 386 infected, Exposure is 3.0 in day 4 at move 2
*When No. 136 infected, Exposure is 2.0 in day 4 at move 3
*When No. 25 infected, Exposure is 2.0 in day 4 at move 4
*When No. 158 infected, Exposure is 3.0 in day 4 at move 4
No. 65 exposure increased to 4.0 in day 4 at 5
No. 351 exposure increased to 1.0 in day 4 at 5
No. 755 exposure increased to 2.0 in day 4 at 5
*When No. 890 infected, Exposure is 3.0 in day 4 at move 5
No. 897 exposure increased to 3.0 in day 4 at 5
No. 967 exposure increased to 1.0 in day 4 at 5
No. 977 exposure increased to 1.0 in day 4 at 5
  105/10000 [..............................] - ETA: 13:57:32 - reward: 709.1300*When No. 65 infected, Exposure is 4.0 in day 4 at move 0
No. 46 exposure increased to 1.0 in day 4 at 1
No. 99 exposure increased to 1.0 in day 4 at 1
No. 351 exposure increased to 2.0 in day 4 at 1
No. 361 exposure increased to 1.0 in day 4 at 1
No. 601 exposure increased to 1.0 in day 4 at 1
No. 755 exposure increased to 3.0 in day 4 at 1
No. 886 exposure increased to 1.0 in day 4 at 1
No. 897 exposure increased to 4.0 in day 4 at 1
No. 967 exposure increased to 2.0 in day 4 at 1
No. 977 exposure increased to 2.0 in day 4 at 1
  106/10000 [..............................] - ETA: 13:57:40 - reward: 711.4912*When No. 897 infected, Exposure is 4.0 in day 4 at move 0
No. 46 exposure increased to 2.0 in day 4 at 1
No. 99 exposure increased to 2.0 in day 4 at 1
No. 152 exposure increased to 1.0 in day 4 at 1
No. 165 exposure increased to 2.0 in day 4 at 1
No. 172 exposure increased to 1.0 in day 4 at 1
No. 233 exposure increased to 1.0 in day 4 at 1
No. 351 exposure increased to 3.0 in day 4 at 1
No. 361 exposure increased to 2.0 in day 4 at 1
No. 415 exposure increased to 1.0 in day 4 at 1
No. 564 exposure increased to 1.0 in day 4 at 1
No. 601 exposure increased to 2.0 in day 4 at 1
*When No. 755 infected, Exposure is 3.0 in day 4 at move 1
No. 808 exposure increased to 1.0 in day 4 at 1
No. 813 exposure increased to 2.0 in day 4 at 1
No. 886 exposure increased to 2.0 in day 4 at 1
No. 967 exposure increased to 3.0 in day 4 at 1
No. 970 exposure increased to 2.0 in day 4 at 1
No. 977 exposure increased to 3.0 in day 4 at 1
  107/10000 [..............................] - ETA: 13:57:44 - reward: 713.1508*When No. 361 infected, Exposure is 2.0 in day 4 at move 1
*When No. 46 infected, Exposure is 2.0 in day 4 at move 2
*When No. 977 infected, Exposure is 3.0 in day 4 at move 2
*When No. 99 infected, Exposure is 2.0 in day 4 at move 4
*When No. 886 infected, Exposure is 2.0 in day 4 at move 4
No. 73 exposure increased to 2.0 in day 4 at 5
No. 82 exposure increased to 1.0 in day 4 at 5
No. 133 exposure increased to 1.0 in day 4 at 5
No. 151 exposure increased to 1.0 in day 4 at 5
No. 152 exposure increased to 2.0 in day 4 at 5
No. 165 exposure increased to 3.0 in day 4 at 5
No. 172 exposure increased to 2.0 in day 4 at 5
No. 208 exposure increased to 1.0 in day 4 at 5
No. 233 exposure increased to 2.0 in day 4 at 5
No. 351 exposure increased to 4.0 in day 4 at 5
No. 407 exposure increased to 1.0 in day 4 at 5
No. 415 exposure increased to 2.0 in day 4 at 5
No. 564 exposure increased to 2.0 in day 4 at 5
No. 582 exposure increased to 1.0 in day 4 at 5
No. 601 exposure increased to 3.0 in day 4 at 5
No. 708 exposure increased to 2.0 in day 4 at 5
No. 764 exposure increased to 1.0 in day 4 at 5
No. 781 exposure increased to 1.0 in day 4 at 5
No. 808 exposure increased to 2.0 in day 4 at 5
No. 810 exposure increased to 1.0 in day 4 at 5
No. 813 exposure increased to 3.0 in day 4 at 5
No. 949 exposure increased to 1.0 in day 4 at 5
No. 967 exposure increased to 4.0 in day 4 at 5
No. 970 exposure increased to 3.0 in day 4 at 5
No. 974 exposure increased to 1.0 in day 4 at 5
  108/10000 [..............................] - ETA: 14:12:54 - reward: 713.7698*When No. 73 infected, Exposure is 2.0 in day 4 at move 0
*When No. 351 infected, Exposure is 4.0 in day 4 at move 0
*When No. 152 infected, Exposure is 2.0 in day 4 at move 2
*When No. 601 infected, Exposure is 3.0 in day 4 at move 2
*When No. 708 infected, Exposure is 2.0 in day 4 at move 2
*When No. 813 infected, Exposure is 3.0 in day 4 at move 2
*When No. 808 infected, Exposure is 2.0 in day 4 at move 4
No. 82 exposure increased to 2.0 in day 4 at 5
No. 133 exposure increased to 2.0 in day 4 at 5
No. 151 exposure increased to 2.0 in day 4 at 5
No. 165 exposure increased to 4.0 in day 4 at 5
No. 172 exposure increased to 3.0 in day 4 at 5
No. 208 exposure increased to 2.0 in day 4 at 5
No. 233 exposure increased to 3.0 in day 4 at 5
No. 238 exposure increased to 2.0 in day 4 at 5
No. 290 exposure increased to 1.0 in day 4 at 5
No. 325 exposure increased to 1.0 in day 4 at 5
No. 328 exposure increased to 1.0 in day 4 at 5
No. 381 exposure increased to 1.0 in day 4 at 5
No. 383 exposure increased to 1.0 in day 4 at 5
No. 391 exposure increased to 1.0 in day 4 at 5
No. 395 exposure increased to 1.0 in day 4 at 5
No. 407 exposure increased to 2.0 in day 4 at 5
No. 415 exposure increased to 3.0 in day 4 at 5
No. 564 exposure increased to 3.0 in day 4 at 5
No. 582 exposure increased to 2.0 in day 4 at 5
No. 585 exposure increased to 1.0 in day 4 at 5
No. 603 exposure increased to 1.0 in day 4 at 5
No. 764 exposure increased to 2.0 in day 4 at 5
No. 781 exposure increased to 2.0 in day 4 at 5
No. 810 exposure increased to 2.0 in day 4 at 5
No. 853 exposure increased to 1.0 in day 4 at 5
No. 925 exposure increased to 1.0 in day 4 at 5
No. 938 exposure increased to 2.0 in day 4 at 5
No. 949 exposure increased to 2.0 in day 4 at 5
No. 966 exposure increased to 1.0 in day 4 at 5
*When No. 967 infected, Exposure is 4.0 in day 4 at move 5
No. 970 exposure increased to 4.0 in day 4 at 5
No. 974 exposure increased to 2.0 in day 4 at 5
  109/10000 [..............................] - ETA: 14:29:33 - reward: 715.9246*When No. 165 infected, Exposure is 4.0 in day 4 at move 0
*When No. 233 infected, Exposure is 3.0 in day 4 at move 0
*When No. 781 infected, Exposure is 2.0 in day 4 at move 0
No. 82 exposure increased to 3.0 in day 4 at 1
No. 100 exposure increased to 1.0 in day 4 at 1
No. 133 exposure increased to 3.0 in day 4 at 1
No. 151 exposure increased to 3.0 in day 4 at 1
No. 172 exposure increased to 4.0 in day 4 at 1
No. 208 exposure increased to 3.0 in day 4 at 1
No. 238 exposure increased to 3.0 in day 4 at 1
No. 290 exposure increased to 2.0 in day 4 at 1
No. 325 exposure increased to 2.0 in day 4 at 1
No. 328 exposure increased to 2.0 in day 4 at 1
No. 381 exposure increased to 2.0 in day 4 at 1
No. 383 exposure increased to 2.0 in day 4 at 1
No. 391 exposure increased to 2.0 in day 4 at 1
No. 395 exposure increased to 2.0 in day 4 at 1
*When No. 407 infected, Exposure is 2.0 in day 4 at move 1
No. 415 exposure increased to 4.0 in day 4 at 1
No. 564 exposure increased to 4.0 in day 4 at 1
No. 577 exposure increased to 2.0 in day 4 at 1
No. 582 exposure increased to 3.0 in day 4 at 1
No. 585 exposure increased to 2.0 in day 4 at 1
No. 603 exposure increased to 2.0 in day 4 at 1
No. 764 exposure increased to 3.0 in day 4 at 1
No. 810 exposure increased to 3.0 in day 4 at 1
No. 828 exposure increased to 2.0 in day 4 at 1
No. 853 exposure increased to 2.0 in day 4 at 1
No. 925 exposure increased to 2.0 in day 4 at 1
No. 938 exposure increased to 3.0 in day 4 at 1
No. 949 exposure increased to 3.0 in day 4 at 1
No. 966 exposure increased to 2.0 in day 4 at 1
No. 970 exposure increased to 5.0 in day 4 at 1
*When No. 974 infected, Exposure is 2.0 in day 4 at move 1
  110/10000 [..............................] - ETA: 14:29:27 - reward: 716.4198*When No. 82 infected, Exposure is 3.0 in day 4 at move 0
*When No. 172 infected, Exposure is 4.0 in day 4 at move 0
*When No. 208 infected, Exposure is 3.0 in day 4 at move 0
*When No. 764 infected, Exposure is 3.0 in day 4 at move 0
*When No. 810 infected, Exposure is 3.0 in day 4 at move 0
*When No. 949 infected, Exposure is 3.0 in day 4 at move 0
*When No. 238 infected, Exposure is 3.0 in day 4 at move 1
*When No. 328 infected, Exposure is 2.0 in day 4 at move 1
*When No. 415 infected, Exposure is 4.0 in day 4 at move 1
*When No. 577 infected, Exposure is 2.0 in day 4 at move 1
*When No. 133 infected, Exposure is 3.0 in day 4 at move 2
*When No. 582 infected, Exposure is 3.0 in day 4 at move 2
*When No. 970 infected, Exposure is 5.0 in day 4 at move 2
*When No. 381 infected, Exposure is 2.0 in day 4 at move 3
*When No. 564 infected, Exposure is 4.0 in day 4 at move 3
No. 7 exposure increased to 1.0 in day 4 at 5
No. 52 exposure increased to 1.0 in day 4 at 5
No. 64 exposure increased to 1.0 in day 4 at 5
No. 70 exposure increased to 1.0 in day 4 at 5
No. 75 exposure increased to 1.0 in day 4 at 5
No. 100 exposure increased to 2.0 in day 4 at 5
*When No. 151 infected, Exposure is 3.0 in day 4 at move 5
No. 160 exposure increased to 2.0 in day 4 at 5
No. 200 exposure increased to 1.0 in day 4 at 5
*When No. 290 infected, Exposure is 2.0 in day 4 at move 5
No. 325 exposure increased to 3.0 in day 4 at 5
No. 345 exposure increased to 1.0 in day 4 at 5
No. 383 exposure increased to 3.0 in day 4 at 5
No. 391 exposure increased to 3.0 in day 4 at 5
No. 395 exposure increased to 3.0 in day 4 at 5
No. 422 exposure increased to 2.0 in day 4 at 5
No. 485 exposure increased to 1.0 in day 4 at 5
No. 501 exposure increased to 1.0 in day 4 at 5
No. 549 exposure increased to 1.0 in day 4 at 5
*When No. 585 infected, Exposure is 2.0 in day 4 at move 5
No. 603 exposure increased to 3.0 in day 4 at 5
No. 692 exposure increased to 1.0 in day 4 at 5
No. 713 exposure increased to 1.0 in day 4 at 5
No. 731 exposure increased to 1.0 in day 4 at 5
No. 761 exposure increased to 1.0 in day 4 at 5
No. 775 exposure increased to 1.0 in day 4 at 5
No. 779 exposure increased to 2.0 in day 4 at 5
No. 804 exposure increased to 2.0 in day 4 at 5
*When No. 828 infected, Exposure is 2.0 in day 4 at move 5
No. 853 exposure increased to 3.0 in day 4 at 5
No. 859 exposure increased to 1.0 in day 4 at 5
*When No. 925 infected, Exposure is 2.0 in day 4 at move 5
No. 938 exposure increased to 4.0 in day 4 at 5
No. 966 exposure increased to 3.0 in day 4 at 5
  111/10000 [..............................] - ETA: 14:45:40 - reward: 717.1018*When No. 160 infected, Exposure is 2.0 in day 4 at move 0
*When No. 853 infected, Exposure is 3.0 in day 4 at move 0
No. 7 exposure increased to 2.0 in day 4 at 1
No. 52 exposure increased to 2.0 in day 4 at 1
No. 64 exposure increased to 2.0 in day 4 at 1
No. 70 exposure increased to 2.0 in day 4 at 1
No. 75 exposure increased to 2.0 in day 4 at 1
No. 100 exposure increased to 3.0 in day 4 at 1
No. 200 exposure increased to 2.0 in day 4 at 1
No. 251 exposure increased to 1.0 in day 4 at 1
No. 253 exposure increased to 1.0 in day 4 at 1
No. 325 exposure increased to 4.0 in day 4 at 1
No. 345 exposure increased to 2.0 in day 4 at 1
No. 383 exposure increased to 4.0 in day 4 at 1
No. 391 exposure increased to 4.0 in day 4 at 1
No. 395 exposure increased to 4.0 in day 4 at 1
No. 422 exposure increased to 3.0 in day 4 at 1
No. 454 exposure increased to 2.0 in day 4 at 1
No. 467 exposure increased to 1.0 in day 4 at 1
No. 485 exposure increased to 2.0 in day 4 at 1
No. 497 exposure increased to 1.0 in day 4 at 1
No. 501 exposure increased to 2.0 in day 4 at 1
No. 549 exposure increased to 2.0 in day 4 at 1
No. 552 exposure increased to 1.0 in day 4 at 1
No. 603 exposure increased to 4.0 in day 4 at 1
No. 692 exposure increased to 2.0 in day 4 at 1
No. 713 exposure increased to 2.0 in day 4 at 1
No. 731 exposure increased to 2.0 in day 4 at 1
No. 761 exposure increased to 2.0 in day 4 at 1
No. 775 exposure increased to 2.0 in day 4 at 1
No. 779 exposure increased to 3.0 in day 4 at 1
No. 804 exposure increased to 3.0 in day 4 at 1
No. 844 exposure increased to 1.0 in day 4 at 1
No. 859 exposure increased to 2.0 in day 4 at 1
No. 879 exposure increased to 1.0 in day 4 at 1
No. 938 exposure increased to 5.0 in day 4 at 1
No. 966 exposure increased to 4.0 in day 4 at 1
  112/10000 [..............................] - ETA: 14:45:37 - reward: 718.9329*When No. 345 infected, Exposure is 2.0 in day 4 at move 0
*When No. 501 infected, Exposure is 2.0 in day 4 at move 0
*When No. 966 infected, Exposure is 4.0 in day 4 at move 0
*When No. 52 infected, Exposure is 2.0 in day 4 at move 1
*When No. 75 infected, Exposure is 2.0 in day 4 at move 1
*When No. 200 infected, Exposure is 2.0 in day 4 at move 1
*When No. 775 infected, Exposure is 2.0 in day 4 at move 1
*When No. 325 infected, Exposure is 4.0 in day 4 at move 2
*When No. 804 infected, Exposure is 3.0 in day 4 at move 2
*When No. 938 infected, Exposure is 5.0 in day 4 at move 2
*When No. 395 infected, Exposure is 4.0 in day 4 at move 3
*When No. 422 infected, Exposure is 3.0 in day 4 at move 3
*When No. 731 infected, Exposure is 2.0 in day 4 at move 3
*When No. 454 infected, Exposure is 2.0 in day 4 at move 4
*When No. 761 infected, Exposure is 2.0 in day 4 at move 4
No. 6 exposure increased to 1.0 in day 4 at 5
No. 7 exposure increased to 3.0 in day 4 at 5
No. 23 exposure increased to 1.0 in day 4 at 5
No. 43 exposure increased to 1.0 in day 4 at 5
No. 57 exposure increased to 2.0 in day 4 at 5
No. 64 exposure increased to 3.0 in day 4 at 5
*When No. 70 infected, Exposure is 2.0 in day 4 at move 5
No. 88 exposure increased to 1.0 in day 4 at 5
No. 100 exposure increased to 4.0 in day 4 at 5
No. 218 exposure increased to 2.0 in day 4 at 5
No. 224 exposure increased to 1.0 in day 4 at 5
No. 229 exposure increased to 2.0 in day 4 at 5
No. 251 exposure increased to 2.0 in day 4 at 5
No. 253 exposure increased to 2.0 in day 4 at 5
No. 291 exposure increased to 1.0 in day 4 at 5
No. 310 exposure increased to 1.0 in day 4 at 5
No. 359 exposure increased to 1.0 in day 4 at 5
No. 372 exposure increased to 2.0 in day 4 at 5
No. 383 exposure increased to 5.0 in day 4 at 5
*When No. 391 infected, Exposure is 4.0 in day 4 at move 5
No. 412 exposure increased to 1.0 in day 4 at 5
No. 467 exposure increased to 2.0 in day 4 at 5
No. 473 exposure increased to 1.0 in day 4 at 5
No. 476 exposure increased to 1.0 in day 4 at 5
No. 485 exposure increased to 3.0 in day 4 at 5
No. 497 exposure increased to 2.0 in day 4 at 5
No. 534 exposure increased to 1.0 in day 4 at 5
No. 539 exposure increased to 1.0 in day 4 at 5
No. 549 exposure increased to 3.0 in day 4 at 5
No. 552 exposure increased to 2.0 in day 4 at 5
No. 597 exposure increased to 2.0 in day 4 at 5
No. 603 exposure increased to 5.0 in day 4 at 5
No. 605 exposure increased to 1.0 in day 4 at 5
No. 608 exposure increased to 1.0 in day 4 at 5
No. 692 exposure increased to 3.0 in day 4 at 5
*When No. 713 infected, Exposure is 2.0 in day 4 at move 5
No. 753 exposure increased to 1.0 in day 4 at 5
*When No. 779 infected, Exposure is 3.0 in day 4 at move 5
No. 844 exposure increased to 2.0 in day 4 at 5
No. 859 exposure increased to 3.0 in day 4 at 5
No. 867 exposure increased to 1.0 in day 4 at 5
No. 879 exposure increased to 2.0 in day 4 at 5
No. 891 exposure increased to 1.0 in day 4 at 5
No. 943 exposure increased to 2.0 in day 4 at 5
No. 945 exposure increased to 1.0 in day 4 at 5
No. 964 exposure increased to 1.0 in day 4 at 5
No. 999 exposure increased to 1.0 in day 4 at 5
  113/10000 [..............................] - ETA: 15:00:50 - reward: 719.6692*When No. 383 infected, Exposure is 5.0 in day 4 at move 0
*When No. 467 infected, Exposure is 2.0 in day 4 at move 0
*When No. 485 infected, Exposure is 3.0 in day 4 at move 0
*When No. 552 infected, Exposure is 2.0 in day 4 at move 0
*When No. 859 infected, Exposure is 3.0 in day 4 at move 0
*When No. 879 infected, Exposure is 2.0 in day 4 at move 0
No. 6 exposure increased to 2.0 in day 4 at 1
*When No. 7 infected, Exposure is 3.0 in day 4 at move 1
No. 23 exposure increased to 2.0 in day 4 at 1
No. 43 exposure increased to 2.0 in day 4 at 1
No. 57 exposure increased to 3.0 in day 4 at 1
No. 64 exposure increased to 4.0 in day 4 at 1
No. 88 exposure increased to 2.0 in day 4 at 1
*When No. 100 infected, Exposure is 4.0 in day 4 at move 1
No. 218 exposure increased to 3.0 in day 4 at 1
No. 224 exposure increased to 2.0 in day 4 at 1
No. 229 exposure increased to 3.0 in day 4 at 1
No. 251 exposure increased to 3.0 in day 4 at 1
No. 253 exposure increased to 3.0 in day 4 at 1
No. 256 exposure increased to 1.0 in day 4 at 1
No. 291 exposure increased to 2.0 in day 4 at 1
No. 310 exposure increased to 2.0 in day 4 at 1
No. 359 exposure increased to 2.0 in day 4 at 1
No. 372 exposure increased to 3.0 in day 4 at 1
No. 408 exposure increased to 2.0 in day 4 at 1
No. 412 exposure increased to 2.0 in day 4 at 1
No. 473 exposure increased to 2.0 in day 4 at 1
No. 476 exposure increased to 2.0 in day 4 at 1
No. 497 exposure increased to 3.0 in day 4 at 1
No. 534 exposure increased to 2.0 in day 4 at 1
No. 539 exposure increased to 2.0 in day 4 at 1
No. 549 exposure increased to 4.0 in day 4 at 1
No. 557 exposure increased to 1.0 in day 4 at 1
No. 597 exposure increased to 3.0 in day 4 at 1
No. 603 exposure increased to 6.0 in day 4 at 1
No. 605 exposure increased to 2.0 in day 4 at 1
No. 608 exposure increased to 2.0 in day 4 at 1
No. 642 exposure increased to 2.0 in day 4 at 1
No. 678 exposure increased to 2.0 in day 4 at 1
No. 692 exposure increased to 4.0 in day 4 at 1
No. 707 exposure increased to 1.0 in day 4 at 1
No. 753 exposure increased to 2.0 in day 4 at 1
No. 778 exposure increased to 1.0 in day 4 at 1
No. 836 exposure increased to 1.0 in day 4 at 1
No. 844 exposure increased to 3.0 in day 4 at 1
No. 867 exposure increased to 2.0 in day 4 at 1
No. 878 exposure increased to 1.0 in day 4 at 1
No. 891 exposure increased to 2.0 in day 4 at 1
No. 943 exposure increased to 3.0 in day 4 at 1
No. 945 exposure increased to 2.0 in day 4 at 1
No. 964 exposure increased to 2.0 in day 4 at 1
No. 986 exposure increased to 2.0 in day 4 at 1
No. 999 exposure increased to 2.0 in day 4 at 1
  114/10000 [..............................] - ETA: 15:01:21 - reward: 721.0532*When No. 372 infected, Exposure is 3.0 in day 4 at move 0
*When No. 603 infected, Exposure is 6.0 in day 4 at move 0
*When No. 844 infected, Exposure is 3.0 in day 4 at move 0
*When No. 943 infected, Exposure is 3.0 in day 4 at move 0
*When No. 945 infected, Exposure is 2.0 in day 4 at move 0
No. 6 exposure increased to 3.0 in day 4 at 1
No. 14 exposure increased to 2.0 in day 4 at 1
No. 18 exposure increased to 2.0 in day 4 at 1
No. 23 exposure increased to 3.0 in day 4 at 1
No. 43 exposure increased to 3.0 in day 4 at 1
No. 57 exposure increased to 4.0 in day 4 at 1
No. 64 exposure increased to 5.0 in day 4 at 1
No. 88 exposure increased to 3.0 in day 4 at 1
No. 218 exposure increased to 4.0 in day 4 at 1
No. 224 exposure increased to 3.0 in day 4 at 1
No. 229 exposure increased to 4.0 in day 4 at 1
*When No. 251 infected, Exposure is 3.0 in day 4 at move 1
No. 253 exposure increased to 4.0 in day 4 at 1
No. 256 exposure increased to 2.0 in day 4 at 1
No. 260 exposure increased to 2.0 in day 4 at 1
No. 291 exposure increased to 3.0 in day 4 at 1
No. 310 exposure increased to 3.0 in day 4 at 1
No. 359 exposure increased to 3.0 in day 4 at 1
No. 387 exposure increased to 1.0 in day 4 at 1
No. 408 exposure increased to 3.0 in day 4 at 1
*When No. 412 infected, Exposure is 2.0 in day 4 at move 1
No. 473 exposure increased to 3.0 in day 4 at 1
No. 476 exposure increased to 3.0 in day 4 at 1
No. 497 exposure increased to 4.0 in day 4 at 1
No. 534 exposure increased to 3.0 in day 4 at 1
No. 539 exposure increased to 3.0 in day 4 at 1
No. 549 exposure increased to 5.0 in day 4 at 1
No. 557 exposure increased to 2.0 in day 4 at 1
*When No. 597 infected, Exposure is 3.0 in day 4 at move 1
No. 605 exposure increased to 3.0 in day 4 at 1
No. 608 exposure increased to 3.0 in day 4 at 1
*When No. 642 infected, Exposure is 2.0 in day 4 at move 1
No. 678 exposure increased to 3.0 in day 4 at 1
*When No. 692 infected, Exposure is 4.0 in day 4 at move 1
No. 707 exposure increased to 2.0 in day 4 at 1
*When No. 753 infected, Exposure is 2.0 in day 4 at move 1
No. 778 exposure increased to 2.0 in day 4 at 1
No. 836 exposure increased to 2.0 in day 4 at 1
No. 867 exposure increased to 3.0 in day 4 at 1
No. 878 exposure increased to 2.0 in day 4 at 1
No. 891 exposure increased to 3.0 in day 4 at 1
No. 964 exposure increased to 3.0 in day 4 at 1
No. 986 exposure increased to 3.0 in day 4 at 1
No. 995 exposure increased to 1.0 in day 4 at 1
No. 999 exposure increased to 3.0 in day 4 at 1
  115/10000 [..............................] - ETA: 15:01:22 - reward: 722.0857*When No. 64 infected, Exposure is 5.0 in day 4 at move 0
*When No. 229 infected, Exposure is 4.0 in day 4 at move 0
*When No. 253 infected, Exposure is 4.0 in day 4 at move 0
*When No. 497 infected, Exposure is 4.0 in day 4 at move 0
*When No. 534 infected, Exposure is 3.0 in day 4 at move 0
*When No. 57 infected, Exposure is 4.0 in day 4 at move 1
*When No. 549 infected, Exposure is 5.0 in day 4 at move 1
*When No. 605 infected, Exposure is 3.0 in day 4 at move 1
*When No. 878 infected, Exposure is 2.0 in day 4 at move 1
*When No. 986 infected, Exposure is 3.0 in day 4 at move 1
*When No. 88 infected, Exposure is 3.0 in day 4 at move 2
*When No. 218 infected, Exposure is 4.0 in day 4 at move 2
*When No. 291 infected, Exposure is 3.0 in day 4 at move 2
*When No. 778 infected, Exposure is 2.0 in day 4 at move 2
*When No. 18 infected, Exposure is 2.0 in day 4 at move 3
*When No. 260 infected, Exposure is 2.0 in day 4 at move 3
*When No. 310 infected, Exposure is 3.0 in day 4 at move 3
*When No. 473 infected, Exposure is 3.0 in day 4 at move 3
*When No. 539 infected, Exposure is 3.0 in day 4 at move 3
*When No. 891 infected, Exposure is 3.0 in day 4 at move 3
*When No. 408 infected, Exposure is 3.0 in day 4 at move 4
*When No. 476 infected, Exposure is 3.0 in day 4 at move 4
*When No. 836 infected, Exposure is 2.0 in day 4 at move 4
*When No. 6 infected, Exposure is 3.0 in day 4 at move 5
No. 14 exposure increased to 3.0 in day 4 at 5
No. 23 exposure increased to 4.0 in day 4 at 5
No. 43 exposure increased to 4.0 in day 4 at 5
No. 51 exposure increased to 1.0 in day 4 at 5
No. 106 exposure increased to 1.0 in day 4 at 5
No. 110 exposure increased to 1.0 in day 4 at 5
No. 176 exposure increased to 1.0 in day 4 at 5
No. 193 exposure increased to 1.0 in day 4 at 5
No. 224 exposure increased to 4.0 in day 4 at 5
No. 232 exposure increased to 1.0 in day 4 at 5
No. 256 exposure increased to 3.0 in day 4 at 5
No. 267 exposure increased to 1.0 in day 4 at 5
No. 271 exposure increased to 2.0 in day 4 at 5
No. 348 exposure increased to 1.0 in day 4 at 5
No. 358 exposure increased to 2.0 in day 4 at 5
No. 359 exposure increased to 4.0 in day 4 at 5
No. 387 exposure increased to 2.0 in day 4 at 5
No. 396 exposure increased to 2.0 in day 4 at 5
No. 424 exposure increased to 2.0 in day 4 at 5
No. 432 exposure increased to 1.0 in day 4 at 5
No. 461 exposure increased to 2.0 in day 4 at 5
No. 486 exposure increased to 1.0 in day 4 at 5
No. 490 exposure increased to 1.0 in day 4 at 5
No. 491 exposure increased to 1.0 in day 4 at 5
No. 524 exposure increased to 1.0 in day 4 at 5
No. 526 exposure increased to 2.0 in day 4 at 5
No. 532 exposure increased to 1.0 in day 4 at 5
No. 533 exposure increased to 1.0 in day 4 at 5
No. 536 exposure increased to 1.0 in day 4 at 5
No. 540 exposure increased to 1.0 in day 4 at 5
No. 542 exposure increased to 1.0 in day 4 at 5
No. 557 exposure increased to 3.0 in day 4 at 5
No. 566 exposure increased to 1.0 in day 4 at 5
No. 590 exposure increased to 1.0 in day 4 at 5
No. 608 exposure increased to 4.0 in day 4 at 5
No. 645 exposure increased to 1.0 in day 4 at 5
No. 678 exposure increased to 4.0 in day 4 at 5
No. 684 exposure increased to 1.0 in day 4 at 5
No. 703 exposure increased to 2.0 in day 4 at 5
No. 707 exposure increased to 3.0 in day 4 at 5
No. 709 exposure increased to 1.0 in day 4 at 5
No. 766 exposure increased to 1.0 in day 4 at 5
No. 831 exposure increased to 2.0 in day 4 at 5
No. 867 exposure increased to 4.0 in day 4 at 5
No. 913 exposure increased to 1.0 in day 4 at 5
No. 930 exposure increased to 2.0 in day 4 at 5
No. 947 exposure increased to 1.0 in day 4 at 5
No. 964 exposure increased to 4.0 in day 4 at 5
No. 984 exposure increased to 1.0 in day 4 at 5
No. 989 exposure increased to 1.0 in day 4 at 5
No. 995 exposure increased to 2.0 in day 4 at 5
*When No. 999 infected, Exposure is 3.0 in day 4 at move 5
  116/10000 [..............................] - ETA: 15:17:30 - reward: 721.9916*When No. 43 infected, Exposure is 4.0 in day 4 at move 0
*When No. 256 infected, Exposure is 3.0 in day 4 at move 0
*When No. 678 infected, Exposure is 4.0 in day 4 at move 0
*When No. 703 infected, Exposure is 2.0 in day 4 at move 0
*When No. 930 infected, Exposure is 2.0 in day 4 at move 0
*When No. 995 infected, Exposure is 2.0 in day 4 at move 0
*When No. 271 infected, Exposure is 2.0 in day 4 at move 1
*When No. 526 infected, Exposure is 2.0 in day 4 at move 1
*When No. 14 infected, Exposure is 3.0 in day 4 at move 2
*When No. 224 infected, Exposure is 4.0 in day 4 at move 2
*When No. 359 infected, Exposure is 4.0 in day 4 at move 2
*When No. 831 infected, Exposure is 2.0 in day 4 at move 2
*When No. 461 infected, Exposure is 2.0 in day 4 at move 3
*When No. 707 infected, Exposure is 3.0 in day 4 at move 3
*When No. 964 infected, Exposure is 4.0 in day 4 at move 3
*When No. 608 infected, Exposure is 4.0 in day 4 at move 4
*When No. 867 infected, Exposure is 4.0 in day 4 at move 4
No. 23 exposure increased to 5.0 in day 4 at 5
No. 51 exposure increased to 2.0 in day 4 at 5
No. 106 exposure increased to 2.0 in day 4 at 5
No. 110 exposure increased to 2.0 in day 4 at 5
No. 131 exposure increased to 1.0 in day 4 at 5
No. 154 exposure increased to 1.0 in day 4 at 5
No. 176 exposure increased to 2.0 in day 4 at 5
No. 193 exposure increased to 2.0 in day 4 at 5
No. 207 exposure increased to 1.0 in day 4 at 5
No. 211 exposure increased to 1.0 in day 4 at 5
No. 213 exposure increased to 1.0 in day 4 at 5
No. 225 exposure increased to 1.0 in day 4 at 5
No. 232 exposure increased to 2.0 in day 4 at 5
No. 236 exposure increased to 1.0 in day 4 at 5
No. 267 exposure increased to 2.0 in day 4 at 5
No. 268 exposure increased to 1.0 in day 4 at 5
No. 301 exposure increased to 1.0 in day 4 at 5
No. 331 exposure increased to 1.0 in day 4 at 5
No. 338 exposure increased to 1.0 in day 4 at 5
No. 348 exposure increased to 2.0 in day 4 at 5
No. 352 exposure increased to 1.0 in day 4 at 5
No. 358 exposure increased to 3.0 in day 4 at 5
No. 377 exposure increased to 2.0 in day 4 at 5
No. 387 exposure increased to 3.0 in day 4 at 5
*When No. 396 infected, Exposure is 2.0 in day 4 at move 5
No. 424 exposure increased to 3.0 in day 4 at 5
No. 432 exposure increased to 2.0 in day 4 at 5
No. 453 exposure increased to 1.0 in day 4 at 5
No. 455 exposure increased to 1.0 in day 4 at 5
No. 486 exposure increased to 2.0 in day 4 at 5
No. 490 exposure increased to 2.0 in day 4 at 5
No. 491 exposure increased to 2.0 in day 4 at 5
No. 524 exposure increased to 2.0 in day 4 at 5
No. 529 exposure increased to 1.0 in day 4 at 5
No. 532 exposure increased to 2.0 in day 4 at 5
No. 533 exposure increased to 2.0 in day 4 at 5
No. 536 exposure increased to 2.0 in day 4 at 5
No. 540 exposure increased to 2.0 in day 4 at 5
No. 542 exposure increased to 2.0 in day 4 at 5
No. 557 exposure increased to 4.0 in day 4 at 5
No. 566 exposure increased to 2.0 in day 4 at 5
No. 590 exposure increased to 2.0 in day 4 at 5
No. 598 exposure increased to 1.0 in day 4 at 5
No. 610 exposure increased to 1.0 in day 4 at 5
No. 612 exposure increased to 1.0 in day 4 at 5
No. 628 exposure increased to 2.0 in day 4 at 5
No. 645 exposure increased to 2.0 in day 4 at 5
No. 684 exposure increased to 2.0 in day 4 at 5
No. 699 exposure increased to 1.0 in day 4 at 5
No. 709 exposure increased to 2.0 in day 4 at 5
No. 722 exposure increased to 1.0 in day 4 at 5
No. 734 exposure increased to 1.0 in day 4 at 5
No. 744 exposure increased to 1.0 in day 4 at 5
No. 766 exposure increased to 2.0 in day 4 at 5
No. 791 exposure increased to 1.0 in day 4 at 5
No. 855 exposure increased to 1.0 in day 4 at 5
No. 896 exposure increased to 1.0 in day 4 at 5
No. 910 exposure increased to 1.0 in day 4 at 5
No. 913 exposure increased to 2.0 in day 4 at 5
No. 917 exposure increased to 1.0 in day 4 at 5
No. 934 exposure increased to 1.0 in day 4 at 5
No. 944 exposure increased to 1.0 in day 4 at 5
No. 947 exposure increased to 2.0 in day 4 at 5
No. 984 exposure increased to 2.0 in day 4 at 5
No. 989 exposure increased to 2.0 in day 4 at 5
  117/10000 [..............................] - ETA: 15:34:09 - reward: 721.9951*When No. 106 infected, Exposure is 2.0 in day 4 at move 0
*When No. 540 infected, Exposure is 2.0 in day 4 at move 0
*When No. 628 infected, Exposure is 2.0 in day 4 at move 0
*When No. 913 infected, Exposure is 2.0 in day 4 at move 0
*When No. 23 infected, Exposure is 5.0 in day 4 at move 1
*When No. 387 infected, Exposure is 3.0 in day 4 at move 1
*When No. 566 infected, Exposure is 2.0 in day 4 at move 1
*When No. 193 infected, Exposure is 2.0 in day 4 at move 2
*When No. 557 infected, Exposure is 4.0 in day 4 at move 2
*When No. 984 infected, Exposure is 2.0 in day 4 at move 2
*When No. 51 infected, Exposure is 2.0 in day 4 at move 3
*When No. 358 infected, Exposure is 3.0 in day 4 at move 3
*When No. 424 infected, Exposure is 3.0 in day 4 at move 3
*When No. 491 infected, Exposure is 2.0 in day 4 at move 3
*When No. 377 infected, Exposure is 2.0 in day 4 at move 4
No. 9 exposure increased to 1.0 in day 4 at 5
No. 10 exposure increased to 1.0 in day 4 at 5
No. 45 exposure increased to 1.0 in day 4 at 5
No. 84 exposure increased to 1.0 in day 4 at 5
No. 110 exposure increased to 3.0 in day 4 at 5
No. 117 exposure increased to 1.0 in day 4 at 5
No. 127 exposure increased to 1.0 in day 4 at 5
No. 131 exposure increased to 2.0 in day 4 at 5
No. 154 exposure increased to 2.0 in day 4 at 5
No. 157 exposure increased to 1.0 in day 4 at 5
No. 176 exposure increased to 3.0 in day 4 at 5
No. 202 exposure increased to 1.0 in day 4 at 5
No. 207 exposure increased to 2.0 in day 4 at 5
No. 211 exposure increased to 2.0 in day 4 at 5
No. 213 exposure increased to 2.0 in day 4 at 5
No. 225 exposure increased to 2.0 in day 4 at 5
No. 232 exposure increased to 3.0 in day 4 at 5
No. 236 exposure increased to 2.0 in day 4 at 5
No. 258 exposure increased to 1.0 in day 4 at 5
No. 262 exposure increased to 2.0 in day 4 at 5
*When No. 267 infected, Exposure is 2.0 in day 4 at move 5
No. 268 exposure increased to 2.0 in day 4 at 5
No. 280 exposure increased to 1.0 in day 4 at 5
No. 283 exposure increased to 1.0 in day 4 at 5
No. 292 exposure increased to 1.0 in day 4 at 5
No. 301 exposure increased to 2.0 in day 4 at 5
No. 331 exposure increased to 2.0 in day 4 at 5
No. 338 exposure increased to 2.0 in day 4 at 5
No. 343 exposure increased to 1.0 in day 4 at 5
No. 346 exposure increased to 1.0 in day 4 at 5
No. 348 exposure increased to 3.0 in day 4 at 5
No. 352 exposure increased to 2.0 in day 4 at 5
No. 385 exposure increased to 1.0 in day 4 at 5
No. 420 exposure increased to 1.0 in day 4 at 5
No. 432 exposure increased to 3.0 in day 4 at 5
No. 445 exposure increased to 1.0 in day 4 at 5
No. 453 exposure increased to 2.0 in day 4 at 5
No. 455 exposure increased to 2.0 in day 4 at 5
No. 486 exposure increased to 3.0 in day 4 at 5
*When No. 490 infected, Exposure is 2.0 in day 4 at move 5
No. 492 exposure increased to 1.0 in day 4 at 5
No. 513 exposure increased to 1.0 in day 4 at 5
*When No. 524 infected, Exposure is 2.0 in day 4 at move 5
No. 529 exposure increased to 2.0 in day 4 at 5
*When No. 532 infected, Exposure is 2.0 in day 4 at move 5
No. 533 exposure increased to 3.0 in day 4 at 5
No. 536 exposure increased to 3.0 in day 4 at 5
No. 542 exposure increased to 3.0 in day 4 at 5
No. 554 exposure increased to 2.0 in day 4 at 5
No. 558 exposure increased to 1.0 in day 4 at 5
No. 590 exposure increased to 3.0 in day 4 at 5
No. 596 exposure increased to 1.0 in day 4 at 5
No. 598 exposure increased to 2.0 in day 4 at 5
No. 610 exposure increased to 2.0 in day 4 at 5
No. 612 exposure increased to 2.0 in day 4 at 5
No. 614 exposure increased to 1.0 in day 4 at 5
No. 638 exposure increased to 2.0 in day 4 at 5
No. 645 exposure increased to 3.0 in day 4 at 5
No. 684 exposure increased to 3.0 in day 4 at 5
No. 699 exposure increased to 2.0 in day 4 at 5
*When No. 709 infected, Exposure is 2.0 in day 4 at move 5
No. 722 exposure increased to 2.0 in day 4 at 5
No. 734 exposure increased to 2.0 in day 4 at 5
No. 744 exposure increased to 2.0 in day 4 at 5
No. 749 exposure increased to 1.0 in day 4 at 5
No. 762 exposure increased to 1.0 in day 4 at 5
No. 766 exposure increased to 3.0 in day 4 at 5
No. 788 exposure increased to 1.0 in day 4 at 5
No. 791 exposure increased to 2.0 in day 4 at 5
No. 816 exposure increased to 1.0 in day 4 at 5
No. 820 exposure increased to 2.0 in day 4 at 5
No. 855 exposure increased to 2.0 in day 4 at 5
No. 872 exposure increased to 1.0 in day 4 at 5
No. 896 exposure increased to 2.0 in day 4 at 5
No. 910 exposure increased to 2.0 in day 4 at 5
No. 917 exposure increased to 2.0 in day 4 at 5
No. 934 exposure increased to 2.0 in day 4 at 5
No. 936 exposure increased to 1.0 in day 4 at 5
No. 944 exposure increased to 2.0 in day 4 at 5
No. 947 exposure increased to 3.0 in day 4 at 5
No. 989 exposure increased to 3.0 in day 4 at 5
  118/10000 [..............................] - ETA: 15:49:42 - reward: 722.2121*When No. 213 infected, Exposure is 2.0 in day 4 at move 0
*When No. 262 infected, Exposure is 2.0 in day 4 at move 0
*When No. 348 infected, Exposure is 3.0 in day 4 at move 0
*When No. 533 infected, Exposure is 3.0 in day 4 at move 0
*When No. 536 infected, Exposure is 3.0 in day 4 at move 0
*When No. 722 infected, Exposure is 2.0 in day 4 at move 0
*When No. 947 infected, Exposure is 3.0 in day 4 at move 0
No. 9 exposure increased to 2.0 in day 4 at 1
No. 10 exposure increased to 2.0 in day 4 at 1
No. 45 exposure increased to 2.0 in day 4 at 1
No. 84 exposure increased to 2.0 in day 4 at 1
No. 98 exposure increased to 1.0 in day 4 at 1
No. 101 exposure increased to 2.0 in day 4 at 1
No. 110 exposure increased to 4.0 in day 4 at 1
No. 117 exposure increased to 2.0 in day 4 at 1
No. 127 exposure increased to 2.0 in day 4 at 1
No. 131 exposure increased to 3.0 in day 4 at 1
No. 137 exposure increased to 2.0 in day 4 at 1
No. 154 exposure increased to 3.0 in day 4 at 1
No. 157 exposure increased to 2.0 in day 4 at 1
No. 163 exposure increased to 1.0 in day 4 at 1
*When No. 176 infected, Exposure is 3.0 in day 4 at move 1
No. 202 exposure increased to 2.0 in day 4 at 1
No. 207 exposure increased to 3.0 in day 4 at 1
No. 211 exposure increased to 3.0 in day 4 at 1
No. 225 exposure increased to 3.0 in day 4 at 1
No. 232 exposure increased to 4.0 in day 4 at 1
No. 236 exposure increased to 3.0 in day 4 at 1
No. 258 exposure increased to 2.0 in day 4 at 1
No. 268 exposure increased to 3.0 in day 4 at 1
No. 280 exposure increased to 2.0 in day 4 at 1
No. 283 exposure increased to 2.0 in day 4 at 1
No. 292 exposure increased to 2.0 in day 4 at 1
No. 301 exposure increased to 3.0 in day 4 at 1
No. 331 exposure increased to 3.0 in day 4 at 1
No. 338 exposure increased to 3.0 in day 4 at 1
No. 343 exposure increased to 2.0 in day 4 at 1
No. 346 exposure increased to 2.0 in day 4 at 1
No. 352 exposure increased to 3.0 in day 4 at 1
No. 385 exposure increased to 2.0 in day 4 at 1
No. 420 exposure increased to 2.0 in day 4 at 1
No. 432 exposure increased to 4.0 in day 4 at 1
No. 445 exposure increased to 2.0 in day 4 at 1
No. 453 exposure increased to 3.0 in day 4 at 1
No. 455 exposure increased to 3.0 in day 4 at 1
No. 486 exposure increased to 4.0 in day 4 at 1
No. 492 exposure increased to 2.0 in day 4 at 1
No. 513 exposure increased to 2.0 in day 4 at 1
No. 529 exposure increased to 3.0 in day 4 at 1
No. 542 exposure increased to 4.0 in day 4 at 1
No. 554 exposure increased to 3.0 in day 4 at 1
No. 558 exposure increased to 2.0 in day 4 at 1
No. 590 exposure increased to 4.0 in day 4 at 1
No. 596 exposure increased to 2.0 in day 4 at 1
*When No. 598 infected, Exposure is 2.0 in day 4 at move 1
No. 610 exposure increased to 3.0 in day 4 at 1
No. 612 exposure increased to 3.0 in day 4 at 1
No. 614 exposure increased to 2.0 in day 4 at 1
*When No. 638 infected, Exposure is 2.0 in day 4 at move 1
No. 645 exposure increased to 4.0 in day 4 at 1
No. 677 exposure increased to 1.0 in day 4 at 1
*When No. 684 infected, Exposure is 3.0 in day 4 at move 1
No. 699 exposure increased to 3.0 in day 4 at 1
No. 706 exposure increased to 2.0 in day 4 at 1
No. 734 exposure increased to 3.0 in day 4 at 1
No. 744 exposure increased to 3.0 in day 4 at 1
No. 749 exposure increased to 2.0 in day 4 at 1
No. 762 exposure increased to 2.0 in day 4 at 1
No. 766 exposure increased to 4.0 in day 4 at 1
No. 788 exposure increased to 2.0 in day 4 at 1
No. 791 exposure increased to 3.0 in day 4 at 1
No. 816 exposure increased to 2.0 in day 4 at 1
No. 820 exposure increased to 3.0 in day 4 at 1
No. 855 exposure increased to 3.0 in day 4 at 1
No. 872 exposure increased to 2.0 in day 4 at 1
No. 888 exposure increased to 1.0 in day 4 at 1
No. 896 exposure increased to 3.0 in day 4 at 1
*When No. 910 infected, Exposure is 2.0 in day 4 at move 1
No. 917 exposure increased to 3.0 in day 4 at 1
No. 934 exposure increased to 3.0 in day 4 at 1
No. 936 exposure increased to 2.0 in day 4 at 1
No. 944 exposure increased to 3.0 in day 4 at 1
No. 989 exposure increased to 4.0 in day 4 at 1
  119/10000 [..............................] - ETA: 15:49:50 - reward: 722.6140*When No. 45 infected, Exposure is 2.0 in day 4 at move 0
*When No. 211 infected, Exposure is 3.0 in day 4 at move 0
*When No. 236 infected, Exposure is 3.0 in day 4 at move 0
*When No. 292 infected, Exposure is 2.0 in day 4 at move 0
*When No. 432 infected, Exposure is 4.0 in day 4 at move 0
*When No. 455 infected, Exposure is 3.0 in day 4 at move 0
*When No. 486 infected, Exposure is 4.0 in day 4 at move 0
*When No. 645 infected, Exposure is 4.0 in day 4 at move 0
*When No. 699 infected, Exposure is 3.0 in day 4 at move 0
*When No. 766 infected, Exposure is 4.0 in day 4 at move 0
*When No. 816 infected, Exposure is 2.0 in day 4 at move 0
*When No. 896 infected, Exposure is 3.0 in day 4 at move 0
No. 9 exposure increased to 3.0 in day 4 at 1
No. 10 exposure increased to 3.0 in day 4 at 1
No. 55 exposure increased to 2.0 in day 4 at 1
*When No. 84 infected, Exposure is 2.0 in day 4 at move 1
No. 98 exposure increased to 2.0 in day 4 at 1
No. 101 exposure increased to 3.0 in day 4 at 1
No. 110 exposure increased to 5.0 in day 4 at 1
No. 117 exposure increased to 3.0 in day 4 at 1
No. 127 exposure increased to 3.0 in day 4 at 1
No. 131 exposure increased to 4.0 in day 4 at 1
*When No. 137 infected, Exposure is 2.0 in day 4 at move 1
No. 154 exposure increased to 4.0 in day 4 at 1
No. 157 exposure increased to 3.0 in day 4 at 1
No. 163 exposure increased to 2.0 in day 4 at 1
No. 169 exposure increased to 1.0 in day 4 at 1
No. 197 exposure increased to 1.0 in day 4 at 1
No. 202 exposure increased to 3.0 in day 4 at 1
*When No. 207 infected, Exposure is 3.0 in day 4 at move 1
No. 210 exposure increased to 1.0 in day 4 at 1
*When No. 225 infected, Exposure is 3.0 in day 4 at move 1
No. 232 exposure increased to 5.0 in day 4 at 1
No. 258 exposure increased to 3.0 in day 4 at 1
No. 268 exposure increased to 4.0 in day 4 at 1
No. 280 exposure increased to 3.0 in day 4 at 1
No. 283 exposure increased to 3.0 in day 4 at 1
No. 301 exposure increased to 4.0 in day 4 at 1
No. 331 exposure increased to 4.0 in day 4 at 1
No. 338 exposure increased to 4.0 in day 4 at 1
No. 343 exposure increased to 3.0 in day 4 at 1
*When No. 346 infected, Exposure is 2.0 in day 4 at move 1
No. 352 exposure increased to 4.0 in day 4 at 1
No. 378 exposure increased to 2.0 in day 4 at 1
No. 385 exposure increased to 3.0 in day 4 at 1
No. 404 exposure increased to 2.0 in day 4 at 1
No. 420 exposure increased to 3.0 in day 4 at 1
No. 445 exposure increased to 3.0 in day 4 at 1
No. 453 exposure increased to 4.0 in day 4 at 1
No. 492 exposure increased to 3.0 in day 4 at 1
No. 513 exposure increased to 3.0 in day 4 at 1
*When No. 529 infected, Exposure is 3.0 in day 4 at move 1
No. 542 exposure increased to 5.0 in day 4 at 1
No. 554 exposure increased to 4.0 in day 4 at 1
No. 558 exposure increased to 3.0 in day 4 at 1
*When No. 590 infected, Exposure is 4.0 in day 4 at move 1
No. 596 exposure increased to 3.0 in day 4 at 1
No. 610 exposure increased to 4.0 in day 4 at 1
*When No. 612 infected, Exposure is 3.0 in day 4 at move 1
*When No. 614 infected, Exposure is 2.0 in day 4 at move 1
No. 629 exposure increased to 2.0 in day 4 at 1
No. 640 exposure increased to 2.0 in day 4 at 1
No. 651 exposure increased to 2.0 in day 4 at 1
No. 677 exposure increased to 2.0 in day 4 at 1
No. 706 exposure increased to 3.0 in day 4 at 1
No. 715 exposure increased to 1.0 in day 4 at 1
No. 734 exposure increased to 4.0 in day 4 at 1
No. 744 exposure increased to 4.0 in day 4 at 1
No. 749 exposure increased to 3.0 in day 4 at 1
No. 762 exposure increased to 3.0 in day 4 at 1
No. 774 exposure increased to 1.0 in day 4 at 1
No. 788 exposure increased to 3.0 in day 4 at 1
No. 791 exposure increased to 4.0 in day 4 at 1
No. 820 exposure increased to 4.0 in day 4 at 1
No. 855 exposure increased to 4.0 in day 4 at 1
No. 872 exposure increased to 3.0 in day 4 at 1
No. 888 exposure increased to 2.0 in day 4 at 1
*When No. 917 infected, Exposure is 3.0 in day 4 at move 1
No. 934 exposure increased to 4.0 in day 4 at 1
No. 936 exposure increased to 3.0 in day 4 at 1
No. 944 exposure increased to 4.0 in day 4 at 1
*When No. 989 infected, Exposure is 4.0 in day 4 at move 1
  120/10000 [..............................] - ETA: 15:50:03 - reward: 722.2943*When No. 9 infected, Exposure is 3.0 in day 4 at move 0
*When No. 127 infected, Exposure is 3.0 in day 4 at move 0
*When No. 131 infected, Exposure is 4.0 in day 4 at move 0
*When No. 232 infected, Exposure is 5.0 in day 4 at move 0
*When No. 268 infected, Exposure is 4.0 in day 4 at move 0
*When No. 283 infected, Exposure is 3.0 in day 4 at move 0
*When No. 378 infected, Exposure is 2.0 in day 4 at move 0
*When No. 385 infected, Exposure is 3.0 in day 4 at move 0
*When No. 492 infected, Exposure is 3.0 in day 4 at move 0
*When No. 542 infected, Exposure is 5.0 in day 4 at move 0
*When No. 554 infected, Exposure is 4.0 in day 4 at move 0
*When No. 596 infected, Exposure is 3.0 in day 4 at move 0
*When No. 706 infected, Exposure is 3.0 in day 4 at move 0
*When No. 788 infected, Exposure is 3.0 in day 4 at move 0
*When No. 791 infected, Exposure is 4.0 in day 4 at move 0
No. 10 exposure increased to 4.0 in day 4 at 1
No. 13 exposure increased to 1.0 in day 4 at 1
No. 55 exposure increased to 3.0 in day 4 at 1
No. 98 exposure increased to 3.0 in day 4 at 1
No. 101 exposure increased to 4.0 in day 4 at 1
*When No. 110 infected, Exposure is 5.0 in day 4 at move 1
No. 117 exposure increased to 4.0 in day 4 at 1
*When No. 154 infected, Exposure is 4.0 in day 4 at move 1
No. 157 exposure increased to 4.0 in day 4 at 1
No. 163 exposure increased to 3.0 in day 4 at 1
No. 169 exposure increased to 2.0 in day 4 at 1
No. 197 exposure increased to 2.0 in day 4 at 1
No. 202 exposure increased to 4.0 in day 4 at 1
No. 210 exposure increased to 2.0 in day 4 at 1
No. 258 exposure increased to 4.0 in day 4 at 1
No. 272 exposure increased to 2.0 in day 4 at 1
No. 280 exposure increased to 4.0 in day 4 at 1
*When No. 301 infected, Exposure is 4.0 in day 4 at move 1
No. 331 exposure increased to 5.0 in day 4 at 1
*When No. 338 infected, Exposure is 4.0 in day 4 at move 1
No. 343 exposure increased to 4.0 in day 4 at 1
*When No. 352 infected, Exposure is 4.0 in day 4 at move 1
No. 366 exposure increased to 1.0 in day 4 at 1
No. 404 exposure increased to 3.0 in day 4 at 1
No. 420 exposure increased to 4.0 in day 4 at 1
*When No. 445 infected, Exposure is 3.0 in day 4 at move 1
*When No. 453 infected, Exposure is 4.0 in day 4 at move 1
No. 508 exposure increased to 2.0 in day 4 at 1
No. 513 exposure increased to 4.0 in day 4 at 1
No. 558 exposure increased to 4.0 in day 4 at 1
No. 610 exposure increased to 5.0 in day 4 at 1
No. 629 exposure increased to 3.0 in day 4 at 1
No. 640 exposure increased to 3.0 in day 4 at 1
No. 651 exposure increased to 3.0 in day 4 at 1
No. 658 exposure increased to 2.0 in day 4 at 1
No. 668 exposure increased to 1.0 in day 4 at 1
*When No. 677 infected, Exposure is 2.0 in day 4 at move 1
No. 715 exposure increased to 2.0 in day 4 at 1
*When No. 734 infected, Exposure is 4.0 in day 4 at move 1
No. 744 exposure increased to 5.0 in day 4 at 1
No. 749 exposure increased to 4.0 in day 4 at 1
No. 762 exposure increased to 4.0 in day 4 at 1
No. 774 exposure increased to 2.0 in day 4 at 1
No. 820 exposure increased to 5.0 in day 4 at 1
No. 832 exposure increased to 2.0 in day 4 at 1
No. 834 exposure increased to 1.0 in day 4 at 1
No. 855 exposure increased to 5.0 in day 4 at 1
No. 872 exposure increased to 4.0 in day 4 at 1
No. 888 exposure increased to 3.0 in day 4 at 1
No. 895 exposure increased to 1.0 in day 4 at 1
No. 927 exposure increased to 1.0 in day 4 at 1
*When No. 934 infected, Exposure is 4.0 in day 4 at move 1
No. 936 exposure increased to 4.0 in day 4 at 1
*When No. 944 infected, Exposure is 4.0 in day 4 at move 1
No. 988 exposure increased to 1.0 in day 4 at 1
  121/10000 [..............................] - ETA: 15:50:14 - reward: 721.9404*When No. 10 infected, Exposure is 4.0 in day 4 at move 0
*When No. 163 infected, Exposure is 3.0 in day 4 at move 0
*When No. 258 infected, Exposure is 4.0 in day 4 at move 0
*When No. 331 infected, Exposure is 5.0 in day 4 at move 0
*When No. 343 infected, Exposure is 4.0 in day 4 at move 0
*When No. 420 infected, Exposure is 4.0 in day 4 at move 0
*When No. 774 infected, Exposure is 2.0 in day 4 at move 0
*When No. 855 infected, Exposure is 5.0 in day 4 at move 0
*When No. 101 infected, Exposure is 4.0 in day 4 at move 1
*When No. 157 infected, Exposure is 4.0 in day 4 at move 1
*When No. 513 infected, Exposure is 4.0 in day 4 at move 1
*When No. 610 infected, Exposure is 5.0 in day 4 at move 1
*When No. 744 infected, Exposure is 5.0 in day 4 at move 1
*When No. 820 infected, Exposure is 5.0 in day 4 at move 1
*When No. 872 infected, Exposure is 4.0 in day 4 at move 1
*When No. 117 infected, Exposure is 4.0 in day 4 at move 2
*When No. 169 infected, Exposure is 2.0 in day 4 at move 2
*When No. 280 infected, Exposure is 4.0 in day 4 at move 2
*When No. 651 infected, Exposure is 3.0 in day 4 at move 2
*When No. 762 infected, Exposure is 4.0 in day 4 at move 2
*When No. 55 infected, Exposure is 3.0 in day 4 at move 3
*When No. 629 infected, Exposure is 3.0 in day 4 at move 3
*When No. 936 infected, Exposure is 4.0 in day 4 at move 3
*When No. 404 infected, Exposure is 3.0 in day 4 at move 4
*When No. 558 infected, Exposure is 4.0 in day 4 at move 4
No. 11 exposure increased to 1.0 in day 4 at 5
No. 13 exposure increased to 2.0 in day 4 at 5
No. 31 exposure increased to 2.0 in day 4 at 5
No. 77 exposure increased to 2.0 in day 4 at 5
*When No. 98 infected, Exposure is 3.0 in day 4 at move 5
No. 105 exposure increased to 1.0 in day 4 at 5
No. 132 exposure increased to 2.0 in day 4 at 5
No. 179 exposure increased to 1.0 in day 4 at 5
No. 197 exposure increased to 3.0 in day 4 at 5
No. 201 exposure increased to 1.0 in day 4 at 5
No. 202 exposure increased to 5.0 in day 4 at 5
No. 210 exposure increased to 3.0 in day 4 at 5
No. 226 exposure increased to 1.0 in day 4 at 5
No. 231 exposure increased to 1.0 in day 4 at 5
No. 265 exposure increased to 1.0 in day 4 at 5
No. 272 exposure increased to 3.0 in day 4 at 5
No. 299 exposure increased to 1.0 in day 4 at 5
No. 312 exposure increased to 1.0 in day 4 at 5
No. 314 exposure increased to 1.0 in day 4 at 5
No. 316 exposure increased to 1.0 in day 4 at 5
No. 366 exposure increased to 2.0 in day 4 at 5
No. 388 exposure increased to 2.0 in day 4 at 5
No. 406 exposure increased to 1.0 in day 4 at 5
No. 428 exposure increased to 1.0 in day 4 at 5
No. 463 exposure increased to 1.0 in day 4 at 5
No. 464 exposure increased to 2.0 in day 4 at 5
No. 470 exposure increased to 1.0 in day 4 at 5
No. 481 exposure increased to 1.0 in day 4 at 5
No. 508 exposure increased to 3.0 in day 4 at 5
No. 515 exposure increased to 1.0 in day 4 at 5
No. 541 exposure increased to 1.0 in day 4 at 5
No. 551 exposure increased to 1.0 in day 4 at 5
No. 565 exposure increased to 1.0 in day 4 at 5
No. 570 exposure increased to 2.0 in day 4 at 5
No. 573 exposure increased to 2.0 in day 4 at 5
No. 581 exposure increased to 1.0 in day 4 at 5
No. 584 exposure increased to 1.0 in day 4 at 5
No. 604 exposure increased to 1.0 in day 4 at 5
No. 640 exposure increased to 4.0 in day 4 at 5
No. 658 exposure increased to 3.0 in day 4 at 5
No. 668 exposure increased to 2.0 in day 4 at 5
No. 715 exposure increased to 3.0 in day 4 at 5
No. 720 exposure increased to 1.0 in day 4 at 5
No. 721 exposure increased to 1.0 in day 4 at 5
No. 727 exposure increased to 1.0 in day 4 at 5
No. 736 exposure increased to 1.0 in day 4 at 5
*When No. 749 infected, Exposure is 4.0 in day 4 at move 5
No. 763 exposure increased to 1.0 in day 4 at 5
No. 792 exposure increased to 1.0 in day 4 at 5
No. 807 exposure increased to 1.0 in day 4 at 5
No. 819 exposure increased to 1.0 in day 4 at 5
No. 821 exposure increased to 1.0 in day 4 at 5
No. 826 exposure increased to 1.0 in day 4 at 5
No. 832 exposure increased to 3.0 in day 4 at 5
No. 834 exposure increased to 2.0 in day 4 at 5
No. 847 exposure increased to 1.0 in day 4 at 5
No. 873 exposure increased to 1.0 in day 4 at 5
No. 880 exposure increased to 1.0 in day 4 at 5
No. 885 exposure increased to 2.0 in day 4 at 5
*When No. 888 infected, Exposure is 3.0 in day 4 at move 5
No. 895 exposure increased to 2.0 in day 4 at 5
No. 901 exposure increased to 1.0 in day 4 at 5
No. 923 exposure increased to 1.0 in day 4 at 5
No. 927 exposure increased to 2.0 in day 4 at 5
No. 968 exposure increased to 1.0 in day 4 at 5
No. 969 exposure increased to 1.0 in day 4 at 5
No. 988 exposure increased to 2.0 in day 4 at 5
  122/10000 [..............................] - ETA: 16:06:25 - reward: 721.3926*When No. 272 infected, Exposure is 3.0 in day 4 at move 0
*When No. 640 infected, Exposure is 4.0 in day 4 at move 0
*When No. 668 infected, Exposure is 2.0 in day 4 at move 0
*When No. 464 infected, Exposure is 2.0 in day 4 at move 1
*When No. 202 infected, Exposure is 5.0 in day 4 at move 2
*When No. 832 infected, Exposure is 3.0 in day 4 at move 2
*When No. 31 infected, Exposure is 2.0 in day 4 at move 3
*When No. 77 infected, Exposure is 2.0 in day 4 at move 3
*When No. 132 infected, Exposure is 2.0 in day 4 at move 3
*When No. 197 infected, Exposure is 3.0 in day 4 at move 3
*When No. 715 infected, Exposure is 3.0 in day 4 at move 3
*When No. 366 infected, Exposure is 2.0 in day 4 at move 4
*When No. 658 infected, Exposure is 3.0 in day 4 at move 4
*When No. 885 infected, Exposure is 2.0 in day 4 at move 4
No. 11 exposure increased to 2.0 in day 4 at 5
No. 13 exposure increased to 3.0 in day 4 at 5
No. 54 exposure increased to 1.0 in day 4 at 5
No. 62 exposure increased to 1.0 in day 4 at 5
No. 68 exposure increased to 1.0 in day 4 at 5
No. 69 exposure increased to 1.0 in day 4 at 5
No. 92 exposure increased to 2.0 in day 4 at 5
No. 105 exposure increased to 2.0 in day 4 at 5
No. 107 exposure increased to 2.0 in day 4 at 5
No. 120 exposure increased to 1.0 in day 4 at 5
No. 166 exposure increased to 1.0 in day 4 at 5
No. 175 exposure increased to 1.0 in day 4 at 5
No. 179 exposure increased to 2.0 in day 4 at 5
No. 183 exposure increased to 1.0 in day 4 at 5
No. 201 exposure increased to 2.0 in day 4 at 5
No. 210 exposure increased to 4.0 in day 4 at 5
No. 220 exposure increased to 1.0 in day 4 at 5
No. 226 exposure increased to 2.0 in day 4 at 5
No. 228 exposure increased to 2.0 in day 4 at 5
No. 231 exposure increased to 2.0 in day 4 at 5
No. 265 exposure increased to 2.0 in day 4 at 5
No. 299 exposure increased to 2.0 in day 4 at 5
No. 306 exposure increased to 2.0 in day 4 at 5
No. 312 exposure increased to 2.0 in day 4 at 5
No. 314 exposure increased to 2.0 in day 4 at 5
No. 316 exposure increased to 2.0 in day 4 at 5
No. 317 exposure increased to 1.0 in day 4 at 5
No. 355 exposure increased to 1.0 in day 4 at 5
No. 388 exposure increased to 3.0 in day 4 at 5
No. 394 exposure increased to 1.0 in day 4 at 5
No. 406 exposure increased to 2.0 in day 4 at 5
No. 419 exposure increased to 1.0 in day 4 at 5
No. 426 exposure increased to 1.0 in day 4 at 5
No. 428 exposure increased to 2.0 in day 4 at 5
No. 439 exposure increased to 1.0 in day 4 at 5
No. 449 exposure increased to 2.0 in day 4 at 5
No. 463 exposure increased to 2.0 in day 4 at 5
No. 466 exposure increased to 1.0 in day 4 at 5
No. 470 exposure increased to 2.0 in day 4 at 5
No. 477 exposure increased to 2.0 in day 4 at 5
No. 481 exposure increased to 2.0 in day 4 at 5
No. 508 exposure increased to 4.0 in day 4 at 5
No. 515 exposure increased to 2.0 in day 4 at 5
No. 541 exposure increased to 2.0 in day 4 at 5
No. 551 exposure increased to 2.0 in day 4 at 5
No. 562 exposure increased to 1.0 in day 4 at 5
No. 565 exposure increased to 2.0 in day 4 at 5
No. 570 exposure increased to 3.0 in day 4 at 5
No. 573 exposure increased to 3.0 in day 4 at 5
No. 581 exposure increased to 2.0 in day 4 at 5
No. 584 exposure increased to 2.0 in day 4 at 5
No. 591 exposure increased to 1.0 in day 4 at 5
No. 604 exposure increased to 2.0 in day 4 at 5
No. 672 exposure increased to 1.0 in day 4 at 5
No. 679 exposure increased to 1.0 in day 4 at 5
No. 695 exposure increased to 2.0 in day 4 at 5
No. 704 exposure increased to 1.0 in day 4 at 5
No. 720 exposure increased to 2.0 in day 4 at 5
No. 721 exposure increased to 2.0 in day 4 at 5
No. 727 exposure increased to 2.0 in day 4 at 5
No. 732 exposure increased to 1.0 in day 4 at 5
No. 736 exposure increased to 2.0 in day 4 at 5
No. 741 exposure increased to 1.0 in day 4 at 5
No. 763 exposure increased to 2.0 in day 4 at 5
No. 784 exposure increased to 1.0 in day 4 at 5
No. 792 exposure increased to 2.0 in day 4 at 5
No. 793 exposure increased to 1.0 in day 4 at 5
No. 794 exposure increased to 1.0 in day 4 at 5
No. 797 exposure increased to 1.0 in day 4 at 5
No. 807 exposure increased to 2.0 in day 4 at 5
No. 819 exposure increased to 2.0 in day 4 at 5
No. 821 exposure increased to 2.0 in day 4 at 5
No. 824 exposure increased to 2.0 in day 4 at 5
No. 826 exposure increased to 2.0 in day 4 at 5
*When No. 834 infected, Exposure is 2.0 in day 4 at move 5
No. 838 exposure increased to 1.0 in day 4 at 5
No. 847 exposure increased to 2.0 in day 4 at 5
No. 854 exposure increased to 1.0 in day 4 at 5
No. 861 exposure increased to 1.0 in day 4 at 5
No. 873 exposure increased to 2.0 in day 4 at 5
No. 876 exposure increased to 1.0 in day 4 at 5
No. 880 exposure increased to 2.0 in day 4 at 5
No. 895 exposure increased to 3.0 in day 4 at 5
No. 901 exposure increased to 2.0 in day 4 at 5
No. 923 exposure increased to 2.0 in day 4 at 5
No. 927 exposure increased to 3.0 in day 4 at 5
No. 968 exposure increased to 2.0 in day 4 at 5
No. 969 exposure increased to 2.0 in day 4 at 5
No. 981 exposure increased to 1.0 in day 4 at 5
*When No. 988 infected, Exposure is 2.0 in day 4 at move 5
No. 994 exposure increased to 1.0 in day 4 at 5
  123/10000 [..............................] - ETA: 16:19:53 - reward: 720.4410*When No. 92 infected, Exposure is 2.0 in day 4 at move 0
*When No. 449 infected, Exposure is 2.0 in day 4 at move 0
*When No. 463 infected, Exposure is 2.0 in day 4 at move 0
*When No. 515 infected, Exposure is 2.0 in day 4 at move 0
*When No. 573 infected, Exposure is 3.0 in day 4 at move 0
*When No. 581 infected, Exposure is 2.0 in day 4 at move 0
*When No. 792 infected, Exposure is 2.0 in day 4 at move 0
*When No. 847 infected, Exposure is 2.0 in day 4 at move 0
*When No. 179 infected, Exposure is 2.0 in day 4 at move 1
*When No. 210 infected, Exposure is 4.0 in day 4 at move 1
*When No. 551 infected, Exposure is 2.0 in day 4 at move 1
*When No. 880 infected, Exposure is 2.0 in day 4 at move 1
*When No. 565 infected, Exposure is 2.0 in day 4 at move 2
*When No. 604 infected, Exposure is 2.0 in day 4 at move 2
*When No. 901 infected, Exposure is 2.0 in day 4 at move 2
*When No. 720 infected, Exposure is 2.0 in day 4 at move 3
*When No. 826 infected, Exposure is 2.0 in day 4 at move 3
*When No. 306 infected, Exposure is 2.0 in day 4 at move 4
*When No. 312 infected, Exposure is 2.0 in day 4 at move 4
*When No. 819 infected, Exposure is 2.0 in day 4 at move 4
No. 11 exposure increased to 3.0 in day 4 at 5
No. 13 exposure increased to 4.0 in day 4 at 5
No. 37 exposure increased to 1.0 in day 4 at 5
No. 41 exposure increased to 1.0 in day 4 at 5
No. 54 exposure increased to 2.0 in day 4 at 5
No. 62 exposure increased to 2.0 in day 4 at 5
No. 67 exposure increased to 1.0 in day 4 at 5
No. 68 exposure increased to 2.0 in day 4 at 5
No. 69 exposure increased to 2.0 in day 4 at 5
No. 94 exposure increased to 1.0 in day 4 at 5
*When No. 105 infected, Exposure is 2.0 in day 4 at move 5
No. 107 exposure increased to 3.0 in day 4 at 5
No. 120 exposure increased to 2.0 in day 4 at 5
No. 145 exposure increased to 2.0 in day 4 at 5
No. 156 exposure increased to 1.0 in day 4 at 5
No. 166 exposure increased to 2.0 in day 4 at 5
No. 175 exposure increased to 2.0 in day 4 at 5
No. 183 exposure increased to 2.0 in day 4 at 5
No. 201 exposure increased to 3.0 in day 4 at 5
No. 220 exposure increased to 2.0 in day 4 at 5
No. 221 exposure increased to 1.0 in day 4 at 5
No. 226 exposure increased to 3.0 in day 4 at 5
No. 228 exposure increased to 3.0 in day 4 at 5
No. 231 exposure increased to 3.0 in day 4 at 5
No. 255 exposure increased to 1.0 in day 4 at 5
No. 265 exposure increased to 3.0 in day 4 at 5
No. 279 exposure increased to 2.0 in day 4 at 5
No. 299 exposure increased to 3.0 in day 4 at 5
No. 314 exposure increased to 3.0 in day 4 at 5
No. 316 exposure increased to 3.0 in day 4 at 5
No. 317 exposure increased to 2.0 in day 4 at 5
No. 355 exposure increased to 2.0 in day 4 at 5
No. 374 exposure increased to 1.0 in day 4 at 5
No. 388 exposure increased to 4.0 in day 4 at 5
No. 394 exposure increased to 2.0 in day 4 at 5
*When No. 406 infected, Exposure is 2.0 in day 4 at move 5
No. 419 exposure increased to 2.0 in day 4 at 5
No. 426 exposure increased to 2.0 in day 4 at 5
No. 428 exposure increased to 3.0 in day 4 at 5
No. 439 exposure increased to 2.0 in day 4 at 5
No. 459 exposure increased to 1.0 in day 4 at 5
No. 466 exposure increased to 2.0 in day 4 at 5
No. 470 exposure increased to 3.0 in day 4 at 5
No. 477 exposure increased to 3.0 in day 4 at 5
No. 481 exposure increased to 3.0 in day 4 at 5
No. 506 exposure increased to 1.0 in day 4 at 5
No. 507 exposure increased to 1.0 in day 4 at 5
No. 508 exposure increased to 5.0 in day 4 at 5
*When No. 541 infected, Exposure is 2.0 in day 4 at move 5
No. 562 exposure increased to 2.0 in day 4 at 5
No. 570 exposure increased to 4.0 in day 4 at 5
No. 580 exposure increased to 2.0 in day 4 at 5
No. 584 exposure increased to 3.0 in day 4 at 5
No. 591 exposure increased to 2.0 in day 4 at 5
No. 600 exposure increased to 1.0 in day 4 at 5
No. 622 exposure increased to 1.0 in day 4 at 5
No. 672 exposure increased to 2.0 in day 4 at 5
No. 679 exposure increased to 2.0 in day 4 at 5
No. 695 exposure increased to 3.0 in day 4 at 5
No. 704 exposure increased to 2.0 in day 4 at 5
No. 721 exposure increased to 3.0 in day 4 at 5
No. 723 exposure increased to 2.0 in day 4 at 5
No. 727 exposure increased to 3.0 in day 4 at 5
No. 732 exposure increased to 2.0 in day 4 at 5
*When No. 736 infected, Exposure is 2.0 in day 4 at move 5
No. 741 exposure increased to 2.0 in day 4 at 5
No. 763 exposure increased to 3.0 in day 4 at 5
No. 768 exposure increased to 1.0 in day 4 at 5
No. 773 exposure increased to 1.0 in day 4 at 5
No. 782 exposure increased to 2.0 in day 4 at 5
No. 784 exposure increased to 2.0 in day 4 at 5
No. 785 exposure increased to 1.0 in day 4 at 5
No. 793 exposure increased to 2.0 in day 4 at 5
No. 794 exposure increased to 2.0 in day 4 at 5
No. 797 exposure increased to 2.0 in day 4 at 5
No. 807 exposure increased to 3.0 in day 4 at 5
No. 821 exposure increased to 3.0 in day 4 at 5
No. 824 exposure increased to 3.0 in day 4 at 5
No. 838 exposure increased to 2.0 in day 4 at 5
No. 850 exposure increased to 1.0 in day 4 at 5
No. 854 exposure increased to 2.0 in day 4 at 5
No. 856 exposure increased to 2.0 in day 4 at 5
No. 861 exposure increased to 2.0 in day 4 at 5
No. 873 exposure increased to 3.0 in day 4 at 5
No. 875 exposure increased to 1.0 in day 4 at 5
No. 876 exposure increased to 2.0 in day 4 at 5
No. 895 exposure increased to 4.0 in day 4 at 5
No. 923 exposure increased to 3.0 in day 4 at 5
No. 927 exposure increased to 4.0 in day 4 at 5
No. 937 exposure increased to 2.0 in day 4 at 5
No. 942 exposure increased to 1.0 in day 4 at 5
No. 963 exposure increased to 1.0 in day 4 at 5
No. 968 exposure increased to 3.0 in day 4 at 5
No. 969 exposure increased to 3.0 in day 4 at 5
No. 981 exposure increased to 2.0 in day 4 at 5
No. 994 exposure increased to 2.0 in day 4 at 5
  124/10000 [..............................] - ETA: 16:32:47 - reward: 719.7485*When No. 13 infected, Exposure is 4.0 in day 4 at move 0
*When No. 68 infected, Exposure is 2.0 in day 4 at move 0
*When No. 166 infected, Exposure is 2.0 in day 4 at move 0
*When No. 299 infected, Exposure is 3.0 in day 4 at move 0
*When No. 314 infected, Exposure is 3.0 in day 4 at move 0
*When No. 470 infected, Exposure is 3.0 in day 4 at move 0
*When No. 477 infected, Exposure is 3.0 in day 4 at move 0
*When No. 570 infected, Exposure is 4.0 in day 4 at move 0
*When No. 821 infected, Exposure is 3.0 in day 4 at move 0
*When No. 824 infected, Exposure is 3.0 in day 4 at move 0
*When No. 981 infected, Exposure is 2.0 in day 4 at move 0
*When No. 11 infected, Exposure is 3.0 in day 4 at move 1
*When No. 107 infected, Exposure is 3.0 in day 4 at move 1
*When No. 228 infected, Exposure is 3.0 in day 4 at move 1
*When No. 388 infected, Exposure is 4.0 in day 4 at move 1
*When No. 481 infected, Exposure is 3.0 in day 4 at move 1
*When No. 508 infected, Exposure is 5.0 in day 4 at move 1
*When No. 580 infected, Exposure is 2.0 in day 4 at move 1
*When No. 672 infected, Exposure is 2.0 in day 4 at move 1
*When No. 679 infected, Exposure is 2.0 in day 4 at move 1
*When No. 721 infected, Exposure is 3.0 in day 4 at move 1
*When No. 732 infected, Exposure is 2.0 in day 4 at move 1
*When No. 317 infected, Exposure is 2.0 in day 4 at move 2
*When No. 419 infected, Exposure is 2.0 in day 4 at move 2
*When No. 439 infected, Exposure is 2.0 in day 4 at move 2
*When No. 591 infected, Exposure is 2.0 in day 4 at move 2
*When No. 763 infected, Exposure is 3.0 in day 4 at move 2
*When No. 838 infected, Exposure is 2.0 in day 4 at move 2
*When No. 62 infected, Exposure is 2.0 in day 4 at move 3
*When No. 226 infected, Exposure is 3.0 in day 4 at move 3
*When No. 279 infected, Exposure is 2.0 in day 4 at move 3
*When No. 355 infected, Exposure is 2.0 in day 4 at move 3
*When No. 695 infected, Exposure is 3.0 in day 4 at move 3
*When No. 794 infected, Exposure is 2.0 in day 4 at move 3
*When No. 923 infected, Exposure is 3.0 in day 4 at move 3
*When No. 231 infected, Exposure is 3.0 in day 4 at move 4
*When No. 584 infected, Exposure is 3.0 in day 4 at move 4
*When No. 727 infected, Exposure is 3.0 in day 4 at move 4
No. 4 exposure increased to 2.0 in day 4 at 5
No. 5 exposure increased to 1.0 in day 4 at 5
No. 37 exposure increased to 2.0 in day 4 at 5
No. 41 exposure increased to 2.0 in day 4 at 5
No. 54 exposure increased to 3.0 in day 4 at 5
No. 67 exposure increased to 2.0 in day 4 at 5
No. 69 exposure increased to 3.0 in day 4 at 5
No. 71 exposure increased to 1.0 in day 4 at 5
No. 83 exposure increased to 2.0 in day 4 at 5
No. 87 exposure increased to 1.0 in day 4 at 5
No. 94 exposure increased to 2.0 in day 4 at 5
No. 104 exposure increased to 2.0 in day 4 at 5
No. 120 exposure increased to 3.0 in day 4 at 5
No. 145 exposure increased to 3.0 in day 4 at 5
No. 148 exposure increased to 1.0 in day 4 at 5
No. 156 exposure increased to 2.0 in day 4 at 5
No. 175 exposure increased to 3.0 in day 4 at 5
No. 180 exposure increased to 1.0 in day 4 at 5
No. 183 exposure increased to 3.0 in day 4 at 5
No. 196 exposure increased to 1.0 in day 4 at 5
No. 201 exposure increased to 4.0 in day 4 at 5
No. 214 exposure increased to 1.0 in day 4 at 5
No. 220 exposure increased to 3.0 in day 4 at 5
No. 221 exposure increased to 2.0 in day 4 at 5
No. 244 exposure increased to 2.0 in day 4 at 5
No. 255 exposure increased to 2.0 in day 4 at 5
No. 265 exposure increased to 4.0 in day 4 at 5
No. 269 exposure increased to 2.0 in day 4 at 5
No. 289 exposure increased to 2.0 in day 4 at 5
No. 309 exposure increased to 2.0 in day 4 at 5
No. 316 exposure increased to 4.0 in day 4 at 5
No. 339 exposure increased to 1.0 in day 4 at 5
No. 374 exposure increased to 2.0 in day 4 at 5
No. 382 exposure increased to 1.0 in day 4 at 5
No. 394 exposure increased to 3.0 in day 4 at 5
No. 426 exposure increased to 3.0 in day 4 at 5
No. 428 exposure increased to 4.0 in day 4 at 5
No. 459 exposure increased to 2.0 in day 4 at 5
No. 466 exposure increased to 3.0 in day 4 at 5
No. 503 exposure increased to 1.0 in day 4 at 5
No. 506 exposure increased to 2.0 in day 4 at 5
No. 507 exposure increased to 2.0 in day 4 at 5
No. 522 exposure increased to 1.0 in day 4 at 5
No. 527 exposure increased to 1.0 in day 4 at 5
No. 562 exposure increased to 3.0 in day 4 at 5
No. 600 exposure increased to 2.0 in day 4 at 5
No. 622 exposure increased to 2.0 in day 4 at 5
No. 657 exposure increased to 2.0 in day 4 at 5
No. 660 exposure increased to 2.0 in day 4 at 5
No. 661 exposure increased to 1.0 in day 4 at 5
No. 666 exposure increased to 1.0 in day 4 at 5
No. 700 exposure increased to 1.0 in day 4 at 5
No. 704 exposure increased to 3.0 in day 4 at 5
No. 723 exposure increased to 3.0 in day 4 at 5
No. 730 exposure increased to 1.0 in day 4 at 5
No. 739 exposure increased to 1.0 in day 4 at 5
No. 741 exposure increased to 3.0 in day 4 at 5
No. 745 exposure increased to 1.0 in day 4 at 5
No. 747 exposure increased to 1.0 in day 4 at 5
No. 765 exposure increased to 1.0 in day 4 at 5
No. 768 exposure increased to 2.0 in day 4 at 5
No. 773 exposure increased to 2.0 in day 4 at 5
No. 782 exposure increased to 3.0 in day 4 at 5
No. 784 exposure increased to 3.0 in day 4 at 5
No. 785 exposure increased to 2.0 in day 4 at 5
No. 793 exposure increased to 3.0 in day 4 at 5
No. 797 exposure increased to 3.0 in day 4 at 5
No. 805 exposure increased to 1.0 in day 4 at 5
No. 807 exposure increased to 4.0 in day 4 at 5
No. 809 exposure increased to 1.0 in day 4 at 5
No. 848 exposure increased to 1.0 in day 4 at 5
No. 850 exposure increased to 2.0 in day 4 at 5
No. 854 exposure increased to 3.0 in day 4 at 5
No. 856 exposure increased to 3.0 in day 4 at 5
No. 861 exposure increased to 3.0 in day 4 at 5
*When No. 873 infected, Exposure is 3.0 in day 4 at move 5
No. 875 exposure increased to 2.0 in day 4 at 5
*When No. 876 infected, Exposure is 2.0 in day 4 at move 5
No. 877 exposure increased to 1.0 in day 4 at 5
No. 892 exposure increased to 2.0 in day 4 at 5
No. 895 exposure increased to 5.0 in day 4 at 5
No. 924 exposure increased to 2.0 in day 4 at 5
*When No. 927 infected, Exposure is 4.0 in day 4 at move 5
No. 937 exposure increased to 3.0 in day 4 at 5
No. 942 exposure increased to 2.0 in day 4 at 5
No. 963 exposure increased to 2.0 in day 4 at 5
No. 968 exposure increased to 4.0 in day 4 at 5
No. 969 exposure increased to 4.0 in day 4 at 5
No. 971 exposure increased to 1.0 in day 4 at 5
No. 994 exposure increased to 3.0 in day 4 at 5
  125/10000 [..............................] - ETA: 16:45:31 - reward: 719.3365*When No. 4 infected, Exposure is 2.0 in day 4 at move 0
*When No. 37 infected, Exposure is 2.0 in day 4 at move 0
*When No. 221 infected, Exposure is 2.0 in day 4 at move 0
*When No. 265 infected, Exposure is 4.0 in day 4 at move 0
*When No. 428 infected, Exposure is 4.0 in day 4 at move 0
*When No. 459 infected, Exposure is 2.0 in day 4 at move 0
*When No. 562 infected, Exposure is 3.0 in day 4 at move 0
*When No. 784 infected, Exposure is 3.0 in day 4 at move 0
*When No. 807 infected, Exposure is 4.0 in day 4 at move 0
*When No. 856 infected, Exposure is 3.0 in day 4 at move 0
*When No. 924 infected, Exposure is 2.0 in day 4 at move 0
*When No. 968 infected, Exposure is 4.0 in day 4 at move 0
No. 5 exposure increased to 2.0 in day 4 at 1
No. 41 exposure increased to 3.0 in day 4 at 1
No. 54 exposure increased to 4.0 in day 4 at 1
No. 67 exposure increased to 3.0 in day 4 at 1
*When No. 69 infected, Exposure is 3.0 in day 4 at move 1
No. 71 exposure increased to 2.0 in day 4 at 1
No. 83 exposure increased to 3.0 in day 4 at 1
No. 87 exposure increased to 2.0 in day 4 at 1
No. 94 exposure increased to 3.0 in day 4 at 1
No. 104 exposure increased to 3.0 in day 4 at 1
No. 120 exposure increased to 4.0 in day 4 at 1
No. 124 exposure increased to 1.0 in day 4 at 1
No. 145 exposure increased to 4.0 in day 4 at 1
No. 148 exposure increased to 2.0 in day 4 at 1
No. 155 exposure increased to 1.0 in day 4 at 1
No. 156 exposure increased to 3.0 in day 4 at 1
No. 164 exposure increased to 2.0 in day 4 at 1
No. 175 exposure increased to 4.0 in day 4 at 1
No. 180 exposure increased to 2.0 in day 4 at 1
No. 183 exposure increased to 4.0 in day 4 at 1
No. 192 exposure increased to 2.0 in day 4 at 1
No. 196 exposure increased to 2.0 in day 4 at 1
No. 201 exposure increased to 5.0 in day 4 at 1
No. 214 exposure increased to 2.0 in day 4 at 1
No. 220 exposure increased to 4.0 in day 4 at 1
No. 244 exposure increased to 3.0 in day 4 at 1
No. 255 exposure increased to 3.0 in day 4 at 1
No. 269 exposure increased to 3.0 in day 4 at 1
No. 289 exposure increased to 3.0 in day 4 at 1
No. 309 exposure increased to 3.0 in day 4 at 1
No. 316 exposure increased to 5.0 in day 4 at 1
No. 339 exposure increased to 2.0 in day 4 at 1
No. 374 exposure increased to 3.0 in day 4 at 1
No. 382 exposure increased to 2.0 in day 4 at 1
No. 394 exposure increased to 4.0 in day 4 at 1
No. 414 exposure increased to 2.0 in day 4 at 1
*When No. 426 infected, Exposure is 3.0 in day 4 at move 1
No. 466 exposure increased to 4.0 in day 4 at 1
No. 503 exposure increased to 2.0 in day 4 at 1
No. 506 exposure increased to 3.0 in day 4 at 1
No. 507 exposure increased to 3.0 in day 4 at 1
No. 522 exposure increased to 2.0 in day 4 at 1
No. 527 exposure increased to 2.0 in day 4 at 1
No. 579 exposure increased to 1.0 in day 4 at 1
No. 600 exposure increased to 3.0 in day 4 at 1
No. 622 exposure increased to 3.0 in day 4 at 1
No. 657 exposure increased to 3.0 in day 4 at 1
No. 660 exposure increased to 3.0 in day 4 at 1
No. 661 exposure increased to 2.0 in day 4 at 1
No. 662 exposure increased to 1.0 in day 4 at 1
No. 666 exposure increased to 2.0 in day 4 at 1
No. 681 exposure increased to 1.0 in day 4 at 1
No. 700 exposure increased to 2.0 in day 4 at 1
No. 704 exposure increased to 4.0 in day 4 at 1
*When No. 723 infected, Exposure is 3.0 in day 4 at move 1
No. 730 exposure increased to 2.0 in day 4 at 1
No. 739 exposure increased to 2.0 in day 4 at 1
*When No. 741 infected, Exposure is 3.0 in day 4 at move 1
No. 745 exposure increased to 2.0 in day 4 at 1
No. 747 exposure increased to 2.0 in day 4 at 1
No. 765 exposure increased to 2.0 in day 4 at 1
No. 768 exposure increased to 3.0 in day 4 at 1
*When No. 773 infected, Exposure is 2.0 in day 4 at move 1
No. 782 exposure increased to 4.0 in day 4 at 1
No. 785 exposure increased to 3.0 in day 4 at 1
No. 793 exposure increased to 4.0 in day 4 at 1
No. 797 exposure increased to 4.0 in day 4 at 1
No. 805 exposure increased to 2.0 in day 4 at 1
No. 809 exposure increased to 2.0 in day 4 at 1
No. 848 exposure increased to 2.0 in day 4 at 1
No. 850 exposure increased to 3.0 in day 4 at 1
No. 854 exposure increased to 4.0 in day 4 at 1
No. 861 exposure increased to 4.0 in day 4 at 1
No. 865 exposure increased to 2.0 in day 4 at 1
No. 868 exposure increased to 2.0 in day 4 at 1
*When No. 875 infected, Exposure is 2.0 in day 4 at move 1
No. 877 exposure increased to 2.0 in day 4 at 1
No. 892 exposure increased to 3.0 in day 4 at 1
No. 895 exposure increased to 6.0 in day 4 at 1
No. 918 exposure increased to 1.0 in day 4 at 1
No. 937 exposure increased to 4.0 in day 4 at 1
No. 942 exposure increased to 3.0 in day 4 at 1
*When No. 963 infected, Exposure is 2.0 in day 4 at move 1
*When No. 969 infected, Exposure is 4.0 in day 4 at move 1
No. 971 exposure increased to 2.0 in day 4 at 1
*When No. 994 infected, Exposure is 3.0 in day 4 at move 1
  126/10000 [..............................] - ETA: 16:44:16 - reward: 718.3275*When No. 145 infected, Exposure is 4.0 in day 4 at move 0
*When No. 183 infected, Exposure is 4.0 in day 4 at move 0
*When No. 220 infected, Exposure is 4.0 in day 4 at move 0
*When No. 255 infected, Exposure is 3.0 in day 4 at move 0
*When No. 374 infected, Exposure is 3.0 in day 4 at move 0
*When No. 622 infected, Exposure is 3.0 in day 4 at move 0
*When No. 704 infected, Exposure is 4.0 in day 4 at move 0
*When No. 782 infected, Exposure is 4.0 in day 4 at move 0
*When No. 793 infected, Exposure is 4.0 in day 4 at move 0
*When No. 971 infected, Exposure is 2.0 in day 4 at move 0
*When No. 41 infected, Exposure is 3.0 in day 4 at move 1
*When No. 120 infected, Exposure is 4.0 in day 4 at move 1
*When No. 164 infected, Exposure is 2.0 in day 4 at move 1
*When No. 309 infected, Exposure is 3.0 in day 4 at move 1
*When No. 414 infected, Exposure is 2.0 in day 4 at move 1
*When No. 506 infected, Exposure is 3.0 in day 4 at move 1
*When No. 937 infected, Exposure is 4.0 in day 4 at move 1
*When No. 83 infected, Exposure is 3.0 in day 4 at move 2
*When No. 104 infected, Exposure is 3.0 in day 4 at move 2
*When No. 660 infected, Exposure is 3.0 in day 4 at move 2
*When No. 861 infected, Exposure is 4.0 in day 4 at move 2
*When No. 868 infected, Exposure is 2.0 in day 4 at move 2
*When No. 156 infected, Exposure is 3.0 in day 4 at move 3
*When No. 214 infected, Exposure is 2.0 in day 4 at move 3
*When No. 522 infected, Exposure is 2.0 in day 4 at move 3
*When No. 739 infected, Exposure is 2.0 in day 4 at move 3
*When No. 747 infected, Exposure is 2.0 in day 4 at move 3
*When No. 805 infected, Exposure is 2.0 in day 4 at move 3
*When No. 809 infected, Exposure is 2.0 in day 4 at move 3
*When No. 854 infected, Exposure is 4.0 in day 4 at move 3
*When No. 175 infected, Exposure is 4.0 in day 4 at move 4
*When No. 316 infected, Exposure is 5.0 in day 4 at move 4
*When No. 850 infected, Exposure is 3.0 in day 4 at move 4
*When No. 892 infected, Exposure is 3.0 in day 4 at move 4
*When No. 942 infected, Exposure is 3.0 in day 4 at move 4
No. 5 exposure increased to 3.0 in day 4 at 5
No. 47 exposure increased to 1.0 in day 4 at 5
No. 48 exposure increased to 1.0 in day 4 at 5
No. 53 exposure increased to 1.0 in day 4 at 5
No. 54 exposure increased to 5.0 in day 4 at 5
No. 67 exposure increased to 4.0 in day 4 at 5
No. 71 exposure increased to 3.0 in day 4 at 5
No. 87 exposure increased to 3.0 in day 4 at 5
No. 94 exposure increased to 4.0 in day 4 at 5
No. 122 exposure increased to 1.0 in day 4 at 5
No. 124 exposure increased to 2.0 in day 4 at 5
No. 148 exposure increased to 3.0 in day 4 at 5
No. 150 exposure increased to 2.0 in day 4 at 5
No. 155 exposure increased to 2.0 in day 4 at 5
No. 180 exposure increased to 3.0 in day 4 at 5
No. 182 exposure increased to 1.0 in day 4 at 5
No. 192 exposure increased to 3.0 in day 4 at 5
No. 196 exposure increased to 3.0 in day 4 at 5
No. 201 exposure increased to 6.0 in day 4 at 5
No. 206 exposure increased to 1.0 in day 4 at 5
No. 217 exposure increased to 1.0 in day 4 at 5
No. 222 exposure increased to 2.0 in day 4 at 5
No. 244 exposure increased to 4.0 in day 4 at 5
No. 252 exposure increased to 1.0 in day 4 at 5
No. 269 exposure increased to 4.0 in day 4 at 5
*When No. 289 infected, Exposure is 3.0 in day 4 at move 5
No. 294 exposure increased to 1.0 in day 4 at 5
No. 337 exposure increased to 1.0 in day 4 at 5
No. 339 exposure increased to 3.0 in day 4 at 5
No. 349 exposure increased to 1.0 in day 4 at 5
No. 382 exposure increased to 3.0 in day 4 at 5
No. 394 exposure increased to 5.0 in day 4 at 5
No. 434 exposure increased to 1.0 in day 4 at 5
No. 466 exposure increased to 5.0 in day 4 at 5
No. 474 exposure increased to 1.0 in day 4 at 5
No. 478 exposure increased to 2.0 in day 4 at 5
No. 503 exposure increased to 3.0 in day 4 at 5
No. 507 exposure increased to 4.0 in day 4 at 5
No. 520 exposure increased to 1.0 in day 4 at 5
No. 527 exposure increased to 3.0 in day 4 at 5
No. 579 exposure increased to 2.0 in day 4 at 5
No. 593 exposure increased to 1.0 in day 4 at 5
No. 600 exposure increased to 4.0 in day 4 at 5
No. 626 exposure increased to 1.0 in day 4 at 5
No. 637 exposure increased to 1.0 in day 4 at 5
No. 657 exposure increased to 4.0 in day 4 at 5
No. 661 exposure increased to 3.0 in day 4 at 5
No. 662 exposure increased to 2.0 in day 4 at 5
No. 666 exposure increased to 3.0 in day 4 at 5
No. 681 exposure increased to 2.0 in day 4 at 5
No. 700 exposure increased to 3.0 in day 4 at 5
No. 730 exposure increased to 3.0 in day 4 at 5
No. 737 exposure increased to 1.0 in day 4 at 5
No. 742 exposure increased to 2.0 in day 4 at 5
No. 745 exposure increased to 3.0 in day 4 at 5
*When No. 765 infected, Exposure is 2.0 in day 4 at move 5
No. 768 exposure increased to 4.0 in day 4 at 5
No. 785 exposure increased to 4.0 in day 4 at 5
*When No. 797 infected, Exposure is 4.0 in day 4 at move 5
No. 800 exposure increased to 1.0 in day 4 at 5
No. 802 exposure increased to 1.0 in day 4 at 5
No. 848 exposure increased to 3.0 in day 4 at 5
No. 865 exposure increased to 3.0 in day 4 at 5
No. 877 exposure increased to 3.0 in day 4 at 5
No. 895 exposure increased to 7.0 in day 4 at 5
No. 898 exposure increased to 1.0 in day 4 at 5
No. 918 exposure increased to 2.0 in day 4 at 5
No. 991 exposure increased to 1.0 in day 4 at 5
No. 998 exposure increased to 1.0 in day 4 at 5
  127/10000 [..............................] - ETA: 16:55:42 - reward: 716.8611*When No. 54 infected, Exposure is 5.0 in day 4 at move 0
*When No. 67 infected, Exposure is 4.0 in day 4 at move 0
*When No. 87 infected, Exposure is 3.0 in day 4 at move 0
*When No. 466 infected, Exposure is 5.0 in day 4 at move 0
*When No. 657 infected, Exposure is 4.0 in day 4 at move 0
*When No. 681 infected, Exposure is 2.0 in day 4 at move 0
*When No. 865 infected, Exposure is 3.0 in day 4 at move 0
*When No. 895 infected, Exposure is 7.0 in day 4 at move 0
*When No. 5 infected, Exposure is 3.0 in day 4 at move 1
No. 32 exposure increased to 1.0 in day 4 at 1
No. 47 exposure increased to 2.0 in day 4 at 1
No. 48 exposure increased to 2.0 in day 4 at 1
No. 53 exposure increased to 2.0 in day 4 at 1
No. 71 exposure increased to 4.0 in day 4 at 1
No. 94 exposure increased to 5.0 in day 4 at 1
No. 122 exposure increased to 2.0 in day 4 at 1
No. 124 exposure increased to 3.0 in day 4 at 1
No. 140 exposure increased to 2.0 in day 4 at 1
No. 144 exposure increased to 1.0 in day 4 at 1
No. 148 exposure increased to 4.0 in day 4 at 1
No. 150 exposure increased to 3.0 in day 4 at 1
No. 155 exposure increased to 3.0 in day 4 at 1
No. 180 exposure increased to 4.0 in day 4 at 1
No. 182 exposure increased to 2.0 in day 4 at 1
No. 192 exposure increased to 4.0 in day 4 at 1
No. 196 exposure increased to 4.0 in day 4 at 1
No. 201 exposure increased to 7.0 in day 4 at 1
No. 206 exposure increased to 2.0 in day 4 at 1
No. 217 exposure increased to 2.0 in day 4 at 1
No. 222 exposure increased to 3.0 in day 4 at 1
*When No. 244 infected, Exposure is 4.0 in day 4 at move 1
No. 252 exposure increased to 2.0 in day 4 at 1
No. 269 exposure increased to 5.0 in day 4 at 1
No. 294 exposure increased to 2.0 in day 4 at 1
No. 337 exposure increased to 2.0 in day 4 at 1
No. 339 exposure increased to 4.0 in day 4 at 1
No. 349 exposure increased to 2.0 in day 4 at 1
No. 382 exposure increased to 4.0 in day 4 at 1
No. 394 exposure increased to 6.0 in day 4 at 1
No. 421 exposure increased to 2.0 in day 4 at 1
No. 434 exposure increased to 2.0 in day 4 at 1
No. 451 exposure increased to 2.0 in day 4 at 1
No. 472 exposure increased to 2.0 in day 4 at 1
No. 474 exposure increased to 2.0 in day 4 at 1
No. 478 exposure increased to 3.0 in day 4 at 1
No. 493 exposure increased to 1.0 in day 4 at 1
No. 503 exposure increased to 4.0 in day 4 at 1
*When No. 507 infected, Exposure is 4.0 in day 4 at move 1
No. 520 exposure increased to 2.0 in day 4 at 1
*When No. 527 infected, Exposure is 3.0 in day 4 at move 1
No. 559 exposure increased to 1.0 in day 4 at 1
No. 579 exposure increased to 3.0 in day 4 at 1
No. 593 exposure increased to 2.0 in day 4 at 1
No. 600 exposure increased to 5.0 in day 4 at 1
No. 621 exposure increased to 1.0 in day 4 at 1
No. 626 exposure increased to 2.0 in day 4 at 1
No. 634 exposure increased to 1.0 in day 4 at 1
No. 637 exposure increased to 2.0 in day 4 at 1
No. 661 exposure increased to 4.0 in day 4 at 1
No. 662 exposure increased to 3.0 in day 4 at 1
No. 666 exposure increased to 4.0 in day 4 at 1
No. 700 exposure increased to 4.0 in day 4 at 1
No. 730 exposure increased to 4.0 in day 4 at 1
No. 737 exposure increased to 2.0 in day 4 at 1
No. 742 exposure increased to 3.0 in day 4 at 1
*When No. 745 infected, Exposure is 3.0 in day 4 at move 1
No. 750 exposure increased to 1.0 in day 4 at 1
No. 768 exposure increased to 5.0 in day 4 at 1
No. 785 exposure increased to 5.0 in day 4 at 1
No. 800 exposure increased to 2.0 in day 4 at 1
No. 802 exposure increased to 2.0 in day 4 at 1
No. 823 exposure increased to 1.0 in day 4 at 1
No. 848 exposure increased to 4.0 in day 4 at 1
No. 877 exposure increased to 4.0 in day 4 at 1
No. 898 exposure increased to 2.0 in day 4 at 1
*When No. 918 infected, Exposure is 2.0 in day 4 at move 1
No. 991 exposure increased to 2.0 in day 4 at 1
No. 998 exposure increased to 2.0 in day 4 at 1
  128/10000 [..............................] - ETA: 16:54:11 - reward: 715.8656*When No. 94 infected, Exposure is 5.0 in day 4 at move 0
*When No. 124 infected, Exposure is 3.0 in day 4 at move 0
*When No. 192 infected, Exposure is 4.0 in day 4 at move 0
*When No. 201 infected, Exposure is 7.0 in day 4 at move 0
*When No. 269 infected, Exposure is 5.0 in day 4 at move 0
*When No. 382 infected, Exposure is 4.0 in day 4 at move 0
*When No. 503 infected, Exposure is 4.0 in day 4 at move 0
*When No. 579 infected, Exposure is 3.0 in day 4 at move 0
*When No. 742 infected, Exposure is 3.0 in day 4 at move 0
*When No. 991 infected, Exposure is 2.0 in day 4 at move 0
No. 32 exposure increased to 2.0 in day 4 at 1
No. 47 exposure increased to 3.0 in day 4 at 1
No. 48 exposure increased to 3.0 in day 4 at 1
No. 53 exposure increased to 3.0 in day 4 at 1
No. 71 exposure increased to 5.0 in day 4 at 1
*When No. 122 infected, Exposure is 2.0 in day 4 at move 1
No. 140 exposure increased to 3.0 in day 4 at 1
No. 144 exposure increased to 2.0 in day 4 at 1
No. 148 exposure increased to 5.0 in day 4 at 1
No. 150 exposure increased to 4.0 in day 4 at 1
*When No. 155 infected, Exposure is 3.0 in day 4 at move 1
No. 180 exposure increased to 5.0 in day 4 at 1
No. 182 exposure increased to 3.0 in day 4 at 1
*When No. 196 infected, Exposure is 4.0 in day 4 at move 1
No. 206 exposure increased to 3.0 in day 4 at 1
No. 217 exposure increased to 3.0 in day 4 at 1
No. 222 exposure increased to 4.0 in day 4 at 1
No. 252 exposure increased to 3.0 in day 4 at 1
No. 294 exposure increased to 3.0 in day 4 at 1
No. 296 exposure increased to 1.0 in day 4 at 1
No. 334 exposure increased to 2.0 in day 4 at 1
No. 337 exposure increased to 3.0 in day 4 at 1
No. 339 exposure increased to 5.0 in day 4 at 1
No. 349 exposure increased to 3.0 in day 4 at 1
*When No. 394 infected, Exposure is 6.0 in day 4 at move 1
No. 421 exposure increased to 3.0 in day 4 at 1
No. 434 exposure increased to 3.0 in day 4 at 1
No. 451 exposure increased to 3.0 in day 4 at 1
No. 472 exposure increased to 3.0 in day 4 at 1
No. 474 exposure increased to 3.0 in day 4 at 1
No. 478 exposure increased to 4.0 in day 4 at 1
No. 493 exposure increased to 2.0 in day 4 at 1
No. 520 exposure increased to 3.0 in day 4 at 1
No. 555 exposure increased to 1.0 in day 4 at 1
No. 559 exposure increased to 2.0 in day 4 at 1
No. 593 exposure increased to 3.0 in day 4 at 1
*When No. 600 infected, Exposure is 5.0 in day 4 at move 1
No. 621 exposure increased to 2.0 in day 4 at 1
No. 626 exposure increased to 3.0 in day 4 at 1
No. 634 exposure increased to 2.0 in day 4 at 1
No. 637 exposure increased to 3.0 in day 4 at 1
*When No. 661 infected, Exposure is 4.0 in day 4 at move 1
No. 662 exposure increased to 4.0 in day 4 at 1
No. 666 exposure increased to 5.0 in day 4 at 1
No. 700 exposure increased to 5.0 in day 4 at 1
No. 730 exposure increased to 5.0 in day 4 at 1
No. 737 exposure increased to 3.0 in day 4 at 1
No. 750 exposure increased to 2.0 in day 4 at 1
No. 768 exposure increased to 6.0 in day 4 at 1
No. 785 exposure increased to 6.0 in day 4 at 1
No. 790 exposure increased to 1.0 in day 4 at 1
No. 800 exposure increased to 3.0 in day 4 at 1
*When No. 802 infected, Exposure is 2.0 in day 4 at move 1
No. 814 exposure increased to 2.0 in day 4 at 1
No. 823 exposure increased to 2.0 in day 4 at 1
No. 848 exposure increased to 5.0 in day 4 at 1
*When No. 877 infected, Exposure is 4.0 in day 4 at move 1
*When No. 898 infected, Exposure is 2.0 in day 4 at move 1
No. 911 exposure increased to 1.0 in day 4 at 1
No. 998 exposure increased to 3.0 in day 4 at 1
  129/10000 [..............................] - ETA: 16:52:45 - reward: 714.4744*When No. 150 infected, Exposure is 4.0 in day 4 at move 0
*When No. 180 infected, Exposure is 5.0 in day 4 at move 0
*When No. 206 infected, Exposure is 3.0 in day 4 at move 0
*When No. 294 infected, Exposure is 3.0 in day 4 at move 0
*When No. 339 infected, Exposure is 5.0 in day 4 at move 0
*When No. 785 infected, Exposure is 6.0 in day 4 at move 0
*When No. 848 infected, Exposure is 5.0 in day 4 at move 0
No. 32 exposure increased to 3.0 in day 4 at 1
No. 47 exposure increased to 4.0 in day 4 at 1
No. 48 exposure increased to 4.0 in day 4 at 1
No. 53 exposure increased to 4.0 in day 4 at 1
No. 71 exposure increased to 6.0 in day 4 at 1
No. 96 exposure increased to 1.0 in day 4 at 1
No. 140 exposure increased to 4.0 in day 4 at 1
No. 144 exposure increased to 3.0 in day 4 at 1
No. 148 exposure increased to 6.0 in day 4 at 1
No. 182 exposure increased to 4.0 in day 4 at 1
*When No. 217 infected, Exposure is 3.0 in day 4 at move 1
No. 222 exposure increased to 5.0 in day 4 at 1
No. 249 exposure increased to 2.0 in day 4 at 1
*When No. 252 infected, Exposure is 3.0 in day 4 at move 1
No. 296 exposure increased to 2.0 in day 4 at 1
No. 334 exposure increased to 3.0 in day 4 at 1
No. 337 exposure increased to 4.0 in day 4 at 1
*When No. 349 infected, Exposure is 3.0 in day 4 at move 1
No. 421 exposure increased to 4.0 in day 4 at 1
No. 434 exposure increased to 4.0 in day 4 at 1
No. 451 exposure increased to 4.0 in day 4 at 1
No. 469 exposure increased to 2.0 in day 4 at 1
No. 472 exposure increased to 4.0 in day 4 at 1
No. 474 exposure increased to 4.0 in day 4 at 1
No. 478 exposure increased to 5.0 in day 4 at 1
No. 493 exposure increased to 3.0 in day 4 at 1
No. 520 exposure increased to 4.0 in day 4 at 1
No. 555 exposure increased to 2.0 in day 4 at 1
No. 559 exposure increased to 3.0 in day 4 at 1
No. 593 exposure increased to 4.0 in day 4 at 1
No. 621 exposure increased to 3.0 in day 4 at 1
No. 626 exposure increased to 4.0 in day 4 at 1
No. 634 exposure increased to 3.0 in day 4 at 1
No. 637 exposure increased to 4.0 in day 4 at 1
No. 639 exposure increased to 1.0 in day 4 at 1
No. 650 exposure increased to 1.0 in day 4 at 1
No. 662 exposure increased to 5.0 in day 4 at 1
No. 666 exposure increased to 6.0 in day 4 at 1
No. 667 exposure increased to 1.0 in day 4 at 1
No. 700 exposure increased to 6.0 in day 4 at 1
No. 714 exposure increased to 2.0 in day 4 at 1
*When No. 730 infected, Exposure is 5.0 in day 4 at move 1
No. 737 exposure increased to 4.0 in day 4 at 1
*When No. 750 infected, Exposure is 2.0 in day 4 at move 1
*When No. 768 infected, Exposure is 6.0 in day 4 at move 1
No. 790 exposure increased to 2.0 in day 4 at 1
No. 800 exposure increased to 4.0 in day 4 at 1
*When No. 814 infected, Exposure is 2.0 in day 4 at move 1
No. 823 exposure increased to 3.0 in day 4 at 1
No. 887 exposure increased to 1.0 in day 4 at 1
No. 911 exposure increased to 2.0 in day 4 at 1
No. 998 exposure increased to 4.0 in day 4 at 1
  130/10000 [..............................] - ETA: 16:50:50 - reward: 713.4411*When No. 32 infected, Exposure is 3.0 in day 4 at move 0
*When No. 48 infected, Exposure is 4.0 in day 4 at move 0
*When No. 421 infected, Exposure is 4.0 in day 4 at move 0
*When No. 451 infected, Exposure is 4.0 in day 4 at move 0
*When No. 593 infected, Exposure is 4.0 in day 4 at move 0
*When No. 626 infected, Exposure is 4.0 in day 4 at move 0
*When No. 662 infected, Exposure is 5.0 in day 4 at move 0
*When No. 790 infected, Exposure is 2.0 in day 4 at move 0
*When No. 911 infected, Exposure is 2.0 in day 4 at move 0
*When No. 434 infected, Exposure is 4.0 in day 4 at move 1
*When No. 493 infected, Exposure is 3.0 in day 4 at move 1
*When No. 520 infected, Exposure is 4.0 in day 4 at move 1
*When No. 634 infected, Exposure is 3.0 in day 4 at move 1
*When No. 637 infected, Exposure is 4.0 in day 4 at move 1
*When No. 998 infected, Exposure is 4.0 in day 4 at move 1
*When No. 71 infected, Exposure is 6.0 in day 4 at move 2
*When No. 478 infected, Exposure is 5.0 in day 4 at move 2
*When No. 737 infected, Exposure is 4.0 in day 4 at move 2
*When No. 148 infected, Exposure is 6.0 in day 4 at move 3
*When No. 182 infected, Exposure is 4.0 in day 4 at move 3
*When No. 337 infected, Exposure is 4.0 in day 4 at move 3
*When No. 472 infected, Exposure is 4.0 in day 4 at move 3
*When No. 474 infected, Exposure is 4.0 in day 4 at move 3
*When No. 621 infected, Exposure is 3.0 in day 4 at move 3
*When No. 666 infected, Exposure is 6.0 in day 4 at move 3
*When No. 700 infected, Exposure is 6.0 in day 4 at move 3
*When No. 800 infected, Exposure is 4.0 in day 4 at move 3
*When No. 53 infected, Exposure is 4.0 in day 4 at move 4
*When No. 140 infected, Exposure is 4.0 in day 4 at move 4
*When No. 555 infected, Exposure is 2.0 in day 4 at move 4
*When No. 559 infected, Exposure is 3.0 in day 4 at move 4
No. 33 exposure increased to 1.0 in day 4 at 5
No. 47 exposure increased to 5.0 in day 4 at 5
No. 96 exposure increased to 2.0 in day 4 at 5
No. 144 exposure increased to 4.0 in day 4 at 5
No. 216 exposure increased to 1.0 in day 4 at 5
*When No. 222 infected, Exposure is 5.0 in day 4 at move 5
No. 249 exposure increased to 3.0 in day 4 at 5
No. 277 exposure increased to 2.0 in day 4 at 5
No. 281 exposure increased to 1.0 in day 4 at 5
No. 282 exposure increased to 1.0 in day 4 at 5
No. 296 exposure increased to 3.0 in day 4 at 5
No. 318 exposure increased to 1.0 in day 4 at 5
No. 334 exposure increased to 4.0 in day 4 at 5
No. 360 exposure increased to 2.0 in day 4 at 5
No. 371 exposure increased to 1.0 in day 4 at 5
No. 469 exposure increased to 3.0 in day 4 at 5
No. 516 exposure increased to 1.0 in day 4 at 5
No. 548 exposure increased to 1.0 in day 4 at 5
No. 560 exposure increased to 1.0 in day 4 at 5
No. 639 exposure increased to 2.0 in day 4 at 5
No. 650 exposure increased to 2.0 in day 4 at 5
No. 667 exposure increased to 2.0 in day 4 at 5
No. 714 exposure increased to 3.0 in day 4 at 5
No. 746 exposure increased to 1.0 in day 4 at 5
No. 780 exposure increased to 1.0 in day 4 at 5
No. 812 exposure increased to 1.0 in day 4 at 5
No. 818 exposure increased to 1.0 in day 4 at 5
No. 823 exposure increased to 4.0 in day 4 at 5
No. 841 exposure increased to 1.0 in day 4 at 5
No. 860 exposure increased to 1.0 in day 4 at 5
No. 887 exposure increased to 2.0 in day 4 at 5
No. 948 exposure increased to 1.0 in day 4 at 5
No. 973 exposure increased to 1.0 in day 4 at 5
  131/10000 [..............................] - ETA: 17:01:32 - reward: 711.9198*When No. 47 infected, Exposure is 5.0 in day 4 at move 1
*When No. 296 infected, Exposure is 3.0 in day 4 at move 1
*When No. 334 infected, Exposure is 4.0 in day 4 at move 1
*When No. 887 infected, Exposure is 2.0 in day 4 at move 1
*When No. 249 infected, Exposure is 3.0 in day 4 at move 2
No. 33 exposure increased to 2.0 in day 4 at 5
No. 39 exposure increased to 1.0 in day 4 at 5
No. 56 exposure increased to 1.0 in day 4 at 5
No. 96 exposure increased to 3.0 in day 4 at 5
*When No. 144 infected, Exposure is 4.0 in day 4 at move 5
No. 216 exposure increased to 2.0 in day 4 at 5
No. 277 exposure increased to 3.0 in day 4 at 5
No. 281 exposure increased to 2.0 in day 4 at 5
No. 282 exposure increased to 2.0 in day 4 at 5
No. 318 exposure increased to 2.0 in day 4 at 5
No. 356 exposure increased to 1.0 in day 4 at 5
No. 360 exposure increased to 3.0 in day 4 at 5
No. 362 exposure increased to 1.0 in day 4 at 5
No. 363 exposure increased to 2.0 in day 4 at 5
No. 365 exposure increased to 2.0 in day 4 at 5
No. 371 exposure increased to 2.0 in day 4 at 5
No. 376 exposure increased to 1.0 in day 4 at 5
No. 397 exposure increased to 1.0 in day 4 at 5
No. 429 exposure increased to 2.0 in day 4 at 5
No. 438 exposure increased to 1.0 in day 4 at 5
No. 458 exposure increased to 1.0 in day 4 at 5
No. 469 exposure increased to 4.0 in day 4 at 5
No. 471 exposure increased to 1.0 in day 4 at 5
No. 487 exposure increased to 1.0 in day 4 at 5
No. 494 exposure increased to 1.0 in day 4 at 5
No. 502 exposure increased to 2.0 in day 4 at 5
No. 509 exposure increased to 1.0 in day 4 at 5
No. 516 exposure increased to 2.0 in day 4 at 5
No. 548 exposure increased to 2.0 in day 4 at 5
No. 560 exposure increased to 2.0 in day 4 at 5
No. 586 exposure increased to 1.0 in day 4 at 5
No. 588 exposure increased to 2.0 in day 4 at 5
No. 624 exposure increased to 1.0 in day 4 at 5
No. 627 exposure increased to 1.0 in day 4 at 5
No. 639 exposure increased to 3.0 in day 4 at 5
No. 650 exposure increased to 3.0 in day 4 at 5
No. 655 exposure increased to 2.0 in day 4 at 5
No. 664 exposure increased to 1.0 in day 4 at 5
No. 667 exposure increased to 3.0 in day 4 at 5
No. 680 exposure increased to 1.0 in day 4 at 5
No. 714 exposure increased to 4.0 in day 4 at 5
No. 735 exposure increased to 1.0 in day 4 at 5
No. 746 exposure increased to 2.0 in day 4 at 5
No. 760 exposure increased to 1.0 in day 4 at 5
No. 767 exposure increased to 2.0 in day 4 at 5
No. 780 exposure increased to 2.0 in day 4 at 5
No. 812 exposure increased to 2.0 in day 4 at 5
No. 815 exposure increased to 2.0 in day 4 at 5
No. 818 exposure increased to 2.0 in day 4 at 5
No. 823 exposure increased to 5.0 in day 4 at 5
No. 825 exposure increased to 1.0 in day 4 at 5
No. 841 exposure increased to 2.0 in day 4 at 5
No. 849 exposure increased to 1.0 in day 4 at 5
No. 860 exposure increased to 2.0 in day 4 at 5
No. 864 exposure increased to 1.0 in day 4 at 5
No. 905 exposure increased to 1.0 in day 4 at 5
No. 915 exposure increased to 1.0 in day 4 at 5
No. 928 exposure increased to 1.0 in day 4 at 5
No. 948 exposure increased to 2.0 in day 4 at 5
No. 973 exposure increased to 2.0 in day 4 at 5
No. 982 exposure increased to 1.0 in day 4 at 5
No. 993 exposure increased to 1.0 in day 4 at 5
  132/10000 [..............................] - ETA: 17:10:15 - reward: 710.6496*When No. 363 infected, Exposure is 2.0 in day 4 at move 0
*When No. 516 infected, Exposure is 2.0 in day 4 at move 0
*When No. 639 infected, Exposure is 3.0 in day 4 at move 0
*When No. 281 infected, Exposure is 2.0 in day 4 at move 1
*When No. 469 infected, Exposure is 4.0 in day 4 at move 1
*When No. 502 infected, Exposure is 2.0 in day 4 at move 1
*When No. 650 infected, Exposure is 3.0 in day 4 at move 1
*When No. 823 infected, Exposure is 5.0 in day 4 at move 1
*When No. 841 infected, Exposure is 2.0 in day 4 at move 1
*When No. 360 infected, Exposure is 3.0 in day 4 at move 2
*When No. 560 infected, Exposure is 2.0 in day 4 at move 2
*When No. 33 infected, Exposure is 2.0 in day 4 at move 3
*When No. 365 infected, Exposure is 2.0 in day 4 at move 3
*When No. 548 infected, Exposure is 2.0 in day 4 at move 4
*When No. 973 infected, Exposure is 2.0 in day 4 at move 4
No. 39 exposure increased to 2.0 in day 4 at 5
No. 56 exposure increased to 2.0 in day 4 at 5
No. 96 exposure increased to 4.0 in day 4 at 5
No. 139 exposure increased to 1.0 in day 4 at 5
No. 146 exposure increased to 1.0 in day 4 at 5
No. 167 exposure increased to 1.0 in day 4 at 5
No. 188 exposure increased to 1.0 in day 4 at 5
*When No. 216 infected, Exposure is 2.0 in day 4 at move 5
No. 257 exposure increased to 1.0 in day 4 at 5
No. 264 exposure increased to 1.0 in day 4 at 5
No. 277 exposure increased to 4.0 in day 4 at 5
No. 282 exposure increased to 3.0 in day 4 at 5
No. 305 exposure increased to 1.0 in day 4 at 5
No. 318 exposure increased to 3.0 in day 4 at 5
No. 356 exposure increased to 2.0 in day 4 at 5
No. 362 exposure increased to 2.0 in day 4 at 5
No. 371 exposure increased to 3.0 in day 4 at 5
No. 376 exposure increased to 2.0 in day 4 at 5
No. 397 exposure increased to 2.0 in day 4 at 5
No. 398 exposure increased to 1.0 in day 4 at 5
No. 423 exposure increased to 1.0 in day 4 at 5
No. 429 exposure increased to 3.0 in day 4 at 5
No. 438 exposure increased to 2.0 in day 4 at 5
No. 440 exposure increased to 1.0 in day 4 at 5
No. 441 exposure increased to 1.0 in day 4 at 5
No. 458 exposure increased to 2.0 in day 4 at 5
No. 471 exposure increased to 2.0 in day 4 at 5
No. 487 exposure increased to 2.0 in day 4 at 5
No. 489 exposure increased to 2.0 in day 4 at 5
No. 494 exposure increased to 2.0 in day 4 at 5
No. 509 exposure increased to 2.0 in day 4 at 5
No. 512 exposure increased to 1.0 in day 4 at 5
No. 531 exposure increased to 1.0 in day 4 at 5
No. 563 exposure increased to 2.0 in day 4 at 5
No. 586 exposure increased to 2.0 in day 4 at 5
No. 588 exposure increased to 3.0 in day 4 at 5
No. 624 exposure increased to 2.0 in day 4 at 5
No. 627 exposure increased to 2.0 in day 4 at 5
No. 630 exposure increased to 1.0 in day 4 at 5
No. 647 exposure increased to 1.0 in day 4 at 5
No. 655 exposure increased to 3.0 in day 4 at 5
No. 664 exposure increased to 2.0 in day 4 at 5
*When No. 667 infected, Exposure is 3.0 in day 4 at move 5
No. 680 exposure increased to 2.0 in day 4 at 5
*When No. 714 infected, Exposure is 4.0 in day 4 at move 5
No. 716 exposure increased to 1.0 in day 4 at 5
No. 735 exposure increased to 2.0 in day 4 at 5
No. 740 exposure increased to 1.0 in day 4 at 5
No. 746 exposure increased to 3.0 in day 4 at 5
No. 748 exposure increased to 2.0 in day 4 at 5
No. 760 exposure increased to 2.0 in day 4 at 5
No. 767 exposure increased to 3.0 in day 4 at 5
No. 769 exposure increased to 2.0 in day 4 at 5
No. 770 exposure increased to 1.0 in day 4 at 5
No. 780 exposure increased to 3.0 in day 4 at 5
No. 812 exposure increased to 3.0 in day 4 at 5
No. 815 exposure increased to 3.0 in day 4 at 5
No. 817 exposure increased to 1.0 in day 4 at 5
No. 818 exposure increased to 3.0 in day 4 at 5
No. 825 exposure increased to 2.0 in day 4 at 5
No. 846 exposure increased to 1.0 in day 4 at 5
No. 849 exposure increased to 2.0 in day 4 at 5
No. 860 exposure increased to 3.0 in day 4 at 5
No. 863 exposure increased to 1.0 in day 4 at 5
No. 864 exposure increased to 2.0 in day 4 at 5
No. 869 exposure increased to 1.0 in day 4 at 5
No. 870 exposure increased to 1.0 in day 4 at 5
No. 894 exposure increased to 1.0 in day 4 at 5
No. 905 exposure increased to 2.0 in day 4 at 5
No. 915 exposure increased to 2.0 in day 4 at 5
No. 928 exposure increased to 2.0 in day 4 at 5
No. 948 exposure increased to 3.0 in day 4 at 5
No. 952 exposure increased to 1.0 in day 4 at 5
No. 954 exposure increased to 1.0 in day 4 at 5
No. 982 exposure increased to 2.0 in day 4 at 5
No. 985 exposure increased to 1.0 in day 4 at 5
No. 993 exposure increased to 2.0 in day 4 at 5
  133/10000 [..............................] - ETA: 17:17:29 - reward: 708.8874*When No. 96 infected, Exposure is 4.0 in day 4 at move 0
*When No. 277 infected, Exposure is 4.0 in day 4 at move 0
*When No. 489 infected, Exposure is 2.0 in day 4 at move 0
*When No. 494 infected, Exposure is 2.0 in day 4 at move 0
*When No. 905 infected, Exposure is 2.0 in day 4 at move 0
*When No. 56 infected, Exposure is 2.0 in day 4 at move 1
*When No. 371 infected, Exposure is 3.0 in day 4 at move 1
*When No. 376 infected, Exposure is 2.0 in day 4 at move 1
*When No. 471 infected, Exposure is 2.0 in day 4 at move 1
*When No. 487 infected, Exposure is 2.0 in day 4 at move 1
*When No. 655 infected, Exposure is 3.0 in day 4 at move 1
*When No. 769 infected, Exposure is 2.0 in day 4 at move 1
*When No. 928 infected, Exposure is 2.0 in day 4 at move 1
*When No. 588 infected, Exposure is 3.0 in day 4 at move 2
*When No. 812 infected, Exposure is 3.0 in day 4 at move 2
*When No. 915 infected, Exposure is 2.0 in day 4 at move 2
*When No. 948 infected, Exposure is 3.0 in day 4 at move 2
*When No. 746 infected, Exposure is 3.0 in day 4 at move 3
*When No. 760 infected, Exposure is 2.0 in day 4 at move 3
*When No. 815 infected, Exposure is 3.0 in day 4 at move 3
*When No. 39 infected, Exposure is 2.0 in day 4 at move 4
*When No. 318 infected, Exposure is 3.0 in day 4 at move 4
*When No. 780 infected, Exposure is 3.0 in day 4 at move 4
No. 42 exposure increased to 1.0 in day 4 at 5
No. 116 exposure increased to 1.0 in day 4 at 5
No. 139 exposure increased to 2.0 in day 4 at 5
No. 146 exposure increased to 2.0 in day 4 at 5
No. 167 exposure increased to 2.0 in day 4 at 5
No. 186 exposure increased to 1.0 in day 4 at 5
No. 188 exposure increased to 2.0 in day 4 at 5
No. 227 exposure increased to 1.0 in day 4 at 5
No. 242 exposure increased to 1.0 in day 4 at 5
No. 248 exposure increased to 1.0 in day 4 at 5
No. 254 exposure increased to 2.0 in day 4 at 5
No. 257 exposure increased to 2.0 in day 4 at 5
No. 264 exposure increased to 2.0 in day 4 at 5
No. 282 exposure increased to 4.0 in day 4 at 5
No. 305 exposure increased to 2.0 in day 4 at 5
No. 333 exposure increased to 1.0 in day 4 at 5
No. 356 exposure increased to 3.0 in day 4 at 5
*When No. 362 infected, Exposure is 2.0 in day 4 at move 5
No. 397 exposure increased to 3.0 in day 4 at 5
No. 398 exposure increased to 2.0 in day 4 at 5
No. 401 exposure increased to 1.0 in day 4 at 5
No. 423 exposure increased to 2.0 in day 4 at 5
No. 429 exposure increased to 4.0 in day 4 at 5
No. 438 exposure increased to 3.0 in day 4 at 5
No. 440 exposure increased to 2.0 in day 4 at 5
No. 441 exposure increased to 2.0 in day 4 at 5
No. 458 exposure increased to 3.0 in day 4 at 5
No. 505 exposure increased to 1.0 in day 4 at 5
No. 509 exposure increased to 3.0 in day 4 at 5
No. 512 exposure increased to 2.0 in day 4 at 5
No. 531 exposure increased to 2.0 in day 4 at 5
No. 563 exposure increased to 3.0 in day 4 at 5
No. 578 exposure increased to 1.0 in day 4 at 5
No. 586 exposure increased to 3.0 in day 4 at 5
No. 594 exposure increased to 1.0 in day 4 at 5
No. 595 exposure increased to 1.0 in day 4 at 5
No. 624 exposure increased to 3.0 in day 4 at 5
No. 627 exposure increased to 3.0 in day 4 at 5
No. 630 exposure increased to 2.0 in day 4 at 5
No. 644 exposure increased to 1.0 in day 4 at 5
No. 647 exposure increased to 2.0 in day 4 at 5
No. 652 exposure increased to 1.0 in day 4 at 5
No. 656 exposure increased to 1.0 in day 4 at 5
No. 664 exposure increased to 3.0 in day 4 at 5
No. 680 exposure increased to 3.0 in day 4 at 5
No. 716 exposure increased to 2.0 in day 4 at 5
No. 717 exposure increased to 1.0 in day 4 at 5
No. 735 exposure increased to 3.0 in day 4 at 5
No. 740 exposure increased to 2.0 in day 4 at 5
No. 748 exposure increased to 3.0 in day 4 at 5
No. 767 exposure increased to 4.0 in day 4 at 5
No. 770 exposure increased to 2.0 in day 4 at 5
No. 789 exposure increased to 1.0 in day 4 at 5
No. 796 exposure increased to 1.0 in day 4 at 5
No. 811 exposure increased to 1.0 in day 4 at 5
No. 817 exposure increased to 2.0 in day 4 at 5
No. 818 exposure increased to 4.0 in day 4 at 5
No. 825 exposure increased to 3.0 in day 4 at 5
No. 827 exposure increased to 1.0 in day 4 at 5
No. 846 exposure increased to 2.0 in day 4 at 5
No. 849 exposure increased to 3.0 in day 4 at 5
*When No. 860 infected, Exposure is 3.0 in day 4 at move 5
No. 863 exposure increased to 2.0 in day 4 at 5
No. 864 exposure increased to 3.0 in day 4 at 5
No. 869 exposure increased to 2.0 in day 4 at 5
No. 870 exposure increased to 2.0 in day 4 at 5
No. 894 exposure increased to 2.0 in day 4 at 5
No. 899 exposure increased to 1.0 in day 4 at 5
No. 902 exposure increased to 1.0 in day 4 at 5
No. 929 exposure increased to 2.0 in day 4 at 5
No. 950 exposure increased to 1.0 in day 4 at 5
No. 952 exposure increased to 2.0 in day 4 at 5
No. 954 exposure increased to 2.0 in day 4 at 5
No. 979 exposure increased to 2.0 in day 4 at 5
No. 982 exposure increased to 3.0 in day 4 at 5
No. 985 exposure increased to 2.0 in day 4 at 5
No. 993 exposure increased to 3.0 in day 4 at 5
  134/10000 [..............................] - ETA: 17:24:15 - reward: 707.4283*When No. 146 infected, Exposure is 2.0 in day 4 at move 0
*When No. 356 infected, Exposure is 3.0 in day 4 at move 0
*When No. 397 infected, Exposure is 3.0 in day 4 at move 0
*When No. 735 infected, Exposure is 3.0 in day 4 at move 0
*When No. 864 infected, Exposure is 3.0 in day 4 at move 0
*When No. 429 infected, Exposure is 4.0 in day 4 at move 1
*When No. 438 infected, Exposure is 3.0 in day 4 at move 1
*When No. 512 infected, Exposure is 2.0 in day 4 at move 1
*When No. 563 infected, Exposure is 3.0 in day 4 at move 1
*When No. 627 infected, Exposure is 3.0 in day 4 at move 1
*When No. 664 infected, Exposure is 3.0 in day 4 at move 1
*When No. 818 infected, Exposure is 4.0 in day 4 at move 1
*When No. 849 infected, Exposure is 3.0 in day 4 at move 1
*When No. 139 infected, Exposure is 2.0 in day 4 at move 2
*When No. 167 infected, Exposure is 2.0 in day 4 at move 2
*When No. 624 infected, Exposure is 3.0 in day 4 at move 2
*When No. 767 infected, Exposure is 4.0 in day 4 at move 2
*When No. 979 infected, Exposure is 2.0 in day 4 at move 2
*When No. 398 infected, Exposure is 2.0 in day 4 at move 3
*When No. 458 infected, Exposure is 3.0 in day 4 at move 3
*When No. 509 infected, Exposure is 3.0 in day 4 at move 3
*When No. 740 infected, Exposure is 2.0 in day 4 at move 3
*When No. 264 infected, Exposure is 2.0 in day 4 at move 4
*When No. 846 infected, Exposure is 2.0 in day 4 at move 4
*When No. 869 infected, Exposure is 2.0 in day 4 at move 4
*When No. 952 infected, Exposure is 2.0 in day 4 at move 4
No. 3 exposure increased to 1.0 in day 4 at 5
No. 42 exposure increased to 2.0 in day 4 at 5
No. 109 exposure increased to 1.0 in day 4 at 5
No. 116 exposure increased to 2.0 in day 4 at 5
No. 125 exposure increased to 1.0 in day 4 at 5
No. 174 exposure increased to 1.0 in day 4 at 5
No. 186 exposure increased to 2.0 in day 4 at 5
No. 188 exposure increased to 3.0 in day 4 at 5
No. 195 exposure increased to 1.0 in day 4 at 5
No. 199 exposure increased to 2.0 in day 4 at 5
No. 209 exposure increased to 2.0 in day 4 at 5
No. 227 exposure increased to 2.0 in day 4 at 5
No. 242 exposure increased to 2.0 in day 4 at 5
No. 248 exposure increased to 2.0 in day 4 at 5
No. 254 exposure increased to 3.0 in day 4 at 5
No. 257 exposure increased to 3.0 in day 4 at 5
*When No. 282 infected, Exposure is 4.0 in day 4 at move 5
No. 305 exposure increased to 3.0 in day 4 at 5
No. 323 exposure increased to 1.0 in day 4 at 5
No. 333 exposure increased to 2.0 in day 4 at 5
No. 367 exposure increased to 1.0 in day 4 at 5
No. 401 exposure increased to 2.0 in day 4 at 5
No. 413 exposure increased to 1.0 in day 4 at 5
*When No. 423 infected, Exposure is 2.0 in day 4 at move 5
No. 427 exposure increased to 2.0 in day 4 at 5
No. 437 exposure increased to 1.0 in day 4 at 5
No. 440 exposure increased to 3.0 in day 4 at 5
No. 441 exposure increased to 3.0 in day 4 at 5
No. 468 exposure increased to 1.0 in day 4 at 5
No. 505 exposure increased to 2.0 in day 4 at 5
No. 531 exposure increased to 3.0 in day 4 at 5
No. 578 exposure increased to 2.0 in day 4 at 5
No. 583 exposure increased to 1.0 in day 4 at 5
No. 586 exposure increased to 4.0 in day 4 at 5
No. 594 exposure increased to 2.0 in day 4 at 5
No. 595 exposure increased to 2.0 in day 4 at 5
No. 602 exposure increased to 1.0 in day 4 at 5
No. 630 exposure increased to 3.0 in day 4 at 5
No. 644 exposure increased to 2.0 in day 4 at 5
No. 646 exposure increased to 1.0 in day 4 at 5
No. 647 exposure increased to 3.0 in day 4 at 5
No. 652 exposure increased to 2.0 in day 4 at 5
No. 656 exposure increased to 2.0 in day 4 at 5
No. 671 exposure increased to 1.0 in day 4 at 5
No. 674 exposure increased to 2.0 in day 4 at 5
No. 680 exposure increased to 4.0 in day 4 at 5
No. 716 exposure increased to 3.0 in day 4 at 5
No. 717 exposure increased to 2.0 in day 4 at 5
No. 748 exposure increased to 4.0 in day 4 at 5
No. 770 exposure increased to 3.0 in day 4 at 5
No. 789 exposure increased to 2.0 in day 4 at 5
No. 796 exposure increased to 2.0 in day 4 at 5
No. 811 exposure increased to 2.0 in day 4 at 5
*When No. 817 infected, Exposure is 2.0 in day 4 at move 5
*When No. 825 infected, Exposure is 3.0 in day 4 at move 5
No. 827 exposure increased to 2.0 in day 4 at 5
No. 863 exposure increased to 3.0 in day 4 at 5
No. 870 exposure increased to 3.0 in day 4 at 5
No. 894 exposure increased to 3.0 in day 4 at 5
No. 899 exposure increased to 2.0 in day 4 at 5
No. 902 exposure increased to 2.0 in day 4 at 5
No. 907 exposure increased to 1.0 in day 4 at 5
No. 912 exposure increased to 2.0 in day 4 at 5
No. 929 exposure increased to 3.0 in day 4 at 5
No. 940 exposure increased to 1.0 in day 4 at 5
No. 950 exposure increased to 2.0 in day 4 at 5
No. 951 exposure increased to 1.0 in day 4 at 5
No. 954 exposure increased to 3.0 in day 4 at 5
No. 957 exposure increased to 2.0 in day 4 at 5
*When No. 982 infected, Exposure is 3.0 in day 4 at move 5
No. 985 exposure increased to 3.0 in day 4 at 5
No. 993 exposure increased to 4.0 in day 4 at 5
No. 996 exposure increased to 1.0 in day 4 at 5
  135/10000 [..............................] - ETA: 17:38:34 - reward: 705.8340*When No. 242 infected, Exposure is 2.0 in day 4 at move 0
*When No. 254 infected, Exposure is 3.0 in day 4 at move 0
*When No. 305 infected, Exposure is 3.0 in day 4 at move 0
*When No. 505 infected, Exposure is 2.0 in day 4 at move 0
*When No. 531 infected, Exposure is 3.0 in day 4 at move 0
*When No. 586 infected, Exposure is 4.0 in day 4 at move 0
*When No. 827 infected, Exposure is 2.0 in day 4 at move 0
*When No. 894 infected, Exposure is 3.0 in day 4 at move 0
*When No. 954 infected, Exposure is 3.0 in day 4 at move 0
No. 3 exposure increased to 2.0 in day 4 at 1
No. 42 exposure increased to 3.0 in day 4 at 1
No. 109 exposure increased to 2.0 in day 4 at 1
No. 116 exposure increased to 3.0 in day 4 at 1
No. 125 exposure increased to 2.0 in day 4 at 1
No. 174 exposure increased to 2.0 in day 4 at 1
No. 186 exposure increased to 3.0 in day 4 at 1
*When No. 188 infected, Exposure is 3.0 in day 4 at move 1
No. 195 exposure increased to 2.0 in day 4 at 1
No. 199 exposure increased to 3.0 in day 4 at 1
No. 209 exposure increased to 3.0 in day 4 at 1
No. 227 exposure increased to 3.0 in day 4 at 1
No. 248 exposure increased to 3.0 in day 4 at 1
No. 257 exposure increased to 4.0 in day 4 at 1
No. 304 exposure increased to 1.0 in day 4 at 1
No. 307 exposure increased to 1.0 in day 4 at 1
No. 313 exposure increased to 2.0 in day 4 at 1
No. 323 exposure increased to 2.0 in day 4 at 1
*When No. 333 infected, Exposure is 2.0 in day 4 at move 1
No. 367 exposure increased to 2.0 in day 4 at 1
No. 401 exposure increased to 3.0 in day 4 at 1
No. 402 exposure increased to 1.0 in day 4 at 1
No. 411 exposure increased to 2.0 in day 4 at 1
No. 413 exposure increased to 2.0 in day 4 at 1
No. 427 exposure increased to 3.0 in day 4 at 1
No. 437 exposure increased to 2.0 in day 4 at 1
No. 440 exposure increased to 4.0 in day 4 at 1
No. 441 exposure increased to 4.0 in day 4 at 1
No. 457 exposure increased to 2.0 in day 4 at 1
No. 468 exposure increased to 2.0 in day 4 at 1
No. 504 exposure increased to 1.0 in day 4 at 1
No. 578 exposure increased to 3.0 in day 4 at 1
No. 583 exposure increased to 2.0 in day 4 at 1
No. 594 exposure increased to 3.0 in day 4 at 1
No. 595 exposure increased to 3.0 in day 4 at 1
No. 602 exposure increased to 2.0 in day 4 at 1
No. 630 exposure increased to 4.0 in day 4 at 1
No. 644 exposure increased to 3.0 in day 4 at 1
No. 646 exposure increased to 2.0 in day 4 at 1
*When No. 647 infected, Exposure is 3.0 in day 4 at move 1
No. 652 exposure increased to 3.0 in day 4 at 1
No. 656 exposure increased to 3.0 in day 4 at 1
No. 671 exposure increased to 2.0 in day 4 at 1
No. 674 exposure increased to 3.0 in day 4 at 1
*When No. 680 infected, Exposure is 4.0 in day 4 at move 1
*When No. 716 infected, Exposure is 3.0 in day 4 at move 1
No. 717 exposure increased to 3.0 in day 4 at 1
*When No. 748 infected, Exposure is 4.0 in day 4 at move 1
No. 770 exposure increased to 4.0 in day 4 at 1
No. 789 exposure increased to 3.0 in day 4 at 1
No. 796 exposure increased to 3.0 in day 4 at 1
No. 806 exposure increased to 1.0 in day 4 at 1
No. 811 exposure increased to 3.0 in day 4 at 1
*When No. 863 infected, Exposure is 3.0 in day 4 at move 1
No. 870 exposure increased to 4.0 in day 4 at 1
No. 899 exposure increased to 3.0 in day 4 at 1
No. 902 exposure increased to 3.0 in day 4 at 1
No. 907 exposure increased to 2.0 in day 4 at 1
No. 912 exposure increased to 3.0 in day 4 at 1
*When No. 929 infected, Exposure is 3.0 in day 4 at move 1
No. 940 exposure increased to 2.0 in day 4 at 1
No. 950 exposure increased to 3.0 in day 4 at 1
No. 951 exposure increased to 2.0 in day 4 at 1
*When No. 957 infected, Exposure is 2.0 in day 4 at move 1
*When No. 985 infected, Exposure is 3.0 in day 4 at move 1
No. 993 exposure increased to 5.0 in day 4 at 1
No. 996 exposure increased to 2.0 in day 4 at 1
  136/10000 [..............................] - ETA: 17:35:22 - reward: 704.3217*When No. 209 infected, Exposure is 3.0 in day 4 at move 0
*When No. 227 infected, Exposure is 3.0 in day 4 at move 0
*When No. 257 infected, Exposure is 4.0 in day 4 at move 0
*When No. 313 infected, Exposure is 2.0 in day 4 at move 0
*When No. 457 infected, Exposure is 2.0 in day 4 at move 0
*When No. 578 infected, Exposure is 3.0 in day 4 at move 0
*When No. 594 infected, Exposure is 3.0 in day 4 at move 0
*When No. 652 infected, Exposure is 3.0 in day 4 at move 0
*When No. 796 infected, Exposure is 3.0 in day 4 at move 0
*When No. 811 infected, Exposure is 3.0 in day 4 at move 0
*When No. 116 infected, Exposure is 3.0 in day 4 at move 1
*When No. 595 infected, Exposure is 3.0 in day 4 at move 1
*When No. 630 infected, Exposure is 4.0 in day 4 at move 1
*When No. 656 infected, Exposure is 3.0 in day 4 at move 1
*When No. 674 infected, Exposure is 3.0 in day 4 at move 1
*When No. 940 infected, Exposure is 2.0 in day 4 at move 1
*When No. 993 infected, Exposure is 5.0 in day 4 at move 1
*When No. 411 infected, Exposure is 2.0 in day 4 at move 2
*When No. 248 infected, Exposure is 3.0 in day 4 at move 3
*When No. 671 infected, Exposure is 2.0 in day 4 at move 3
*When No. 717 infected, Exposure is 3.0 in day 4 at move 3
*When No. 789 infected, Exposure is 3.0 in day 4 at move 3
*When No. 907 infected, Exposure is 2.0 in day 4 at move 3
*When No. 912 infected, Exposure is 3.0 in day 4 at move 3
*When No. 186 infected, Exposure is 3.0 in day 4 at move 4
*When No. 195 infected, Exposure is 2.0 in day 4 at move 4
*When No. 199 infected, Exposure is 3.0 in day 4 at move 4
*When No. 413 infected, Exposure is 2.0 in day 4 at move 4
*When No. 427 infected, Exposure is 3.0 in day 4 at move 4
*When No. 644 infected, Exposure is 3.0 in day 4 at move 4
*When No. 870 infected, Exposure is 4.0 in day 4 at move 4
No. 3 exposure increased to 3.0 in day 4 at 5
No. 38 exposure increased to 1.0 in day 4 at 5
No. 42 exposure increased to 4.0 in day 4 at 5
No. 91 exposure increased to 1.0 in day 4 at 5
No. 103 exposure increased to 1.0 in day 4 at 5
No. 108 exposure increased to 1.0 in day 4 at 5
No. 109 exposure increased to 3.0 in day 4 at 5
No. 125 exposure increased to 3.0 in day 4 at 5
No. 141 exposure increased to 1.0 in day 4 at 5
No. 168 exposure increased to 1.0 in day 4 at 5
No. 174 exposure increased to 3.0 in day 4 at 5
No. 215 exposure increased to 1.0 in day 4 at 5
No. 239 exposure increased to 1.0 in day 4 at 5
No. 303 exposure increased to 2.0 in day 4 at 5
No. 304 exposure increased to 2.0 in day 4 at 5
No. 307 exposure increased to 2.0 in day 4 at 5
No. 323 exposure increased to 3.0 in day 4 at 5
No. 326 exposure increased to 1.0 in day 4 at 5
No. 350 exposure increased to 1.0 in day 4 at 5
No. 367 exposure increased to 3.0 in day 4 at 5
No. 368 exposure increased to 1.0 in day 4 at 5
No. 401 exposure increased to 4.0 in day 4 at 5
No. 402 exposure increased to 2.0 in day 4 at 5
No. 437 exposure increased to 3.0 in day 4 at 5
*When No. 440 infected, Exposure is 4.0 in day 4 at move 5
No. 441 exposure increased to 5.0 in day 4 at 5
No. 468 exposure increased to 3.0 in day 4 at 5
No. 504 exposure increased to 2.0 in day 4 at 5
No. 514 exposure increased to 1.0 in day 4 at 5
No. 519 exposure increased to 1.0 in day 4 at 5
No. 543 exposure increased to 1.0 in day 4 at 5
No. 583 exposure increased to 3.0 in day 4 at 5
No. 587 exposure increased to 1.0 in day 4 at 5
No. 602 exposure increased to 3.0 in day 4 at 5
No. 643 exposure increased to 2.0 in day 4 at 5
No. 646 exposure increased to 3.0 in day 4 at 5
No. 676 exposure increased to 1.0 in day 4 at 5
No. 687 exposure increased to 1.0 in day 4 at 5
No. 691 exposure increased to 1.0 in day 4 at 5
No. 770 exposure increased to 5.0 in day 4 at 5
No. 772 exposure increased to 1.0 in day 4 at 5
No. 806 exposure increased to 2.0 in day 4 at 5
No. 883 exposure increased to 2.0 in day 4 at 5
No. 884 exposure increased to 1.0 in day 4 at 5
No. 899 exposure increased to 4.0 in day 4 at 5
No. 902 exposure increased to 4.0 in day 4 at 5
No. 903 exposure increased to 1.0 in day 4 at 5
No. 921 exposure increased to 1.0 in day 4 at 5
No. 922 exposure increased to 1.0 in day 4 at 5
No. 926 exposure increased to 1.0 in day 4 at 5
No. 931 exposure increased to 1.0 in day 4 at 5
No. 950 exposure increased to 4.0 in day 4 at 5
No. 951 exposure increased to 3.0 in day 4 at 5
No. 987 exposure increased to 1.0 in day 4 at 5
No. 996 exposure increased to 3.0 in day 4 at 5
  137/10000 [..............................] - ETA: 17:42:42 - reward: 702.2826*When No. 3 infected, Exposure is 3.0 in day 4 at move 0
*When No. 42 infected, Exposure is 4.0 in day 4 at move 0
*When No. 303 infected, Exposure is 2.0 in day 4 at move 0
*When No. 323 infected, Exposure is 3.0 in day 4 at move 0
*When No. 367 infected, Exposure is 3.0 in day 4 at move 0
*When No. 401 infected, Exposure is 4.0 in day 4 at move 0
*When No. 402 infected, Exposure is 2.0 in day 4 at move 0
*When No. 437 infected, Exposure is 3.0 in day 4 at move 0
*When No. 583 infected, Exposure is 3.0 in day 4 at move 0
*When No. 643 infected, Exposure is 2.0 in day 4 at move 0
*When No. 304 infected, Exposure is 2.0 in day 4 at move 1
*When No. 646 infected, Exposure is 3.0 in day 4 at move 1
*When No. 770 infected, Exposure is 5.0 in day 4 at move 3
*When No. 899 infected, Exposure is 4.0 in day 4 at move 4
*When No. 902 infected, Exposure is 4.0 in day 4 at move 4
*When No. 950 infected, Exposure is 4.0 in day 4 at move 4
*When No. 996 infected, Exposure is 3.0 in day 4 at move 4
No. 2 exposure increased to 1.0 in day 4 at 5
No. 20 exposure increased to 2.0 in day 4 at 5
No. 38 exposure increased to 2.0 in day 4 at 5
No. 63 exposure increased to 1.0 in day 4 at 5
No. 89 exposure increased to 1.0 in day 4 at 5
No. 91 exposure increased to 2.0 in day 4 at 5
No. 93 exposure increased to 1.0 in day 4 at 5
No. 102 exposure increased to 2.0 in day 4 at 5
No. 103 exposure increased to 2.0 in day 4 at 5
No. 108 exposure increased to 2.0 in day 4 at 5
No. 109 exposure increased to 4.0 in day 4 at 5
No. 125 exposure increased to 4.0 in day 4 at 5
No. 135 exposure increased to 1.0 in day 4 at 5
No. 141 exposure increased to 2.0 in day 4 at 5
No. 168 exposure increased to 2.0 in day 4 at 5
No. 170 exposure increased to 1.0 in day 4 at 5
No. 173 exposure increased to 1.0 in day 4 at 5
No. 174 exposure increased to 4.0 in day 4 at 5
No. 184 exposure increased to 1.0 in day 4 at 5
No. 215 exposure increased to 2.0 in day 4 at 5
No. 239 exposure increased to 2.0 in day 4 at 5
No. 273 exposure increased to 1.0 in day 4 at 5
No. 276 exposure increased to 1.0 in day 4 at 5
No. 287 exposure increased to 1.0 in day 4 at 5
No. 297 exposure increased to 1.0 in day 4 at 5
No. 300 exposure increased to 1.0 in day 4 at 5
No. 307 exposure increased to 3.0 in day 4 at 5
No. 322 exposure increased to 1.0 in day 4 at 5
No. 326 exposure increased to 2.0 in day 4 at 5
No. 350 exposure increased to 2.0 in day 4 at 5
No. 354 exposure increased to 2.0 in day 4 at 5
No. 368 exposure increased to 2.0 in day 4 at 5
No. 373 exposure increased to 2.0 in day 4 at 5
No. 389 exposure increased to 2.0 in day 4 at 5
No. 393 exposure increased to 1.0 in day 4 at 5
No. 441 exposure increased to 6.0 in day 4 at 5
No. 446 exposure increased to 1.0 in day 4 at 5
No. 452 exposure increased to 1.0 in day 4 at 5
No. 468 exposure increased to 4.0 in day 4 at 5
No. 483 exposure increased to 1.0 in day 4 at 5
No. 495 exposure increased to 1.0 in day 4 at 5
No. 500 exposure increased to 1.0 in day 4 at 5
No. 504 exposure increased to 3.0 in day 4 at 5
No. 510 exposure increased to 2.0 in day 4 at 5
No. 514 exposure increased to 2.0 in day 4 at 5
No. 519 exposure increased to 2.0 in day 4 at 5
No. 543 exposure increased to 2.0 in day 4 at 5
No. 576 exposure increased to 1.0 in day 4 at 5
No. 587 exposure increased to 2.0 in day 4 at 5
*When No. 602 infected, Exposure is 3.0 in day 4 at move 5
No. 633 exposure increased to 2.0 in day 4 at 5
No. 649 exposure increased to 1.0 in day 4 at 5
No. 659 exposure increased to 1.0 in day 4 at 5
No. 665 exposure increased to 2.0 in day 4 at 5
No. 676 exposure increased to 2.0 in day 4 at 5
No. 687 exposure increased to 2.0 in day 4 at 5
No. 691 exposure increased to 2.0 in day 4 at 5
No. 696 exposure increased to 1.0 in day 4 at 5
No. 705 exposure increased to 1.0 in day 4 at 5
No. 718 exposure increased to 1.0 in day 4 at 5
No. 733 exposure increased to 1.0 in day 4 at 5
No. 756 exposure increased to 1.0 in day 4 at 5
No. 772 exposure increased to 2.0 in day 4 at 5
No. 803 exposure increased to 1.0 in day 4 at 5
No. 806 exposure increased to 3.0 in day 4 at 5
No. 822 exposure increased to 1.0 in day 4 at 5
No. 842 exposure increased to 1.0 in day 4 at 5
No. 862 exposure increased to 1.0 in day 4 at 5
No. 866 exposure increased to 1.0 in day 4 at 5
No. 874 exposure increased to 2.0 in day 4 at 5
No. 883 exposure increased to 3.0 in day 4 at 5
No. 884 exposure increased to 2.0 in day 4 at 5
No. 889 exposure increased to 1.0 in day 4 at 5
No. 903 exposure increased to 2.0 in day 4 at 5
No. 921 exposure increased to 2.0 in day 4 at 5
No. 922 exposure increased to 2.0 in day 4 at 5
No. 926 exposure increased to 2.0 in day 4 at 5
No. 931 exposure increased to 2.0 in day 4 at 5
*When No. 951 infected, Exposure is 3.0 in day 4 at move 5
No. 987 exposure increased to 2.0 in day 4 at 5
  138/10000 [..............................] - ETA: 17:53:30 - reward: 700.5001*When No. 125 infected, Exposure is 4.0 in day 4 at move 0
*When No. 174 infected, Exposure is 4.0 in day 4 at move 0
*When No. 307 infected, Exposure is 3.0 in day 4 at move 0
*When No. 468 infected, Exposure is 4.0 in day 4 at move 0
*When No. 108 infected, Exposure is 2.0 in day 4 at move 1
*When No. 109 infected, Exposure is 4.0 in day 4 at move 1
*When No. 587 infected, Exposure is 2.0 in day 4 at move 1
*When No. 772 infected, Exposure is 2.0 in day 4 at move 1
*When No. 884 infected, Exposure is 2.0 in day 4 at move 1
*When No. 987 infected, Exposure is 2.0 in day 4 at move 1
*When No. 38 infected, Exposure is 2.0 in day 4 at move 2
*When No. 102 infected, Exposure is 2.0 in day 4 at move 2
*When No. 103 infected, Exposure is 2.0 in day 4 at move 2
*When No. 883 infected, Exposure is 3.0 in day 4 at move 2
*When No. 903 infected, Exposure is 2.0 in day 4 at move 2
*When No. 931 infected, Exposure is 2.0 in day 4 at move 2
*When No. 326 infected, Exposure is 2.0 in day 4 at move 3
*When No. 514 infected, Exposure is 2.0 in day 4 at move 3
*When No. 350 infected, Exposure is 2.0 in day 4 at move 4
*When No. 504 infected, Exposure is 3.0 in day 4 at move 4
*When No. 806 infected, Exposure is 3.0 in day 4 at move 4
*When No. 926 infected, Exposure is 2.0 in day 4 at move 4
No. 2 exposure increased to 2.0 in day 4 at 5
*When No. 20 infected, Exposure is 2.0 in day 4 at move 5
No. 27 exposure increased to 1.0 in day 4 at 5
No. 29 exposure increased to 1.0 in day 4 at 5
No. 40 exposure increased to 1.0 in day 4 at 5
No. 50 exposure increased to 1.0 in day 4 at 5
No. 60 exposure increased to 1.0 in day 4 at 5
No. 63 exposure increased to 2.0 in day 4 at 5
No. 89 exposure increased to 2.0 in day 4 at 5
No. 91 exposure increased to 3.0 in day 4 at 5
No. 93 exposure increased to 2.0 in day 4 at 5
No. 114 exposure increased to 1.0 in day 4 at 5
No. 118 exposure increased to 1.0 in day 4 at 5
No. 135 exposure increased to 2.0 in day 4 at 5
No. 141 exposure increased to 3.0 in day 4 at 5
No. 142 exposure increased to 2.0 in day 4 at 5
No. 168 exposure increased to 3.0 in day 4 at 5
No. 170 exposure increased to 2.0 in day 4 at 5
No. 173 exposure increased to 2.0 in day 4 at 5
No. 181 exposure increased to 1.0 in day 4 at 5
No. 184 exposure increased to 2.0 in day 4 at 5
No. 191 exposure increased to 1.0 in day 4 at 5
No. 215 exposure increased to 3.0 in day 4 at 5
No. 239 exposure increased to 3.0 in day 4 at 5
No. 273 exposure increased to 2.0 in day 4 at 5
No. 276 exposure increased to 2.0 in day 4 at 5
No. 284 exposure increased to 1.0 in day 4 at 5
No. 285 exposure increased to 1.0 in day 4 at 5
No. 287 exposure increased to 2.0 in day 4 at 5
No. 293 exposure increased to 1.0 in day 4 at 5
No. 297 exposure increased to 2.0 in day 4 at 5
No. 300 exposure increased to 2.0 in day 4 at 5
No. 322 exposure increased to 2.0 in day 4 at 5
No. 329 exposure increased to 1.0 in day 4 at 5
No. 353 exposure increased to 1.0 in day 4 at 5
No. 354 exposure increased to 3.0 in day 4 at 5
*When No. 368 infected, Exposure is 2.0 in day 4 at move 5
No. 373 exposure increased to 3.0 in day 4 at 5
No. 375 exposure increased to 1.0 in day 4 at 5
No. 389 exposure increased to 3.0 in day 4 at 5
No. 393 exposure increased to 2.0 in day 4 at 5
No. 409 exposure increased to 1.0 in day 4 at 5
No. 417 exposure increased to 1.0 in day 4 at 5
No. 433 exposure increased to 1.0 in day 4 at 5
*When No. 441 infected, Exposure is 6.0 in day 4 at move 5
No. 446 exposure increased to 2.0 in day 4 at 5
No. 448 exposure increased to 1.0 in day 4 at 5
No. 450 exposure increased to 1.0 in day 4 at 5
No. 452 exposure increased to 2.0 in day 4 at 5
No. 483 exposure increased to 2.0 in day 4 at 5
No. 495 exposure increased to 2.0 in day 4 at 5
No. 500 exposure increased to 2.0 in day 4 at 5
No. 510 exposure increased to 3.0 in day 4 at 5
No. 519 exposure increased to 3.0 in day 4 at 5
No. 543 exposure increased to 3.0 in day 4 at 5
No. 547 exposure increased to 1.0 in day 4 at 5
No. 572 exposure increased to 1.0 in day 4 at 5
No. 575 exposure increased to 1.0 in day 4 at 5
No. 576 exposure increased to 2.0 in day 4 at 5
No. 609 exposure increased to 1.0 in day 4 at 5
No. 631 exposure increased to 1.0 in day 4 at 5
No. 633 exposure increased to 3.0 in day 4 at 5
No. 649 exposure increased to 2.0 in day 4 at 5
No. 659 exposure increased to 2.0 in day 4 at 5
*When No. 665 infected, Exposure is 2.0 in day 4 at move 5
No. 676 exposure increased to 3.0 in day 4 at 5
No. 687 exposure increased to 3.0 in day 4 at 5
*When No. 691 infected, Exposure is 2.0 in day 4 at move 5
No. 696 exposure increased to 2.0 in day 4 at 5
No. 705 exposure increased to 2.0 in day 4 at 5
No. 718 exposure increased to 2.0 in day 4 at 5
No. 733 exposure increased to 2.0 in day 4 at 5
No. 743 exposure increased to 1.0 in day 4 at 5
No. 756 exposure increased to 2.0 in day 4 at 5
No. 803 exposure increased to 2.0 in day 4 at 5
No. 822 exposure increased to 2.0 in day 4 at 5
No. 835 exposure increased to 1.0 in day 4 at 5
No. 842 exposure increased to 2.0 in day 4 at 5
No. 862 exposure increased to 2.0 in day 4 at 5
No. 866 exposure increased to 2.0 in day 4 at 5
No. 874 exposure increased to 3.0 in day 4 at 5
No. 889 exposure increased to 2.0 in day 4 at 5
No. 893 exposure increased to 1.0 in day 4 at 5
No. 914 exposure increased to 1.0 in day 4 at 5
No. 921 exposure increased to 3.0 in day 4 at 5
*When No. 922 infected, Exposure is 2.0 in day 4 at move 5
No. 933 exposure increased to 1.0 in day 4 at 5
No. 946 exposure increased to 1.0 in day 4 at 5
No. 975 exposure increased to 1.0 in day 4 at 5
No. 980 exposure increased to 1.0 in day 4 at 5
No. 997 exposure increased to 1.0 in day 4 at 5
  139/10000 [..............................] - ETA: 18:02:48 - reward: 698.4278*When No. 91 infected, Exposure is 3.0 in day 4 at move 0
*When No. 93 infected, Exposure is 2.0 in day 4 at move 0
*When No. 142 infected, Exposure is 2.0 in day 4 at move 0
*When No. 239 infected, Exposure is 3.0 in day 4 at move 0
*When No. 354 infected, Exposure is 3.0 in day 4 at move 0
*When No. 373 infected, Exposure is 3.0 in day 4 at move 0
*When No. 687 infected, Exposure is 3.0 in day 4 at move 0
*When No. 756 infected, Exposure is 2.0 in day 4 at move 0
*When No. 822 infected, Exposure is 2.0 in day 4 at move 0
*When No. 874 infected, Exposure is 3.0 in day 4 at move 0
No. 2 exposure increased to 3.0 in day 4 at 1
No. 22 exposure increased to 1.0 in day 4 at 1
No. 27 exposure increased to 2.0 in day 4 at 1
No. 29 exposure increased to 2.0 in day 4 at 1
No. 40 exposure increased to 2.0 in day 4 at 1
No. 50 exposure increased to 2.0 in day 4 at 1
No. 60 exposure increased to 2.0 in day 4 at 1
No. 63 exposure increased to 3.0 in day 4 at 1
No. 89 exposure increased to 3.0 in day 4 at 1
No. 114 exposure increased to 2.0 in day 4 at 1
No. 118 exposure increased to 2.0 in day 4 at 1
No. 126 exposure increased to 1.0 in day 4 at 1
No. 135 exposure increased to 3.0 in day 4 at 1
No. 141 exposure increased to 4.0 in day 4 at 1
*When No. 168 infected, Exposure is 3.0 in day 4 at move 1
No. 170 exposure increased to 3.0 in day 4 at 1
No. 173 exposure increased to 3.0 in day 4 at 1
No. 181 exposure increased to 2.0 in day 4 at 1
No. 184 exposure increased to 3.0 in day 4 at 1
No. 191 exposure increased to 2.0 in day 4 at 1
*When No. 215 infected, Exposure is 3.0 in day 4 at move 1
No. 270 exposure increased to 2.0 in day 4 at 1
No. 273 exposure increased to 3.0 in day 4 at 1
No. 276 exposure increased to 3.0 in day 4 at 1
No. 284 exposure increased to 2.0 in day 4 at 1
No. 285 exposure increased to 2.0 in day 4 at 1
No. 287 exposure increased to 3.0 in day 4 at 1
No. 293 exposure increased to 2.0 in day 4 at 1
No. 297 exposure increased to 3.0 in day 4 at 1
No. 300 exposure increased to 3.0 in day 4 at 1
No. 311 exposure increased to 2.0 in day 4 at 1
*When No. 322 infected, Exposure is 2.0 in day 4 at move 1
No. 329 exposure increased to 2.0 in day 4 at 1
No. 353 exposure increased to 2.0 in day 4 at 1
No. 375 exposure increased to 2.0 in day 4 at 1
No. 389 exposure increased to 4.0 in day 4 at 1
No. 393 exposure increased to 3.0 in day 4 at 1
No. 409 exposure increased to 2.0 in day 4 at 1
No. 417 exposure increased to 2.0 in day 4 at 1
No. 433 exposure increased to 2.0 in day 4 at 1
No. 446 exposure increased to 3.0 in day 4 at 1
No. 448 exposure increased to 2.0 in day 4 at 1
No. 450 exposure increased to 2.0 in day 4 at 1
No. 452 exposure increased to 3.0 in day 4 at 1
No. 456 exposure increased to 2.0 in day 4 at 1
No. 483 exposure increased to 3.0 in day 4 at 1
No. 495 exposure increased to 3.0 in day 4 at 1
No. 500 exposure increased to 3.0 in day 4 at 1
No. 510 exposure increased to 4.0 in day 4 at 1
No. 511 exposure increased to 2.0 in day 4 at 1
*When No. 519 infected, Exposure is 3.0 in day 4 at move 1
No. 543 exposure increased to 4.0 in day 4 at 1
No. 547 exposure increased to 2.0 in day 4 at 1
No. 572 exposure increased to 2.0 in day 4 at 1
No. 575 exposure increased to 2.0 in day 4 at 1
No. 576 exposure increased to 3.0 in day 4 at 1
No. 609 exposure increased to 2.0 in day 4 at 1
No. 620 exposure increased to 2.0 in day 4 at 1
No. 631 exposure increased to 2.0 in day 4 at 1
No. 633 exposure increased to 4.0 in day 4 at 1
No. 649 exposure increased to 3.0 in day 4 at 1
No. 659 exposure increased to 3.0 in day 4 at 1
No. 676 exposure increased to 4.0 in day 4 at 1
No. 696 exposure increased to 3.0 in day 4 at 1
No. 705 exposure increased to 3.0 in day 4 at 1
No. 718 exposure increased to 3.0 in day 4 at 1
No. 733 exposure increased to 3.0 in day 4 at 1
No. 743 exposure increased to 2.0 in day 4 at 1
No. 801 exposure increased to 1.0 in day 4 at 1
No. 803 exposure increased to 3.0 in day 4 at 1
No. 835 exposure increased to 2.0 in day 4 at 1
No. 839 exposure increased to 1.0 in day 4 at 1
*When No. 842 infected, Exposure is 2.0 in day 4 at move 1
*When No. 862 infected, Exposure is 2.0 in day 4 at move 1
No. 866 exposure increased to 3.0 in day 4 at 1
No. 889 exposure increased to 3.0 in day 4 at 1
No. 893 exposure increased to 2.0 in day 4 at 1
No. 914 exposure increased to 2.0 in day 4 at 1
No. 921 exposure increased to 4.0 in day 4 at 1
No. 933 exposure increased to 2.0 in day 4 at 1
No. 946 exposure increased to 2.0 in day 4 at 1
No. 975 exposure increased to 2.0 in day 4 at 1
No. 980 exposure increased to 2.0 in day 4 at 1
No. 997 exposure increased to 2.0 in day 4 at 1
  140/10000 [..............................] - ETA: 18:02:26 - reward: 696.8402*When No. 2 infected, Exposure is 3.0 in day 4 at move 0
*When No. 29 infected, Exposure is 2.0 in day 4 at move 0
*When No. 184 infected, Exposure is 3.0 in day 4 at move 0
*When No. 297 infected, Exposure is 3.0 in day 4 at move 0
*When No. 329 infected, Exposure is 2.0 in day 4 at move 0
*When No. 389 infected, Exposure is 4.0 in day 4 at move 0
*When No. 433 infected, Exposure is 2.0 in day 4 at move 0
*When No. 483 infected, Exposure is 3.0 in day 4 at move 0
*When No. 511 infected, Exposure is 2.0 in day 4 at move 0
*When No. 633 infected, Exposure is 4.0 in day 4 at move 0
*When No. 835 infected, Exposure is 2.0 in day 4 at move 0
*When No. 889 infected, Exposure is 3.0 in day 4 at move 0
*When No. 141 infected, Exposure is 4.0 in day 4 at move 1
*When No. 181 infected, Exposure is 2.0 in day 4 at move 1
*When No. 300 infected, Exposure is 3.0 in day 4 at move 1
*When No. 448 infected, Exposure is 2.0 in day 4 at move 1
*When No. 452 infected, Exposure is 3.0 in day 4 at move 1
*When No. 676 infected, Exposure is 4.0 in day 4 at move 1
*When No. 743 infected, Exposure is 2.0 in day 4 at move 1
*When No. 803 infected, Exposure is 3.0 in day 4 at move 1
*When No. 866 infected, Exposure is 3.0 in day 4 at move 1
*When No. 114 infected, Exposure is 2.0 in day 4 at move 2
*When No. 135 infected, Exposure is 3.0 in day 4 at move 2
*When No. 191 infected, Exposure is 2.0 in day 4 at move 2
*When No. 284 infected, Exposure is 2.0 in day 4 at move 2
*When No. 287 infected, Exposure is 3.0 in day 4 at move 2
*When No. 576 infected, Exposure is 3.0 in day 4 at move 2
*When No. 609 infected, Exposure is 2.0 in day 4 at move 2
*When No. 914 infected, Exposure is 2.0 in day 4 at move 2
*When No. 946 infected, Exposure is 2.0 in day 4 at move 2
*When No. 170 infected, Exposure is 3.0 in day 4 at move 3
*When No. 417 infected, Exposure is 2.0 in day 4 at move 3
*When No. 495 infected, Exposure is 3.0 in day 4 at move 3
*When No. 659 infected, Exposure is 3.0 in day 4 at move 3
*When No. 921 infected, Exposure is 4.0 in day 4 at move 3
*When No. 27 infected, Exposure is 2.0 in day 4 at move 4
*When No. 89 infected, Exposure is 3.0 in day 4 at move 4
*When No. 173 infected, Exposure is 3.0 in day 4 at move 4
*When No. 276 infected, Exposure is 3.0 in day 4 at move 4
*When No. 311 infected, Exposure is 2.0 in day 4 at move 4
*When No. 375 infected, Exposure is 2.0 in day 4 at move 4
*When No. 543 infected, Exposure is 4.0 in day 4 at move 4
*When No. 733 infected, Exposure is 3.0 in day 4 at move 4
No. 0 exposure increased to 1.0 in day 4 at 5
No. 1 exposure increased to 1.0 in day 4 at 5
No. 15 exposure increased to 1.0 in day 4 at 5
No. 22 exposure increased to 2.0 in day 4 at 5
No. 24 exposure increased to 1.0 in day 4 at 5
No. 40 exposure increased to 3.0 in day 4 at 5
No. 50 exposure increased to 3.0 in day 4 at 5
No. 60 exposure increased to 3.0 in day 4 at 5
No. 63 exposure increased to 4.0 in day 4 at 5
No. 112 exposure increased to 2.0 in day 4 at 5
No. 118 exposure increased to 3.0 in day 4 at 5
No. 126 exposure increased to 2.0 in day 4 at 5
No. 130 exposure increased to 1.0 in day 4 at 5
No. 189 exposure increased to 1.0 in day 4 at 5
No. 234 exposure increased to 2.0 in day 4 at 5
No. 247 exposure increased to 2.0 in day 4 at 5
No. 263 exposure increased to 1.0 in day 4 at 5
No. 266 exposure increased to 1.0 in day 4 at 5
No. 270 exposure increased to 3.0 in day 4 at 5
No. 273 exposure increased to 4.0 in day 4 at 5
No. 285 exposure increased to 3.0 in day 4 at 5
No. 293 exposure increased to 3.0 in day 4 at 5
No. 302 exposure increased to 2.0 in day 4 at 5
No. 315 exposure increased to 2.0 in day 4 at 5
No. 342 exposure increased to 2.0 in day 4 at 5
*When No. 353 infected, Exposure is 2.0 in day 4 at move 5
No. 357 exposure increased to 1.0 in day 4 at 5
No. 379 exposure increased to 1.0 in day 4 at 5
No. 384 exposure increased to 1.0 in day 4 at 5
No. 393 exposure increased to 4.0 in day 4 at 5
No. 409 exposure increased to 3.0 in day 4 at 5
No. 446 exposure increased to 4.0 in day 4 at 5
No. 450 exposure increased to 3.0 in day 4 at 5
No. 456 exposure increased to 3.0 in day 4 at 5
No. 500 exposure increased to 4.0 in day 4 at 5
No. 510 exposure increased to 5.0 in day 4 at 5
No. 518 exposure increased to 1.0 in day 4 at 5
No. 528 exposure increased to 1.0 in day 4 at 5
No. 530 exposure increased to 1.0 in day 4 at 5
No. 535 exposure increased to 1.0 in day 4 at 5
No. 547 exposure increased to 3.0 in day 4 at 5
No. 571 exposure increased to 1.0 in day 4 at 5
No. 572 exposure increased to 3.0 in day 4 at 5
No. 575 exposure increased to 3.0 in day 4 at 5
No. 611 exposure increased to 1.0 in day 4 at 5
No. 615 exposure increased to 1.0 in day 4 at 5
No. 618 exposure increased to 1.0 in day 4 at 5
No. 620 exposure increased to 3.0 in day 4 at 5
No. 623 exposure increased to 1.0 in day 4 at 5
No. 631 exposure increased to 3.0 in day 4 at 5
No. 649 exposure increased to 4.0 in day 4 at 5
No. 682 exposure increased to 1.0 in day 4 at 5
No. 696 exposure increased to 4.0 in day 4 at 5
No. 701 exposure increased to 1.0 in day 4 at 5
No. 705 exposure increased to 4.0 in day 4 at 5
No. 718 exposure increased to 4.0 in day 4 at 5
No. 771 exposure increased to 1.0 in day 4 at 5
No. 787 exposure increased to 1.0 in day 4 at 5
No. 801 exposure increased to 2.0 in day 4 at 5
No. 839 exposure increased to 2.0 in day 4 at 5
No. 840 exposure increased to 1.0 in day 4 at 5
No. 882 exposure increased to 1.0 in day 4 at 5
No. 893 exposure increased to 3.0 in day 4 at 5
No. 900 exposure increased to 1.0 in day 4 at 5
No. 908 exposure increased to 1.0 in day 4 at 5
No. 933 exposure increased to 3.0 in day 4 at 5
No. 935 exposure increased to 1.0 in day 4 at 5
No. 961 exposure increased to 1.0 in day 4 at 5
No. 965 exposure increased to 1.0 in day 4 at 5
No. 975 exposure increased to 3.0 in day 4 at 5
No. 980 exposure increased to 3.0 in day 4 at 5
No. 997 exposure increased to 3.0 in day 4 at 5
  141/10000 [..............................] - ETA: 18:07:21 - reward: 695.0104*When No. 118 infected, Exposure is 3.0 in day 4 at move 0
*When No. 273 infected, Exposure is 4.0 in day 4 at move 0
*When No. 547 infected, Exposure is 3.0 in day 4 at move 0
*When No. 572 infected, Exposure is 3.0 in day 4 at move 0
*When No. 705 infected, Exposure is 4.0 in day 4 at move 0
*When No. 893 infected, Exposure is 3.0 in day 4 at move 0
No. 0 exposure increased to 2.0 in day 4 at 1
No. 1 exposure increased to 2.0 in day 4 at 1
No. 12 exposure increased to 2.0 in day 4 at 1
No. 15 exposure increased to 2.0 in day 4 at 1
No. 22 exposure increased to 3.0 in day 4 at 1
No. 24 exposure increased to 2.0 in day 4 at 1
No. 26 exposure increased to 2.0 in day 4 at 1
No. 28 exposure increased to 1.0 in day 4 at 1
No. 40 exposure increased to 4.0 in day 4 at 1
No. 50 exposure increased to 4.0 in day 4 at 1
No. 60 exposure increased to 4.0 in day 4 at 1
No. 63 exposure increased to 5.0 in day 4 at 1
No. 72 exposure increased to 2.0 in day 4 at 1
No. 112 exposure increased to 3.0 in day 4 at 1
No. 126 exposure increased to 3.0 in day 4 at 1
No. 130 exposure increased to 2.0 in day 4 at 1
No. 189 exposure increased to 2.0 in day 4 at 1
No. 234 exposure increased to 3.0 in day 4 at 1
*When No. 247 infected, Exposure is 2.0 in day 4 at move 1
No. 263 exposure increased to 2.0 in day 4 at 1
No. 266 exposure increased to 2.0 in day 4 at 1
No. 270 exposure increased to 4.0 in day 4 at 1
No. 285 exposure increased to 4.0 in day 4 at 1
No. 293 exposure increased to 4.0 in day 4 at 1
No. 302 exposure increased to 3.0 in day 4 at 1
No. 315 exposure increased to 3.0 in day 4 at 1
No. 342 exposure increased to 3.0 in day 4 at 1
No. 357 exposure increased to 2.0 in day 4 at 1
No. 379 exposure increased to 2.0 in day 4 at 1
No. 384 exposure increased to 2.0 in day 4 at 1
No. 393 exposure increased to 5.0 in day 4 at 1
No. 409 exposure increased to 4.0 in day 4 at 1
No. 435 exposure increased to 1.0 in day 4 at 1
No. 443 exposure increased to 1.0 in day 4 at 1
No. 446 exposure increased to 5.0 in day 4 at 1
No. 450 exposure increased to 4.0 in day 4 at 1
No. 456 exposure increased to 4.0 in day 4 at 1
No. 498 exposure increased to 1.0 in day 4 at 1
No. 500 exposure increased to 5.0 in day 4 at 1
No. 510 exposure increased to 6.0 in day 4 at 1
No. 518 exposure increased to 2.0 in day 4 at 1
No. 523 exposure increased to 2.0 in day 4 at 1
No. 528 exposure increased to 2.0 in day 4 at 1
No. 530 exposure increased to 2.0 in day 4 at 1
No. 535 exposure increased to 2.0 in day 4 at 1
No. 550 exposure increased to 1.0 in day 4 at 1
No. 571 exposure increased to 2.0 in day 4 at 1
No. 575 exposure increased to 4.0 in day 4 at 1
No. 611 exposure increased to 2.0 in day 4 at 1
No. 615 exposure increased to 2.0 in day 4 at 1
No. 618 exposure increased to 2.0 in day 4 at 1
*When No. 620 infected, Exposure is 3.0 in day 4 at move 1
No. 623 exposure increased to 2.0 in day 4 at 1
No. 631 exposure increased to 4.0 in day 4 at 1
No. 641 exposure increased to 1.0 in day 4 at 1
No. 649 exposure increased to 5.0 in day 4 at 1
No. 682 exposure increased to 2.0 in day 4 at 1
No. 696 exposure increased to 5.0 in day 4 at 1
No. 698 exposure increased to 1.0 in day 4 at 1
No. 701 exposure increased to 2.0 in day 4 at 1
*When No. 718 infected, Exposure is 4.0 in day 4 at move 1
No. 771 exposure increased to 2.0 in day 4 at 1
No. 776 exposure increased to 1.0 in day 4 at 1
No. 787 exposure increased to 2.0 in day 4 at 1
*When No. 801 infected, Exposure is 2.0 in day 4 at move 1
No. 839 exposure increased to 3.0 in day 4 at 1
No. 840 exposure increased to 2.0 in day 4 at 1
No. 882 exposure increased to 2.0 in day 4 at 1
No. 900 exposure increased to 2.0 in day 4 at 1
No. 908 exposure increased to 2.0 in day 4 at 1
No. 933 exposure increased to 4.0 in day 4 at 1
No. 935 exposure increased to 2.0 in day 4 at 1
No. 961 exposure increased to 2.0 in day 4 at 1
No. 962 exposure increased to 2.0 in day 4 at 1
No. 965 exposure increased to 2.0 in day 4 at 1
No. 975 exposure increased to 4.0 in day 4 at 1
No. 980 exposure increased to 4.0 in day 4 at 1
No. 997 exposure increased to 4.0 in day 4 at 1
  142/10000 [..............................] - ETA: 18:05:31 - reward: 693.4425*When No. 1 infected, Exposure is 2.0 in day 4 at move 0
*When No. 40 infected, Exposure is 4.0 in day 4 at move 0
*When No. 60 infected, Exposure is 4.0 in day 4 at move 0
*When No. 72 infected, Exposure is 2.0 in day 4 at move 0
*When No. 126 infected, Exposure is 3.0 in day 4 at move 0
*When No. 234 infected, Exposure is 3.0 in day 4 at move 0
*When No. 270 infected, Exposure is 4.0 in day 4 at move 0
*When No. 285 infected, Exposure is 4.0 in day 4 at move 0
*When No. 293 infected, Exposure is 4.0 in day 4 at move 0
*When No. 446 infected, Exposure is 5.0 in day 4 at move 0
*When No. 450 infected, Exposure is 4.0 in day 4 at move 0
*When No. 510 infected, Exposure is 6.0 in day 4 at move 0
*When No. 518 infected, Exposure is 2.0 in day 4 at move 0
*When No. 571 infected, Exposure is 2.0 in day 4 at move 0
*When No. 618 infected, Exposure is 2.0 in day 4 at move 0
*When No. 631 infected, Exposure is 4.0 in day 4 at move 0
*When No. 649 infected, Exposure is 5.0 in day 4 at move 0
*When No. 696 infected, Exposure is 5.0 in day 4 at move 0
*When No. 882 infected, Exposure is 2.0 in day 4 at move 0
*When No. 933 infected, Exposure is 4.0 in day 4 at move 0
*When No. 980 infected, Exposure is 4.0 in day 4 at move 0
*When No. 0 infected, Exposure is 2.0 in day 4 at move 1
*When No. 12 infected, Exposure is 2.0 in day 4 at move 1
*When No. 50 infected, Exposure is 4.0 in day 4 at move 1
*When No. 112 infected, Exposure is 3.0 in day 4 at move 1
*When No. 379 infected, Exposure is 2.0 in day 4 at move 1
*When No. 500 infected, Exposure is 5.0 in day 4 at move 1
*When No. 623 infected, Exposure is 2.0 in day 4 at move 1
*When No. 997 infected, Exposure is 4.0 in day 4 at move 1
*When No. 24 infected, Exposure is 2.0 in day 4 at move 2
*When No. 393 infected, Exposure is 5.0 in day 4 at move 2
*When No. 528 infected, Exposure is 2.0 in day 4 at move 2
*When No. 530 infected, Exposure is 2.0 in day 4 at move 2
*When No. 787 infected, Exposure is 2.0 in day 4 at move 2
*When No. 22 infected, Exposure is 3.0 in day 4 at move 3
*When No. 63 infected, Exposure is 5.0 in day 4 at move 3
*When No. 302 infected, Exposure is 3.0 in day 4 at move 3
*When No. 611 infected, Exposure is 2.0 in day 4 at move 3
*When No. 771 infected, Exposure is 2.0 in day 4 at move 3
*When No. 839 infected, Exposure is 3.0 in day 4 at move 3
*When No. 15 infected, Exposure is 2.0 in day 4 at move 4
*When No. 315 infected, Exposure is 3.0 in day 4 at move 4
*When No. 342 infected, Exposure is 3.0 in day 4 at move 4
*When No. 456 infected, Exposure is 4.0 in day 4 at move 4
*When No. 975 infected, Exposure is 4.0 in day 4 at move 4
No. 17 exposure increased to 1.0 in day 4 at 5
No. 19 exposure increased to 2.0 in day 4 at 5
No. 26 exposure increased to 3.0 in day 4 at 5
No. 28 exposure increased to 2.0 in day 4 at 5
No. 30 exposure increased to 1.0 in day 4 at 5
No. 59 exposure increased to 2.0 in day 4 at 5
No. 66 exposure increased to 1.0 in day 4 at 5
No. 79 exposure increased to 1.0 in day 4 at 5
No. 115 exposure increased to 1.0 in day 4 at 5
No. 130 exposure increased to 3.0 in day 4 at 5
No. 189 exposure increased to 3.0 in day 4 at 5
No. 205 exposure increased to 2.0 in day 4 at 5
No. 237 exposure increased to 1.0 in day 4 at 5
No. 245 exposure increased to 1.0 in day 4 at 5
No. 263 exposure increased to 3.0 in day 4 at 5
No. 266 exposure increased to 3.0 in day 4 at 5
No. 295 exposure increased to 1.0 in day 4 at 5
No. 308 exposure increased to 1.0 in day 4 at 5
No. 321 exposure increased to 1.0 in day 4 at 5
No. 324 exposure increased to 1.0 in day 4 at 5
No. 347 exposure increased to 1.0 in day 4 at 5
No. 357 exposure increased to 3.0 in day 4 at 5
No. 384 exposure increased to 3.0 in day 4 at 5
No. 392 exposure increased to 1.0 in day 4 at 5
No. 400 exposure increased to 1.0 in day 4 at 5
*When No. 409 infected, Exposure is 4.0 in day 4 at move 5
No. 425 exposure increased to 1.0 in day 4 at 5
No. 435 exposure increased to 2.0 in day 4 at 5
No. 436 exposure increased to 1.0 in day 4 at 5
No. 443 exposure increased to 2.0 in day 4 at 5
No. 444 exposure increased to 1.0 in day 4 at 5
No. 447 exposure increased to 2.0 in day 4 at 5
No. 462 exposure increased to 1.0 in day 4 at 5
No. 480 exposure increased to 1.0 in day 4 at 5
No. 488 exposure increased to 1.0 in day 4 at 5
No. 498 exposure increased to 2.0 in day 4 at 5
No. 499 exposure increased to 1.0 in day 4 at 5
No. 523 exposure increased to 3.0 in day 4 at 5
No. 535 exposure increased to 3.0 in day 4 at 5
No. 537 exposure increased to 2.0 in day 4 at 5
No. 550 exposure increased to 2.0 in day 4 at 5
No. 556 exposure increased to 1.0 in day 4 at 5
No. 561 exposure increased to 1.0 in day 4 at 5
No. 567 exposure increased to 2.0 in day 4 at 5
*When No. 575 infected, Exposure is 4.0 in day 4 at move 5
No. 606 exposure increased to 2.0 in day 4 at 5
No. 615 exposure increased to 3.0 in day 4 at 5
No. 641 exposure increased to 2.0 in day 4 at 5
No. 654 exposure increased to 1.0 in day 4 at 5
No. 682 exposure increased to 3.0 in day 4 at 5
No. 693 exposure increased to 2.0 in day 4 at 5
No. 697 exposure increased to 1.0 in day 4 at 5
No. 698 exposure increased to 2.0 in day 4 at 5
No. 701 exposure increased to 3.0 in day 4 at 5
No. 712 exposure increased to 1.0 in day 4 at 5
No. 725 exposure increased to 1.0 in day 4 at 5
No. 726 exposure increased to 1.0 in day 4 at 5
No. 728 exposure increased to 1.0 in day 4 at 5
No. 738 exposure increased to 1.0 in day 4 at 5
No. 776 exposure increased to 2.0 in day 4 at 5
No. 795 exposure increased to 1.0 in day 4 at 5
No. 840 exposure increased to 3.0 in day 4 at 5
No. 900 exposure increased to 3.0 in day 4 at 5
No. 908 exposure increased to 3.0 in day 4 at 5
No. 909 exposure increased to 1.0 in day 4 at 5
No. 919 exposure increased to 2.0 in day 4 at 5
No. 920 exposure increased to 2.0 in day 4 at 5
No. 935 exposure increased to 3.0 in day 4 at 5
No. 953 exposure increased to 1.0 in day 4 at 5
No. 961 exposure increased to 3.0 in day 4 at 5
No. 962 exposure increased to 3.0 in day 4 at 5
No. 965 exposure increased to 3.0 in day 4 at 5
  143/10000 [..............................] - ETA: 18:10:56 - reward: 691.7868*When No. 189 infected, Exposure is 3.0 in day 4 at move 0
*When No. 357 infected, Exposure is 3.0 in day 4 at move 0
*When No. 443 infected, Exposure is 2.0 in day 4 at move 0
*When No. 908 infected, Exposure is 3.0 in day 4 at move 0
*When No. 263 infected, Exposure is 3.0 in day 4 at move 1
*When No. 435 infected, Exposure is 2.0 in day 4 at move 1
*When No. 535 infected, Exposure is 3.0 in day 4 at move 1
*When No. 615 infected, Exposure is 3.0 in day 4 at move 1
*When No. 900 infected, Exposure is 3.0 in day 4 at move 1
*When No. 962 infected, Exposure is 3.0 in day 4 at move 1
*When No. 523 infected, Exposure is 3.0 in day 4 at move 2
*When No. 641 infected, Exposure is 2.0 in day 4 at move 2
*When No. 693 infected, Exposure is 2.0 in day 4 at move 2
*When No. 59 infected, Exposure is 2.0 in day 4 at move 3
*When No. 26 infected, Exposure is 3.0 in day 4 at move 4
*When No. 130 infected, Exposure is 3.0 in day 4 at move 4
*When No. 701 infected, Exposure is 3.0 in day 4 at move 4
*When No. 935 infected, Exposure is 3.0 in day 4 at move 4
*When No. 961 infected, Exposure is 3.0 in day 4 at move 4
No. 17 exposure increased to 2.0 in day 4 at 5
No. 19 exposure increased to 3.0 in day 4 at 5
No. 28 exposure increased to 3.0 in day 4 at 5
No. 30 exposure increased to 2.0 in day 4 at 5
No. 34 exposure increased to 1.0 in day 4 at 5
No. 44 exposure increased to 1.0 in day 4 at 5
No. 66 exposure increased to 2.0 in day 4 at 5
No. 79 exposure increased to 2.0 in day 4 at 5
No. 90 exposure increased to 1.0 in day 4 at 5
No. 115 exposure increased to 2.0 in day 4 at 5
No. 123 exposure increased to 1.0 in day 4 at 5
No. 149 exposure increased to 1.0 in day 4 at 5
No. 161 exposure increased to 1.0 in day 4 at 5
No. 185 exposure increased to 1.0 in day 4 at 5
No. 187 exposure increased to 2.0 in day 4 at 5
No. 205 exposure increased to 3.0 in day 4 at 5
No. 219 exposure increased to 1.0 in day 4 at 5
No. 237 exposure increased to 2.0 in day 4 at 5
No. 245 exposure increased to 2.0 in day 4 at 5
No. 266 exposure increased to 4.0 in day 4 at 5
No. 288 exposure increased to 1.0 in day 4 at 5
No. 295 exposure increased to 2.0 in day 4 at 5
No. 308 exposure increased to 2.0 in day 4 at 5
No. 321 exposure increased to 2.0 in day 4 at 5
No. 324 exposure increased to 2.0 in day 4 at 5
No. 330 exposure increased to 1.0 in day 4 at 5
No. 340 exposure increased to 1.0 in day 4 at 5
No. 347 exposure increased to 2.0 in day 4 at 5
No. 364 exposure increased to 1.0 in day 4 at 5
No. 370 exposure increased to 1.0 in day 4 at 5
No. 384 exposure increased to 4.0 in day 4 at 5
No. 392 exposure increased to 2.0 in day 4 at 5
No. 400 exposure increased to 2.0 in day 4 at 5
No. 425 exposure increased to 2.0 in day 4 at 5
No. 436 exposure increased to 2.0 in day 4 at 5
No. 444 exposure increased to 2.0 in day 4 at 5
*When No. 447 infected, Exposure is 2.0 in day 4 at move 5
No. 462 exposure increased to 2.0 in day 4 at 5
No. 465 exposure increased to 2.0 in day 4 at 5
No. 480 exposure increased to 2.0 in day 4 at 5
No. 488 exposure increased to 2.0 in day 4 at 5
No. 498 exposure increased to 3.0 in day 4 at 5
No. 499 exposure increased to 2.0 in day 4 at 5
No. 537 exposure increased to 3.0 in day 4 at 5
No. 550 exposure increased to 3.0 in day 4 at 5
No. 553 exposure increased to 1.0 in day 4 at 5
No. 556 exposure increased to 2.0 in day 4 at 5
No. 561 exposure increased to 2.0 in day 4 at 5
No. 567 exposure increased to 3.0 in day 4 at 5
No. 592 exposure increased to 1.0 in day 4 at 5
*When No. 606 infected, Exposure is 2.0 in day 4 at move 5
No. 653 exposure increased to 1.0 in day 4 at 5
No. 654 exposure increased to 2.0 in day 4 at 5
No. 670 exposure increased to 1.0 in day 4 at 5
No. 673 exposure increased to 1.0 in day 4 at 5
No. 682 exposure increased to 4.0 in day 4 at 5
No. 685 exposure increased to 1.0 in day 4 at 5
No. 689 exposure increased to 1.0 in day 4 at 5
No. 690 exposure increased to 1.0 in day 4 at 5
No. 697 exposure increased to 2.0 in day 4 at 5
No. 698 exposure increased to 3.0 in day 4 at 5
No. 712 exposure increased to 2.0 in day 4 at 5
No. 719 exposure increased to 1.0 in day 4 at 5
No. 725 exposure increased to 2.0 in day 4 at 5
No. 726 exposure increased to 2.0 in day 4 at 5
No. 728 exposure increased to 2.0 in day 4 at 5
No. 738 exposure increased to 2.0 in day 4 at 5
No. 757 exposure increased to 1.0 in day 4 at 5
No. 776 exposure increased to 3.0 in day 4 at 5
No. 795 exposure increased to 2.0 in day 4 at 5
No. 833 exposure increased to 1.0 in day 4 at 5
No. 840 exposure increased to 4.0 in day 4 at 5
No. 858 exposure increased to 1.0 in day 4 at 5
No. 904 exposure increased to 2.0 in day 4 at 5
No. 909 exposure increased to 2.0 in day 4 at 5
No. 916 exposure increased to 1.0 in day 4 at 5
No. 919 exposure increased to 3.0 in day 4 at 5
No. 920 exposure increased to 3.0 in day 4 at 5
No. 953 exposure increased to 2.0 in day 4 at 5
No. 955 exposure increased to 2.0 in day 4 at 5
No. 960 exposure increased to 2.0 in day 4 at 5
No. 965 exposure increased to 4.0 in day 4 at 5
No. 983 exposure increased to 1.0 in day 4 at 5
No. 990 exposure increased to 1.0 in day 4 at 5
  144/10000 [..............................] - ETA: 18:14:49 - reward: 689.6534*When No. 28 infected, Exposure is 3.0 in day 4 at move 0
*When No. 384 infected, Exposure is 4.0 in day 4 at move 0
*When No. 392 infected, Exposure is 2.0 in day 4 at move 0
*When No. 436 infected, Exposure is 2.0 in day 4 at move 0
*When No. 498 infected, Exposure is 3.0 in day 4 at move 0
*When No. 795 infected, Exposure is 2.0 in day 4 at move 0
*When No. 955 infected, Exposure is 2.0 in day 4 at move 0
*When No. 79 infected, Exposure is 2.0 in day 4 at move 1
*When No. 400 infected, Exposure is 2.0 in day 4 at move 1
*When No. 682 infected, Exposure is 4.0 in day 4 at move 1
*When No. 725 infected, Exposure is 2.0 in day 4 at move 1
*When No. 909 infected, Exposure is 2.0 in day 4 at move 1
*When No. 919 infected, Exposure is 3.0 in day 4 at move 1
*When No. 115 infected, Exposure is 2.0 in day 4 at move 2
*When No. 347 infected, Exposure is 2.0 in day 4 at move 2
*When No. 444 infected, Exposure is 2.0 in day 4 at move 2
*When No. 537 infected, Exposure is 3.0 in day 4 at move 2
*When No. 561 infected, Exposure is 2.0 in day 4 at move 2
*When No. 965 infected, Exposure is 4.0 in day 4 at move 2
*When No. 66 infected, Exposure is 2.0 in day 4 at move 3
*When No. 321 infected, Exposure is 2.0 in day 4 at move 3
*When No. 567 infected, Exposure is 3.0 in day 4 at move 3
*When No. 776 infected, Exposure is 3.0 in day 4 at move 3
*When No. 840 infected, Exposure is 4.0 in day 4 at move 3
*When No. 904 infected, Exposure is 2.0 in day 4 at move 3
*When No. 465 infected, Exposure is 2.0 in day 4 at move 4
*When No. 480 infected, Exposure is 2.0 in day 4 at move 4
No. 17 exposure increased to 3.0 in day 4 at 5
No. 19 exposure increased to 4.0 in day 4 at 5
No. 30 exposure increased to 3.0 in day 4 at 5
No. 34 exposure increased to 2.0 in day 4 at 5
No. 36 exposure increased to 2.0 in day 4 at 5
No. 44 exposure increased to 2.0 in day 4 at 5
No. 74 exposure increased to 2.0 in day 4 at 5
No. 78 exposure increased to 1.0 in day 4 at 5
No. 81 exposure increased to 1.0 in day 4 at 5
No. 90 exposure increased to 2.0 in day 4 at 5
No. 123 exposure increased to 2.0 in day 4 at 5
No. 143 exposure increased to 1.0 in day 4 at 5
No. 149 exposure increased to 2.0 in day 4 at 5
No. 159 exposure increased to 1.0 in day 4 at 5
No. 161 exposure increased to 2.0 in day 4 at 5
No. 162 exposure increased to 1.0 in day 4 at 5
No. 171 exposure increased to 1.0 in day 4 at 5
No. 178 exposure increased to 1.0 in day 4 at 5
No. 185 exposure increased to 2.0 in day 4 at 5
No. 187 exposure increased to 3.0 in day 4 at 5
No. 194 exposure increased to 1.0 in day 4 at 5
No. 205 exposure increased to 4.0 in day 4 at 5
No. 212 exposure increased to 1.0 in day 4 at 5
No. 219 exposure increased to 2.0 in day 4 at 5
No. 223 exposure increased to 2.0 in day 4 at 5
No. 237 exposure increased to 3.0 in day 4 at 5
*When No. 245 infected, Exposure is 2.0 in day 4 at move 5
No. 259 exposure increased to 1.0 in day 4 at 5
No. 261 exposure increased to 1.0 in day 4 at 5
No. 266 exposure increased to 5.0 in day 4 at 5
No. 274 exposure increased to 1.0 in day 4 at 5
No. 288 exposure increased to 2.0 in day 4 at 5
No. 295 exposure increased to 3.0 in day 4 at 5
No. 308 exposure increased to 3.0 in day 4 at 5
No. 324 exposure increased to 3.0 in day 4 at 5
No. 330 exposure increased to 2.0 in day 4 at 5
No. 332 exposure increased to 1.0 in day 4 at 5
No. 340 exposure increased to 2.0 in day 4 at 5
No. 341 exposure increased to 1.0 in day 4 at 5
No. 344 exposure increased to 1.0 in day 4 at 5
No. 364 exposure increased to 2.0 in day 4 at 5
No. 370 exposure increased to 2.0 in day 4 at 5
No. 403 exposure increased to 2.0 in day 4 at 5
No. 425 exposure increased to 3.0 in day 4 at 5
No. 462 exposure increased to 3.0 in day 4 at 5
No. 488 exposure increased to 3.0 in day 4 at 5
No. 499 exposure increased to 3.0 in day 4 at 5
No. 521 exposure increased to 2.0 in day 4 at 5
No. 544 exposure increased to 2.0 in day 4 at 5
No. 546 exposure increased to 2.0 in day 4 at 5
No. 550 exposure increased to 4.0 in day 4 at 5
No. 553 exposure increased to 2.0 in day 4 at 5
No. 556 exposure increased to 3.0 in day 4 at 5
No. 589 exposure increased to 1.0 in day 4 at 5
No. 592 exposure increased to 2.0 in day 4 at 5
No. 599 exposure increased to 1.0 in day 4 at 5
No. 619 exposure increased to 2.0 in day 4 at 5
No. 653 exposure increased to 2.0 in day 4 at 5
No. 654 exposure increased to 3.0 in day 4 at 5
No. 670 exposure increased to 2.0 in day 4 at 5
No. 673 exposure increased to 2.0 in day 4 at 5
No. 685 exposure increased to 2.0 in day 4 at 5
No. 688 exposure increased to 1.0 in day 4 at 5
No. 689 exposure increased to 2.0 in day 4 at 5
No. 690 exposure increased to 2.0 in day 4 at 5
No. 697 exposure increased to 3.0 in day 4 at 5
No. 698 exposure increased to 4.0 in day 4 at 5
*When No. 712 infected, Exposure is 2.0 in day 4 at move 5
No. 719 exposure increased to 2.0 in day 4 at 5
No. 726 exposure increased to 3.0 in day 4 at 5
No. 728 exposure increased to 3.0 in day 4 at 5
No. 738 exposure increased to 3.0 in day 4 at 5
No. 751 exposure increased to 1.0 in day 4 at 5
No. 754 exposure increased to 1.0 in day 4 at 5
No. 757 exposure increased to 2.0 in day 4 at 5
No. 777 exposure increased to 1.0 in day 4 at 5
No. 798 exposure increased to 1.0 in day 4 at 5
No. 830 exposure increased to 1.0 in day 4 at 5
No. 833 exposure increased to 2.0 in day 4 at 5
No. 845 exposure increased to 1.0 in day 4 at 5
No. 857 exposure increased to 1.0 in day 4 at 5
No. 858 exposure increased to 2.0 in day 4 at 5
No. 871 exposure increased to 1.0 in day 4 at 5
No. 906 exposure increased to 1.0 in day 4 at 5
No. 916 exposure increased to 2.0 in day 4 at 5
No. 920 exposure increased to 4.0 in day 4 at 5
No. 953 exposure increased to 3.0 in day 4 at 5
No. 960 exposure increased to 3.0 in day 4 at 5
No. 972 exposure increased to 1.0 in day 4 at 5
No. 983 exposure increased to 2.0 in day 4 at 5
No. 990 exposure increased to 2.0 in day 4 at 5
No. 992 exposure increased to 2.0 in day 4 at 5
  145/10000 [..............................] - ETA: 18:14:17 - reward: 687.6646*When No. 17 infected, Exposure is 3.0 in day 4 at move 0
*When No. 30 infected, Exposure is 3.0 in day 4 at move 0
*When No. 187 infected, Exposure is 3.0 in day 4 at move 0
*When No. 550 infected, Exposure is 4.0 in day 4 at move 0
*When No. 619 infected, Exposure is 2.0 in day 4 at move 0
*When No. 719 infected, Exposure is 2.0 in day 4 at move 0
*When No. 757 infected, Exposure is 2.0 in day 4 at move 0
*When No. 19 infected, Exposure is 4.0 in day 4 at move 1
No. 34 exposure increased to 3.0 in day 4 at 1
No. 36 exposure increased to 3.0 in day 4 at 1
No. 44 exposure increased to 3.0 in day 4 at 1
No. 74 exposure increased to 3.0 in day 4 at 1
No. 76 exposure increased to 1.0 in day 4 at 1
No. 78 exposure increased to 2.0 in day 4 at 1
No. 81 exposure increased to 2.0 in day 4 at 1
No. 90 exposure increased to 3.0 in day 4 at 1
No. 123 exposure increased to 3.0 in day 4 at 1
No. 129 exposure increased to 2.0 in day 4 at 1
No. 143 exposure increased to 2.0 in day 4 at 1
No. 149 exposure increased to 3.0 in day 4 at 1
No. 159 exposure increased to 2.0 in day 4 at 1
No. 161 exposure increased to 3.0 in day 4 at 1
No. 162 exposure increased to 2.0 in day 4 at 1
No. 171 exposure increased to 2.0 in day 4 at 1
No. 178 exposure increased to 2.0 in day 4 at 1
No. 185 exposure increased to 3.0 in day 4 at 1
No. 194 exposure increased to 2.0 in day 4 at 1
*When No. 205 infected, Exposure is 4.0 in day 4 at move 1
No. 212 exposure increased to 2.0 in day 4 at 1
No. 219 exposure increased to 3.0 in day 4 at 1
No. 223 exposure increased to 3.0 in day 4 at 1
No. 235 exposure increased to 2.0 in day 4 at 1
No. 237 exposure increased to 4.0 in day 4 at 1
No. 259 exposure increased to 2.0 in day 4 at 1
No. 261 exposure increased to 2.0 in day 4 at 1
No. 266 exposure increased to 6.0 in day 4 at 1
No. 274 exposure increased to 2.0 in day 4 at 1
No. 288 exposure increased to 3.0 in day 4 at 1
*When No. 295 infected, Exposure is 3.0 in day 4 at move 1
No. 308 exposure increased to 4.0 in day 4 at 1
No. 320 exposure increased to 2.0 in day 4 at 1
No. 324 exposure increased to 4.0 in day 4 at 1
No. 330 exposure increased to 3.0 in day 4 at 1
No. 332 exposure increased to 2.0 in day 4 at 1
No. 335 exposure increased to 2.0 in day 4 at 1
No. 340 exposure increased to 3.0 in day 4 at 1
No. 341 exposure increased to 2.0 in day 4 at 1
No. 344 exposure increased to 2.0 in day 4 at 1
No. 364 exposure increased to 3.0 in day 4 at 1
No. 370 exposure increased to 3.0 in day 4 at 1
No. 390 exposure increased to 1.0 in day 4 at 1
No. 403 exposure increased to 3.0 in day 4 at 1
No. 425 exposure increased to 4.0 in day 4 at 1
No. 442 exposure increased to 1.0 in day 4 at 1
No. 462 exposure increased to 4.0 in day 4 at 1
No. 488 exposure increased to 4.0 in day 4 at 1
No. 499 exposure increased to 4.0 in day 4 at 1
No. 521 exposure increased to 3.0 in day 4 at 1
No. 544 exposure increased to 3.0 in day 4 at 1
No. 546 exposure increased to 3.0 in day 4 at 1
No. 553 exposure increased to 3.0 in day 4 at 1
No. 556 exposure increased to 4.0 in day 4 at 1
No. 589 exposure increased to 2.0 in day 4 at 1
No. 592 exposure increased to 3.0 in day 4 at 1
No. 599 exposure increased to 2.0 in day 4 at 1
No. 613 exposure increased to 2.0 in day 4 at 1
No. 653 exposure increased to 3.0 in day 4 at 1
*When No. 654 infected, Exposure is 3.0 in day 4 at move 1
No. 663 exposure increased to 1.0 in day 4 at 1
No. 669 exposure increased to 2.0 in day 4 at 1
No. 670 exposure increased to 3.0 in day 4 at 1
No. 673 exposure increased to 3.0 in day 4 at 1
No. 685 exposure increased to 3.0 in day 4 at 1
No. 688 exposure increased to 2.0 in day 4 at 1
No. 689 exposure increased to 3.0 in day 4 at 1
No. 690 exposure increased to 3.0 in day 4 at 1
No. 697 exposure increased to 4.0 in day 4 at 1
No. 698 exposure increased to 5.0 in day 4 at 1
No. 710 exposure increased to 1.0 in day 4 at 1
No. 726 exposure increased to 4.0 in day 4 at 1
*When No. 728 infected, Exposure is 3.0 in day 4 at move 1
No. 738 exposure increased to 4.0 in day 4 at 1
No. 751 exposure increased to 2.0 in day 4 at 1
No. 754 exposure increased to 2.0 in day 4 at 1
No. 777 exposure increased to 2.0 in day 4 at 1
No. 798 exposure increased to 2.0 in day 4 at 1
No. 830 exposure increased to 2.0 in day 4 at 1
No. 833 exposure increased to 3.0 in day 4 at 1
No. 845 exposure increased to 2.0 in day 4 at 1
No. 857 exposure increased to 2.0 in day 4 at 1
No. 858 exposure increased to 3.0 in day 4 at 1
No. 871 exposure increased to 2.0 in day 4 at 1
No. 906 exposure increased to 2.0 in day 4 at 1
No. 916 exposure increased to 3.0 in day 4 at 1
No. 920 exposure increased to 5.0 in day 4 at 1
No. 953 exposure increased to 4.0 in day 4 at 1
No. 960 exposure increased to 4.0 in day 4 at 1
No. 972 exposure increased to 2.0 in day 4 at 1
No. 983 exposure increased to 3.0 in day 4 at 1
*When No. 990 infected, Exposure is 2.0 in day 4 at move 1
No. 992 exposure increased to 3.0 in day 4 at 1
  146/10000 [..............................] - ETA: 18:10:47 - reward: 686.0805*When No. 36 infected, Exposure is 3.0 in day 4 at move 0
*When No. 129 infected, Exposure is 2.0 in day 4 at move 0
*When No. 143 infected, Exposure is 2.0 in day 4 at move 0
*When No. 178 infected, Exposure is 2.0 in day 4 at move 0
*When No. 194 infected, Exposure is 2.0 in day 4 at move 0
*When No. 212 infected, Exposure is 2.0 in day 4 at move 0
*When No. 266 infected, Exposure is 6.0 in day 4 at move 0
*When No. 332 infected, Exposure is 2.0 in day 4 at move 0
*When No. 344 infected, Exposure is 2.0 in day 4 at move 0
*When No. 462 infected, Exposure is 4.0 in day 4 at move 0
*When No. 499 infected, Exposure is 4.0 in day 4 at move 0
*When No. 653 infected, Exposure is 3.0 in day 4 at move 0
*When No. 690 infected, Exposure is 3.0 in day 4 at move 0
*When No. 697 infected, Exposure is 4.0 in day 4 at move 0
*When No. 726 infected, Exposure is 4.0 in day 4 at move 0
*When No. 830 infected, Exposure is 2.0 in day 4 at move 0
*When No. 858 infected, Exposure is 3.0 in day 4 at move 0
*When No. 916 infected, Exposure is 3.0 in day 4 at move 0
*When No. 992 infected, Exposure is 3.0 in day 4 at move 0
No. 34 exposure increased to 4.0 in day 4 at 1
No. 44 exposure increased to 4.0 in day 4 at 1
No. 74 exposure increased to 4.0 in day 4 at 1
No. 76 exposure increased to 2.0 in day 4 at 1
No. 78 exposure increased to 3.0 in day 4 at 1
*When No. 81 infected, Exposure is 2.0 in day 4 at move 1
*When No. 90 infected, Exposure is 3.0 in day 4 at move 1
No. 95 exposure increased to 1.0 in day 4 at 1
No. 119 exposure increased to 1.0 in day 4 at 1
No. 123 exposure increased to 4.0 in day 4 at 1
No. 149 exposure increased to 4.0 in day 4 at 1
No. 159 exposure increased to 3.0 in day 4 at 1
No. 161 exposure increased to 4.0 in day 4 at 1
No. 162 exposure increased to 3.0 in day 4 at 1
No. 171 exposure increased to 3.0 in day 4 at 1
No. 185 exposure increased to 4.0 in day 4 at 1
No. 219 exposure increased to 4.0 in day 4 at 1
*When No. 223 infected, Exposure is 3.0 in day 4 at move 1
No. 235 exposure increased to 3.0 in day 4 at 1
No. 237 exposure increased to 5.0 in day 4 at 1
No. 259 exposure increased to 3.0 in day 4 at 1
No. 261 exposure increased to 3.0 in day 4 at 1
No. 274 exposure increased to 3.0 in day 4 at 1
No. 288 exposure increased to 4.0 in day 4 at 1
No. 308 exposure increased to 5.0 in day 4 at 1
No. 320 exposure increased to 3.0 in day 4 at 1
No. 324 exposure increased to 5.0 in day 4 at 1
*When No. 330 infected, Exposure is 3.0 in day 4 at move 1
No. 335 exposure increased to 3.0 in day 4 at 1
No. 340 exposure increased to 4.0 in day 4 at 1
No. 341 exposure increased to 3.0 in day 4 at 1
No. 364 exposure increased to 4.0 in day 4 at 1
*When No. 370 infected, Exposure is 3.0 in day 4 at move 1
No. 390 exposure increased to 2.0 in day 4 at 1
No. 403 exposure increased to 4.0 in day 4 at 1
No. 425 exposure increased to 5.0 in day 4 at 1
No. 442 exposure increased to 2.0 in day 4 at 1
No. 488 exposure increased to 5.0 in day 4 at 1
No. 496 exposure increased to 1.0 in day 4 at 1
No. 521 exposure increased to 4.0 in day 4 at 1
No. 544 exposure increased to 4.0 in day 4 at 1
*When No. 546 infected, Exposure is 3.0 in day 4 at move 1
No. 553 exposure increased to 4.0 in day 4 at 1
No. 556 exposure increased to 5.0 in day 4 at 1
No. 589 exposure increased to 3.0 in day 4 at 1
No. 592 exposure increased to 4.0 in day 4 at 1
No. 599 exposure increased to 3.0 in day 4 at 1
No. 613 exposure increased to 3.0 in day 4 at 1
No. 625 exposure increased to 2.0 in day 4 at 1
No. 663 exposure increased to 2.0 in day 4 at 1
No. 669 exposure increased to 3.0 in day 4 at 1
No. 670 exposure increased to 4.0 in day 4 at 1
No. 673 exposure increased to 4.0 in day 4 at 1
*When No. 685 infected, Exposure is 3.0 in day 4 at move 1
No. 688 exposure increased to 3.0 in day 4 at 1
*When No. 689 infected, Exposure is 3.0 in day 4 at move 1
No. 694 exposure increased to 2.0 in day 4 at 1
No. 698 exposure increased to 6.0 in day 4 at 1
No. 710 exposure increased to 2.0 in day 4 at 1
No. 738 exposure increased to 5.0 in day 4 at 1
No. 751 exposure increased to 3.0 in day 4 at 1
No. 752 exposure increased to 2.0 in day 4 at 1
No. 754 exposure increased to 3.0 in day 4 at 1
No. 759 exposure increased to 1.0 in day 4 at 1
*When No. 777 infected, Exposure is 2.0 in day 4 at move 1
No. 798 exposure increased to 3.0 in day 4 at 1
No. 833 exposure increased to 4.0 in day 4 at 1
No. 845 exposure increased to 3.0 in day 4 at 1
No. 857 exposure increased to 3.0 in day 4 at 1
*When No. 871 infected, Exposure is 2.0 in day 4 at move 1
No. 906 exposure increased to 3.0 in day 4 at 1
No. 920 exposure increased to 6.0 in day 4 at 1
No. 953 exposure increased to 5.0 in day 4 at 1
*When No. 960 infected, Exposure is 4.0 in day 4 at move 1
No. 972 exposure increased to 3.0 in day 4 at 1
No. 983 exposure increased to 4.0 in day 4 at 1
  147/10000 [..............................] - ETA: 18:08:19 - reward: 683.9646*When No. 34 infected, Exposure is 4.0 in day 4 at move 0
*When No. 149 infected, Exposure is 4.0 in day 4 at move 0
*When No. 171 infected, Exposure is 3.0 in day 4 at move 0
*When No. 274 infected, Exposure is 3.0 in day 4 at move 0
*When No. 324 infected, Exposure is 5.0 in day 4 at move 0
*When No. 335 infected, Exposure is 3.0 in day 4 at move 0
*When No. 553 infected, Exposure is 4.0 in day 4 at move 0
*When No. 589 infected, Exposure is 3.0 in day 4 at move 0
*When No. 673 infected, Exposure is 4.0 in day 4 at move 0
*When No. 698 infected, Exposure is 6.0 in day 4 at move 0
*When No. 738 infected, Exposure is 5.0 in day 4 at move 0
*When No. 754 infected, Exposure is 3.0 in day 4 at move 0
*When No. 833 infected, Exposure is 4.0 in day 4 at move 0
*When No. 920 infected, Exposure is 6.0 in day 4 at move 0
*When No. 972 infected, Exposure is 3.0 in day 4 at move 0
No. 44 exposure increased to 5.0 in day 4 at 1
No. 74 exposure increased to 5.0 in day 4 at 1
No. 76 exposure increased to 3.0 in day 4 at 1
No. 78 exposure increased to 4.0 in day 4 at 1
No. 95 exposure increased to 2.0 in day 4 at 1
No. 119 exposure increased to 2.0 in day 4 at 1
No. 123 exposure increased to 5.0 in day 4 at 1
No. 159 exposure increased to 4.0 in day 4 at 1
No. 161 exposure increased to 5.0 in day 4 at 1
No. 162 exposure increased to 4.0 in day 4 at 1
*When No. 185 infected, Exposure is 4.0 in day 4 at move 1
No. 219 exposure increased to 5.0 in day 4 at 1
No. 235 exposure increased to 4.0 in day 4 at 1
No. 237 exposure increased to 6.0 in day 4 at 1
No. 241 exposure increased to 2.0 in day 4 at 1
No. 250 exposure increased to 2.0 in day 4 at 1
No. 259 exposure increased to 4.0 in day 4 at 1
No. 261 exposure increased to 4.0 in day 4 at 1
No. 288 exposure increased to 5.0 in day 4 at 1
*When No. 308 infected, Exposure is 5.0 in day 4 at move 1
No. 320 exposure increased to 4.0 in day 4 at 1
No. 340 exposure increased to 5.0 in day 4 at 1
No. 341 exposure increased to 4.0 in day 4 at 1
No. 364 exposure increased to 5.0 in day 4 at 1
No. 390 exposure increased to 3.0 in day 4 at 1
No. 399 exposure increased to 1.0 in day 4 at 1
*When No. 403 infected, Exposure is 4.0 in day 4 at move 1
*When No. 425 infected, Exposure is 5.0 in day 4 at move 1
No. 442 exposure increased to 3.0 in day 4 at 1
No. 488 exposure increased to 6.0 in day 4 at 1
No. 496 exposure increased to 2.0 in day 4 at 1
No. 517 exposure increased to 2.0 in day 4 at 1
*When No. 521 infected, Exposure is 4.0 in day 4 at move 1
No. 525 exposure increased to 1.0 in day 4 at 1
No. 544 exposure increased to 5.0 in day 4 at 1
*When No. 556 infected, Exposure is 5.0 in day 4 at move 1
No. 568 exposure increased to 1.0 in day 4 at 1
No. 574 exposure increased to 1.0 in day 4 at 1
No. 592 exposure increased to 5.0 in day 4 at 1
No. 599 exposure increased to 4.0 in day 4 at 1
No. 613 exposure increased to 4.0 in day 4 at 1
No. 616 exposure increased to 2.0 in day 4 at 1
No. 625 exposure increased to 3.0 in day 4 at 1
No. 632 exposure increased to 2.0 in day 4 at 1
*When No. 663 infected, Exposure is 2.0 in day 4 at move 1
No. 669 exposure increased to 4.0 in day 4 at 1
*When No. 670 infected, Exposure is 4.0 in day 4 at move 1
No. 688 exposure increased to 4.0 in day 4 at 1
No. 694 exposure increased to 3.0 in day 4 at 1
No. 710 exposure increased to 3.0 in day 4 at 1
No. 751 exposure increased to 4.0 in day 4 at 1
No. 752 exposure increased to 3.0 in day 4 at 1
No. 759 exposure increased to 2.0 in day 4 at 1
No. 786 exposure increased to 2.0 in day 4 at 1
No. 798 exposure increased to 4.0 in day 4 at 1
*When No. 845 infected, Exposure is 3.0 in day 4 at move 1
No. 851 exposure increased to 2.0 in day 4 at 1
No. 857 exposure increased to 4.0 in day 4 at 1
No. 881 exposure increased to 1.0 in day 4 at 1
No. 906 exposure increased to 4.0 in day 4 at 1
No. 932 exposure increased to 1.0 in day 4 at 1
No. 953 exposure increased to 6.0 in day 4 at 1
*When No. 983 infected, Exposure is 4.0 in day 4 at move 1
  148/10000 [..............................] - ETA: 18:04:05 - reward: 682.2084*When No. 74 infected, Exposure is 5.0 in day 4 at move 0
*When No. 78 infected, Exposure is 4.0 in day 4 at move 0
*When No. 123 infected, Exposure is 5.0 in day 4 at move 0
*When No. 159 infected, Exposure is 4.0 in day 4 at move 0
*When No. 162 infected, Exposure is 4.0 in day 4 at move 0
*When No. 219 infected, Exposure is 5.0 in day 4 at move 0
*When No. 259 infected, Exposure is 4.0 in day 4 at move 0
*When No. 261 infected, Exposure is 4.0 in day 4 at move 0
*When No. 288 infected, Exposure is 5.0 in day 4 at move 0
*When No. 341 infected, Exposure is 4.0 in day 4 at move 0
*When No. 364 infected, Exposure is 5.0 in day 4 at move 0
*When No. 688 infected, Exposure is 4.0 in day 4 at move 0
*When No. 710 infected, Exposure is 3.0 in day 4 at move 0
*When No. 751 infected, Exposure is 4.0 in day 4 at move 0
*When No. 857 infected, Exposure is 4.0 in day 4 at move 0
*When No. 953 infected, Exposure is 6.0 in day 4 at move 0
*When No. 390 infected, Exposure is 3.0 in day 4 at move 1
*When No. 488 infected, Exposure is 6.0 in day 4 at move 1
*When No. 599 infected, Exposure is 4.0 in day 4 at move 1
*When No. 625 infected, Exposure is 3.0 in day 4 at move 1
*When No. 798 infected, Exposure is 4.0 in day 4 at move 1
*When No. 76 infected, Exposure is 3.0 in day 4 at move 2
*When No. 95 infected, Exposure is 2.0 in day 4 at move 2
*When No. 119 infected, Exposure is 2.0 in day 4 at move 2
*When No. 161 infected, Exposure is 5.0 in day 4 at move 2
*When No. 237 infected, Exposure is 6.0 in day 4 at move 2
*When No. 496 infected, Exposure is 2.0 in day 4 at move 2
*When No. 544 infected, Exposure is 5.0 in day 4 at move 2
*When No. 669 infected, Exposure is 4.0 in day 4 at move 2
*When No. 694 infected, Exposure is 3.0 in day 4 at move 2
*When No. 250 infected, Exposure is 2.0 in day 4 at move 3
*When No. 320 infected, Exposure is 4.0 in day 4 at move 3
*When No. 340 infected, Exposure is 5.0 in day 4 at move 3
*When No. 235 infected, Exposure is 4.0 in day 4 at move 4
*When No. 906 infected, Exposure is 4.0 in day 4 at move 4
No. 44 exposure increased to 6.0 in day 4 at 5
No. 49 exposure increased to 1.0 in day 4 at 5
No. 80 exposure increased to 2.0 in day 4 at 5
No. 86 exposure increased to 1.0 in day 4 at 5
No. 111 exposure increased to 1.0 in day 4 at 5
No. 121 exposure increased to 1.0 in day 4 at 5
No. 138 exposure increased to 1.0 in day 4 at 5
No. 153 exposure increased to 1.0 in day 4 at 5
No. 177 exposure increased to 2.0 in day 4 at 5
No. 198 exposure increased to 1.0 in day 4 at 5
No. 241 exposure increased to 3.0 in day 4 at 5
No. 275 exposure increased to 1.0 in day 4 at 5
No. 286 exposure increased to 1.0 in day 4 at 5
No. 380 exposure increased to 2.0 in day 4 at 5
No. 399 exposure increased to 2.0 in day 4 at 5
No. 410 exposure increased to 2.0 in day 4 at 5
*When No. 442 infected, Exposure is 3.0 in day 4 at move 5
No. 460 exposure increased to 1.0 in day 4 at 5
No. 479 exposure increased to 1.0 in day 4 at 5
No. 517 exposure increased to 3.0 in day 4 at 5
No. 525 exposure increased to 2.0 in day 4 at 5
No. 538 exposure increased to 1.0 in day 4 at 5
No. 545 exposure increased to 1.0 in day 4 at 5
No. 568 exposure increased to 2.0 in day 4 at 5
No. 574 exposure increased to 2.0 in day 4 at 5
No. 592 exposure increased to 6.0 in day 4 at 5
No. 613 exposure increased to 5.0 in day 4 at 5
No. 616 exposure increased to 3.0 in day 4 at 5
No. 617 exposure increased to 1.0 in day 4 at 5
No. 632 exposure increased to 3.0 in day 4 at 5
No. 636 exposure increased to 1.0 in day 4 at 5
No. 711 exposure increased to 1.0 in day 4 at 5
No. 729 exposure increased to 1.0 in day 4 at 5
No. 752 exposure increased to 4.0 in day 4 at 5
No. 758 exposure increased to 1.0 in day 4 at 5
No. 759 exposure increased to 3.0 in day 4 at 5
No. 786 exposure increased to 3.0 in day 4 at 5
*When No. 851 infected, Exposure is 2.0 in day 4 at move 5
No. 881 exposure increased to 2.0 in day 4 at 5
No. 932 exposure increased to 2.0 in day 4 at 5
No. 939 exposure increased to 1.0 in day 4 at 5
  149/10000 [..............................] - ETA: 18:04:07 - reward: 680.3168*When No. 44 infected, Exposure is 6.0 in day 4 at move 0
*When No. 525 infected, Exposure is 2.0 in day 4 at move 0
*When No. 592 infected, Exposure is 6.0 in day 4 at move 0
*When No. 613 infected, Exposure is 5.0 in day 4 at move 0
*When No. 786 infected, Exposure is 3.0 in day 4 at move 0
*When No. 932 infected, Exposure is 2.0 in day 4 at move 0
No. 21 exposure increased to 2.0 in day 4 at 1
No. 35 exposure increased to 2.0 in day 4 at 1
No. 49 exposure increased to 2.0 in day 4 at 1
No. 58 exposure increased to 1.0 in day 4 at 1
No. 80 exposure increased to 3.0 in day 4 at 1
No. 86 exposure increased to 2.0 in day 4 at 1
No. 111 exposure increased to 2.0 in day 4 at 1
No. 121 exposure increased to 2.0 in day 4 at 1
No. 138 exposure increased to 2.0 in day 4 at 1
No. 153 exposure increased to 2.0 in day 4 at 1
*When No. 177 infected, Exposure is 2.0 in day 4 at move 1
No. 198 exposure increased to 2.0 in day 4 at 1
No. 204 exposure increased to 1.0 in day 4 at 1
No. 241 exposure increased to 4.0 in day 4 at 1
No. 275 exposure increased to 2.0 in day 4 at 1
No. 286 exposure increased to 2.0 in day 4 at 1
No. 298 exposure increased to 2.0 in day 4 at 1
No. 369 exposure increased to 1.0 in day 4 at 1
No. 380 exposure increased to 3.0 in day 4 at 1
No. 399 exposure increased to 3.0 in day 4 at 1
No. 410 exposure increased to 3.0 in day 4 at 1
No. 460 exposure increased to 2.0 in day 4 at 1
No. 479 exposure increased to 2.0 in day 4 at 1
No. 517 exposure increased to 4.0 in day 4 at 1
No. 538 exposure increased to 2.0 in day 4 at 1
No. 545 exposure increased to 2.0 in day 4 at 1
No. 568 exposure increased to 3.0 in day 4 at 1
No. 574 exposure increased to 3.0 in day 4 at 1
*When No. 616 infected, Exposure is 3.0 in day 4 at move 1
No. 617 exposure increased to 2.0 in day 4 at 1
No. 632 exposure increased to 4.0 in day 4 at 1
No. 636 exposure increased to 2.0 in day 4 at 1
No. 711 exposure increased to 2.0 in day 4 at 1
No. 729 exposure increased to 2.0 in day 4 at 1
No. 752 exposure increased to 5.0 in day 4 at 1
No. 758 exposure increased to 2.0 in day 4 at 1
No. 759 exposure increased to 4.0 in day 4 at 1
No. 829 exposure increased to 2.0 in day 4 at 1
No. 881 exposure increased to 3.0 in day 4 at 1
No. 939 exposure increased to 2.0 in day 4 at 1
  150/10000 [..............................] - ETA: 18:00:51 - reward: 678.7707*When No. 80 infected, Exposure is 3.0 in day 4 at move 0
*When No. 298 infected, Exposure is 2.0 in day 4 at move 0
*When No. 399 infected, Exposure is 3.0 in day 4 at move 0
*When No. 460 infected, Exposure is 2.0 in day 4 at move 0
*When No. 632 infected, Exposure is 4.0 in day 4 at move 0
*When No. 752 infected, Exposure is 5.0 in day 4 at move 0
*When No. 35 infected, Exposure is 2.0 in day 4 at move 1
*When No. 153 infected, Exposure is 2.0 in day 4 at move 1
*When No. 410 infected, Exposure is 3.0 in day 4 at move 1
*When No. 574 infected, Exposure is 3.0 in day 4 at move 1
*When No. 138 infected, Exposure is 2.0 in day 4 at move 2
*When No. 286 infected, Exposure is 2.0 in day 4 at move 2
*When No. 49 infected, Exposure is 2.0 in day 4 at move 3
*When No. 380 infected, Exposure is 3.0 in day 4 at move 3
*When No. 517 infected, Exposure is 4.0 in day 4 at move 3
*When No. 829 infected, Exposure is 2.0 in day 4 at move 3
*When No. 241 infected, Exposure is 4.0 in day 4 at move 4
*When No. 759 infected, Exposure is 4.0 in day 4 at move 4
No. 16 exposure increased to 2.0 in day 4 at 5
No. 21 exposure increased to 3.0 in day 4 at 5
No. 58 exposure increased to 2.0 in day 4 at 5
No. 61 exposure increased to 1.0 in day 4 at 5
*When No. 86 infected, Exposure is 2.0 in day 4 at move 5
No. 111 exposure increased to 3.0 in day 4 at 5
No. 113 exposure increased to 1.0 in day 4 at 5
No. 121 exposure increased to 3.0 in day 4 at 5
No. 190 exposure increased to 1.0 in day 4 at 5
No. 198 exposure increased to 3.0 in day 4 at 5
No. 204 exposure increased to 2.0 in day 4 at 5
No. 230 exposure increased to 1.0 in day 4 at 5
No. 246 exposure increased to 1.0 in day 4 at 5
No. 275 exposure increased to 3.0 in day 4 at 5
No. 327 exposure increased to 1.0 in day 4 at 5
No. 369 exposure increased to 2.0 in day 4 at 5
No. 431 exposure increased to 1.0 in day 4 at 5
No. 479 exposure increased to 3.0 in day 4 at 5
No. 482 exposure increased to 1.0 in day 4 at 5
No. 484 exposure increased to 1.0 in day 4 at 5
No. 538 exposure increased to 3.0 in day 4 at 5
No. 545 exposure increased to 3.0 in day 4 at 5
No. 568 exposure increased to 4.0 in day 4 at 5
No. 617 exposure increased to 3.0 in day 4 at 5
No. 636 exposure increased to 3.0 in day 4 at 5
No. 711 exposure increased to 3.0 in day 4 at 5
No. 729 exposure increased to 3.0 in day 4 at 5
No. 758 exposure increased to 3.0 in day 4 at 5
No. 799 exposure increased to 2.0 in day 4 at 5
No. 881 exposure increased to 4.0 in day 4 at 5
No. 939 exposure increased to 3.0 in day 4 at 5
No. 958 exposure increased to 1.0 in day 4 at 5
No. 976 exposure increased to 1.0 in day 4 at 5
No. 978 exposure increased to 1.0 in day 4 at 5
  151/10000 [..............................] - ETA: 18:00:00 - reward: 677.2000*When No. 198 infected, Exposure is 3.0 in day 4 at move 0
*When No. 275 infected, Exposure is 3.0 in day 4 at move 0
*When No. 538 infected, Exposure is 3.0 in day 4 at move 0
*When No. 568 infected, Exposure is 4.0 in day 4 at move 1
*When No. 617 infected, Exposure is 3.0 in day 4 at move 1
*When No. 729 infected, Exposure is 3.0 in day 4 at move 1
*When No. 479 infected, Exposure is 3.0 in day 4 at move 2
*When No. 636 infected, Exposure is 3.0 in day 4 at move 2
*When No. 711 infected, Exposure is 3.0 in day 4 at move 2
*When No. 16 infected, Exposure is 2.0 in day 4 at move 3
*When No. 799 infected, Exposure is 2.0 in day 4 at move 3
*When No. 881 infected, Exposure is 4.0 in day 4 at move 3
*When No. 121 infected, Exposure is 3.0 in day 4 at move 4
*When No. 545 infected, Exposure is 3.0 in day 4 at move 4
*When No. 939 infected, Exposure is 3.0 in day 4 at move 4
No. 21 exposure increased to 4.0 in day 4 at 5
No. 58 exposure increased to 3.0 in day 4 at 5
No. 61 exposure increased to 2.0 in day 4 at 5
No. 85 exposure increased to 1.0 in day 4 at 5
*When No. 111 infected, Exposure is 3.0 in day 4 at move 5
No. 113 exposure increased to 2.0 in day 4 at 5
No. 190 exposure increased to 2.0 in day 4 at 5
No. 204 exposure increased to 3.0 in day 4 at 5
No. 230 exposure increased to 2.0 in day 4 at 5
No. 243 exposure increased to 1.0 in day 4 at 5
No. 246 exposure increased to 2.0 in day 4 at 5
No. 327 exposure increased to 2.0 in day 4 at 5
*When No. 369 infected, Exposure is 2.0 in day 4 at move 5
No. 431 exposure increased to 2.0 in day 4 at 5
No. 475 exposure increased to 2.0 in day 4 at 5
No. 482 exposure increased to 2.0 in day 4 at 5
No. 484 exposure increased to 2.0 in day 4 at 5
No. 569 exposure increased to 1.0 in day 4 at 5
No. 686 exposure increased to 1.0 in day 4 at 5
No. 702 exposure increased to 1.0 in day 4 at 5
No. 758 exposure increased to 4.0 in day 4 at 5
No. 956 exposure increased to 1.0 in day 4 at 5
No. 958 exposure increased to 2.0 in day 4 at 5
No. 959 exposure increased to 1.0 in day 4 at 5
No. 976 exposure increased to 2.0 in day 4 at 5
No. 978 exposure increased to 2.0 in day 4 at 5
  152/10000 [..............................] - ETA: 17:57:40 - reward: 675.9421*When No. 21 infected, Exposure is 4.0 in day 4 at move 0
*When No. 61 infected, Exposure is 2.0 in day 4 at move 0
*When No. 204 infected, Exposure is 3.0 in day 4 at move 0
*When No. 758 infected, Exposure is 4.0 in day 4 at move 0
*When No. 958 infected, Exposure is 2.0 in day 4 at move 0
*When No. 190 infected, Exposure is 2.0 in day 4 at move 1
*When No. 327 infected, Exposure is 2.0 in day 4 at move 2
*When No. 58 infected, Exposure is 3.0 in day 4 at move 3
*When No. 246 infected, Exposure is 2.0 in day 4 at move 3
*When No. 230 infected, Exposure is 2.0 in day 4 at move 4
No. 85 exposure increased to 2.0 in day 4 at 5
No. 113 exposure increased to 3.0 in day 4 at 5
No. 243 exposure increased to 2.0 in day 4 at 5
No. 278 exposure increased to 2.0 in day 4 at 5
*When No. 431 infected, Exposure is 2.0 in day 4 at move 5
No. 475 exposure increased to 3.0 in day 4 at 5
No. 482 exposure increased to 3.0 in day 4 at 5
*When No. 484 infected, Exposure is 2.0 in day 4 at move 5
No. 569 exposure increased to 2.0 in day 4 at 5
No. 635 exposure increased to 1.0 in day 4 at 5
No. 686 exposure increased to 2.0 in day 4 at 5
No. 702 exposure increased to 2.0 in day 4 at 5
No. 724 exposure increased to 1.0 in day 4 at 5
No. 941 exposure increased to 1.0 in day 4 at 5
No. 956 exposure increased to 2.0 in day 4 at 5
No. 959 exposure increased to 2.0 in day 4 at 5
No. 976 exposure increased to 3.0 in day 4 at 5
No. 978 exposure increased to 3.0 in day 4 at 5
  153/10000 [..............................] - ETA: 17:54:44 - reward: 674.3105*When No. 956 infected, Exposure is 2.0 in day 4 at move 0
*When No. 959 infected, Exposure is 2.0 in day 4 at move 0
*When No. 976 infected, Exposure is 3.0 in day 4 at move 1
*When No. 482 infected, Exposure is 3.0 in day 4 at move 2
*When No. 278 infected, Exposure is 2.0 in day 4 at move 3
*When No. 475 infected, Exposure is 3.0 in day 4 at move 4
No. 85 exposure increased to 3.0 in day 4 at 5
*When No. 113 infected, Exposure is 3.0 in day 4 at move 5
No. 128 exposure increased to 2.0 in day 4 at 5
No. 243 exposure increased to 3.0 in day 4 at 5
No. 418 exposure increased to 1.0 in day 4 at 5
No. 569 exposure increased to 3.0 in day 4 at 5
No. 635 exposure increased to 2.0 in day 4 at 5
No. 686 exposure increased to 3.0 in day 4 at 5
No. 702 exposure increased to 3.0 in day 4 at 5
No. 724 exposure increased to 2.0 in day 4 at 5
No. 941 exposure increased to 2.0 in day 4 at 5
*When No. 978 infected, Exposure is 3.0 in day 4 at move 5
  154/10000 [..............................] - ETA: 17:50:43 - reward: 672.5406*When No. 243 infected, Exposure is 3.0 in day 4 at move 0
*When No. 569 infected, Exposure is 3.0 in day 4 at move 0
*When No. 85 infected, Exposure is 3.0 in day 4 at move 1
No. 128 exposure increased to 3.0 in day 4 at 1
No. 240 exposure increased to 2.0 in day 4 at 1
No. 418 exposure increased to 2.0 in day 4 at 1
No. 635 exposure increased to 3.0 in day 4 at 1
No. 686 exposure increased to 4.0 in day 4 at 1
*When No. 702 infected, Exposure is 3.0 in day 4 at move 1
No. 724 exposure increased to 3.0 in day 4 at 1
No. 783 exposure increased to 2.0 in day 4 at 1
No. 941 exposure increased to 3.0 in day 4 at 1
  155/10000 [..............................] - ETA: 17:44:57 - reward: 671.0137*When No. 128 infected, Exposure is 3.0 in day 4 at move 1
*When No. 686 infected, Exposure is 4.0 in day 4 at move 1
*When No. 418 infected, Exposure is 2.0 in day 4 at move 2
*When No. 941 infected, Exposure is 3.0 in day 4 at move 2
No. 240 exposure increased to 3.0 in day 4 at 5
No. 405 exposure increased to 1.0 in day 4 at 5
No. 635 exposure increased to 4.0 in day 4 at 5
No. 724 exposure increased to 4.0 in day 4 at 5
No. 783 exposure increased to 3.0 in day 4 at 5
  156/10000 [..............................] - ETA: 17:41:41 - reward: 670.0984*When No. 783 infected, Exposure is 3.0 in day 4 at move 0
No. 240 exposure increased to 4.0 in day 4 at 1
No. 405 exposure increased to 2.0 in day 4 at 1
*When No. 635 infected, Exposure is 4.0 in day 4 at move 1
*When No. 724 infected, Exposure is 4.0 in day 4 at move 1
  157/10000 [..............................] - ETA: 17:36:05 - reward: 668.8320*When No. 240 infected, Exposure is 4.0 in day 4 at move 3
No. 405 exposure increased to 3.0 in day 4 at 5
  158/10000 [..............................] - ETA: 17:33:10 - reward: 668.1597*When No. 405 infected, Exposure is 3.0 in day 4 at move 2
  203/10000 [..............................] - ETA: 14:54:36 - reward: 701.4776No. 63 exposure increased to 1.0 in day 4 at 1
  204/10000 [..............................] - ETA: 14:54:17 - reward: 702.2252No. 63 exposure increased to 2.0 in day 4 at 5
No. 70 exposure increased to 1.0 in day 4 at 5
No. 296 exposure increased to 1.0 in day 4 at 5
No. 477 exposure increased to 1.0 in day 4 at 5
No. 617 exposure increased to 1.0 in day 4 at 5
No. 771 exposure increased to 1.0 in day 4 at 5
No. 831 exposure increased to 2.0 in day 4 at 5
No. 878 exposure increased to 1.0 in day 4 at 5
  205/10000 [..............................] - ETA: 15:07:52 - reward: 702.9697No. 63 exposure increased to 3.0 in day 4 at 5
No. 70 exposure increased to 2.0 in day 4 at 5
No. 94 exposure increased to 1.0 in day 4 at 5
No. 296 exposure increased to 2.0 in day 4 at 5
No. 477 exposure increased to 2.0 in day 4 at 5
No. 582 exposure increased to 1.0 in day 4 at 5
No. 615 exposure increased to 1.0 in day 4 at 5
No. 617 exposure increased to 2.0 in day 4 at 5
No. 771 exposure increased to 2.0 in day 4 at 5
No. 800 exposure increased to 1.0 in day 4 at 5
No. 831 exposure increased to 3.0 in day 4 at 5
No. 878 exposure increased to 2.0 in day 4 at 5
No. 887 exposure increased to 1.0 in day 4 at 5
  206/10000 [..............................] - ETA: 15:22:14 - reward: 703.5621*When No. 617 infected, Exposure is 2.0 in day 4 at move 1
*When No. 63 infected, Exposure is 3.0 in day 4 at move 2
*When No. 831 infected, Exposure is 3.0 in day 4 at move 3
*When No. 477 infected, Exposure is 2.0 in day 4 at move 4
No. 60 exposure increased to 2.0 in day 4 at 5
No. 70 exposure increased to 3.0 in day 4 at 5
No. 80 exposure increased to 1.0 in day 4 at 5
No. 94 exposure increased to 2.0 in day 4 at 5
No. 296 exposure increased to 3.0 in day 4 at 5
No. 311 exposure increased to 1.0 in day 4 at 5
No. 368 exposure increased to 1.0 in day 4 at 5
No. 582 exposure increased to 2.0 in day 4 at 5
No. 615 exposure increased to 2.0 in day 4 at 5
No. 771 exposure increased to 3.0 in day 4 at 5
No. 800 exposure increased to 2.0 in day 4 at 5
No. 863 exposure increased to 1.0 in day 4 at 5
No. 878 exposure increased to 3.0 in day 4 at 5
No. 887 exposure increased to 2.0 in day 4 at 5
  207/10000 [..............................] - ETA: 15:29:14 - reward: 704.0850*When No. 70 infected, Exposure is 3.0 in day 4 at move 0
*When No. 296 infected, Exposure is 3.0 in day 4 at move 1
*When No. 878 infected, Exposure is 3.0 in day 4 at move 1
*When No. 60 infected, Exposure is 2.0 in day 4 at move 4
*When No. 771 infected, Exposure is 3.0 in day 4 at move 4
No. 80 exposure increased to 2.0 in day 4 at 5
No. 82 exposure increased to 1.0 in day 4 at 5
No. 94 exposure increased to 3.0 in day 4 at 5
No. 145 exposure increased to 1.0 in day 4 at 5
No. 236 exposure increased to 1.0 in day 4 at 5
No. 311 exposure increased to 2.0 in day 4 at 5
No. 368 exposure increased to 2.0 in day 4 at 5
No. 474 exposure increased to 1.0 in day 4 at 5
No. 582 exposure increased to 3.0 in day 4 at 5
No. 615 exposure increased to 3.0 in day 4 at 5
No. 632 exposure increased to 1.0 in day 4 at 5
No. 669 exposure increased to 1.0 in day 4 at 5
No. 758 exposure increased to 1.0 in day 4 at 5
No. 800 exposure increased to 3.0 in day 4 at 5
No. 848 exposure increased to 1.0 in day 4 at 5
No. 853 exposure increased to 1.0 in day 4 at 5
No. 863 exposure increased to 2.0 in day 4 at 5
No. 877 exposure increased to 1.0 in day 4 at 5
No. 887 exposure increased to 3.0 in day 4 at 5
No. 953 exposure increased to 1.0 in day 4 at 5
  208/10000 [..............................] - ETA: 15:43:18 - reward: 705.0567*When No. 800 infected, Exposure is 3.0 in day 4 at move 0
*When No. 615 infected, Exposure is 3.0 in day 4 at move 3
*When No. 887 infected, Exposure is 3.0 in day 4 at move 3
No. 80 exposure increased to 3.0 in day 4 at 5
No. 82 exposure increased to 2.0 in day 4 at 5
*When No. 94 infected, Exposure is 3.0 in day 4 at move 5
No. 145 exposure increased to 2.0 in day 4 at 5
No. 193 exposure increased to 1.0 in day 4 at 5
No. 236 exposure increased to 2.0 in day 4 at 5
No. 291 exposure increased to 1.0 in day 4 at 5
*When No. 311 infected, Exposure is 2.0 in day 4 at move 5
No. 368 exposure increased to 3.0 in day 4 at 5
No. 382 exposure increased to 1.0 in day 4 at 5
No. 415 exposure increased to 1.0 in day 4 at 5
No. 433 exposure increased to 1.0 in day 4 at 5
No. 471 exposure increased to 1.0 in day 4 at 5
No. 474 exposure increased to 2.0 in day 4 at 5
No. 496 exposure increased to 2.0 in day 4 at 5
No. 576 exposure increased to 1.0 in day 4 at 5
No. 582 exposure increased to 4.0 in day 4 at 5
No. 632 exposure increased to 2.0 in day 4 at 5
No. 669 exposure increased to 2.0 in day 4 at 5
No. 758 exposure increased to 2.0 in day 4 at 5
No. 829 exposure increased to 1.0 in day 4 at 5
No. 848 exposure increased to 2.0 in day 4 at 5
No. 853 exposure increased to 2.0 in day 4 at 5
No. 863 exposure increased to 3.0 in day 4 at 5
No. 872 exposure increased to 1.0 in day 4 at 5
No. 877 exposure increased to 2.0 in day 4 at 5
No. 953 exposure increased to 2.0 in day 4 at 5
  209/10000 [..............................] - ETA: 16:01:23 - reward: 706.3254No. 80 exposure increased to 4.0 in day 4 at 1
No. 82 exposure increased to 3.0 in day 4 at 1
No. 90 exposure increased to 1.0 in day 4 at 1
No. 145 exposure increased to 3.0 in day 4 at 1
No. 193 exposure increased to 2.0 in day 4 at 1
No. 236 exposure increased to 3.0 in day 4 at 1
No. 291 exposure increased to 2.0 in day 4 at 1
No. 368 exposure increased to 4.0 in day 4 at 1
No. 382 exposure increased to 2.0 in day 4 at 1
No. 415 exposure increased to 2.0 in day 4 at 1
No. 433 exposure increased to 2.0 in day 4 at 1
No. 471 exposure increased to 2.0 in day 4 at 1
No. 474 exposure increased to 3.0 in day 4 at 1
No. 496 exposure increased to 3.0 in day 4 at 1
No. 576 exposure increased to 2.0 in day 4 at 1
No. 582 exposure increased to 5.0 in day 4 at 1
*When No. 632 infected, Exposure is 2.0 in day 4 at move 1
No. 669 exposure increased to 3.0 in day 4 at 1
No. 732 exposure increased to 1.0 in day 4 at 1
No. 733 exposure increased to 2.0 in day 4 at 1
No. 758 exposure increased to 3.0 in day 4 at 1
No. 829 exposure increased to 2.0 in day 4 at 1
No. 848 exposure increased to 3.0 in day 4 at 1
No. 853 exposure increased to 3.0 in day 4 at 1
No. 863 exposure increased to 4.0 in day 4 at 1
No. 872 exposure increased to 2.0 in day 4 at 1
No. 877 exposure increased to 3.0 in day 4 at 1
No. 905 exposure increased to 1.0 in day 4 at 1
*When No. 953 infected, Exposure is 2.0 in day 4 at move 1
  210/10000 [..............................] - ETA: 16:04:36 - reward: 707.1533*When No. 80 infected, Exposure is 4.0 in day 4 at move 0
*When No. 145 infected, Exposure is 3.0 in day 4 at move 0
*When No. 236 infected, Exposure is 3.0 in day 4 at move 0
*When No. 382 infected, Exposure is 2.0 in day 4 at move 0
*When No. 471 infected, Exposure is 2.0 in day 4 at move 0
*When No. 733 infected, Exposure is 2.0 in day 4 at move 0
No. 27 exposure increased to 1.0 in day 4 at 1
*When No. 82 infected, Exposure is 3.0 in day 4 at move 1
No. 90 exposure increased to 2.0 in day 4 at 1
No. 96 exposure increased to 1.0 in day 4 at 1
No. 193 exposure increased to 3.0 in day 4 at 1
No. 291 exposure increased to 3.0 in day 4 at 1
No. 344 exposure increased to 2.0 in day 4 at 1
No. 368 exposure increased to 5.0 in day 4 at 1
No. 387 exposure increased to 2.0 in day 4 at 1
No. 415 exposure increased to 3.0 in day 4 at 1
No. 433 exposure increased to 3.0 in day 4 at 1
No. 474 exposure increased to 4.0 in day 4 at 1
No. 496 exposure increased to 4.0 in day 4 at 1
No. 576 exposure increased to 3.0 in day 4 at 1
*When No. 582 infected, Exposure is 5.0 in day 4 at move 1
No. 669 exposure increased to 4.0 in day 4 at 1
No. 697 exposure increased to 1.0 in day 4 at 1
No. 732 exposure increased to 2.0 in day 4 at 1
No. 758 exposure increased to 4.0 in day 4 at 1
No. 829 exposure increased to 3.0 in day 4 at 1
No. 848 exposure increased to 4.0 in day 4 at 1
No. 853 exposure increased to 4.0 in day 4 at 1
No. 863 exposure increased to 5.0 in day 4 at 1
*When No. 872 infected, Exposure is 2.0 in day 4 at move 1
No. 877 exposure increased to 4.0 in day 4 at 1
No. 890 exposure increased to 2.0 in day 4 at 1
No. 905 exposure increased to 2.0 in day 4 at 1
  211/10000 [..............................] - ETA: 16:09:39 - reward: 707.7095*When No. 368 infected, Exposure is 5.0 in day 4 at move 0
*When No. 848 infected, Exposure is 4.0 in day 4 at move 0
No. 27 exposure increased to 2.0 in day 4 at 1
No. 90 exposure increased to 3.0 in day 4 at 1
No. 92 exposure increased to 1.0 in day 4 at 1
No. 96 exposure increased to 2.0 in day 4 at 1
No. 131 exposure increased to 1.0 in day 4 at 1
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># scores = dqn.test(env, nb_episodes = 1, visualize = False)</span>
<span class="c1"># print(np.mean(scores.history[&#39;episode_reward&#39;]))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Test the agent</span>
<span class="kn">import</span> <span class="nn">tensorflow</span> <span class="k">as</span> <span class="nn">tf</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">reset</span><span class="p">()</span>
<span class="n">economy</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">states</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">day</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">):</span>
    <span class="n">state</span> <span class="o">=</span> <span class="n">current_state</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
    <span class="n">states</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>
    
    <span class="n">state</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">6</span><span class="p">])</span>
    
    <span class="n">prediction</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">steps</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
    <span class="n">action_by_agent</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">argmax</span><span class="p">(</span><span class="n">prediction</span><span class="p">)</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">one_day</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">action</span> <span class="o">=</span> <span class="n">action_by_agent</span><span class="p">)</span>
    <span class="n">gain</span> <span class="o">=</span> <span class="n">economy_gain</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
    <span class="n">economy</span> <span class="o">+=</span> <span class="n">gain</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">f</span><span class="s2">&quot;Day </span><span class="si">{day}</span><span class="s2">: take action </span><span class="si">{action_by_agent}</span><span class="s2">, total_reward: </span><span class="si">{economy}</span><span class="s2">. </span><span class="si">{prediction}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[96]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">model</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s2">&quot;model_ann_4_6_states&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>INFO:tensorflow:Assets written to: model_ann_4_6_states/assets
</pre>
</div>
</div>

</div>
</div>

</div>
    </div>
  </div>
</body>

 


</html>

