#!/usr/bin/env python3

import argparse
import webbrowser
import urllib.parse
import time
import json
import sys

BANNER = r"""
   ______  ____              __
  / ____/ / __ \____  ____  / /__
 / / __  / / / / __ \/ __ \/ //_/
/ /_/ / / /_/ / /_/ / /_/ / ,<   
\____/  \____/\____/\____/_/|_|  

    GDork v1.0

    Author: Inayat Hussain
    (Senior Offensive Security Engineer)
"""

# --- Github dorks for Github data 
def generate_dorks(domain):
    return {
        "Secrets / Keys": [
            f'"{domain}" "api_key"',
            f'"{domain}" "apikey"',
            f'"{domain}" "secret_key"',
            f'"{domain}" "access_key"',
            f'"{domain}" "auth_token"',
            f'"{domain}" "client_secret"',
            f'"{domain}" "private_key"',
        ],
        "Configs": [
            f'"{domain}" ".env"',
            f'"{domain}" filetype:env',
            f'"{domain}" filetype:json "key"',
            f'"{domain}" filetype:yml "secret"',
            f'"{domain}" filetype:yaml "password"',
            f'"{domain}" filetype:ini "password"',
        ],
        "Cloud": [
            f'"{domain}" "AWS_ACCESS_KEY_ID"',
            f'"{domain}" "AWS_SECRET_ACCESS_KEY"',
            f'"{domain}" "x-api-key"',
        ],
        "Database": [
            f'"{domain}" "connection_string"',
            f'"{domain}" "jdbc:mysql://"',
            f'"{domain}" "mongodb://"',
        ],
        "Auth / User Data": [
            f'"{domain}" "authorization: bearer"',
            f'"{domain}" "token="',
            f'"{domain}" "password="',
            f'"{domain}" "email="',
        ],
        "Sensitive Files": [
            f'"{domain}" "BEGIN RSA PRIVATE KEY"',
            f'"{domain}" "BEGIN OPENSSH PRIVATE KEY"',
            f'"{domain}" "ftp://"',
            f'"{domain}" "ssh2_auth_password"',
            f'"{domain}" filetype:log "{domain}"',
        ]
    }


# --- Flatten dorks into list (max 30) ---
def flatten_dorks(dork_dict):
    dorks = []
    for category in dork_dict.values():
        dorks.extend(category)
    return dorks[:30]


# --- Build search URL ---
def build_url(dork, engine):
    if engine == "github":
        query = urllib.parse.quote(dork)
        return f"https://github.com/search?q={query}&type=code"
    else:
        query = urllib.parse.quote(dork + " site:github.com")
        return f"https://www.google.com/search?q={query}"


# --- Open in browser ---
def open_dorks(dorks, engine, delay):
    for d in dorks:
        url = build_url(d, engine)
        webbrowser.open(url)
        time.sleep(delay)


# --- Save output ---
def save_output(dorks, filename, fmt):
    if fmt == "json":
        with open(filename, "w") as f:
            json.dump(dorks, f, indent=2)
    else:
        with open(filename, "w") as f:
            for d in dorks:
                f.write(d + "\n")


# --- Main ---
def main():
    parser = argparse.ArgumentParser(description="GDork - GitHub Recon Dork Tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("-o", "--output", help="Save output to file")
    parser.add_argument("--open", action="store_true", help="Open dorks in browser")
    parser.add_argument("--engine", choices=["google", "github"], default="google", help="Search engine")
    parser.add_argument("--delay", type=float, default=1, help="Delay between opening tabs")
    parser.add_argument("--format", choices=["txt", "json"], default="txt", help="Output format")
    parser.add_argument("--quiet", action="store_true", help="No banner")

    args = parser.parse_args()

    if not args.quiet:
        print(BANNER)

    dork_dict = generate_dorks(args.domain)

    print(":: Generated Github dorks \n")

    count = 1
    all_dorks = []

    for category, dorks in dork_dict.items():
        print(f"[{category}]")
        for d in dorks:
            if count > 30:
                break
            print(f"[{count:02}] {d}")
            all_dorks.append(d)
            count += 1
        print()

    # --- Save ---
    if args.output:
        save_output(all_dorks, args.output, args.format)
        print(f"[+] Saved to {args.output}")

    # --- Open ---
    if args.open:
        print("[+] Opening dorks in browser...")
        open_dorks(all_dorks, args.engine, args.delay)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\n[!] Interrupted by user")
