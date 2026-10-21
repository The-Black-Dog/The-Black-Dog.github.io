#!/usr/bin/env python3
"""Refresh the script hashes in index.html's Content-Security-Policy.

The page only runs inline scripts whose exact contents match a hash in its
Content-Security-Policy. After ANY edit inside a <script> block, run:

    python3 tools/update_csp_hashes.py

from the repository folder, then commit index.html. If you skip this, the
browser blocks the edited script and the page's buttons stop working.
"""
import base64, hashlib, re, sys
from pathlib import Path

path = Path(sys.argv[1] if len(sys.argv) > 1 else "index.html")
html = path.read_text(encoding="utf-8")
scripts = re.findall(r"<script>(.*?)</script>", html, flags=re.S)
hashes = " ".join(
    "'sha256-" + base64.b64encode(hashlib.sha256(s.encode("utf-8")).digest()).decode() + "'"
    for s in scripts
)
new_html, n = re.subn(r"script-src [^;\"]+;", f"script-src {hashes};", html, count=1)
if n != 1:
    sys.exit("Could not find script-src in the Content-Security-Policy.")
if new_html == html:
    print(f"Already up to date ({len(scripts)} scripts).")
else:
    path.write_text(new_html, encoding="utf-8")
    print(f"Updated hashes for {len(scripts)} scripts in {path}.")
