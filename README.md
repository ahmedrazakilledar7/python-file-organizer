# File Organizer

This project renames all `.jpg` files in a folder.

Instead of manually changing file names one by one, the script renames every image in order like this:

```
image1.jpg
image2.jpg
image3.jpg
```

## How to run

1. Put your `.jpg` files inside the target folder.
2. Update the folder path in `main.py`.
3. Run:

```bash
python main.py
```

## Example

Before:

```
dog.jpg
holiday.jpg
photo.jpg
```

After:

```
image1.jpg
image2.jpg
image3.jpg
```

## What I used

- Python
- os module

## Why I made this

I wanted to practice working with files and folders in Python. This project helped me understand how to list files, filter them by extension, and rename them automatically.

I'll keep improving it by adding support for more file types and custom file names.