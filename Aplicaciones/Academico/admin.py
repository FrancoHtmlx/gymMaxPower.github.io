from django.contrib import admin
from .models import Cliente
from .models import Entrenador
from .models import Clase
from .models import Caja
from .models import Productos
from .models import Facturas
from .models import Rutinas
from .models import Recibos

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Entrenador)
admin.site.register(Clase)
admin.site.register(Caja)
admin.site.register(Productos)
admin.site.register(Facturas)
admin.site.register(Rutinas)
admin.site.register(Recibos)

