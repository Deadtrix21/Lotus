from helpers.containers.databaseHelper import *


class AutoLoadConfig(BaseModel):
    extensions: str
    listeners: str
    tasks: str

class SpotifyConfig(BaseModel):
    clientId: str
    clientSecret: str

class LavalinkConfig(BaseModel):
    host: str
    port: int
    password: str
    ssl: bool
    heartbeat: int
    spotify: SpotifyConfig

class DatabaseConfig(BaseModel):
    sqlServerUrl: str
    mongoDbUrl: str

class ContainerConfig(BaseModel):
    prefix: List[str]
    database: DatabaseConfig
    lavalink: LavalinkConfig

class DiscordConfig(BaseModel):
    token: str
    applicationVersionName: str
    container: ContainerConfig

class EnvironmentConfig(BaseModel):
    name: str
    development: DiscordConfig
    production: DiscordConfig

class ApplicationConfig(BaseModel):
    autoLoad: AutoLoadConfig
    environment: EnvironmentConfig