from pydantic_settings import BaseSettings, SettingsConfigDict #Nos sirve apra verificar de donde estamos llamando las variables
from pydantic import Field

class Config(BaseSettings):
    
    #allowed_origins:list[str] = Field(default=["http://localhost:3000"], alias="ALLOWED_ORIGINS")
    supabase_url:str = Field(default="", alias="SUPABASE_URL")
    supabase_key:str = Field(default="",alias="SUPABASE_KEY")
    supabase_schema:str =Field(default="public", alias="SUPABASE_SCHEMA")
    table_products:str = Field(default="products", alias="SUPABASEE_TABLE_PRODUCTS")
    #prueba1:str = Field(default = "Hola, prueba1 borrada de .env", alias = "PRUEBA1")
    #prueba2:int = Field(default = 258, alias = "PRUEBA2")
    #allowed:list[str] = Field(default = ["https://www.youtube.com/"], alias = "ALLOWED_ORIGINS")

    model_config = SettingsConfigDict( #Configuracion del modelo
        env_file = ".env",
        env_file_encoding = "utf-8",
        extra = "ignore" #Ignorar variables que no esten declaradas en el modelo
    )

config = Config()

