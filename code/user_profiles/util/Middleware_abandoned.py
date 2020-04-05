from django.utils.deprecation import MiddlewareMixin


class MyMiddle(MiddlewareMixin):
    # 在视图执行前调用
    def process_request(self,reqeust):
        print('get请求，参数name: ', reqeust.GET.get('name'))
        return reqeust

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        return response




"""
- __init__
    不需要传参，服务器响应第一个请求的时，会自动调用，用于确定是否启用中间件 
- process_request(self,request)
    在视图执行前调用(即分配url匹配视图之前),每个请求都会调用，返回None或HttpResponse对象
- process_view(self,request,view_func,view_args,view_kwargs)
    调用视图之前执行,每个请求都会调用，返回None或HttpResponse对象
- process_templae_response(self,request,response)
    在视图刚好执行完后调用，每个请求都会调用，返回None或HttpResponse对象
- process_response(self,request,response)
    所有响应返回浏览器之前调用，每个请求都会调用，返回None或HttpResponse对象 
- process_exception(self,request,exception)
    当视图出现异常时调用，返回HttpResponse对象
"""