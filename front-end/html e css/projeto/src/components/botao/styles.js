import styled from "styled-components";

export const ButtonContainer = styled.button`
  padding: 20px; /* Aumenta o padding para dar mais espaço dentro do botão */
  border: 1px solid #CDCDCD;
  background: #00AFFA;
  color: white;
  font-size: 24px;
  font-weight: 700;
  width: 100%; /* Garante que o botão ocupe 100% da largura do seu container */
  flex: 1;

  &:hover {
    opacity: 0.6;
  }

  outline: none; /* Remove a borda de foco padrão ao clicar no botão */
  transition: transform 0.1s ease, background-color 0.2s ease; /* Animação suave de clique */

  &:hover {
    opacity: 0.8; /* Efeito no hover para desktop */
  }

  &:active {
    transform: scale(0.95); /* Animação de pressionamento no celular e desktop */
    background-color: #0096D6; /* Mudança na cor ao pressionar */
  }

  /* Remove o highlight azul ao tocar no botão em dispositivos móveis */
  -webkit-tap-highlight-color: transparent;

  /* Remove o comportamento de focus e highlight após o clique */
  &:focus {
    outline: none; /* Desabilita a borda de foco */
  }

  @media (hover: hover) {
    &:hover {
      opacity: 0.8; /* Efeito hover para desktop */
    }
  }

  /* Estilos para dispositivos móveis */
  @media (max-width: 768px) {
    font-size: 20px; /* Ajusta o tamanho da fonte em telas menores */
    padding: 15px;   /* Reduz um pouco o padding para telas menores */
  }

  @media (max-width: 480px) {
    font-size: 18px; /* Reduz ainda mais o tamanho da fonte em celulares */
    padding: 10px;   /* Padding menor para telas pequenas */
  }
`;

