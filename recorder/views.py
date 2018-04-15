from django.shortcuts import render, redirect
from .models import Point, Picture
from .jpeg import Jpeg
import os
import datetime
UPLOADED_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'


def form(request):
    # フォームからの POST でない場合（普通にアクセスされた場合）はフォームを返して終了
    if request.method != 'POST':
        return render(request, 'recorder/form.html')

    # アップロードされたファイルを取り出し
    file = request.FILES['file']
    path = os.path.join(UPLOADED_DIR, file.name)
    destination = open(path, 'wb')

    # ファイルを書き出し
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()

    # 保存された JPEG ファイルを解析
    result = {}
    data = open(path, 'rb').read()
    jpeg_parser = Jpeg()
    if jpeg_parser.can_parse(data):
        result = jpeg_parser.parse(data)

    # Picture を生成、オブジェクトとアップロードされたファイルを関連付け
    picture = Picture()
    picture.file_name = file.name
    picture.save()

    # 写真の撮影時データオブジェクトを生成
    point = Point()
    point.name = file.name
    # 緯度、経度、撮影時刻を取得
    if 'latitude' in result:
        point.latitude = latlng_to_decimal(result['latitude'])
    if 'longitude' in result:
        point.longitude = latlng_to_decimal(result['longitude'])
    if 'DateTimeOriginal' in result:
        point.time = datetime.datetime.strptime(result['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')
    # Picture オブジェクトと関連付け
    point.picture = picture
    point.save()

    return redirect('recorder:complete')


def complete(request):
    return render(request, 'recorder/complete.html')


def latlng_to_decimal(latlng):
    degree = latlng[0] / latlng[1]
    minute = latlng[2] / latlng[3]
    second = latlng[4] / latlng[5]
    return degree + (minute / 60) + (second / 3600)
