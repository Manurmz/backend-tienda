from pydantic import BaseModel

class Proveedor(BaseModel):
  nombre_proveedor: str
  precio_de_compra: float
  unidades_por_lote: int