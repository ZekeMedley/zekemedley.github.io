
<!DOCTYPE html>
<head>
<meta charset='UTF-8'>
<title>Zeke</title>
<link rel="stylesheet" href="styles/type.css"></link>
<link rel="stylesheet" href="styles/position.css"></link>
<link href="styles/prism.css" rel="stylesheet" />
<!-- Favicon is GitHub profile image. -->
<link rel="icon" href="https://avatars1.githubusercontent.com/u/30676292?s=180&v=4">
</head>
<body>
<div class="wrapper">
    <nav>
      <a href="index.md"><img src="media/logo.gif" alt="ZM Logo"></a>
      <ul>
          <li><a href="https://www.linkedin.com/in/zeke-medley-b1261a173/">Linkedin</a></li>
          <li><a href="https://github.com/ZekeMedley">GitHub</a></li>
          <li><a href="interesting-things.md">Interesting</a></li>
      </ul>
    </nav>
<section id="main">
<h1>Discrete Time Periodicity</h1>
<h3>Mar 2020</h3>
<p>We say that a function is periodic if, for some <code>p</code>, <code>f(x) = f(x + p)</code>
for all <code>x</code>. This is all pretty familiar. If you've ever taken a
geometry class before, you've probably encountered quite a few trig
functions who are periodic. Here, for example, is our dear friend
<code>sin(x)</code> plotted in continuous time from 0 to 6π.</p>
<p><img class="med-img" src="media/sin_x_ct.svg" alt="sin of x from zero to 6π" /></p>
<p>Both a visual and mathematical examination of this function will
reveal that it is periodic. We learn this pretty early along in our
math careers and a simple google search will tell you that its period
is <code>2π</code>.</p>
<p>More generally, the condition for this function to be periodic is that
there exists a positive <code>p</code> for which <code>sin(wx) = sin(w(x+p)) = sin(wx + wp)</code>. Because we know that the underlying <code>sin</code> function here
is periodic, this requirement holds if <code>wp = 2πk</code> for some <code>k</code>.</p>
<p>In our continuous time case, we know exactly how to solve this
one. Dividing by <code>w</code>, we find the period to be <code>2πk/w</code>.</p>
<p>What about the discrete time case though? Much to my surprise
recently, it actually turns out that <code>sin(wx)</code> is only periodic under
rather draconian conditions in discrete time. Consider our signal
above, but this time its discretized version.</p>
<p><img class="med-img" src="media/sin_x_dt.svg" alt="sin of x from zero to 6π" /></p>
<p>Things still look fairly periodic, but something isn't quite
right. The wave looks like its repeating, but our samples on each hump
aren't quite the same. Is our wave still periodic?</p>
<p>Well, lets return to our earlier definition of periodicity. We know
that this wave will be periodic with period <code>p</code> if <code>sin(wn) = sin(w(n+p)) = sin(wn + wp)</code> (I've switched to using <code>n</code> here as our
variable as we're now in discrete time). Working this out, we arrive
at a familiar formula: <code>p = 2πk/w</code>, but in our <code>sin(n)</code> function
<code>w = 1</code>!</p>
<p>Something is wrong, our period is now an irrational number. What this
means is that in discrete time, our friend <code>sin(n)</code> is no longer a
periodic function.</p>
<p>I thought this was quite interesting.</p>

</section>
</div>
<script src="styles/prism.js"></script>
</body>
</html>
