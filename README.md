## autofuzz

This project aims to help people get started with fuzzing.

Fuzzing a lib/tool already described in a formula (see "formulas" folder),
is as simple as:

    ./fuzz xz

This will pull the xz library, from git master, build with afl instrumentation
and start fuzzing using a supplied xz sample (see "testcases" folder).

It is currently built around american-fuzzy-lop, with the intention of expanding
to include other fuzzers.
