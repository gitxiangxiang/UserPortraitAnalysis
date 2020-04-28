from user_profiles.models.Appeallor import Appeallor


class AppeallorDao:
    """
    """

    @staticmethod
    def save_appeallor(name):
        """
        保存诉求人信息，如果匿名则视为新人
        :param name:
        :param is_anonymous:
        :return:
        """
        is_anonymous = False
        if (name.endswith('先生') or name.endswith('女士') or (name.find('市民') != -1)) and (len(name) <= 3):
            is_anonymous = True
        # 匿名或不匿名但没有被记录过的诉求人，存到数据库
        print(name)
        if is_anonymous or Appeallor.objects(name=name, is_anonymous=False).count() == 0:
            appeallor = Appeallor(name=name, is_anonymous=is_anonymous)
            return appeallor.save()
        else:
            return Appeallor.objects(name=name, is_anonymous=False).first()

    @staticmethod
    def get_appeallor_by_name(appeallor_name):
        """
        根据诉求人姓名获取诉求人信息
        :param appeallor_name:
        :return:
        """
        return Appeallor.objects(name=appeallor_name).first()
