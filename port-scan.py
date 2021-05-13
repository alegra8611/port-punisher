from multiprocessing import Process
from datetime import datetime
import requests
import subprocess
import argparse
import socket
import time
import math
import os
import yaml


banner = subprocess.call("./banner.sh")

def is_port_open(address, port, timeout=0.3):
	try:
		socket.create_connection((address, port), timeout).close()
		return True
	except:
		return False

def scan_address(address, start_port, end_port):
	protocolname = 'tcp'
	for port in range(start_port, end_port+1):
		if is_port_open(address, port):
			try:
				print("Port: %s is Open => Service: %s" %(port, socket.getservbyport(port, protocolname)))

			except socket.error as error:
				if error:
					print(f'Port: {port} is Open => Service: Unknown')

			if output:
				mode = 'a' if os.path.exists(output) else 'w'
				try:
					with open(output, mode) as l:
						l.write("Port: %s is Open => Service: %s" %(port, socket.getservbyport(port, protocolname)))
						l.write('\n')
				except socket.error as error:
					if error:
						with open(output, mode) as l:
							l.write(f'Port: {port} is Open => Service: Unknown\n')


def scan_host(hostname, start_port, end_port, workers):
	if hostname:
		address = socket.gethostbyname(hostname)
		print ("-" * 150)
		print(f'HOST: {hostname}')
		print(f'Address: {address}')
		print("Scanning Started at:" + str(datetime.now()))
		print ("-" * 150)
		if output:
			mode = 'a' if os.path.exists(output) else 'w'
			with open(output, mode) as l:
				l.write("-" * 150)
				l.write(f'\nHOST: {hostname} | Address: {address}\n')
				l.write("Scanning Started at:" + str(datetime.now()))
				l.write('\n')
				l.write("-" * 150)
				l.write('\n')

		step = math.ceil((end_port - start_port + 1) / workers)

		processes = []

		for port in range(start_port, end_port + 1, step):
			args = (address, port, min(port + step - 1, end_port))
			process = Process(target=scan_address, args=args)
			process.start()
			processes.append(process)

		for process in processes:
			process.join()

	if filename:

		with open(filename, 'r') as f:
			for host in f:
				hostname = host.strip()
				address = socket.gethostbyname(hostname)

				print ("-" * 150)
				print(f'HOST: {hostname}')
				print(f'Address: {address}')
				print("Scanning Started at:" + str(datetime.now()))
				print ("-" * 150)
				if output:
					mode = 'a' if os.path.exists(output) else 'w'
					with open(output, mode) as l:
						l.write("-" * 150)
						l.write(f'\nHOST: {hostname} | Address: {address}\n')
						l.write("Scanning Started at:" + str(datetime.now()))
						l.write('\n')
						l.write("-" * 150)
						l.write('\n')


				step = math.ceil((end_port - start_port + 1) / workers)

				processes = []

				for port in range(start_port, end_port + 1, step):
					args = (address, port, min(port + step - 1, end_port))
					process = Process(target=scan_address, args=args)
					process.start()
					processes.append(process)

				for process in processes:
					process.join()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-F', '--filename', type=str)
	parser.add_argument('-T', '--hostname', type=str)
	parser.add_argument('-O', '--output', type=str)
	parser.add_argument('-SP', '--start-port', type=int, default=1)
	parser.add_argument('-EP', '--end-port', type=int, default=65535)
	parser.add_argument('-W', '--workers', type=int, default=1000)

	args = parser.parse_args()
	filename = args.filename
	output = args.output
	start_time = time.time()

	scan_host(args.hostname, args.start_port, args.end_port, args.workers)

	end_time = time.time()

	print ("-" * 150)
	print(f'Elapsed time: {round(end_time - start_time)} seconds')
	print ("-" * 150)
	print("")

	if output:
		mode = 'a' if os.path.exists(output) else 'w'
		with open(output, mode) as l:
			l.write("-" * 150)
			l.write('\n')
			l.write(f'Elapsed time: {round(end_time - start_time)} seconds\n')
			l.write("-" * 150)
			l.write('\n')