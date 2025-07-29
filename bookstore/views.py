from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import git

@csrf_exempt
def update(request):
    if request.method == "POST":
        try:
            repo = git.Repo('/home/drsantos20/bookstore')
            origin = repo.remotes.origin
            origin.pull()
            return HttpResponse("✅ Código atualizado com sucesso!", status=200)
        except Exception as e:
            return HttpResponse(f"❌ Erro ao atualizar o código: {str(e)}", status=500)
    return HttpResponse("Método não permitido", status=405)

def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render({}, request))
