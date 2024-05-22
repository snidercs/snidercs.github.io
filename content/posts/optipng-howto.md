---
title: How to Optimize Web Images with `optipng`
date: 2024-03-16T01:01:59-04:00
draft: false
hideFooter: false
ShowWordCount: true
ShowPostNavLinks: true
ShowReadingTime: true
---

![PNG Compression](/images/featured-png.png)

### What is optipng?

`optipng` is a command-line tool that optimizes PNG images. It works by recompressing image files to reduce their size while maintaining the original image quality—this is known as "lossless" compression. Smaller image files are a significant advantage for websites.

### Why Optimize Images for Websites?

* **Faster Page Loads:** Smaller PNG files mean your website content loads faster for visitors. This is crucial for a positive user experience.
* **Improved SEO:** Search engines like Google favor fast-loading websites, so image optimization can indirectly boost your search engine rankings.
* **Reduced Bandwidth Costs:** If you have a high-traffic website, smaller image sizes translate to less bandwidth used, potentially saving you money on hosting costs.

### Installing optipng on Linux

The installation process varies slightly depending on your Linux distribution:

#### Debian/Ubuntu based

```bash
sudo apt-get update
sudo apt-get install optipng
```

#### Fedora/RHEL based

```bash
sudo dnf install optipng 
```

#### Arch based

```bash
sudo pacman -S optipng
```

### Batch Processing Images with optipng

#### Basic Usage

**Optimize all PNGs in the current directory:**

```bash
optipng *.png
```

#### Advanced Examples

**Optimize PNGs in the current directory and all subdirectories recursively:**

```bash
optipng -dir . *.png 
```

**Optimize PNGs while preserving the original file's timestamp (useful for version control):**

```bash
optipng -preserve *.png
```

**More aggressive optimization level (slightly slower, but can yield better compression):**

```bash
optipng -o7 *.png
```

**Optimize only PNGs that are larger than 500KB:**

```bash
find . -size +500k -iname "*.png" -exec optipng -o7 {} \; 
```

#### Explanation of Common Options

* `-dir`:  Specifies a directory for output files. Useful for recursive optimization when you want to maintain directory structure and avoid overwriting originals.
* `-preserve`: Preserves the original file's modification timestamp.
* `-o7`: Highest optimization level. Offers maximum compression, but the process may be slightly slower.

#### Important Considerations

* `optipng` works in-place, meaning it directly modifies the original files. It's always advisable to create backups of your images before running large batch optimizations.

### Using a Bash Script + `find`

Here's a simple bash script to optimize all PNG files in a directory:

```bash
#!/bin/bash

for file in *.png; do
    optipng -o7 "$file"  # -o7 for maximum optimization
done
```

#### How to Use the Script

1. **Save:** Save the code above as a file (e.g., `optimize_images.sh`)
2. **Place in Directory:** Put the script file in the directory containing your PNG images.
3. **Make Executable:**  Run `chmod +x optimize_images.sh` in your terminal to make the script executable.
4. **Run:** Execute the script by typing `./optimize_images.sh`

##### Important Notes

* Optipng creates optimized versions of images. It's a good practice to back up your original images before running it.
* The script overwrites the original PNGs. If you want to keep the originals, modify the script to save optimized versions with a different filename.
