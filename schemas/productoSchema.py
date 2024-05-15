from models.producto import Producto
from models.proveedor import Proveedor

def productoEntity(producto:dict) -> Producto:
  if '_id' in producto.keys():
    aux_id = str(producto['_id'])
    producto.pop('_id')
    producto['id'] = aux_id
  proveedores_data = producto.pop('proveedores',[])
  proveedores = [Proveedor(**prov) for prov in proveedores_data]
  return Producto(proveedores=proveedores, **producto)

def productosEntity(productos:list) -> list:
    return [productoEntity(producto) for producto in productos]