from Favourites import views as FavouriteViews
from Later import views as LaterViews
from Trails import views as TrailsViews
from Users import views as userStatsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Trails', TrailsViews.UserCompletedTrailsListView)
router.register('UserStats', userStatsView.UserStatsListView)
router.register('Favourites', FavouriteViews.FavouriteTrailsView)
# TODO:
router.register('Later', LaterViews.LaterTrailsView)
