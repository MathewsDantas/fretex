import React from "react";
import { Container, Description, Title } from "./styles";
import { Wrapper } from "../../styles";
import HomeBox from "../../components/HomeBox/index";
import freteiro from "../../assets/images/caminhao.svg";
import cliente from "../../assets/images/cliente.svg";
import negociacao from "../../assets/images/negociacao.svg";
import HomeVideoSection from "../../components/HomeVideoSection";
import SectionVantagens from "../../components/SectionVantagens";
import Footer from "../../components/Footer";

const Home = () => {
  return (
    <>
      <HomeVideoSection />
      <Wrapper>
        <Title>Como a FreteX funciona?</Title>

        <Description>
          Nós facilitamos a oferta do serviço de frete em todo o Brasil,
          atendendo Clientes e Freteiros Autônomos.
        </Description>

        <Container>
          <HomeBox
            title="Clientes"
            desc="Eles publicam os fretes em nossa plataforma"
            img={cliente}
          />
          <HomeBox
            title="Freteiros"
            desc="Eles procuram os fretes compatíveis e de seu interesse"
            img={freteiro}
            line={true}
          />
          <HomeBox
            title="Negociação"
            desc="Ambos negociam diretamente o frete, sem intermediário"
            img={negociacao}
          />
        </Container>
      </Wrapper>
      <SectionVantagens/>
      <Footer/>
    </>
  );
};

export default Home;
