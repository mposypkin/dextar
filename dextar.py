import sympy as sym
import dexdat as dd


print("Run dextar")
f1 = sym.lambdify(dd.x, dd.f1)
print(f1(9))