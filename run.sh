#!/usr/bin/env bash

project_path_code= '/Users/uma2103/Insight'
project_path= '/Users/uma2103/Insight/test' #'/Users/uma2103/Downloads/ICC-master/insight_testsuite/tests/test-1-paymo-trans'

python .${project_path_code}/src/INSIGHT_CODE.py -f1 .${project_path}/paymo_input/batch_payment.txt -f2 .${project_path}/paymo_input/stream_payment.txt -o1 .${project_path}/paymo_output/output1.txt -o2 .${project_path}/paymo_output/output2.txt -o3 .${project_path}/paymo_output/output3.txt

#python ./src/INSIGHT_CODE.py -f1 ./paymo_input/batch_payment.txt -f2 ./paymo_input/stream_payment.txt -o1 ./paymo_output/output1.txt -o2 ./paymo_output/output2.txt -o3 ./paymo_output/output3.txt

