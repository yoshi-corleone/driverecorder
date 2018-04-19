from django.views import generic
from editor.models import Course
from .models import Key


class IndexView(generic.ListView):
    template_name = 'viewer/index.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        # コースすべてを取得
        return Course.objects.all()


class DetailView(generic.DetailView):
    model = Course
    template_name = 'viewer/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 対象コースを取得
        course = self.object
        # 対象コースと関連づけられている Point を撮影日時の昇順で取得
        points = course.points.all().order_by('time')
        # Point のリスト
        context['points'] = points
        # 出発地点と到着地点
        context['start'] = points[0]
        context['end'] = points[len(points) - 1]
        # 経由地は points の中の start と end の間
        waypoints = points[1:len(points) - 1] if len(points) >= 3 else []
        # 経由地が8箇所以上となると Google Maps のエラーとなるため間引きを行う
        if len(waypoints) > 8:
            coefficient = len(waypoints) / 8
            temp = []
            for i in range(8):
                temp.append(waypoints[int(i * coefficient)])
            waypoints = temp
        context['waypoints'] = waypoints
        # API_KEY をデータベースから取得
        api_key = Key.objects.get(name='GoogleMapsJavascript')
        context['api_key'] = api_key.api_key
        return context

