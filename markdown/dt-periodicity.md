# Discrete Time Periodicity
### Mar 2020

We say that a function is periodic if, for some `p`, `f(x) = f(x + p)`
for all `x`. This is all pretty familiar. If you've ever taken a
geometry class before, you've probably encountered quite a few trig
functions who are periodic. Here, for example, is our dear friend
`sin(x)` plotted in continuous time from 0 to 6π.

![sin of x from zero to 6π](media/sin_x_ct.svg )

Both a visual and mathematical examination of this function will
reveal that it is periodic. We learn this pretty early along in our
math careers and a simple google search will tell you that its period
is `2π`.

More generally, the condition for this function to be periodic is that
there exists a positive `p` for which `sin(wx) = sin(w(x+p)) =
sin(wx + wp)`. Because we know that the underlying `sin` function here
is periodic, this requirement holds if `wp = 2πk` for some `k`.

In our continuous time case, we know exactly how to solve this
one. Dividing by `w`, we find the period to be `2πk/w`.

What about the discrete time case though? Much to my surprise
recently, it actually turns out that `sin(wx)` is only periodic under
rather draconian conditions in discrete time. Consider our signal
above, but this time its discretized version.

![sin of x from zero to 6π](media/sin_x_dt.svg )

Things still look fairly periodic, but something isn't quite
right. The wave looks like its repeating, but our samples on each hump
aren't quite the same. Is our wave still periodic?

Well, lets return to our earlier definition of periodicity. We know
that this wave will be periodic with period `p` if `sin(wn) =
sin(w(n+p)) = sin(wn + wp)` (I've switched to using `n` here as our
variable as we're now in discrete time). Working this out, we arrive
at a familiar formula: `p = 2πk/w`, but in our `sin(n)` function
`w = 1`!

Something is wrong, our period is now an irrational number. What this
means is that in discrete time, our friend `sin(n)` is no longer a
periodic function.

I thought this was quite interesting.
