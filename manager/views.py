from django.shortcuts import get_object_or_404, render
from rest_framework import generics, response, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from .lib.utils import Util


from .models import Player, Team, User
from .serializers import (
    EditTeamSerializer,
    PlayerInfoUpdateSerializer,
    RegisterSerializer,
    SetPlayerOnTransferSerializer,
    UserLoginSerializer,
    TransferMarketSerializer,
    TransferPlayerSerializer,
    TeamsSerializer,
)

# Create your views here.


class RegisterApiView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
                return response.Response(
                    {"message": "Success", "data": serializer.data},
                    status=status.HTTP_201_CREATED,
                )
            except Exception as err:
                return response.Response(
                    {"message!": str(err)}, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return response.Response(
                {"message!": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    token, _ = Token.objects.get_or_create(user=user)
                    return response.Response(
                        data={
                            "token": token.key,
                            "success": "You've successfully Logged in",
                        },
                        status=status.HTTP_200_OK,
                    )

            except User.DoesNotExist:
                return response.Response(
                    data={
                        "message": "error",
                        "data": "Ensure email and password are correct and you have verified your account",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        return response.Response(
            data={"success": "You've been logged out"}, status=status.HTTP_200_OK
        )


class EditTeamView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = EditTeamSerializer
    queryset = Team.objects.all()

    def patch(self, request, *args, **kwargs):
        team = get_object_or_404(Team, user__id=request.user.id)
        serializer = self.serializer_class(Team, data=request.data, partial=True)
        if serializer.is_valid():
            team.name = serializer.validated_data["name"]
            team.country = serializer.validated_data["country"]
            team.save()
            return response.Response(
                self.serializer_class(team).data, status=status.HTTP_202_ACCEPTED
            )
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlayerInfoUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = PlayerInfoUpdateSerializer
    queryset = Player.objects.all()

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        team = get_object_or_404(Team, user__id=request.user.id)
        player = get_object_or_404(Player, pk=kwargs["pk"])

        if team != player.team:
            return response.Response(
                data={"message": "You are unauthorized for that action"},
                status=status.HTTP_403_FORBIDDEN,
            )

        if serializer.is_valid():
            player.first_name = (
                serializer.validated_data["first_name"] or player.first_name
            )
            player.last_name = (
                serializer.validated_data["last_name"] or player.last_name
            )
            player.country = serializer.validated_data["country"] or player.country

            player.save()

            return response.Response(
                {
                    "message": "Successfully updated",
                    "data": self.serializer_class(player).data,
                },
                status=status.HTTP_200_OK,
            )
        return response.Response(
            data=serializer.errors, status=status.HTTP_404_NOT_FOUND
        )


class SetPlayerOnTransferView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = SetPlayerOnTransferSerializer
    queryset = Player.objects.all()

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        team = get_object_or_404(Team, user__id=request.user.id)
        player = get_object_or_404(Player, pk=kwargs["pk"])

        # if team.user != request.user:
        if team != player.team:
            return response.Response(
                data={"message": "You are unauthorized for that action"},
                status=status.HTTP_403_FORBIDDEN,
            )

        if serializer.is_valid():
            transfer_status = serializer.validated_data["transfer_status"]

            if transfer_status != "A":
                return response.Response(
                    data={
                        "message": "You can not set market value without adding player to transfer list"
                    },
                    status=status.HTTP_403_FORBIDDEN,
                )

            player.market_value = serializer.validated_data["market_value"]
            player.transfer_status = serializer.validated_data["transfer_status"]

            player.save()

            return response.Response(
                {
                    "message": "Successfully Added to transfer",
                    "data": self.serializer_class(player).data,
                },
                status=status.HTTP_200_OK,
            )
        return response.Response(
            data=serializer.errors, status=status.HTTP_404_NOT_FOUND
        )


class TransferMarketList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = TransferMarketSerializer

    def get_queryset(self):
        return Player.objects.filter(transfer_status="A")
    
class TransferPlayer(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = TransferPlayerSerializer

    def get_queryset(self):
        return Player.objects.filter(transfer_status="A")

    def get(self, request, *args, **kwargs):
        try:

            team = Team.objects.all()
            current_team = team.get(user=request.user)

            new_team = team.get(id=kwargs["team_id"])
            player = self.get_queryset().get(pk=kwargs["player_id"])
            if (new_team.team_budget >= player.market_value) and (
                new_team.id != current_team.id
            ):
                # remove player from current team and recalculate budget and team value
                current_team.team_budget += player.market_value 
                current_team.value -= player.player_value
                print(current_team.value)

                # transfer player to new team and recalculate budget, team value and player value
                new_team.team_budget -= player.market_value
                player.team = new_team
                player.player_value = Util.player_value(player.player_value)
                new_team.value += player.player_value
                player.transfer_status = "UA"
                player.market_value = 0.0
                player.save()
                new_team.save()
                current_team.save()
                return response.Response(
                    self.serializer_class(player).data, status=status.HTTP_200_OK
                )

            else:
                raise Exception("You cant buy your own player or budget not enough")

        except Exception as error:
            return response.Response(
                {"error": f"{error}"}, status=status.HTTP_400_BAD_REQUEST
            )

    
class TeamListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = TeamsSerializer
    queryset = Team.objects.all()


class TeamView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = TeamsSerializer

    def get_queryset(self):
        return Team.objects.all()


class PlayersListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = TransferPlayerSerializer

    def get_queryset(self):
        return Player.objects.filter(team__id=self.kwargs["pk"])


class PlayerView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = TransferMarketSerializer
    queryset = Player.objects.all()