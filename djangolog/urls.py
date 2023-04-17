from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/account/', include('account.urls', namespace='account')),
    path('api/image/', include('image.urls', namespace='image')),
    path('api/category/', include('category.urls', namespace='category')),
    path('api/contact/', include('contact.urls', namespace='contact')),
    path('api/gig/', include('gig.urls', namespace='gig')),
    path('api/comment/', include('comment.urls', namespace='comment')),
    path('api/package/', include('package.urls', namespace='package')),
    path('api/chat/', include('chat.urls', namespace='chat')),
    path('api/profile/', include('profiles.urls', namespace='profile')),
    path('api/advertisement/', include('advertisement.urls', namespace='advertisement')),
    path('api/order/', include('order.urls', namespace='order')),
    path('api/event/', include('event.urls', namespace='event')),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
