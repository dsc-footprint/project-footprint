from Favourites import views as FavouriteViews
from Later import views as LaterViews
from Trails import views as TrailsViews
from Users import views as userStatsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('UserTrails', TrailsViews.UserCompletedTrailsListView)
router.register('users', userStatsView.UserStatsListView)
# TODO:
# router.register('favourites', FvaouriteViews.PostsViewSet)
# router.register('later', LaterViews.LikesViewSet)
