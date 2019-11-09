from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shop.views import GoodsView, CategoriesView, OrdersView
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'goods', GoodsView)
router.register(r'categories', CategoriesView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('order/', OrdersView.as_view(), name="Order")
]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
