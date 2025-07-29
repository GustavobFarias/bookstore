from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import git

import json

@csrf_exempt
def update(request):
    if request.method == "POST":
        try:
            print("🚀 Webhook recebido!")
            payload = request.body
            data = json.loads(payload)
            print("Payload recebido:", data)

            repo = git.Repo('/home/gfarias/bookstore')
            origin = repo.remotes.origin
            origin.pull()
            return HttpResponse("✅ Código atualizado com sucesso!", status=200)
        except Exception as e:
            return HttpResponse(f"❌ Erro ao atualizar o repositório: {e}", status=500)
    return HttpResponse("Método não permitido", status=405)