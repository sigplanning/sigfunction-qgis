import os 

def nombre_capa(path_capa):
    '''
    Esta función regresa el nombre de una capa sin extensión 

    :param path_capa: ruta de la capa
    :type path_capa: str 


    '''
    if "/" in path_capa:
        nombre_capa=(path_capa.split("/")[-1:])[0]
    else:
        nombre_capa=(path_capa.split("\\")[-1:])[0]
    return nombre_capa

def lista_archivos(path, n_ext='.tif'):
    '''
    Ésta función busca dentro de un directorio todos los archivos con el tipo de extensión
    declarada.

    :param path: ruta del direcctorio que contiene los archivos
    :type path: str

    :returns: lista con la ruta de cada archivo localizado en el directorio y subdirectorios
    :rtype: list 
    '''
    lista_shp=[]
    for root, dirs, files in os.walk(path):
        for name in files:
            extension = os.path.splitext(name)
            if extension[1].lower() == n_ext:
                ruta = (root.replace("\\","/")+"/").replace("//","/")+name
                lista_shp.append(ruta)
    return lista_shp

def get_dir(p_file):
    return "/".join(p_file.split(".")[0].split("/")[:-1]) + "/"

def graph_version(p_fig,extension = '.png'):
    vn=1
    fig_dir = get_dir(p_fig)
    fig_files = [nombre_capa(f) for f in lista_archivos(fig_dir, n_ext='.png')]
    name_fig = nombre_capa(p_fig).split(".")[0]
    for nf in fig_files:
        if name_fig in nf:
            vn+=1
    return p_fig.split(".")[0]+f"_v{vn}.png"

def fv_version(p_fv,extension = '.tif'):
    vn=1
    fig_dir = get_dir(p_fv)
    fig_files = [nombre_capa(f) for f in lista_archivos(fig_dir, n_ext='.tif')]
    name_fig = nombre_capa(p_fv).split(".")[0]
    for nf in fig_files:
        if name_fig in nf:
            vn+=1
    return p_fv.split(".")[0]+f"_v{vn}.tif"

    
