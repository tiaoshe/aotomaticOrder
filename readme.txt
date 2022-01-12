1-创建目录结构 -安装pytest
2-环境打包
--pip freeze > requirements.txt
--pip install -d /path/to/save/package -r requirements.txt  # 安装包到指定位置
3-配置好github
3.1-通过pycharm创建github项目，并且将新建的项目commit
3.2-push的时候遇到报错，处理方式如下，创建秘钥，配置秘钥到github中，成功push
--tiaoshe
C:\Users\admin>ssh-keygen -t rsa -C "tiaoshe"
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\admin/.ssh/id_rsa):
C:\Users\admin/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\admin/.ssh/id_rsa.
Your public key has been saved in C:\Users\admin/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:uYhNxq/ALFFJB+tOYLAlaRDvLDhAm+3oRiQwJnaxgM8 tiaoshe
4-公共代码库新增config.ini 控制文件 问题：调用方法与指定方法层级不同会找不到对应的文件，每个层级不同的文件传入filepath 保证其正常运行
5-日志记录文件 writelog 文件编写
6-新增excel读写操作文件
7-B端登录公共文件调通
8-测试案例相关公共代码配置
9-编写部分工作测试用例
10-Faker安装
--pip临时源配置
1、采用国内源，加速下载模块的速度
2、常用pip源：
    -- 豆瓣：https://pypi.douban.com/simple
    -- 阿里：https://mirrors.aliyun.com/pypi/simple
    -- 清华：https://pypi.tuna.tsinghua.edu.cn/simple
    -- 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
    -- 华中理工大学：http://pypi.hustunique.com/
    -- 山东理工大学：http://pypi.sdutlinux.org/
3、加速安装的命令：
    -- >: pip install -i https://pypi.douban.com/simple 模块名

11-通过har文件自动生成yaml文件
--未做
12-通过yaml文件自动生成code文件
--通过jinja2完成code生成代码，test.py文件中为试炼场
13-榴芒传说接口测试lmcsb.py是B端相关调用接口文件，test_b.py是测试相关数据
14-通过文件管理测试数据，还需要思考下

15-allure-pytest 安装   准备研究下测试报告生成
    --安装allure-pytest
    --运行的时候生成对应的json报告 在edit configurations 里面配置生成文件的路径  其他地方的生成似乎有点问题
    pytest --alluredir D:\pythonProject\aotomaticOrder\report\report test_smj_scene.py::TestSmj::test_add_coupon
    --安装allure客户端，配置环境变量，通过命令生成对应的html文件
    --将json文件格式的报告转换成html格式的报告
        allure generate ./run/ -o ./report/run/ --clean
16-研究下allure教程，看看如何生成自己想要的报告文件

