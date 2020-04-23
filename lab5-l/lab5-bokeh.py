from bokeh.plotting import figure, save

# создание окна и указание заголовка
p = figure(title="Интерактивная карта")

print(p)

# Список координат
x_coords = [0,1,2,3,4]
y_coords = [5,4,1,2,0]

# создание точки на карте
p.circle(x=x_coords, y=y_coords, size=10, color="red")

outfp = r"./bokeh/points.html"

save(obj=p, filename=outfp)

