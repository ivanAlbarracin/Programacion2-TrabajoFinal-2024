from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    info_y_bodegas = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='static/image', null=True)

    def obtener_vecinos(self):
        # Busca las rutas donde esta ciudad es la ciudad de inicio
        rutas_salientes = Route.objects.filter(start_city=self)
        # Genera una lista de tuplas (vecino, distancia)
        vecinos = [(ruta.end_city, ruta.distance) for ruta in rutas_salientes]
        return vecinos

    def __str__(self):
        return self.name

class Route(models.Model):
    start_city = models.ForeignKey(City, related_name='route_start', on_delete=models.CASCADE)
    end_city = models.ForeignKey(City, related_name='route_end', on_delete=models.CASCADE)
    distance = models.FloatField()

    def __str__(self):
        return f"{self.start_city} -> {self.end_city} ({self.distance} km)"
