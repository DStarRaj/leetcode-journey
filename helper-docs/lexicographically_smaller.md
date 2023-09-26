# Lexicographically Smaller

A string `a` is **lexicographically smaller** than a string `b` if in the first position where `a` and `b` differ, string `a` has a letter that appears earlier in the alphabet than the corresponding letter in `b`.

If the first `min(a.length, b.length)` characters do not differ, then the shorter string is the lexicographically smaller one.