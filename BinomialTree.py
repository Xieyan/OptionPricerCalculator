from math import exp, sqrt

def binominalTree(S, sigma, r, T, K, N, optionType):
	t = T/N
	u = exp(sigma*sqrt(t))
	d = exp(-sigma*sqrt(t))
	p = (exp(r*t)-d) / (u-d)
	StockPrice = {0: [S]}
	for n in range(N):
		StockPrice[n+1] = []
		for price in StockPrice[n]:
			StockPrice[n+1].append(price*u)
		StockPrice[n+1].append(StockPrice[n][-1] * d)

	OptionPrice = {N: []}
	if optionType == 'call':
		for price in StockPrice[N]:
			if price > K:
				OptionPrice[N].append(price-K)
			else:
				OptionPrice[N].append(0.0)
		for n in range(N)[::-1]:
			OptionPrice[n] = []
			for i in range(len(OptionPrice[n+1])-1):
				fu = OptionPrice[n+1][i]
				fd = OptionPrice[n+1][i+1]
				f = exp(-r*t) * (p*fu+(1-p)*fd)
				OptionPrice[n].append( max(f, StockPrice[n][i]-K) )
	if optionType == 'put':
		for price in StockPrice[N]:
			if price < K:
				OptionPrice[N].append(K-price)
			else:
				OptionPrice[N].append(0.0)
		for n in range(N)[::-1]:
			OptionPrice[n] = []
			for i in range(len(OptionPrice[n+1])-1):
				fu = OptionPrice[n+1][i]
				fd = OptionPrice[n+1][i+1]
				f = exp(-r*t) * (p*fu+(1-p)*fd)
				OptionPrice[n].append( max(f, K-StockPrice[n][i]) )
	return OptionPrice[0][0]


if __name__ == '__main__':
	S = float(input("spot price of asset S = "))
	sigma = float(input("volatility sigma = "))
	r = float(input("risk-free interest rate r = "))
	T = float(input("time to maturity (in years) T = "))
	K = float(input("strike K = "))
	N = int(input("number of steps N = "))
	optionType = raw_input("option type (call or put): ")
	optionPrice = binominalTree(S, sigma, r, T, K, N, optionType)
	print "The American "+optionType+" option price is: ", optionPrice