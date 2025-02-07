import streamlit as st
import sympy as sp

def solve_quadratic(a, b, c):
    x = sp.Symbol('x')
    equation = a*x**2 + b*x + c
    solutions = sp.solve(equation, x)
    return solutions

def main():
    st.title("Calculadora de Ecuaciones de Segundo Grado")
    st.write("Introduce los coeficientes de la ecuación ax² + bx + c = 0")
    
    a = st.number_input("Coeficiente a", value=1.0, format="%.2f")
    b = st.number_input("Coeficiente b", value=0.0, format="%.2f")
    c = st.number_input("Coeficiente c", value=0.0, format="%.2f")
    
    if st.button("Resolver"):
        if a == 0:
            st.error("El coeficiente 'a' no puede ser 0 en una ecuación cuadrática.")
        else:
            soluciones = solve_quadratic(a, b, c)
            st.write("### Soluciones:")
            for i, sol in enumerate(soluciones, 1):
                st.write(f"Solución {i}: {sol}")

if __name__ == "__main__":
    main()
