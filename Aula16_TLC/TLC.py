func = {'norm': stats.norm, 'expon': stats.expon, 'uniform': stats.uniform, 't': stats.t, 
        'chi2': stats.chi2, 'f': stats.f, 'gamma': stats.gamma, 'beta': stats.beta}

#Se não visualizar o pywidgets:
#conda install -c conda-forge ipywidgets

#Função que utiliza o pywidget
@interact(n = (1, 20, 1), distribuição = sorted(list(func.keys())))
def f(distribuição = 'norm', n = 1):
    
    size = 1000
    loc = 0
    scale = 1
    
    arg = {'loc': loc, 'scale': scale, 'size': size}
    
    #Cada distribuição tem seu conjunto de parâmetros específicos
    if distribuição == 't':
        arg['df'] = 5
    elif distribuição == 'chi2':
        arg['df'] = 5
    elif distribuição == 'f':
        arg['dfn'] = 5
        arg['dfd'] = 7
    elif distribuição == 'gamma':
        arg['a'] = 1
    elif distribuição == 'beta':
        arg['a'] = 0.5
        arg['b'] = 0.5
    
    #Gerar n vetores de 1000 amostras cada
    Xb = func[distribuição].rvs(**arg)
    for i in range(n-1):
        Xb += func[distribuição].rvs(**arg)
        
    #Calcular a média
    Xb = Xb / n
    
    #Prints
    fig = plt.figure(figsize=(10,4))
    
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    
    #Histograma
    pd.Series(Xb).hist(normed=True, ax=ax1)
    
    #Fit e print da pdf
    (mu, sigma) = stats.norm.fit(Xb)
    x = np.arange(Xb.min(), Xb.max(), 0.01)
    ax1.plot(x, stats.norm.pdf(x, loc = mu, scale=sigma))
    
    #QQ-Plot
    stats.probplot(Xb, dist=stats.norm, sparams=(mu, sigma), plot=ax2)
    
    return "Média Amostral: {0:0.2f}, Desvio Padrão Amostral: {1:0.2f}\n".format(Xb.mean(),Xb.std())