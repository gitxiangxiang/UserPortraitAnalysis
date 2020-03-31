class AdapterForReadingExcel:
    personal_field = {'工单编号': 'order_no',
                      '受理员工号': 'acceptor_no',
                      '受理员': 'acceptor_name',
                      '来电人': 'raise_name',
                      '一级分类': 'classification',
                      '二级分类': 'classification',
                      '三级分类': 'classification',
                      '四级分类': 'classification',
                      '五级分类': 'classification',
                      '紧急程度': 'urgent_level',
                      '来电类别': 'raise_category',
                      '受理渠道': 'raise_channel',
                      '主要内容': 'content',
                      '受理时间': 'raise_time',
                      '回复备注': 'NULL',
                      '办理情况': 'NULL',
                      '被催办单ID': 'NULL',
                      '受理备注': 'notes',
                      '工单状态': 'status',
                      '受理类型': 'receive_category',
                      '是否保密': 'is_secrecy',
                      '是否回复': 'is_reply',
                      '办理单位': 'handle_department',
                      '转办时间': 'transfer_time',
                      '转办人姓名': 'transfer_name',
                      '转办人工号': 'transfer_no',
                      '转办意见': 'transfer_opinion',
                      '办结时间': 'finish_time'
                      }
    need_special_handle = {
        '一级分类': 'classification',
        '二级分类': 'classification',
        '三级分类': 'classification',
        '四级分类': 'classification',
        '五级分类': 'classification',
        '紧急程度': 'urgent_level',
        '来电类别': 'raise_category',
        '受理渠道': 'raise_channel',
        '工单状态': 'status',
        '受理类型': 'receive_category',
        '是否保密': 'is_secrecy',
        '是否回复': 'is_reply'
    }
    urgent_level = {
        '紧急': 'EMERGENCY',
        '一般': 'COMMON',
        '无意义': 'INSIGNIFICANT'
    }
    raise_category = {
        '咨询': 'CONSULT',
        '求助': 'SEEK_HELP',
        '投诉': 'COMPLAIN'
    }
    raise_channel = {
        '来电': 'CALL'
    }
    order_status = {
        '办结': 'FINISH',
        '已转办待回复': 'TRANSFER',
        '部门回复': 'APARTMENT',
    }
    receive_category = {
        '直办': 'DIRECT_HANDLE',
        '转办': 'TRANSFER_HANDLE'
    }

    @staticmethod
    def special_handle():

        pass

    @staticmethod
    def convert(table_head, records):
        """
        将excel改造为用于创建诉求对象的字典列表（使用未做提取的记录）
        :param table_head: 表头
        :param records:
        :return: list(dict)
        """
        length = len(table_head)
        col = len(records)
        dic_list = []
        [dic_list.append({}) for i in range(col)]
        for i in range(length):
            th = table_head[i].value
            if th in AdapterForReadingExcel.personal_field.keys() and AdapterForReadingExcel.personal_field[th] != 'NULL':
                # if th in AdapterForReadingExcel.need_special_handle.keys():
                #     AdapterForReadingExcel.special_handle()
                # else:
                #     j = 0
                #     for dic in dic_list:
                #         dic[AdapterForReadingExcel.personal_field[th]] = records[j][i].value
                #         j = j + 1
                for j in range(col):
                    dic_list[j][AdapterForReadingExcel.personal_field[th]] = records[j][i].value
        return dic_list
