# snidercs.org
The Snider CS Website

## Clone
```bash
git clone git@github.com:snidercs/website-static
cd website-static
git submodule update --init
```

## Creating a new Blog Post
Hugo will create the dir and MD. Hugo will also populate the MD file with datetime of creation.
```bash
hugo new content/posts/title-of-article.md
```
## Creating new Pages
Pages are slightly different than posts. `page-name` below will be part of the URL. e.g. `snidercs.org/page-name` for this example. `index.md` lets hugo know to use a page-like template.
```bash
hugo new content/page-name/index.md
```

## Local Webserver
Start up the Hugo website with
```bash
hugo server -D
```
The `-D` flag means Hugo will also generate MD files with draft = true.

## First Scoring API Docs
https://frc-api-docs.firstinspires.org/
