import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from AnnotationServer.models import Record

'''
    db中status列的含义
        0   尚未检测完成
        1   检测完成，分类正确
        2   检测完成，分类错误
'''

class_captions = {
    0:  '突增',
    1:  '向上突刺',
    2:  '突增然后保持',
    3:  '凸型',
    4:  '密集向上突刺',
    5:  '缓慢上升',
    6:  '突降',
    7:  '向下突刺',
    8:  '突降然后保持',
    9:  '凹形',
    10: '密集向下突刺',
    11: '缓慢下降',
    12: '模式渐变',
    13: '剧烈波动',
    14: '突增突降'
}

images_per_page = 20

def get_image_list(class_index):
    image_list = [{'filename': rec.filename, 'img_id': rec.img_id}
                  for rec in Record.objects.filter(class_label=class_index, status=0)[:images_per_page]]
    return image_list

def get_image_remaining(class_index):
    return Record.objects.filter(class_label=class_index, status=0).count()

def reset_all_records(request):
    request.session['url_from'] = request.META.get('HTTP_REFERER', '/')
    Record.objects.all().delete()

    image_list = os.listdir(settings.MEDIA_ROOT)
    image_list.sort()
    for i, img_filename in enumerate(image_list):
        class_label = int(img_filename.split('_')[1][:2])
        img_id = int(img_filename.split('_')[0])
        rec = Record(filename=img_filename, status=0, class_label=class_label, img_id=img_id)
        rec.save()
    return HttpResponseRedirect(request.session['url_from'])

def annotation(request):
    if request.method == 'GET':
        context = {}
        if 'class' in request.GET:
            class_index = int(request.GET['class'])
        else:
            class_index = 0
        context['class_caption'] = f'{class_index:02d} {class_captions[class_index]}'
        context['class_index'] = class_index
        context['images'] = get_image_list(class_index)
        context['images_remaining'] = get_image_remaining(class_index)
        return render(request, 'anno.html', context)

def set_error(request):
    request.session['url_from'] = request.META.get('HTTP_REFERER', '/')
    img_id = request.POST['img_id']
    rec = Record.objects.get(img_id=img_id)
    rec.status = 2
    rec.save()
    return HttpResponseRedirect(request.session['url_from'])

def set_all_correct(request):
    request.session['url_from'] = request.META.get('HTTP_REFERER', '/')
    class_index = request.POST['class_index']
    image_list = get_image_list(class_index)
    for item in image_list:
        img_id = item['img_id']
        rec = Record.objects.get(img_id=img_id)
        rec.status = 1
        rec.save()
    return HttpResponseRedirect(request.session['url_from'])

def index(request):
    context = {}
    context['images_to_be_checked'] = Record.objects.filter(status=0).count()
    context['images_checked'] = Record.objects.filter(status__gt=0).count()
    context['images_total'] = Record.objects.all().count()
    context['images_remaining'] = [get_image_remaining(class_index) for class_index in class_captions]
    return render(request, 'index.html', context)
