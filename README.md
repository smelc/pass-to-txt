# pass-to-txt

Displays the content of `$HOME/.password-store`
(used by the [pass](https://www.passwordstore.org/) tool) as nicely formatted text.
This is useful for example if you want to print your passwords and store
them on a piece of paper.

Given a `$HOME/.password-store` like this:

```
dir1
├── pass1.gpg
└── pass2.gpg
pass3.gpg
```

It prints:

```
└─ dir1
  └─  pass1
      ... content of pass1 ...
  └─  pass2
      ... content of pass2 ...
└ pass3
  ... content of pass3 ...
```

## Execution

Run me as follows: `./main.py` (tested with python `3.10`)
