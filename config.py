#coding:utf-8

def getParam():
    param = {
            'ID': u'资产编号',
            'label': u'标注',
            'train_file': 'train.csv',
            'test_file': 'test.csv',
            'drop_list': [u'客户编号', u'姓名', u'历史平均还款间隔（天）',u'本金余额'],
            'date_cols': [u'起始日', u'到期日']
            }
    #param['drop_list'] += [u'截至倒数第二期剩余期数（月）',u'截至倒数第二期历史最长逾期天数',u'截至倒数第二期已还本金（元）',u'截至倒数第二期逾期本金（元）',u'截至倒数第二期已还利息（元）',u'截至倒数第二期历史逾期次数',u'倒数第二期逾期天数',u'截至倒数第二期历史平均还款间隔（天）',u'截至倒数第二期剩余本金（元）',u'截至倒数第二期剩余利息（元）']
    #param['drop_list'] += [u'截至倒数第三期剩余期数（月）',u'截至倒数第三期历史最长逾期天数',u'截至倒数第三期已还本金（元）',u'截至倒数第三期逾期本金（元）',u'截至倒数第三期已还利息（元）',u'截至倒数第三期历史逾期次数',u'倒数第三期逾期天数',u'截至倒数第三期历史平均还款间隔（天）',u'截至倒数第三期剩余本金（元）',u'截至倒数第三期剩余利息（元）']
    #param['drop_list'] += [u'截至倒数第四期剩余期数（月）',u'截至倒数第四期历史最长逾期天数',u'截至倒数第四期已还本金（元）',u'截至倒数第四期逾期本金（元）',u'截至倒数第四期已还利息（元）',u'截至倒数第四期历史逾期次数',u'倒数第四期逾期天数',u'截至倒数第四期历史平均还款间隔（天）',u'截至倒数第四期剩余本金（元）',u'截至倒数第四期剩余利息（元）']
    #param['drop_list'] += [u'截至倒数第五期剩余期数（月）',u'截至倒数第五期历史最长逾期天数',u'截至倒数第五期已还本金（元）',u'截至倒数第五期逾期本金（元）',u'截至倒数第五期已还利息（元）',u'截至倒数第五期历史逾期次数',u'倒数第五期逾期天数',u'截至倒数第五期历史平均还款间隔（天）',u'截至倒数第五期剩余本金（元）',u'截至倒数第五期剩余利息（元）']
    return param
