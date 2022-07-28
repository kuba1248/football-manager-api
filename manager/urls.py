from django.urls import path

from .views import (
    RegisterApiView,
    LoginView,
    LogoutView,
    EditTeamView,
    PlayerInfoUpdateView,
    SetPlayerOnTransferView,
    TransferMarketList,
    PlayersListView,
    TeamListView,
    TransferPlayer,
    PlayerView,
    TeamView,
)


urlpatterns = [
    path("auth/register/", RegisterApiView.as_view(), name="api-register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("team/edit/", EditTeamView.as_view(), name="edit"),
    path(
        "player/<int:pk>/",
        PlayerInfoUpdateView.as_view(),
        name="edit-player",
    ),
    path(
        "add-to-market/player/<int:pk>/",
        SetPlayerOnTransferView.as_view(),
        name="add-to-market",
    ),
    path("transfer-market/", TransferMarketList.as_view(), name="transfer_market"),
    path(
        "transfer-player/<int:player_id>/<int:team_id>/",
        TransferPlayer.as_view(),
        name="transfer-player",
    ),
    path("players/<int:pk>/", PlayersListView.as_view(), name="all-players"),
    path("teams/", TeamListView.as_view(), name="all-teams"),
    path("player/<int:pk>/", PlayerView.as_view(), name="player"),
    path("team/<int:pk>/", TeamView.as_view(), name="team"),
]
