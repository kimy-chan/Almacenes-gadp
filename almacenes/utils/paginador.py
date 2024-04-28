from django.core.paginator import Paginator

def paginador_general(request,lista_model):
    pagina = request.GET.get('page',1) 
    try:
        paginador = Paginator(lista_model,3)
        paginador_model=paginador.page(pagina)
    except :
        paginador_model= paginador.page(1)
    return paginador_model