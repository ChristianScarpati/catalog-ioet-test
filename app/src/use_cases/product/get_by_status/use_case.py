from app.src.exceptions import ProductRepositoryException

from app.src.repositories import ProductRepository

from .request import FindProductByStatusRequest
from .response import FindProductByStatusResponse


class FindProductByStatus:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def __call__(
        self, request: FindProductByStatusRequest
    ) -> FindProductByStatusResponse:
        try:
            get_products_by_status = self.product_repository.get_by_status(
                request.status
            )

            return FindProductByStatusResponse(products=get_products_by_status)
        except ProductRepositoryException as error:
            raise ProductRepositoryException(str(error))
