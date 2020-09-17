#获取所有学校的接口
from conf import settings
import os
#获取学校文件路径
def get_all_school_interface():
    school_dir=os.path.join(
        settings.DB_PATH, "School"
    )
    #判断学校是否存在
    if not os.path.exists(school_dir):

        return False,"没有学校，请联系管理员"
    #若文件存在，则获取问价中所有文件的名字
    school_list=os.listdir(school_dir)
    return  True,school_list

