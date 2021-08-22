from matplotlib import pyplot as plt


def criarimg(t1,v1,t2,v2,t3,v3, tipo="barra"):
    grupos = [t1, t2, t3]
    valores = [v1, v2, v3]
    explode = (0.1, 0.1, 0.1 )
    if tipo == 'p':
        plt.pie(valores, labels=grupos, autopct='%1.1f%%', shadow=True, explode=explode)

        plt.legend(grupos, loc=3)

        plt.axis('equal')
    elif tipo == "b":
        plt.bar(grupos, valores)
    elif tipo == "bh":
        plt.barh(grupos, valores)
    nome = v1
    plt.savefig(f'static/png-grafico/{nome}.png')
    plt.close('all')
    return nome
