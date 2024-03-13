from typing import List, NamedTuple

from app.src.core.models import Product


class FindProductByStatusResponse(NamedTuple):
    products: List[Product]
