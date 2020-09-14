import os
from conf import settings
import pickle
"""
用于保存对象与获取对象

"""
#保存数据
def svae_data(obj):
    """
    :param obj: 
    :return: 
    
    1.获取对象的保存文件路径
    obj.__class__ 获取当前对象的类
    obj__class__.__name__ 
    """
    class_name=obj.__class__.__name__
    user_dir_path=os.path.join(
        settings.DB_PATH,class_name
    )
    #2,。判断文件夹是否存在，没有的话创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)
    #3 拼接当前用户文件已用户名
    user_path=os.path.join(
        user_dir_path,obj.user

    )
    with open(user_path,"wb") as f :
        pickle.dump(obj,f)
#查看数据
def select_data(cls,username):
    class_name = cls.__name__
    user_dir_path = os.path.join(
        settings.DB_PATH, class_name
    )
    # 2,。判断文件夹是否存在，没有的话创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)
    # 3 拼接当前用户文件已用户名
    user_path = os.path.join(
        user_dir_path, username

    )

    if os.path.exists(user_path):
        with open(user_path, "rb") as f:
           obj= pickle.load(f)
           return obj
    return  None



