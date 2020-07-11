# Thoughts On Firefox & Zeek Performance
### July 2020

With Zeek I felt like with some regularity we were thinking about performance. We were interested in avoiding copies whenever possible, avoiding unnecessary `ref` / `unref` calls, optimizing class data member order to reduce padding, speeding up the main event loop, etc. Many of these concerns were architectural but thoughts about performance were often at the front of my mind. I choke this up to a couple things:

- C++ as a language lends itself to that sort of thinking. It makes it very clear whenever you are making an allocation or copying data.
- Jon was pretty interested in that sort of thing having come from a large scale computing / HPC background.
- Zeek was slow and there was demand for it to be quicker as more performance meant fewer packet drops.

While I haven't been at Firefox for nearly as long I haven't noticed any of that sort of discussion yet. The only time its come up is a brief discussion with Emilio on a patch where he mentioned that we could probably do something in one pass instead of two. What's interesting though is that all of the reasons I listed above for why I thought Zeek was interested in performance also apply to Firefox.

- Firefox is written in C++ and Rust which are both very interested in high performance.
- People at Firefox are very interested in performance. We have an entire team dedicated exclusively to making Firefox faster.
- Firefox being fast is a selling point for the browser much like Zeek not dropping packets is.

My hypothesis for why performance hasn't come up as often here then is that its because Firefox is designed to be fast. The very architecture of the browser is high performance. If you write code within that architecture, your code will be fast. Zeek on the other hand doesn't have that benefit. Zeek is an interpreted scripting language with a weak type system.

I've had this experience working on a variety of projects. At IBM when I was working on a fast program to play Rock Paper Scissors the key to performance wasn't thinking about how to minimize the number of if statements that are used, it was thinking about how the program fit together. The same can be said for when I write semistack. The code in semistack wasn't that performant, but the way it was designed meant that it could compute Fibonacci numbers orders of magnitude quicker than Lox.

In conclusion, if you're thinking about performance, you should probably be thinking about architecture. That's not to say you shouldn't write decently efficient code, but it is to say that you shouldn't spend too much time on it unless you're pretty confident about how everything is fitting together.

