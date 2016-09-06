#!/usr/bin/env python

import requests, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--server', help='Target LB', required=True)
parser.add_argument('-n', '--iterations', type=int, help='Iterations', required=True)
args = parser.parse_args()

results = {}

for i in range(0,args.iterations):
    f = requests.get('http://' + args.server)
    try:
        results[f.text] += 1
    except KeyError:
        results[f.text] = 1

for node in sorted(results):
    print "{}: {}".format(node.rstrip(), results[node])
