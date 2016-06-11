# -*- coding:UTF-8 -*-
__author__ = 'wuxuanyi'

import HTMLTestRunner
import argparse
import unittest
import time
import shutil #copy file
import logging
import os
import re
import sys
from selenium import webdriver
from openpyxl import load_workbook
from time import gmtime, strftime
from GemstoneLib.page_class import para
sys.path.append(os.path.join(os.path.dirname(__file__)))


#===============================================================================
#                               FUNCTIONS
#===============================================================================

# def grab_test_ID_from_excel(sheet_ranges, col_index='D', row_index=2):
def grab_test_ID_from_excel(sheet_ranges, row_index=2):

    """ grab testcase ID from testrun, following the testrail format

    @param col_index string The column to read from
    @param row_index int The starting row to rgit ead from
    @param sheet_ranges wb object The message to be printed.
    @return An list of test_id
    """
    # col_index = 'J'
    # row_index = 2 # start from 2, first row is title

    # print(sheet_ranges[col_index + str(row_index)].value)
    tuple(sheet_ranges['A1':'Z1'])
    for cellObj in sheet_ranges['A1':'Z1']:
        for cell in cellObj:
            if cell.value == 'Case ID':
                col_index = cell.coordinate[:1]

    test_case_id = []
    while sheet_ranges[col_index + str(row_index)].value != None:
        # print col_index + str(row_index)
        # print(sheet_ranges[col_index + str(row_index)].value)
        test_case_id.append(sheet_ranges[col_index + str(row_index)].value)
        row_index = row_index + 1

    return test_case_id


def backup_file(file):
    shutil.copyfile(file, time.strftime('%Y_%m_%d_%H_%M_%S') + '_' + file)


def extract_test_case_id(test_method):
    regex_pattern = 'C[0-9]+'
    searched = re.search(regex_pattern, test_method)
    if searched:
        return searched.group()
    else:
        return test_method

def record_result_file(info):
    file_path = os.path.dirname(os.path.realpath(__file__))+'/do_not_touch'
    with open(file_path, "w") as text_file:
        text_file.write(info)


#===============================================================================


def list_all_available_test():

    logging.basicConfig(level=logging.INFO)
    all_test_method = []
    all_test_method_id = []
    modules_to_pick = []
    test_suite = []
    # if args.verbose:
    #     logging.basicConfig(level=logging.DEBUG)
    print 'Listing all the test cases'
    modules_to_pick.append('')  # must obey the current structure
    current_path = os.path.dirname(os.path.realpath(__file__))
    found_tests = unittest.TestLoader().discover(start_dir=current_path, pattern="test*.py")
    test_suite.append(found_tests)  # list of test suites
    for t in test_suite:
        for ts in t:
            for tc in ts:
                for tm in tc:
                    all_test_method.append(tm)
    print '================='
    counter = 0
    # print out all test methods
    all_test_method.sort()
    for m in all_test_method:
        counter = counter + 1
        print str(m)
        all_test_method_id.append(extract_test_case_id(str(m)))
    print 'Total %i tests' % (counter,)
    print '================='
    for m in all_test_method_id:
        print m


def report():
    # set up test parameters
    para.TEST_SERVER_IP = args.test_server_ip
    para.SCAN_SUBNET = args.test_subnet_ip

    # Setting up log location
    filename='test_report'
    if not args.list:
        filename = str(strftime("%Y_%m_%d_%H_%M_%S")) + '_'  + '.html'
    fp = file(filename, "wb")
    record_result_file(filename)

    # setting up default suit
    suite_to_run = unittest.TestSuite()
    all_test_method = [] # available tests
    test_select = []  # tests selected from excel
    test_suite = []
    current_path = os.path.dirname(os.path.realpath(__file__))
    found_tests = unittest.TestLoader().discover(start_dir=current_path, pattern="test*.py")
    test_suite.append(found_tests)  # list of test suites
    if 'xlsx' in args.run_source:  # for now assume xlsx in the format of excel
        # read from the test run excel
        wb = load_workbook(args.run_source)
        sheet_names = wb.get_sheet_names()
        sheet_ranges = wb.get_sheet_by_name(sheet_names[0])
        test_select = grab_test_ID_from_excel(sheet_ranges)
        for t in test_suite:
            # test suites
            # print t
            for ts in t:
                # test suite
                for tc in ts:
                    # print 'tc'
                    # print(tc)
                    for tt in tc:
                        all_test_method.append(tt)
    print '------------------------'
    counter = 0
    for m in all_test_method:
        counter = counter + 1
    print counter
    print '================='
    added_test_count = 0
    added_test_id = []
    for test_id in test_select:
        # print '=======Test_id=========='
        # print test_id
        # print '================='
        for test_method in all_test_method:
            if test_id in str(test_method):
                # print 'adding to test suite'
                added_test_count = added_test_count + 1
                added_test_id.append(test_id)
                # print test_id
                suite_to_run.addTest(test_method)
    print 'total added tests to run: ' + str(added_test_count)
    print 'test id added: '
    print added_test_id
    print '================='
    logging.info('=================Start test=================')
    if args.debug:
        runner = HTMLTestRunner.HTMLTestRunner(title='Result', description='Test_Report')
    else:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Result', description='Test_Report')
    runner.run(suite_to_run)


def main():
    if args.list:
        list_all_available_test()
    else:
        report()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("--test_server_ip", help="the ip of the test machine, etc, 10,0.10.126", required=True)
    parser.add_argument("--test_subnet_ip", help="the ip of the scan target subnet, etc, 192.168.0.111/24", required=True)
    parser.add_argument("--test_scan_port_ip", help="the ip of the scan port, etc, 192.168.0.111", required=True)
    parser.add_argument("--run_source", help="the test_plan excel path", required=True)
    # parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-l", "--list", action="store_true", help="List all available automation tests")
    parser.add_argument("-d", "--debug", help="Print out test result on stdout", action="store_true")
    # parser.add_argument("--test_port_number", help="the port on the test machine, etc, 0, 1, 2, 3", required=True)
    # parser.add_argument("--test_port_ip", help="the port ip that assigned to the port number, etc, 192.168.0.111", required=True)
    # parser.add_argument("-a", "--all", action="store_true", help="All tests will be executed")
    # parser.add_argument("--module_to_run", help="a comma seperated module names", default="")
    args = parser.parse_args()

    main()
