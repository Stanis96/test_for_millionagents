import environ

env_environ = environ.Env()
environ.Env.read_env(str(".env"))

ENV = env_environ("ENV")
URL = env_environ("URL")
DB = env_environ("DB")
