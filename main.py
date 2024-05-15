from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.producto import Producto
from database import probar_conexion, insertar_producto, obtener_todos_los_producto, actualizar_producto
from schemas.productoSchema import productoEntity, productosEntity

app = FastAPI()

app.add_middleware(
  CORSMiddleware, 
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
) 

@app.get("/")
def read_root():return {"Hello": "World"}

@app.get("/productos")
async def obtener_productos():
  productos = await obtener_todos_los_producto()
  return productosEntity(productos)

@app.post("/productos")
async def crear_producto(producto:Producto):
  res = await insertar_producto(producto.model_dump())
  if res:
    return productoEntity(res)
  raise HTTPException(status_code=400, detail="Producto no creado")
  # return'producto creado'

# prueba de conexion a mongo
@app.get("/prueba-conexion")
async def prueba_conexion():
  await probar_conexion()
  return 'prueba exitosa'

# Actualizar producto
@app.put("/productos/{id}")
async def actualizar(id:str, producto:Producto):
    res = await actualizar_producto(id, producto.model_dump())
    if res:
        return productoEntity(res)
    raise HTTPException(status_code=404, detail="Producto no encontrado")
