from user_profiles.dao.PersonalAppealDao import PersonalAppealDao
from user_profiles.settings import datetime_string_format
from datetime import datetime, timedelta
from ..data_process.word_segment import segment_with_weight


def each_classification(appeallor_name):
    """
    获取各级分类数据
    :param appeallor_name:
    :return:
    """
    data = {"一级分类": [], "二级分类": [], "三级分类": [], "四级分类": [], "五级分类": []}

    for classi in data.keys():
        clsi = PersonalAppealDao.get_dist_cert_field(appeallor_name, classi)
        list1 = sorted(clsi.items(), key=lambda x: x[1], reverse=True)[:15]
        for key, value in list1:
            data[classi].append({'name': key, 'value': value})
    return data


def order_info(appeallor_name):
    """
    获取工单信息数据
    :param appeallor_name:
    :return:
    """
    data = {"紧急程度": [], "来电类别": [], "工单状态": [], "办理单位": [], "受理渠道": [], "受理类型": []}

    for info in data.keys():
        clsi = PersonalAppealDao.get_dist_cert_field(appeallor_name, info)
        list1 = sorted(clsi.items(), key=lambda x: x[1], reverse=True)[:15]
        for key, value in list1:
            data[info].append({'name': key, 'value': value})
    return data


def raise_time_dist(appeallor_name, start_time, end_time, parti_size=0):
    """
    整合时间规律数据
    :param appeallor_name:
    :param start_time:
    :param end_time:
    :param parti_size:
    :return:
    """
    # 0：按日， 1：按周， 2：按月（暂未实现）
    parti_size_dic = {0: timedelta(days=1), 1: timedelta(weeks=1), 2: 0}

    start_date = datetime(int(start_time.split('-')[0]), int(start_time.split('-')[1]), int(start_time.split('-')[2].split(' ')[0]), 0, 0, 0, 0)
    end_date = datetime(int(end_time.split('-')[0]), int(end_time.split('-')[1]), int(end_time.split('-')[2].split(' ')[0]), 0, 0, 0, 0)

    appeal_set = PersonalAppealDao.get_by_time_range(appeallor_name, start_date.__format__(datetime_string_format), end_date.__format__(datetime_string_format))

    appeal_time_data = appeal_time(appeal_set, start_date, parti_size)
    appeal_time_point_data = appeal_time_point(appeal_set)
    handle_time_data = handle_time_length(appeal_set)

    data = {
        'data1': appeal_time_data,
        'data2': appeal_time_point_data,
        'data3': handle_time_data,
    }
    return data


def appeal_time(appeal_set, start_date, parti_size):
    """
    获取诉求时间分布数据
    :param appeal_set:
    :param start_date:
    :param parti_size: 粒度
    :return:
    """
    # 0：按日， 1：按周， 2：按月（暂未实现）
    parti_size_dic = {0: timedelta(days=1), 1: timedelta(weeks=1), 2: 0}
    result = []
    start_date = start_date - parti_size_dic[parti_size]
    for appeal in appeal_set:
        if appeal.raise_time != 'NULL':
            if appeal.raise_time <= start_date.__format__(datetime_string_format):
                result[-1][1] = result[-1][1] + 1
            else:
                start_date = start_date + parti_size_dic[parti_size]
                result.append([start_date.__format__('%Y-%m-%d'), 0])
                if appeal.raise_time <= start_date.__format__(datetime_string_format):
                    result[-1][1] = result[-1][1] + 1
    return result


def appeal_time_point(appeal_set):
    """
    获取诉求时间点分布数据
    :param appeal_set:
    :return:
    """
    result = [
        {'name': '0:00~2:00', 'value': 0},
        {'name': '2:00~4:00', 'value': 0},
        {'name': '4:00~6:00', 'value': 0},
        {'name': '6:00~8:00', 'value': 0},
        {'name': '8:00~10:00', 'value': 0},
        {'name': '10:00~12:00', 'value': 0},
        {'name': '12:00~14:00', 'value': 0},
        {'name': '14:00~16:00', 'value': 0},
        {'name': '16:00~18:00', 'value': 0},
        {'name': '18:00~20:00', 'value': 0},
        {'name': '20:00~22:00', 'value': 0},
        {'name': '22:00~0:00', 'value': 0}
    ]
    for appeal in appeal_set:
        apl_time = int(appeal.raise_time.split(' ')[1].split(':')[0])
        if apl_time % 2 == 0:
            result[apl_time//2]['value'] = result[apl_time//2]['value'] + 1
        else:
            result[(apl_time-1)//2]['value'] = result[(apl_time-1)//2]['value'] + 1
    return result


def handle_time_length(appeal_set):
    """
    获取处理时长数据
    :param appeal_set:
    :return:
    """
    durations = {}
    for appeal in appeal_set:
        if (appeal.raise_time != 'NULL') and (appeal.finish_time != 'NULL'):
            duration = datetime.strptime(appeal.finish_time.split('.')[0], datetime_string_format) \
                       - datetime.strptime(appeal.raise_time.split('.')[0], datetime_string_format)
            if str(duration.days)+'天' in durations.keys():
                durations[str(duration.days)+'天'] = durations[str(duration.days)+'天'] + 1
            else:
                durations[str(duration.days) + '天'] = 1
    result = []
    temp = sorted(durations.items(), key=lambda x: x[1], reverse=True)[:15]
    list1 = sorted(temp, key=lambda x: x[0], reverse=False)
    for key, value in list1:
        result.append({'name': key, 'value': value})
    return result


def lda_topic_extract(appeallor_name, start_time, end_time):
    """
    先测试用
    :param appeallor_name:
    :param start_time:
    :param end_time:
    :param parti_size:
    :return:
    """
    start_date = datetime(int(start_time.split('-')[0]), int(start_time.split('-')[1]),
                          int(start_time.split('-')[2].split(' ')[0]), 0, 0, 0, 0)
    end_date = datetime(int(end_time.split('-')[0]), int(end_time.split('-')[1]),
                        int(end_time.split('-')[2].split(' ')[0]), 0, 0, 0, 0)

    appeal_set = PersonalAppealDao.get_by_time_range(appeallor_name, start_date.__format__(datetime_string_format),
                                                     end_date.__format__(datetime_string_format))
    text = ""
    for appeal in appeal_set:
        if appeal.content != 'NULL':
            text = text + appeal.content
    result = segment_with_weight([text, ])[0]
    data = []
    for word in result:
        data.append({'name': word[0], 'value': word[1]})
    return {'data1': data}
