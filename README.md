GDork v1.0

GDork is a simple automation tool for Google and GitHub dorking. It helps security researchers speed up reconnaissance during authorized testing.

Features
Generates 30 high-value dorks
Supports Google and GitHub search
Categorized queries (secrets, configs, cloud, database, etc.)
Option to open dorks in browser
Save output in TXT or JSON format
Usage
python gdork.py -d example.com
Options
-d, --domain Target domain (required)
-o, --output Save output to file
--open Open dorks in browser
--engine Search engine (google/github)
--delay Delay between tabs
--format Output format (txt/json)
--quiet Hide banner
Example
python gdork.py -d example.com --open --engine github
Disclaimer

This tool is for educational and authorized security testing only. Do not use it on systems without permission.

Author

Inayat Hussain
