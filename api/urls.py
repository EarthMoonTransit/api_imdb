from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import Route, SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views
from .views import (MyTokenObtainPairView, UserViewSet,
                    ReviewsViewSet, CategoryViewSet,
                    TitleViewSet, CommentViewSet, GenresViewSet)


class CustomUserRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list',
                     'post': 'create',
                     },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={'get': 'retrieve',
                     'patch': 'partial_update',
                     'delete': 'destroy',
                     },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),

    ]


class CustomCategoryGenreRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list',
                     'post': 'create',
                     },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={'delete': 'destroy',
                     },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
    ]


router_user = CustomUserRouter()
router_user.register(r'users', UserViewSet)

router_category_genre = CustomCategoryGenreRouter()
router_category_genre.register(r'categories', CategoryViewSet)
router_category_genre.register(r'genres', GenresViewSet)

router = routers.DefaultRouter()
router.register(r'titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews',
    ReviewsViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('users/me/', UserViewSet.as_view(
        {
            'get': 'get_me',
            'patch': 'patch_me',
            'delete': 'delete_me',
        }
    )),
    path('', include(router.urls)),
    path('', include(router_user.urls)),
    path('', include(router_category_genre.urls)),
    path('auth/email/', views.send_confirmation_code),
    path('auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
