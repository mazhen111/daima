## 中添加环境变量
import os ,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print (BASE_DIR)
sys.path.append(BASE_DIR)

#第二种
"""
虽然通过添加环境变量的方式可以实现跨模块导入，但是官方不推荐这么干，因为这样就需要在每个目录下的每个程序里都写一遍添加环境变量的代码。

官方推荐的玩法是，在项目里创建个入口程序，整个程序调用的开始应该是从入口程序发起，这个入口程序一般放在项目的顶级目录

这样做的好处是，项目中的二级目录 apeland_web/views.py中再调用他表亲my_proj/settings.py时就不用再添加环境变量了。

原因是由于manage.py在顶层，manage.py启动时项目的环境变量路径就会自动变成….xxx/my_proj/这一级别
"""