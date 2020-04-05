class Filters:
    """
    设置过滤器（拦截器）
    """

    # 允许跨域请求
    @staticmethod
    def allow_CDR(fn):
        def exe_func(*args):
            response = fn(*args)
            response['Access-Control-Allow-Origin'] = '*'
            return response
        return exe_func
