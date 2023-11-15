from pydantic import BaseModel


class ZhanFieldSchema(BaseModel):
    id: int
    id_field: int
    # geometry: str # TODO: Find the right type for this one.
    product_ty: str | None = None
    number: float
    n_fldname: str | None = None
    country: str | None = None
    sum_oil_pr: float
    sum_gor: float
    bcm_2012: float
    bcm_2013: float
    bcm_2014: float
    bcm_2015: float
    bcm_2016: float
    bcm_2017: float
    bcm_2018: float
    bcm_2019: float

    class Config:
        orm_mode = True
