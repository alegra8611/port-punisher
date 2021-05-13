# port-punisher
A quick port scanner that scans all 65535 ports and enumerates services on a host in under 40 seconds.

- Can scan both single ip addresses or hostnames
- Can scan lists of ip addresses or hostnames (1 per line)
- Can increase the number of workers (processes) to finetune to cpu
- Can save output to a txt file

Requirements:
-
- python3.9

Install:
-
git clone https://github.com/alegra8611/port-punisher.git

Usage:
-

**Scan single host on all ports:

python3 port-scan.py -T target.com

**Scan single host and save output:

python3 port-scan.py -T target.com -O output.txt

**Scan list of hosts:

python3 port-scan.py -F targets.txt -O output.txt

**Increase workers:

python3 port-scan.py -F targets.txt -W 2000 -O output.txt


