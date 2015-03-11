#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import time,clock
from subprocess import Popen, PIPE
from collections import namedtuple
import sys
import os

Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
	# Modify this code to run your optimization algorithm
	# Writes the inputData to a temporay file
	tmp_file_name = 'tmp.data'
	tmp_file = open(tmp_file_name, 'w')
	tmp_file.write(input_data)
	tmp_file.close()
	process = Popen(['julia', 'knapTest.jl', '' + tmp_file_name], stdout=PIPE)
	(stdout, stderr) = process.communicate()	
	print(stdout)
	print(stderr)
	#os.remove(tmp_file_name)	# removes the temporary file
	output_data = stdout.strip()
	# prepare the solution in the specified output format
	#output_data = str(value) + ' ' + str(0) + '\n'
	#output_data += ' '.join(map(str, taken))
	return output_data



if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print input_data
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

