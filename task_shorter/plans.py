from pydantic import BaseModel


class URLBase(BaseModel):
    aim_url: str


class URL(URLBase):
    status: bool


class Config:
    orm_mode = True


class URLInfo(URL):
    url: str
