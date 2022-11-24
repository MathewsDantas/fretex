from core.api.renders import CustomRenderer
from django.contrib.auth.models import User
from plataform.api.serializers import (RegisterClienteSerializer, RegisterFreteiroSerializer, LoginSerializer, UserSerializer, ClienteSerializer, EnderecoSerializer, FreteiroSerializer, PedidoSerializer, ProdutoSerializer, PropostaSerializer, TipoVeiculoSerializer, VeiculoSerializer)
from plataform.models import (Cliente, Endereco, Freteiro, Pedido, Produto, Proposta, TipoVeiculo, Veiculo)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from core.api.helpers import open_api_request_body
from drf_yasg import openapi
from rest_framework.authtoken.models import Token

class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = []
    renderer_classes = [CustomRenderer]
    serializer_class = None

    @action(detail=False, methods=['post'], serializer_class=LoginSerializer)
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email)

        if len(user) == 0:
            return Response({'detail': 'Credenciais incorretas 0'})
        user = user[0]
        success = user.check_password(password)
        if not success:
            return Response({'detail': 'Credenciais incorretas 1'})

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

    @action(detail=False, methods=['get'])
    def user(self, request):
        return Response({'user': UserSerializer(request.user).data})

    @action(detail=False, methods=['post'], serializer_class=RegisterFreteiroSerializer)
    def register_freteiro(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        freteiro = serializer.save()
        return Response(UserSerializer(freteiro.user_ptr).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], serializer_class=RegisterClienteSerializer)
    def register_cliente(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cliente = serializer.save()
        return Response(UserSerializer(cliente.user_ptr).data, status=status.HTTP_201_CREATED)

class EnderecoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EnderecoSerializer
    queryset = Endereco.objects.all()
    renderer_classes = [CustomRenderer]


class FreteiroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FreteiroSerializer
    queryset = Freteiro.objects.all()
    renderer_classes = [CustomRenderer]


class ClienteViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    renderer_classes = [CustomRenderer]


class PedidoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()
    renderer_classes = [CustomRenderer]

    def create(self, request, *args, **kwargs):
        request.data['cliente'] = cliente=Cliente.objects.get(user_ptr=self.request.user)
        request.data['status'] = 'EN'
        return super().create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(
    #         cliente=Cliente.objects.get(user_ptr=self.request.user),
    #         status='EN',
    #     )


class ProdutoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()
    renderer_classes = [CustomRenderer]


class TipoVeiculoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TipoVeiculoSerializer
    queryset = TipoVeiculo.objects.all()
    renderer_classes = [CustomRenderer]


class VeiculoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VeiculoSerializer
    queryset = Veiculo.objects.all()
    renderer_classes = [CustomRenderer]


class PropostaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PropostaSerializer
    queryset = Proposta.objects.all()
    renderer_classes = [CustomRenderer]

