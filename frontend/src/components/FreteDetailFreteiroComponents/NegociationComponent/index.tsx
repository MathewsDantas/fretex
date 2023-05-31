import { HeaderContainer, PropostaContainer2 } from "./styles";
import CardsContainer from "../CardsContainer";
import CardProposta from "../CardProposta";
import ModalProposta from "../ModalProposta";
import { useToggle } from "../../../hooks/useToggle";
import {
  type ICliente,
  type IFreteiro,
  type IProposta,
} from "../../../interfaces";
import { isFreteiro } from "../../../utils/isFreteiro";
import { type MouseEvent } from "react";
import Button from "../../Global/Button";

interface INegociation {
  actualUser: IFreteiro | ICliente;
  pedidoId: number;
  propostas: IProposta[];
  ownerPedido: number;
  pedidoVeiculos: number[];
  isLoading: boolean;
}

const NegociationComponent = ({
  actualUser,
  pedidoId,
  propostas,
  ownerPedido,
  pedidoVeiculos,
  isLoading,
}: INegociation): JSX.Element => {
  const { toggle: toggleModalProposta, value: valueModalProposta } =
    useToggle();
  const { toggle: togglePropostasAtivas, value: valuePropostasAtivas } =
    useToggle(true);

  const handleClick = (e: MouseEvent<HTMLElement>): void => {
    e.preventDefault();
    toggleModalProposta();
  };
  let usuarios: number[] = [];
  if (Array.isArray(propostas) && propostas.length > 0) {
    usuarios = Array.from(new Set(propostas.map((p) => p.usuario))).filter(
      (usuario) => usuario !== ownerPedido
    );
  }

  return (
    <>
      <ModalProposta
        toggle={toggleModalProposta}
        value={valueModalProposta}
        actualUser={actualUser}
        actualUserId={actualUser.id}
        pedidoId={pedidoId}
        pedidoVeiculos={pedidoVeiculos}
      />
      <HeaderContainer>
        <div>
          <h2>Negociação</h2>
          {/** <p>Aguardando freteiro</p> */}
        </div>
        {isFreteiro(actualUser) &&
          (propostas.length > 0
            ? propostas.find((p) => p.usuario === actualUser.id) == null
            : true) && (
            <Button
              type="button"
              isButton
              onClick={handleClick}
              isDisabled={isLoading}
            >
              Realizar proposta
            </Button>
          )}
      </HeaderContainer>
      <PropostaContainer2>
        <div>
          <CardsContainer
            title="Propostas ativas"
            toggle={togglePropostasAtivas}
            value={valuePropostasAtivas}
          >
            {usuarios.length === 0 && !isFreteiro(actualUser) && (
              <p>Nenhuma proposta recebida</p>
            )}

            {!isFreteiro(actualUser) && (
              <div className="containerCards">
                {usuarios.length !== 0 &&
                  !isFreteiro(actualUser) &&
                  usuarios.map((usuarioId) => (
                    <CardProposta
                      key={usuarioId}
                      actualUser={actualUser}
                      propostas={propostas}
                      OwnerPropostasId={usuarioId}
                      pedidoId={pedidoId}
                      ownerPedido={ownerPedido}
                    />
                  ))}
              </div>
            )}

            {!usuarios.find((u) => actualUser.id === u) &&
              isFreteiro(actualUser) && <p>Você não fez nenhuma propostas</p>}

            {usuarios.length !== 0 &&
              isFreteiro(actualUser) &&
              !!usuarios.find((u) => actualUser.id === u) && (
                <div className="containerCards" key={actualUser.id}>
                  <CardProposta
                    actualUser={actualUser}
                    propostas={propostas}
                    OwnerPropostasId={actualUser.id}
                    pedidoId={pedidoId}
                    ownerPedido={ownerPedido}
                  />
                </div>
              )}
          </CardsContainer>
        </div>
      </PropostaContainer2>
    </>
  );
};

export default NegociationComponent;
