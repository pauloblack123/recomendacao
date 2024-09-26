import numpy as np
from sklearn.cluster import KMeans

fa= np.array ([

  [1, 0, 0, 1],
  [1, 1, 0, 0],
  [0, 1, 1, 0],
  [0, 0, 1, 1],
  [1, 0, 1, 0],
  [0, 1, 0, 1]
])

nc = 2
kmeans = KMeans (n_clusters=nc, random_state=0,n_init=10)

kmeans.fit(fa)

grupo_indice = kmeans.predict(fa)

print("Usuario pertence ao seguinte grupo:")
for i, cluster in enumerate(grupo_indice):
  print(f"Usuario {i+1} pertence ao grupo {cluster+1}")

print("\nfilmes assistidos:")
for i in range (len(fa)):
  assistidos = np.where(fa[i] == 1)[0] + 1
  print(f"Usuário {i+1} assistiu aos filmes: {assistidos}")

  def recomendar_filmes(filmes, fa, grupos_indice):

    filmes = np.array(filmes)

    usuario_id = len(fa)
    grupo_usuario = kmeans.predict([filmes])[0]

    usuarios_no_mesmo_grupo = [i for i in range (len(grupos_indice))
    if grupos_indice [1] == grupo_usuario]

    filmes_recomendados = set()
    for usuario in usuarios_no_mesmo_grupo:
        fa = np.where(fa[usuario] == 1)[0]
        filmes_recomendados.update(fa)

    fa = filmes_recomendados - set(np.where(filmes == 1)[0])

    fa = [filmes + 1 for filme in filmes_recomendados]

    return sorted(filmes_recomendados)
