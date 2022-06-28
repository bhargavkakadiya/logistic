class Logistic(pm.Parameterized):
    l = pm.Number(1, bounds=(1, 5), precedence=0.1)
    m = pm.Number(15, bounds=(1, 21e6), step=50000, precedence=1)
    
    def f(self, x):
        """Parameterized Logistic Function"""
        x1 = 1
        y1 = 1e6
        x2 = 15
        y2 = 1e8
        
        # return self.k/(1+np.exp(-x*(self.l - self.s))) + self.m
        return (((1 / (1 + np.exp((-5)*((self.l * x - x1) / (x2 - x1) - 0.5)))) * (1 / 0.8483) - 0.0894)*(y2 - y1) + y1)

    def x(self):
        x = np.linspace(1, self.m, self.m)
        return x

    def curve(self, x):
        y = self.f(x)
        return pd.DataFrame(zip(x, y), columns=['supply', 'price'])

    def view(self):
        x = self.x()
        return self.curve(x).hvplot.line(title='Bonding Curve', x='supply', y='price')
      
s = Logistic()

pn.Row(s, s.view)
