# 📁 File Organizer (Python)

A simple and lightweight Python tool that automatically organizes files in a given folder based on their extensions.
Perfect for cleaning messy Downloads folders, project directories, or any cluttered workspace.

## 🚀 Features

Automatically sorts files into predefined categories:

Images (`.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.svg`)

Documents (`.pdf`, `.docx`, `.doc`, `.txt`, `.md`)

Spreadsheets (`.xlsx`, `.xls`, `.csv`)

Videos (`.mp4`, `.mkv`, `.avi`, `.mov`)

Archives (`.zip`, `.rar`, `.7z`, `.tar`, `.gz`)

Code (`.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.json`)

Everything else → Others

Creates category folders automatically

Skips files if already moved

Clean and readable terminal logs

## 🧰 Requirements

`Python 3.x`

No external libraries needed — uses only the Python standard library.

## 📦 Installation

Just clone or download this script:
~~~
git clone https://github.com/Chandrakant6/file-org
cd file-org/
~~~

No dependencies required.

## ▶️ Usage

Run the script with the folder you want to organize:  
`python file_org.py <target-folder-path>`

Example: `python file_org.py ~/Downloads`


If the folder exists, the script will:

Scan all files

Detect their categories

Create folders like Images/, Documents/, Videos/, etc.

Move files into their respective directories

## 📁 Folder Structure (after organizing)

Example:
~~~
Downloads/
│── Images/
│     ├── photo1.png
│     ├── logo.svg
│
│── Documents/
│     ├── resume.pdf
│     ├── notes.txt
│
│── Code/
│     ├── script.py
│     ├── app.js
│
│── Others/
│     ├── randomfile.xyz
~~~
## ⚠️ Notes

The script does not modify subfolders — only top-level files.

If a file already exists in the destination folder, it is skipped safely.

Unsupported extensions go into `Others/`.

## 📝 License

MIT License — free to use, modify, and distribute.