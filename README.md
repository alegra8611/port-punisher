# port-punisher
A quick port scanner that scans all 65535 ports and enumerates services on a host in under 40 seconds.

Requirements:
-
- python3.9

Install:
-
git clone https://github.com/alegra8611/port-punisher.git

Usage:
-

scan single host on all ports:

python3 port-scan.py -T target.com

scan single host and save output:

python3 port-scan.py -T target.com -O output.txt

