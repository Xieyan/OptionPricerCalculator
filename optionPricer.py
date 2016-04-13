from math import log, sqrt, exp,pow
from scipy.stats import norm
import random
import numpy

"""European option"""
def eurOptionBSformulas(S,K,T,sigma,r,type):
    d1 = (log(S/K)+r*(T)) / (sigma*sqrt(T)) + 0.5*sigma*sqrt(T)
    d2 = (log(S/K)+r*(T)) / (sigma*sqrt(T)) - 0.5*sigma*sqrt(T)
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    Nd1n = norm.cdf(-d1)
    Nd2n = norm.cdf(-d2)
    C = S*Nd1 - K*exp(-r*(T))*Nd2
    P = K*exp(-r*(T))*Nd2n - S*Nd1n
    if type == 'C':
        return C
    if type == 'P':
        return P
"""Implied volatility calculation"""
def impliedVolCal(callput, value, S, K, t, T, r, q):
    sigma = sqrt(2 * abs((log(S/K) + (r-q)*(T-t)) / (T-t)))
        tol = 1e-5
        sigmadiff = 1
        for i in range(0,100):
            f = fx(callput, value, S, K, t, T, sigma, r, q)
                fprime = fxDe(S, K, t, T, sigma, r, q)
                sigmaNew = sigma - f/fprime
                sigmadiff = abs(sigmaNew - sigma)
                if sigmadiff < tol:
                    return sigmaNew
                sigma = sigmaNew
        return 'NaN'

def fx(callput, value, S, K, t, T, sigma, r, q):
    d1 = (log(S/K)+(r-q)*(T-t)) / (sigma*sqrt(T-t)) + 0.5*sigma*sqrt(T-t)
        d2 = (log(S/K)+(r-q)*(T-t)) / (sigma*sqrt(T-t)) - 0.5*sigma*sqrt(T-t)
        Nd1 = norm.cdf(d1)
        Nd2 = norm.cdf(d2)
        Nd1n = norm.cdf(-d1)
        Nd2n = norm.cdf(-d2)
        C = S*exp(-q*(T-t))*Nd1 - K*exp(-r*(T-t))*Nd2
        P = K*exp(-r*(T-t))*Nd2n - S*exp(-q*(T-t))*Nd1n
        if callput == 'C':
            return C-value
        if callput == 'P':
            return P-value

def fxDe(S, K, t, T, sigma, r, q):
    d1 = (log(S/K)+(r-q)*(T-t)) / (sigma*sqrt(T-t)) + 0.5*sigma*sqrt(T-t)
        yprime = S*exp(-q*(T-t))*sqrt(T-t)*norm.pdf(d1)
        return yprime

"""Geometric Asian call/put option"""
def geoAsianCPCal(S, K, sigma, r, T, n, type):
    sigsqT = pow(sigma,2)*T*(n+1)*(2*n+1)/(6*n*n)
    muT = 0.5*sigsqT + (r-0.5*pow(sigma,2))*T*(n+1)/(2*n)
    d1 = (log(S/K) +(muT + 0.5*sigsqT))/sqrt(sigsqT)
    d2 = d1 - sqrt(sigsqT)
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    Nd1n = norm.cdf(-d1)
    Nd2n = norm.cdf(-d2)
    if type == 'C':
        geo = exp(-r*T)*(S*exp(muT)*Nd1 - K*Nd2)
    if type == 'P':
        geo = exp(-r*T)*(-S*exp(muT)*Nd1n + K*Nd2n)
    return geo

"""Geometric Asian basket call/put option"""
def geoBasketCPCal(S1,S2,K, sigma1,sigma2,cor, r, T, type):
    S = sqrt((S1*S2))
    sigsqT = (pow(sigma1,2)+pow(sigma2,2)+2*sigma1*sigma2*cor)*T/(4)
    
    muT = 0.5*sigsqT + (r - 0.5 * (pow(sigma1,2)+pow(sigma2,2))/2)*T
    d1 = (log(S/K) +(muT + 0.5*sigsqT))/sqrt(sigsqT)
    d2 = d1 - sqrt(sigsqT)
    
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    Nd1n = norm.cdf(-d1)
    Nd2n = norm.cdf(-d2)
    if type == 'C':
        geo = exp(-r*T)*(S*exp(muT)*Nd1 - K*Nd2)
    if type == 'P':
        geo = exp(-r*T)*(-S*exp(muT)*Nd1n + K*Nd2n)
    return geo

"""Control variates for Arithmetric Asian Option"""
def arithAsianCPCal(S, K, sigma, r, T, n, type,M,ctl):
    numpy.random.seed(1000)
    Dt = float(T)/n
    drift = exp((r-0.5*pow(sigma,2))*Dt)
    Spath = [None]*n
    arithPayoff =[None]*M
    geoPayoff = [None]*M
    for i in range(0,M):
        growthFactor =  drift * exp(sigma*sqrt(Dt)*numpy.random.randn())
        Spath[0] = S * growthFactor
        for j in range(1,n):
            growthFactor =  drift * exp(sigma*sqrt(Dt)*numpy.random.randn())
            Spath[j] = Spath[j-1] * growthFactor
        arithMean = numpy.mean(Spath)
        geoMean = exp(1.0/n*numpy.sum(numpy.log(Spath)))
        if type == 'C':
            arithPayoff[i] = exp(-r*T)*numpy.maximum(arithMean-K,0)
            geoPayoff[i] = exp(-r*T)*numpy.maximum(geoMean-K,0)
        
        if type == 'P':
            arithPayoff[i] = exp(-r*T)*numpy.maximum(K-arithMean,0)
            geoPayoff[i] = exp(-r*T)*numpy.maximum(K-geoMean,0)

