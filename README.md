# GFW SNI Rules
A List of SNI masquerade (also known as SNI fronting, which use a dummy or empty SNI just to establish TLS connection,
while actual website is indicated by "Host" HTTP header) rules that bypass the GFW.

## start.py
You can use any Chromium-based browser's `host-rules` command line option to apply these rules.
These rules allow you to visit a handful of websites (including github，reddit，web.archive.org，wikipedia.org，torproject.org)
without using a proxy.

Download the start.py and rules.json file to the same folder, click start.py and you are good to go.
