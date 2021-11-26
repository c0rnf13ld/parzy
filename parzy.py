#!/usr/bin/python3

import sys, re

if len(sys.argv) != 2:
	print(f"\nUsage: python3 {sys.argv[0]} <file>")
	sys.exit(1)

file = sys.argv[1]

def parseFile():
	global capture
	capture = []
	with open(file, "r") as f:
		for line in f.readlines():
			capture_ = re.findall(r"\d: .*?:(.*?) ", line)
			if "".join(capture_) in capture:
				continue
			capture += capture_

def convert():
	global ports
	ports = []
	for port_hex in capture:
		ports.append(str(int(port_hex, base=16)))

def checkLen():
	count = 0
	length = []
	for i in ports:
		length.append(len(i))
	space = max(length) - 1
	print()
	for port, port_hex in zip(ports, capture):
		count += 1
		print(f"·{str(count)} : [{str(port_hex)}]{' ' * space}->{' ' * space}[{port}]")

def main():
	parseFile()
	convert()
	checkLen()

if __name__ == '__main__':
	main()