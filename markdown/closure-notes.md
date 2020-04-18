# Notes On Zeek's Closures
### April 2020

At the moment Zeeks' closures are rather error prone. I'm sure there
are more undocumented ones, but here are their reported issues on
GitHub as of April 16 2020:

* [Closures are not properly maintained across event handlers.](https://github.com/zeek/zeek/issues/734)
* [Unexpected lambda behavior after escaping original scope.](https://github.com/zeek/zeek/issues/886)

Both of these issues stem from trouble managing the closure frame of
lambdas. For example, the first issue above stems from the fact that
Zeek doesn't create new call frames for each handler of an event and
instead reuses call frames. Between calls of an event the frame is
reset and values in a lambdas closure are removed.

This is in spite of the fact that the machinery for managing
closures is already quite complex. To list a few such things:

* Lambdas have complex logic for finding non-local variables that they
  will need in their closure at parse time that handles non-local
  variables in nested lambdas.
* Lambdas take care to only clone items in their closures that they're
  using when being cloned.
* Lambdas take care that they only store a weak reference to
  themselves in their closure frame to prevent cyclic references.
  
The result of all this is that lambdas are difficult to reason about
and error prone. This is also largely my fault as I was the original
implementer of closures in Zeek. At the time I didn't grasp the
complexities of Zeek, but now with ~6 months of closures being out in
the wild I have some thoughts about how to resolve these problems.

## 1. Bandaids

One approach would be to try and move through these issues and add
patchwork until they're solved. For example, we could add special
logic so that when a frame gets reset the lambda will move values in
that frame that it cares about into a special list. Then, whenever a
lookup occurs in a frame the frame could first check if the value
being looked up is in that list and then continue with the regular
lookup. Yuck.

__Pros:__

* If there are really only those two issues with lambdas, then adding
  bandaids and calling it a day has the potential to be a lot less
  work than chainging how closures are designed.

__Cons:__

* If there are more issues like the frame reset one, this has the
  potential to get pretty hairy.
* The Frame class needs to be very fast. A serious limiting factor in
  the performance of any programming language is variable lookups and
  adding more branches to a variabe lookup is bound to slow down a
  language.
* The logic around lambdas with closures is already incredibly complex
  and hairy. Adding more things in there risks making it completely
  incomprehensible.
  
## 2. Redesign

Another approach is to take a stab at changing how closures are
managed in Zeek. Perhaps the current issue is design and not
implementation.

__Pros:__

* A good implementation might do wonders for us.

__Cons:__

* Possibly more work.

I detail a potential design in a different post that will be linked
here once I've put it together.

---

### [Lua Upvalue Struct](https://github.com/lua/lua/blob/9b7987a9d1471ba94764286b28e0998f73deb46a/lobject.h#L605-L616)

```c
typedef struct UpVal {
  CommonHeader;
  lu_byte tbc;  /* true if it represents a to-be-closed variable */
  TValue *v;  /* points to stack or to its own value */
  union {
    struct {  /* (when open) */
      struct UpVal *next;  /* linked list */
      struct UpVal **previous;
    } open;
    TValue value;  /* the value (when closed) */
  } u;
} UpVal;
```
