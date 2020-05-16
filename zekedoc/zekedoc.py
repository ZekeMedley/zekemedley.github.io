import mistletoe
import sys
from zekedoc.renderer import ZekeRenderer

header = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset='UTF-8'>
<title>Zeke Medley</title>
<link rel="stylesheet" href="styles/type.css"></link>
<link rel="stylesheet" href="styles/position.css"></link>
<link href="styles/prism.css" rel="stylesheet" />
<!-- Favicon is GitHub profile image. -->
<link rel="icon" href="https://avatars1.githubusercontent.com/u/30676292?s=180&v=4">
</head>
<body>
<div class="wrapper">
    <nav>
      <a href="index.md.html"><img src="media/logo.gif" alt="ZM Logo"></a>
      <ul>
          <li><a href="writing.md">Writing</a></li>
          <li><a href="work.md.html">Work</a></li>
      </ul>
    </nav>
<section id="main">
'''

footer = '''
</section>
</div>
<script src="js/prism.js"></script>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</body>
</html>
'''

def render_file(f):
    return header + mistletoe.markdown(f, ZekeRenderer) + footer
