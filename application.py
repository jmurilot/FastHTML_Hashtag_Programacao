from fasthtml.common import fast_app, serve, Titled, RedirectResponse
from componentes import gerar_titulo, gerar_formulario, gerar_lista_tarefa

app, routes = fast_app()

lista_tarefas = []

@routes("/")
def homepage():
    formulario = gerar_formulario()
    elemento_lista_tarefa = gerar_lista_tarefa(lista_tarefas)
    print(lista_tarefas)
    return Titled("Lista de tarefas", formulario, elemento_lista_tarefa)

@routes("/blog")
def blog():
    return gerar_titulo("Blog","Aprendendo Python e FastHTML")

@routes("/deletar/{posicao}")
def deletar(posicao: int):
    if len(lista_tarefas) > posicao:
        lista_tarefas.pop(posicao)
    return gerar_lista_tarefa(lista_tarefas)

@routes("/adicionar_tarefa", methods=["post"])
def adicionar_tarefa(tarefa: str):
    if tarefa:
        lista_tarefas.append(tarefa)
    return gerar_lista_tarefa(lista_tarefas)



serve()