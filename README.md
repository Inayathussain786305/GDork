GDork v1.0

GDork is a simple automation tool for Google and GitHub dorking.
It helps security researchers speed up reconnaissance during authorized testing.

Features
Generates up to 30 high-value dorks
Supports Google and GitHub search
Categorized queries (Secrets, Configs, Cloud, Database, etc.)
Option to open dorks automatically in browser
Save output in TXT or JSON format
Installation
git clone https://github.com/yourusername/gdork.git
cd gdork
Usage
python gdork.py -d example.com
Options
Option	Description
-d, --domain	Target domain (required)
-o, --output	Save output to file
--open	Open dorks in browser
--engine	Search engine (google/github)
--delay	Delay between tabs (default: 1s)
--format	Output format (txt/json)
--quiet	Hide banner
Example
python gdork.py -d example.com --open --engine github
Disclaimer

This tool is for educational purposes and authorized security testing only.
Do not use it on systems without proper permission.

Author

Inayat Hussain
