import sys
import os
import re
import argparse
from openpyxl import load_workbook
# from GemstoneLib.testrail import testrail_client
from testrail import *
'''
parse the html report result to testrail
The sheet name should be 'Regression_Test'
'''
__author__ = 'ygt'

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

testrail_client = APIClient('http://172.17.3.70/testrail/')
testrail_client.user = 'yigang.tao@Istuary.com'
testrail_client.password = 'w0KB294#!RG33e|y'


def get_report_name():
    file_path = os.path.dirname(os.path.realpath(__file__))+'/do_not_touch'
    with open(file_path, "r") as text_file:
        report = text_file.read()
    return report.strip()


def main():
    # project_id = '232'
    filename = get_report_name()
    # filename = 'result_from_Jason.html'
    testcase_format = re.compile('.*\'testcase\'.*C[\d{6}|\d{6}_.].*')
    # digit5 = re.compile('[0-9]{5}_[0-9]|[0-9]{5}')
    digit5 = re.compile('[0-9]{6}')
    result_format = re.compile('.*pass<.*|.*fail<.*|.*error<.*')
    res = re.compile('pass<|fail<|error<')
    test_id_list = []
    test_result = []

    # read project run_ID from xlsx file
    # current_path = os.path.dirname(os.path.realpath(__file__))
    wb = load_workbook(args.run_source)
    sheet_names = wb.get_sheet_names()
    if 'Regression_Test' in sheet_names:
        sheet_ranges = wb['Regression_Test']
    else:
        sheet_ranges = wb.get_sheet_by_name(sheet_names[0])
    tuple(sheet_ranges['A1':'Z1'])
    for cellObj in sheet_ranges['A1':'Z1']:
        for cell in cellObj:
            if cell.value == 'Run ID':
                new = cell.coordinate[:1]+'2'
                project_id = sheet_ranges[new].value[1:]
                print project_id
    with open(filename) as f:
        content = f.readlines()
    for line in content:
        if testcase_format.match(line):
            m = digit5.search(line)
            case_id = m.group()
            test_id_list.append(case_id)
        elif result_format.match(line):
            n = res.search(line)
            test_result.append(n.group()[:-1])

    print 'Test run ID is %s' % project_id
    if len(test_id_list) == len(test_result):
        for i in range(len(test_result)):
            add_result_for_case = 'add_result_for_case/%s/%s' %(project_id, test_id_list[i])
            print 'The result of %s is %s' %(test_id_list[i], test_result[i])
            if test_result[i] == 'pass':
                try:
                    testrail_client.send_add_result_for_case(project_id, test_id_list[i], {'status_id': testrail_client.passed, 'comment': 'automation'})
                except:
                    print 'Test '+str(test_id_list[i])+' fail to upload the result'
            elif test_result[i] == 'fail':
                try:
                    testrail_client.send_add_result_for_case(project_id, test_id_list[i], {'status_id': testrail_client.failed, 'comment': 'automation'})
                except:
                    print 'Test '+str(test_id_list[i])+' fail to upload the result'
            else:
                print 'Please test '+str(test_id_list[i])+' manually'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--run_source", help="the test_plan excel path", required=True)
    args = parser.parse_args()
    main()