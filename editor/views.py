from django.shortcuts import render, redirect
from recorder.models import Point
from .models import Course
from .forms import CourseForm


def form(request):
    # フォームからの POST でない場合（普通にアクセスされた場合）はフォームを返して終了
    if request.method != 'POST':
        return render(request, 'editor/form.html', {'form': CourseForm()})

    # Course オブジェクトを生成
    course = Course()
    course.name = request.POST['name']
    # ManyToMany は保存されたオブジェクトに対してでなければ追加できないので一旦保存
    course.save()

    # チェックされた項目をリストで取得
    points = request.POST.getlist('points')
    for point in points:
        # point はただの数値（ID）なので、これを使用して DB より Point の　レコードを取得
        point_object = Point.objects.get(id=point)
        # Course に Point を関連付け
        course.points.add(point_object)
    course.save()
    return redirect('viewer:index')
