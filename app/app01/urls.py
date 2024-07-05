from django.contrib import admin
from django.urls import path, include
#将应用的URL配置包含到项目的URL配置中
urlpatterns = [


    #include('app01.urls')：include()函数允许你从另一个URLconf模块中包含URL模式。这里，它指向app01应用内部的urls.py文件。
    # 这意味着app01应用可以有自己的URL配置，独立于项目的主URL配置文件，使得每个应用可以管理自己的路由逻辑，提高了代码的组织性和可维护性。
]