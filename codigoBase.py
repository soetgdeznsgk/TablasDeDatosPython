import pandas as pd

datos1 = {
    "x(m)" : [0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2],
    "F(N)" : [2.2, 6.3, 12.2, 20.3, 30.2, 42.3, 56.2, 72.3, 90.2, 100]
}

datos2 = {
    "Tiempo(s) + o - 1 s (con 95% de confiabilidad)" : [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330],
    "Lectura Voltimetro (V) + o - 0.1V (con 95% de confiabilidad)" : [6.0, 5.2, 4.5, 3.9, 3.4, 2.9, 2.6, 2.2, 1.9, 1.7, 1.4, 1.2, 1.1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.5, 0.4, 0.4, 0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
}

df1, df2 = pd.DataFrame(datos1), pd.DataFrame(datos2)
#with open("a.html", "w") as _file:         si ambas cumpieran en la misma página de un pdf
#    _file.write(df1.head(11).to_html() + "\n\n" + df2.head(34).to_html()) 

df1.to_html("Desktop/tabla1.html")
df2.to_html("Desktop/tabla2.html")
