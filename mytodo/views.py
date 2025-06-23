
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.urls import reverse_lazy
from mytodo.forms import TaskForm # クラスベースビューを継承するのに必要
from .models import Task
from django.views.generic.edit import DeleteView

class IndexView(View):
    def get(self, request):
        # todoリストを取得
        # todo_list = Task.objects.all()
        incomplete_tasks = Task.objects.filter(complete=0).order_by('-start_date')
        complete_tasks = Task.objects.exclude(complete=0).order_by('-start_date')
        context = {
            "incomplete_tasks": incomplete_tasks,
            "complete_tasks": complete_tasks,
        }
        # todo_list = list(incomplete_tasks) + list(complete_tasks)
        # context = {"todo_list": todo_list}

        # テンプレートをレンダリング
        return render(request, "mytodo/index.html", context)


class AddView(View):
    def get(self, request):
        # テンプレートのレンダリング処理
        form = TaskForm()
        return render(request, "mytodo/add.html", {"form": form})

    def post(self, request, *args, **kwargs):
        # 登録処理
        # 入力データをフォームに渡す
        form = TaskForm(request.POST)
        # 入力データに誤りがないかチェック
        is_valid = form.is_valid()

        # データが正常であれば
        if is_valid:
            # モデルに登録
            form.save()
            return redirect('/')

        # データが正常じゃない
        return render(request, 'mytodo/add.html', {'form': form})
class UpdateView(View):
    def get(self, request, pk):
        # テンプレートのレンダリング処理
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, "mytodo/add.html", {'form': form})
        

    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'mytodo/add.html', {'form': form})
    
class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')

        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()

        return redirect('/')
    
class Delete_task_View(DeleteView):
    model = Task
    template_name = 'mytodo/delete.html'  # 削除確認用テンプレート
    success_url = reverse_lazy('index')  # 削除後にリダイレクトするURL

# ビュークラスをインスタンス化
index = IndexView.as_view()
add = AddView.as_view()
update = UpdateView.as_view()
update_task_complete = Update_task_complete.as_view()
delete = Delete_task_View.as_view()