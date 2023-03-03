#
from rest_framework import routers
from django.urls import path, include

#
from .api.item import ItemView
from .api.store import StoreView
from .api.my_bag import MyBagView
from .api.purchase import PurchaseView
from .api.customer import CustomerView
from .api.user_auth import UserAuthView
from .api.store_owner import StoreOwnerView
from .api.item_category import ItemCategoryView
from .api.store_category import StoreCategoryView

router = routers.DefaultRouter()
router.register(r'user_auth', UserAuthView)

urlpatterns = [
    path('', include(router.urls)),
    path('user_auth/login/', UserAuthView.as_view({'post': 'login'}), name='user_auth_login'),
    path('user_auth/register/', UserAuthView.as_view({'post': 'register'}), name='user_auth_register'),
    path('user_auth/logout/', UserAuthView.as_view({'post': 'logout'}), name='user_auth_logout'),
    path('user_auth/verify/', UserAuthView.as_view({'post': 'verify'}), name='user_auth_verify'),
    path('user_auth/reset_password/', UserAuthView.as_view({'post': 'reset_password'}), name='user_auth_reset_password'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #
    path('store_category/<int:id>', StoreCategoryView.check_view),
    path('store_category', StoreCategoryView.as_view()),
    path('item_category/<int:id>', ItemCategoryView.check_view),
    path('item_category', ItemCategoryView.as_view()),
    path('customer/<int:id>', CustomerView.check_view),
    path('customer', CustomerView.as_view()),
    path('store_owner/<int:id>', StoreOwnerView.check_view),
    path('store_owner', StoreOwnerView.as_view()),
    path('store/<int:id>', StoreView.check_view),
    path('store', StoreView.as_view()),
    path('item/<int:id>', ItemView.check_view),
    path('item', ItemView.as_view()),
    path('my_bag/<int:id>', MyBagView.check_view),
    path('my_bag', MyBagView.as_view()),
    path('purchase/<int:id>', PurchaseView.check_view),
    path('purchase', PurchaseView.as_view()),
]
