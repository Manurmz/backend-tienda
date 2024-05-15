from pydantic import BaseModel
from typing import List, Optional
from models.proveedor import Proveedor
from bson import ObjectId

class Producto(BaseModel):
  id: Optional[str] = None
  nombre: str
  descripcion: str
  proveedores: List[Proveedor]
  precio_de_venta: float
  categoria: str
  unidades: int
  aleta_stock: int
  stock_optimo: int
  anotaciones: str = 'ninguna'
  codigo:str
