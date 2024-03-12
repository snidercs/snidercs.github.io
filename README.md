# website
Snider CS Website

## Clone
```bash
git clone git@github.com:snidercs/website-static
cd website-static
git submodule update --init
```

## Theme Features and Help
https://github.com/adityatelange/hugo-PaperMod/wiki/Features

## Useful Hugo commands

Hugo will create the dir and MD. Hugo will also populate the MD file with datetime of creation.
```bash
hugo new content <dir>/example.md
```
Start up the Hugo website with
```bash
hugo server -D
```
The `-D` flag means Hugo will also generate MD files with draft = true.
