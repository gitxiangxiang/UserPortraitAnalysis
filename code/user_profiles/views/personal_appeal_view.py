from django.http import JsonResponse
from user_profiles.service import PersonalAppealService
from user_profiles.util.filters import Filters


@Filters.allow_CDR
def each_classification(request):
    if request.method == 'POST':
        phone = request.POST['phone_id']
        table_name = request.POST.get('table_name')
    else:
        phone = request.GET.get('phone_id')
        table_name = request.GET.get('table_name')
    data = PersonalAppealService.each_classification(phone)
    respond = JsonResponse(data, safe=False)
    return respond


@Filters.allow_CDR
def order_info(request):
    if request.method == 'POST':
        phone = request.POST['phone_id']
    else:
        phone = request.GET.get('phone_id')
    data = PersonalAppealService.order_info(phone)
    return JsonResponse(data, safe=False)


@Filters.allow_CDR
def time_appeal(request):
    """
    诉求时间分布
    :param request:
    :return:
    """
    if request.method == 'POST':
        phone = request.POST['phone_id']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
    else:
        phone = request.GET.get('phone_id')
        start_time = request.GET['start_time']
        end_time = request.GET['end_time']

    data = PersonalAppealService.raise_time_dist(phone, start_time, end_time)
    return JsonResponse(data, safe=False)


@Filters.allow_CDR
def word_cloud(request):
    """
    词云图
    :param request:
    :return:
    """
    if request.method == 'POST':
        phone = request.POST['phone_id']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
    else:
        phone = request.GET.get('phone_id')
        start_time = request.GET['start_time']
        end_time = request.GET['end_time']
    print("wordcloud")
    data = PersonalAppealService.lda_topic_extract(phone, start_time, end_time)
    return JsonResponse(data, safe=False)


