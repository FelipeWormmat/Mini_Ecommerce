from os import name
import pytest
from fastapi.testclient import TestClient
import factory
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from app.db.db import get_db
from app.models.models import Base, Category, Customer, PaymentMethods, Product, User, Supplier, ProductDiscount
from app.app import app


@pytest.fixture()
def db_session():
    engine = create_engine('sqlite:///./test.db',
                           connect_args={'check_same_thread': False})
    Session = sessionmaker(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield Session()


@pytest.fixture()
def override_get_db(db_session):
    def _override_get_db():
        yield db_session

    return _override_get_db


@pytest.fixture()
def client(override_get_db):
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    return client


@pytest.fixture()
def user_factory(db_session):
    class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = User
            sqlalchemy_session = db_session

        id = None
        display_name = factory.Faker('name')
        email = factory.Faker('email')
        role = None
        password = '' 

    return UserFactory

@pytest.fixture()
def adress_test(db_session):
    class Adress_Test(factory.alchemy.SQLAlchemyModelFactory):
        class Test:
            model: Category
            sqlalchemy_session = db_session


        id = factory.Faker('pyint')
        address = factory.Faker('name')
        city = factory.faker('name')
        state = factory.faker('name')
        number = factory.faker('name')
        zipcode = factory.faker('name')
        neighbourhood = factory.faker('name')
        primary = factory.faker('name')
        customer_id = factory.faker('name')
        customer = factory.faker('customer.id')


    return Adress_Test

@pytest.fixture()
def category_test(db_session):
    class Category_Test(factory.alchemy.SQLAlchemyModelFactory):
        class Test:
            model: Category
            sqlalchemy_session = db_session


        id = factory.Faker('pyint')
        name = factory.Faker('name')

    return Category_Test


@pytest.fixture()
def payment_test(db_session):
    class Payment_Test(factory.alchemy.SQLAlchemyModelFactory):
        class Test:
            model: PaymentMethods
            sqlalchemy_session = db_session


        id = factory.Faker('pyint')
        name = factory.Faker('name')
        enabled = True

    return Payment_Test

@pytest.fixture()
def product_discount_test(db_session):
    class Product_Discount_Test(factory.alchemy.SQLAlchemyModelFactory):
        class Test:
            model: ProductDiscount
            sqlalchemy_session = db_session


        id = factory.Faker('pyint')
        name = factory.Faker('name')
        value = factory.Faker('pyfloat')
        product =  factory.SubFactory(product_test)
        payment_method =  factory.SubFactory(payment_test)

    return Product_Discount_Test

@pytest.fixture()
def product_test(db_session):
    class Product_Test(factory.alchemy.SQLAlchemyModelFactory):
        class Test:
            model: Product
            sqlalchemy_session = db_session

            id = factory.Faker('pyint')
            description =  factory.Faker('name')
            price = factory.Faker('pyfloat')
            technical_details = factory.Faker('name')
            image  = factory.Faker('name')
            visible = True
            category =  factory.SubFactory(category_test)
            supplier = factory.SubFactory(supplier_test)


    return Product_Test


@pytest.fixture()
def supplier_test(db_session):
    class Supplier_Test(factory.alchemy.SQLAlchemyModelFactory):
        class Test:
            model: Supplier
            sqlalchemy_session = db_session


        id = factory.Faker('pyint')
        name = factory.Faker('name')

    return Supplier_Test

@pytest.fixture()
def costumer_test(db_session):
    class Customer_Test(factory.alchemy.SQLAlchemyModelFactory):
        class Test:
            model: Customer
            sqlalchemy_session = db_session


        id = factory.Faker('pyint')
        name = factory.Faker('name')
        first_name = factory.faker('name')
        last_name = factory.faker('name')
        phone_number = factory.faker('?')
        genre = factory.faker('?')
        document_id = factory.faker('?')
        birth_date = factory.faker('pyfloat')

    return Customer_Test


@pytest.fixture()
def user_admin_token(user_factory):
    user_factory(role='admin')

    return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjY1NDIwODc0fQ.o_syoOwrg8VOvl5nWYnA0waXxL0pFLdUgJY8HoqMVjM'


@pytest.fixture()
def admin_auth_header(user_admin_token):
    return {'Authorization': f'Bearer {user_admin_token}'}