Pmean = numpy.mean(arithPayoff)
    Pstd = numpy.std(arithPayoff)
    confmlow, comfmup = Pmean-1.96*Pstd/sqrt(M), Pmean+1.96*Pstd/sqrt(M)
    if ctl == 0:
        return confmlow, comfmup

"""Control variate"""
    covXY = numpy.mean(numpy.multiply(arithPayoff,geoPayoff))- numpy.mean(arithPayoff)*numpy.mean(geoPayoff)
    theta = covXY/numpy.var(geoPayoff)
    geo = geoAsianCPCal(S, K, sigma, r, T, n, type)
    
    Z = numpy.add(arithPayoff, numpy.multiply(theta , (numpy.subtract(geo,geoPayoff))))
    Zmean = numpy.mean(Z)
    Zstd = numpy.std(Z)
    
    confcvlow,confcvup = Zmean - 1.96*Zstd/sqrt(M), Zmean + 1.96*Zstd/sqrt(M)
    
    if ctl == 1:
        return confcvlow, confcvup

"""Control variates for Arithmetric Asian Basket Option"""
def arithBasketCPCal(S1,S2,K, sigma1,sigma2,cor, r, T, M, type, ctl):
    numpy.random.seed(1000)
    arithPayoff =[None]*M
    geoPayoff = [None]*M
    for i in range(0,M):
        rdn1 = numpy.random.randn()
        S1T = S1 * exp( (r-0.5*pow(sigma1, 2) * T) + sigma1 * sqrt(T) * rdn1 )
        random2 = cor * rdn1 + sqrt(1 - cor * cor) * numpy.random.randn()
        S2T = S2 * exp( (r-0.5*pow(sigma2, 2) * T) + sigma2 * sqrt(T) * random2 )
        
        arithMean = (S1T+S2T)/2
        geoMean = sqrt(S1T * S2T)
        if type == 'C':
            arithPayoff[i] = exp(-r*T)*numpy.maximum(arithMean-K,0)
            geoPayoff[i] = exp(-r*T)*numpy.maximum(geoMean-K,0)
        
        if type == 'P':
            arithPayoff[i] = exp(-r*T)*numpy.maximum(K-arithMean,0)
            geoPayoff[i] = exp(-r*T)*numpy.maximum(K-geoMean,0)

Pmean = numpy.mean(arithPayoff)
    Pstd = numpy.std(arithPayoff)
    confmlow, comfmup = Pmean-1.96*Pstd/sqrt(M), Pmean+1.96*Pstd/sqrt(M)
    if ctl == 0:
        return confmlow, comfmup

"""Control variate"""
    covXY = numpy.mean(numpy.multiply(arithPayoff,geoPayoff))- numpy.mean(arithPayoff)*numpy.mean(geoPayoff)
    theta = covXY/numpy.var(geoPayoff)
    
    geo = geoBasketCPCal(S1,S2,K,sigma1,sigma2,cor, r, T,  type)
    Z = numpy.add(arithPayoff, numpy.multiply(theta , (numpy.subtract(geo,geoPayoff))))
    Zmean = numpy.mean(Z)
    Zstd = numpy.std(Z)
    
    confcvlow,confcvup = Zmean - 1.96*Zstd/sqrt(M), Zmean + 1.96*Zstd/sqrt(M)
    
    if ctl == 1:
        return confcvlow, confcvup

r = 0.05
T =  3
S = 100
M = 100000
#print geoAsianCPCal(S, 100, 0.3, r, T, 50, 'P')
#print geoAsianCPCal(S, 100, 0.3, r, T, 50, 'C')

#print geoAsianBasketCPCal(100,100,100, 0.3,0.3,0.5, r, T,  'P')
#print geoAsianBasketCPCal(100,100,100, 0.3,0.3,0.5, r, T,  'C')



#print arithAsianCPCal(100, 100, 0.3, r, T, 50, 'P',M,0)
#print arithAsianCPCal(100, 100, 0.3, r, T, 50, 'P',M,1)
#print arithAsianCPCal(100, 100, 0.3, r, T, 50, 'C',M,0)
#print arithAsianCPCal(100, 100, 0.3, r, T, 50, 'C',M,1)

#print arithAsianBasketCPCal(100,100,100, 0.3,0.3,0.5, r, T, M, 'P', 0)
#print arithAsianBasketCPCal(100,100,100, 0.3,0.3,0.5, r, T, M, 'P', 1)
#print arithAsianBasketCPCal(100,100,100, 0.3,0.3,0.5, r, T, M, 'C', 0)
#print arithAsianBasketCPCal(100,100,100, 0.3,0.3,0.5, r, T, M, 'C', 1)