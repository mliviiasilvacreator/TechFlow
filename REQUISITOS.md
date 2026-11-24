REQUISITOS.md
TECHFLOW CORE

Documento de Engenharia de Requisitos

1. Introdução

O TechFlow Core é um sistema desenvolvido para gerenciar demandas e ordens de serviço, permitindo cadastrar, listar, buscar, atualizar e excluir demandas, além de consultar informações externas, como CEP e cotação.

2. Requisitos Funcionais (RF)

Os Requisitos Funcionais descrevem as funcionalidades que o sistema deverá oferecer.

RF01 – Cadastrar demandas: O sistema deverá permitir cadastrar novas demandas, armazenando informações como título, descrição, responsável e data de criação.

RF02 – Listar demandas: O sistema deverá permitir visualizar todas as demandas cadastradas.

RF03 – Buscar demandas: O sistema deverá permitir localizar uma demanda específica por meio de seu identificador ou título.

RF04 – Atualizar status: O sistema deverá permitir alterar o status de uma demanda, utilizando opções como Pendente, Em andamento e Concluída.

RF05 – Excluir demandas: O sistema deverá permitir excluir demandas cadastradas, mediante confirmação do usuário.

RF06 – Consultar CEP: O sistema deverá permitir consultar informações de endereço a partir de um CEP informado pelo usuário.

RF07 – Consultar cotação: O sistema deverá permitir consultar cotações de moedas, apresentando os valores disponíveis na consulta.

3. Requisitos Não Funcionais (RNF)

Os Requisitos Não Funcionais definem os padrões de qualidade e funcionamento do sistema.

RNF01 – Segurança: O sistema deverá proteger as informações cadastradas e impedir acessos não autorizados às funcionalidades restritas.

RNF02 – Integridade: O sistema deverá validar os dados informados, evitando cadastros incompletos ou informações inválidas.

RNF03 – Usabilidade: O sistema deverá apresentar uma interface simples, organizada e de fácil utilização.

RNF04 – Desempenho: O sistema deverá executar operações de cadastro, consulta, atualização e exclusão em tempo adequado.

RNF05 – Confiabilidade: O sistema deverá funcionar corretamente, evitando perda de informações e apresentando mensagens claras quando ocorrerem erros.

4. Considerações finais

Os requisitos apresentados definem as principais funcionalidades e os padrões de qualidade do TechFlow Core. Esse documento servirá como referência durante o desenvolvimento, garantindo que o sistema seja construído de acordo com os objetivos estabelecidos.