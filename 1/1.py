def expenseReport():
    report = open('input.txt', 'r')
    report_list = report.read().splitlines()
    cast_report_list = []
    # report_list = report_list.split(',')

    report.close()
    for item in report_list:
        cast_report_list.append(int(item))
    
    values = []

    values = twoSumExpense(cast_report_list, 2020)

    print(values[0] * values[1])




def twoSumExpense(array, target):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] + array[j] == target:
                return [array[i], array[j]]
        

expenseReport()