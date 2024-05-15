from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
from bson import ObjectId

load_dotenv()
user_mongo = os.getenv("USER_MONGO")
password_mongo = os.getenv("PASSWORD_MONGO")

# uri = f"mongodb+srv://{user_mongo}:{password_mongo}@cluster0.5lpj1iq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
uri = "mongodb://localhost:27017"

client = AsyncIOMotorClient(uri)
dataBase = client.base_de_datos_tienda
collection = dataBase.productos

#get de todos los productos
async def obtener_todos_los_producto():
  try:
    print('se hizo una peticion de todos los producos')
    productos = []
    cursor = collection.find({})
    async for document in cursor:
      productos.append( document)
    return productos
  
  except Exception as e:
    print(e)
    return False

#insertar un producto
async def insertar_producto(producto):
  try:
    del producto['id']
    id = await collection.insert_one(producto)
    producto_creado = await collection.find_one({"_id": id.inserted_id})
    return producto_creado
  
  except Exception as e:
    print(e)
    return False
  

#conexion de prueba
async def probar_conexion():
  try:
    await client.server_info()
    # Si la conexión tiene éxito, imprime un mensaje indicando que la conexión fue exitosa
    print("La conexión a la base de datos MongoDB fue exitosa.")
  except Exception as e:
    # Si ocurre algún error durante la conexión, imprime un mensaje indicando el error
    print(f"Error al conectar con MongoDB: {e}")
    
async def actualizar_producto(id, producto):
  try:
    producto_actualizado = await collection.update_one({"_id": ObjectId(id)}, {"$set": producto})
    # print(producto_actualizado)
    producto_actualizado = await collection.find_one({"_id": ObjectId(id)})
    return producto_actualizado
  
  except Exception as e: 
    print(e)
    return False
