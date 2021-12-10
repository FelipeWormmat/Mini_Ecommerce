from fastapi import APIRouter
from .product.views import router as product_router
from .category.views import router as category_router
from .supplier.views import router as supplier_router 
from .payment_methods.views import router as payment_methods_router
from .product_discount.views import router as product_discount_router
from .coupons.views import router as coupons_router
from .adress.views import router as adress_router
from .customers.views import router as customer_router
from .auth.views import router as auth_router
from .user.views import router as user_router
from .admin.views import router as admin_router
from .order.views import router as order_router
from .category.views import router as catalog_router


from .seed import router as seed_router


router = APIRouter()

router.include_router(product_router, prefix='/products', tags=['product'])
router.include_router(category_router, prefix='/categories', tags=['category'])
router.include_router(supplier_router, prefix='/suppliers', tags=['supplier'])
router.include_router(payment_methods_router, prefix='/paymentmethods', tags=['payment-method'])
router.include_router(product_discount_router, prefix='/prodcuctdiscounts', tags=['product-discount'])
router.include_router(coupons_router, prefix='/coupons', tags=['coupons'])
router.include_router(adress_router, prefix='/adress', tags=['adress'])
router.include_router(customer_router, prefix='/customer', tags=['customer'])


router.include_router(seed_router, tags=['seed'])
router.include_router(user_router, prefix='/users', tags=['users'])
router.include_router(auth_router, prefix='/auth', tags=['auth'])
router.include_router(admin_router, prefix='/admin', tags=['admin'])
router.include_router(order_router, prefix='/order', tags=['order'])
router.include_router(catalog_router, prefix='/catalog', tags=['catalog'])
