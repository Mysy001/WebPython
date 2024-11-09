Request 请求对象封装了从客户端发来的请求报文，可以从其中获取请求报文中的所有数据。
请求解析和响应封装实际上大部分是由 Werkzeug 完成的，Flask 子类化 Werkzeug 的请求(request)和响应(response)对象

使用 Request.args.get() 方法可以获取 GET 请求参数
在浏览器访问网址 
    http://127.0.0.1:5000/?name=andy&age=18
