定义一个路由函数 upload() ,用于上传图片
allowed_file() 函数检测上传的文件类型是否满足设定的要求
使用 random_file() 函数为上传的文件重新创建一个随机的不重复的文件名
提交上传的图片，并在另一个路由函数 uploaded_file() 中显示图片内容

html文件中 From 表单中设置 enctype = 'multipart/form-data' ，用于上传文件

流程
    上传(存在、合法)——>随机文件名(保存)——>显示