def mm1_model(lmbda, mu):
    if lmbda >= mu:
        return {"error": "λ must be less than μ for a stable system."}
    
    rho = lmbda / mu
    L = lmbda / (mu - lmbda)
    Lq = (lmbda ** 2) / (mu * (mu - lmbda))
    W = 1 / (mu - lmbda)
    Wq = lmbda / (mu * (mu - lmbda))

    return {
        "rho": round(rho, 4),
        "L": round(L, 4),
        "Lq": round(Lq, 4),
        "W": round(W, 4),
        "Wq": round(Wq, 4)
    }
