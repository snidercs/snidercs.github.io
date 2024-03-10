# website
Snider CS Website

## Clone
```
git clone git@github.com:snidercs/website-static
cd website-static
git submodule update --init
```

## Useful Hugo commands

Hugo will create the dir and MD. Hugo will also populate the MD file with datetime of creation.
```
hugo new content <dir>/example.md
```
Start up the Hugo website with
```
Hugo server -D
```
-D flag means Hugo will also generate MD files with draft = true.