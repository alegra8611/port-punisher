# port-punisher
A quick multiprocessing port scanner that scans all 65535 ports and enumerates services on a host in under 40 seconds.

- Can scan both single ip addresses or hostnames
- Can scan lists of ip addresses or hostnames (1 per line)
- Can increase the number of workers (processes) to fine tune to cpu
- Can save output to a txt file (included output.txt as example)

Requirements:
-
- python3.9

Install:
-
git clone https://github.com/alegra8611/port-punisher.git

Usage:
-

**Scan single host on all ports:**

python3 port-scan.py -T target.com

**Scan single host and save output:**

python3 port-scan.py -T target.com -O output.txt

**Scan list of hosts:**

python3 port-scan.py -F targets.txt -O output.txt

**Increase workers:**

python3 port-scan.py -F targets.txt -W 2000 -O output.txt

**Change Start and End Port range:**

python3 port-scan.py -F targets.txt -SP 1 -EP 1000 -W 1000 -O output.txt

Screenshots:
-

**Single Host:**

![alt text](https://github.com/alegra8611/port-punisher/tree/main/screenshots/port1.png?raw=true)

**Multiple Host:**

![alt text](https://github.com/alegra8611/port-punisher/tree/main/screenshots/port2.png?raw=true)



