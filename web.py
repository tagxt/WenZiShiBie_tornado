#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Created by sublime_text at home on  2018/2/28—20:12！
@Gnome:   Live and learn!
@Author: 葛绪涛
@Nickname:  wordGe
@QQ:  690815818
@Filename: web.py 
@Blog: http://higexutao.blog.163.com  
"""
import os.path
from tornado import httpserver, web, ioloop


# 功能模块 实现具体的功能
class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write("Hello world!")
        self.render("formSubmit.html")

    def post(self, *args, **kwargs):
        # pass
        # file_metas = self.request.files.get('file')
        # print(type(file_metas))
        # print("Hi")
        user_name = self.get_argument("username")
        user_email = self.get_argument("email")
        user_website = self.get_argument("website")
        user_language = self.get_argument("language")
        self.render("user.html", username=user_name, email=user_email, website=user_website, language=user_language)


template_path = os.path.join(os.path.dirname(__file__), "template")
print(template_path)
# 设置路径
settings = {
    'template_path': "template",
    #     模板文件路径参数 ，一般指 网页
    'static_path': "static",

}

# 路由 也即分机，也可以理解为功能模块在哪里
# 下面是没有加设置参数时的代码，**是设置动态参数
# application = web.Application([
#     (r"/", MainPageHandler),
# ])
# 上面设置了动态参数，下面开始应用，注意是加**settings
application = web.Application([
    (r"/", MainPageHandler),
], **settings)

# handlers = [
#     (r"/", IndexHandler),
#     (r"/user", UserHandler)
# ]
# socket 服务  前台 联系方式   诸如端口
if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(5407)
    ioloop.IOLoop.current().start()
