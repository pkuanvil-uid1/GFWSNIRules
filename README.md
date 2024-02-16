# GFW SNI Rules
A List of SNI masquerade (also known as SNI fronting, which use a dummy or empty SNI just to establish TLS connection,
while actual website is indicated by "Host" HTTP header) rules that bypass the GFW.

## start.py
You can use any Chromium-based browser's `host-rules` command line option to apply these rules.
These rules allow you to visit a handful of websites (including github，reddit，web.archive.org，wikipedia.org，torproject.org)
without using a proxy.

Download the start.py and rules.json file to the same folder, click start.py and you are good to go.
Note: You need to close all existing chrome window before using this script.

## pkuanvil post
https://www.pkuanvil.com/topic/755/

## References
https://github.com/SpaceTimee/Cealing-Host/blob/main/Cealing-Host.json

https://github.com/Manicsteiner/TCPioneer-Hmoegirl/blob/main/default.conf
