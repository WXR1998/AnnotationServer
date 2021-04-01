# 数据分类查错系统

## 简介

使用Django编写的一个简易网页前端，用于手工检查粗分类结果是否有误，并将检查结果保存在数据库中。

## 开始使用

- 首先在`AnnotationServer/settings.py`里配置好MySQL的连接。需要在MySQL里预先创建好`AnnotationServerDB`这个数据库。
- 然后在项目根目录运行\
    `python3 manage.py makemigrations AnnotationServer` \
    `python3 manage.py migrate`\
    这个操作可以自动建好数据表。
- 将粗分类结果的图片以`Imageid_ClassidClassCaption.jpg`格式命名好（如`00012_07向下突刺.jpg`），放在`./templates/img`下。
- 然后访问`X.X.X.X:8000`即可进行分类。

## 数据库格式

| filename | status | class_label | image_id |
| ----- | ----- | ----- | ----- |
| `templates/img`目录下的文件名 | 0: 未检查 1: 分类正确 2: 分类错误 | 0-14 的粗分类结果 | 图片的id，见文件名的第一部分 |

标记完所有数据后，在数据库中查找所有分类错误的项，然后手工标注之即可。