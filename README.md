# Web-Blocker
# Python Web Blocker

## Description
A simple Python-based tool to block and unblock websites using a GUI. It modifies your system's hosts file to redirect specified websites to 127.0.0.1.

## Features
- Easy-to-use GUI using tkinter
- Block multiple websites at once
- Unblock sites anytime
- Maintains a log of blocked/unblocked sites

## How to Use
1. Run `web_blocker.py` with admin privileges.
2. Enter websites separated by commas (e.g., facebook.com, youtube.com)
3. Click **Block** to block them, or **Unblock** to remove them from the block list.

## Note
This tool requires admin privileges to modify system files.

## Log File
- All activity is saved in `blocker_log.txt`
