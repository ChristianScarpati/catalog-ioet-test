import pytest

from app.src.use_cases import GetProductsRequest, GetProductsCase, GetProductsResponse
from app.src.core.models import Product
from adapters.src.repositories import MemoryProductRepository


class TestGetProductsCase:

    def test__get_products_case__with_status__should_return_only_products_with_same_status(
        self,
    ):
        # Arrange
        request = GetProductsRequest(status="Used")
        product_repository = MemoryProductRepository()
        product_repository.products = [
            Product(
                product_id="1",
                user_id="1",
                name="Headphones",
                description="Noise cancellation",
                price=10.5,
                location="Quito",
                status="Used",
                is_available=True,
            ),
            Product(
                product_id="2",
                user_id="2",
                name="Jacket",
                description="Official ioet jacket",
                price=20,
                location="Loja",
                status="Used",
                is_available=True,
            ),
            Product(
                product_id="3",
                user_id="3",
                name="Mac mini",
                description="With the M1 chip",
                price=20,
                location="Guayaquil",
                status="New",
                is_available=False,
            ),
        ]
        get_products_case = GetProductsCase(
            product_repository=product_repository.products
        )

        # Act
        response = get_products_case(request=request)

        # Assert
        assert response == GetProductsResponse(
            products=[
                Product(
                    product_id="1",
                    user_id="1",
                    name="Headphones",
                    description="Noise cancellation",
                    price=10.5,
                    location="Quito",
                    status="Used",
                    is_available=True,
                )._asdict(),
                Product(
                    product_id="2",
                    user_id="2",
                    name="Jacket",
                    description="Official ioet jacket",
                    price=20,
                    location="Loja",
                    status="Used",
                    is_available=True,
                )._asdict(),
            ]
        )

    def test__get_products_case__with_status__should_fail_if_products_has_different_status(
        self,
    ):

        # Arrange
        request = GetProductsRequest(status="New")
        product_repository = MemoryProductRepository()
        product_repository.products = [
            Product(
                product_id="1",
                user_id="1",
                name="Headphones",
                description="Noise cancellation",
                price=10.5,
                location="Quito",
                status="New",
                is_available=True,
            ),
            Product(
                product_id="2",
                user_id="2",
                name="Jacket",
                description="Official ioet jacket",
                price=20,
                location="Loja",
                status="New",
                is_available=True,
            ),
            Product(
                product_id="3",
                user_id="3",
                name="Mac mini",
                description="With the M1 chip",
                price=20,
                location="Guayaquil",
                status="Used",
                is_available=False,
            ),
        ]
        get_products_case = GetProductsCase(
            product_repository=product_repository.products
        )

        # Act
        response = get_products_case(request=request)

        # Assert
        assert response != GetProductsResponse(
            products=[
                Product(
                    product_id="1",
                    user_id="1",
                    name="Headphones",
                    description="Noise cancellation",
                    price=10.5,
                    location="Quito",
                    status="New",
                    is_available=True,
                )._asdict(),
                Product(
                    product_id="2",
                    user_id="2",
                    name="Jacket",
                    description="Official ioet jacket",
                    price=20,
                    location="Loja",
                    status="New",
                    is_available=True,
                )._asdict(),
                Product(
                    product_id="3",
                    user_id="3",
                    name="Mac mini",
                    description="With the M1 chip",
                    price=20,
                    location="Guayaquil",
                    status="Used",
                    is_available=False,
                )._asdict(),
            ]
        )
        assert pytest.raises(
            AssertionError,
            match="assert {'products': [{'product_id': '1', 'user_id': '1', 'name': 'Headphones', 'description': 'Noise cancellation', 'price': Decimal('10.5'), 'location': 'Quito', 'status': 'New', 'is_available': True}, {'product_id': '2', 'user_id': '2', 'name': 'Jacket', 'description': 'Official ioet jacket', 'price': Decimal('20'), 'location': 'Loja', 'status': 'New', 'is_available': True}, {'product_id': '3', 'user_id': '3', 'name': 'Mac mini', 'description': 'With the M1 chip', 'price': Decimal('20'), 'location': 'Guayaquil', 'status': 'Used', 'is_available': False}]} == {'products': [{'product_id': '1', 'user_id': '1', 'name': 'Headphones', 'description': 'Noise cancellation', 'price': Decimal('10.5'), 'location': 'Quito', 'status': 'New', 'is_available': True}, {'product_id': '2', 'user_id': '2', 'name': 'Jacket', 'description': 'Official ioet jacket', 'price': Decimal('20'), 'location': 'Loja', 'status': 'New', 'is_available': True}, {'product_id': '3', 'user_id': '3', 'name': 'Mac mini', 'description': 'With the M1 chip', 'price': Decimal('20'), 'location': 'Guayaquil', 'status': 'Used', 'is_available': False}]}",
        )
