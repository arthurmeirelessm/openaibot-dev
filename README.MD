# Solução openaibot - OpenAI (gpt) com Serviços de IA da Azure 

<br> 

<div align="center">

![openai architecture](https://github.com/arthurmeirelessm/openaibot-dev/assets/78212769/afc52efd-98e5-4c15-8bf5-279b5916ba61)


</div>

<br> 

<br> 

<h2 style="font-size: 24px; font-weight: bold;">Quais recursos foram utilizados na solução e qual foi a razão pela qual foram escolhidos?</h2>

Essa solução de Chatbot foi desenvolvida com diversas tecnologias avançadas para fornecer uma experiência aprimorada aos usuários. Nesse âmbito, foi utilizado um conjunto de soluções, incluindo SDKs da Microsoft Azure, a poderosa OpenAI e recursos de visão computacional (OCR) externos para alcançar um chatbot robusto e inteligente em Python.

<h3>Microsoft Azure - LUIS (Language Understanding Intelligent Service):</h3>
<p>O LUIS capacita o chatbot a compreender e interpretar comandos e intenções dos usuários, proporcionando uma análise profunda da linguagem natural.</p>
<p><strong>Por que foi usado:</strong></p>
<ul>
  <li>Melhora na compreensão de perguntas complexas.</li>
  <li>Fornecimento de respostas mais precisas.</li>
  <li>Tunelamento e redirecionamentos mais assertivos que antecedem o prompt do usuário no GPT.</li>
  <li>Elegância no reconhecimento de intenções e troca de contextos da conversa</li>
</ul>

<hr>

<h3>Microsoft Azure - Text Analytics:</h3>
<p>O Text Analytics realiza análise de sentimento em avaliações e interações dos usuários, proporcionando insights valiosos sobre a satisfação do usuário.</p>
<p><strong>Por que foi usado:</strong></p>
<ul>
  <li>Permite ajustes contínuos para melhorar a experiência geral.</li>
  <li>Oferece uma compreensão mais profunda das emoções dos usuários.</li>
  <li>Utilização pra contagem de LOGS que podem ser posteriormente armazenados em um Azure Blob Store sendo consumido por um Azure Functions, retratando ou alertando responsáveis melhora contínua do Chatbot</li>
  <li>Finalização contextualizada</li>
</ul>

<hr>

<h3>Microsoft Azure - Azure Speech-to-Text:</h3>
<p>O Azure Speech-to-Text permite a transcrição precisa da entrada de voz dos usuários, convertendo-a em texto para processamento pelo chatbot.</p>
<p><strong>Por que foi usado:</strong></p>
<ul>
  <li>Amplia as opções de interação, permitindo aos usuários fornecerem comandos por voz.</li>
  <li>Facilita a entrada de dados sem depender apenas de texto.</li>
  <li>Deixa o Chatbot mais inclusivo e imersivo.</li>
  <li>Possibilita experiências de usuário mais naturais, aproximando-se da forma como as pessoas se comunicam verbalmente.</li>
  <li>Enriquece as interações ao combinar entrada de voz com respostas geradas pelo GPT, proporcionando uma experiência mais natural e envolvente.</li>
</ul>

<hr>

<h3>Microsoft Azure - Text-to-Speech:</h3>
<p>O Text-to-Speech converte as respostas do chatbot em fala, proporcionando uma experiência mais dinâmica e envolvente para os usuários.</p>
<p><strong>Por que foi usado:</strong></p>
<ul>
  <li>Torna as interações mais naturais ao oferecer respostas audíveis.</li>
  <li>Enriquece a experiência do usuário com feedback de áudio.</li>
  <li>Facilita a comunicação de informações extensas de maneira mais acessível, especialmente para usuários com dificuldades na leitura.</li>
  <li>Oferece uma opção conveniente para consumir conteúdo do chatbot em situações onde a leitura de texto não é prática, como ao dirigir ou realizar outras atividades.</li>
  <li>Possibilita a criação de assistentes virtuais com uma presença mais envolvente e amigável, através da expressividade da fala.</li>
  <li>Integração eficiente com a API GPT, permitindo que as respostas geradas pelo modelo sejam convertidas em fala de maneira coesa e natural.</li>
</ul>

<hr>

<h3>OpenAI - GPT-3 e ChatBot Inteligente:</h3>
<p>A API GPT-3 da OpenAI proporciona ao chatbot capacidades avançadas de processamento de linguagem natural, gerando respostas mais contextuais e dinâmicas.</p>
<p><strong>Por que foi usado:</strong></p>
<ul>
  <li>Maior inteligência na interação com o usuário.</li>
  <li>Respostas mais naturalmente contextualizadas.</li>
 <li>Ampliação da capacidade de compreensão de contextos específicos em uma conversa, permitindo respostas mais personalizadas e relevantes.</li>
  <li>Enriquecimento da experiência do usuário com diálogos mais fluidos e coerentes.</li>
  <li>Possibilidade de lidar com perguntas complexas e cenários diversos, melhorando a adaptabilidade do chatbot.</li>
  <li>Integração eficiente com os serviços da Microsoft Azure, proporcionando uma abordagem abrangente e complementar ao processamento de linguagem natural.</li>
  <li>Aprimoramento da capacidade do chatbot de compreender e gerar conteúdo textual em diversos domínios, contribuindo para um serviço mais versátil.</li>
</ul>

<hr>

<h3>Computer Vision com OCR (Optical Character Recognition) - PyPDF2:</h3>
<p>OCR com PyPDF2 extrai texto de PDFs, aprimorando a inteligência do chatbot ao lidar com consultas em bases de conhecimento presentes em documentos PDF.</p>
<p><strong>Por que foi usado:</strong></p>
<ul>
  <li>Enriquece a capacidade do chatbot de extrair informações de documentos.</li>
  <li>Aprimora a busca em bases de conhecimento.</li>
  <li>Integração eficiente com a API GPT-3 da OpenAI, permitindo respostas mais inteligentes e contextualizadas baseadas no conteúdo extraído pelos serviços de OCR.</li>
  <li>Possibilidade de fornecer respostas mais precisas e relevantes ao usuário, utilizando a base de conhecimento extraída dos documentos PDF.</li>
  <li>Ampliação da capacidade do chatbot de lidar com consultas complexas e específicas presentes nos documentos, oferecendo uma experiência mais completa aos usuários.</li>
</ul>

<hr>

<h3>Envio de Mensagens (Notificações pro-ativas com smtplib):</h3>
<p>O uso do smtplib permite ao chatbot enviar e-mails, promovendo uma comunicação eficaz e transparente com os usuários.</p>
<p><strong>Por que foi usado:</strong></p>
<ul>
  <li>Transparência direta na comunicação.</li>
  <li>Notificações proativas e personalizadas.</li>
  <li>Confirmação de ações e engajamento contínuo.</li>
  <li>Comunicação assíncrona eficiente.</li>
</ul>

<hr>

<h3>Serviços ou recursos que eu adotaria pra integrar com essa solução em um cenário real:</h3>
<ul>
  <li>Azure CosmosDB: Perfeito para armazenamento de contexto e informações do usuário, sem falar que é uma integração extremamente viável, tendo em vista que tudo já é ambiente Microsoft Azure</li>
  <li>Azure Functios: Seria integrado para fazer tratamentos de logs e insoghts vindos da analise de sentimento e armazenados no blob file Storage, seria basicamente um consumer para alertas de análise do Chatbots e melhoria</li>
  <li>Azure Blob File Storage: Armazenamento de logs de análise de texto, histórico de usuário, imagens, áudios e mais</li>
  <li>Azure Private endpoint: Conformidade e segurança no tráfego de informações entre usuário e Azure atráves de um firewall de rede</li>
  <li>Azure Key Vault: Credenciais de SDK Azure guardados em cofre para maior segurança</li>
</ul>



---


<h2 style="font-size: 24px; font-weight: bold;">Recursos detalhados detalhados e arquitetura</h2>

<h3>Contexto: Trata-se de um Chatbot da empresa AeroNavigator (Fictício) que tem como assistente virtual a Aria, onde apropria-se de uma voz neural chamada pt-BR-YaraNeural da Microsoft Azure</h3>

<p>OBS: A numeração a baixo é referente a numeração da arquitetura.</p>

<h2>1 - Uso do LUIS na Navegação Principal do ChatBot:</h2>

<p>No menu principal do seu ChatBot, o Language Understanding Intelligent Service (LUIS) desempenha um papel crucial no reconhecimento de intenções, permitindo uma interação mais inteligente e direcionada com os usuários. Eis como o LUIS é aplicado nesse contexto:</p>

<strong>Reconhecimento de Entrada:</strong>
<ul>
  <li>O LUIS é configurado para analisar a entrada do usuário no menu principal, identificando a intenção subjacente por meio de técnicas avançadas de processamento de linguagem natural.</li>
</ul>

<strong>Redirecionamento para Bots/Classes Correlacionados:</strong>
<ul>
  <li>Com base na intenção identificada, o LUIS orienta o ChatBot a redirecionar o usuário para a classe ou módulo específico correspondente à sua intenção, personalizando a experiência do usuário.</li>
</ul>

<strong>Explicação Básica de Intenções:</strong>
<ul>
  <li><strong>Back:</strong> Permite o retorno a opções anteriores, facilitando a navegação.</li>
  <li><strong>ExploreTheWorld:</strong> Oferece informações e curiosidades sobre destinos, incentivando a exploração.</li>
  <li><strong>GotoOut:</strong> Indica a intenção de sair do bot ou finalizar a interação.</li>
  <li><strong>Login:</strong> Facilita o acesso seguro à conta do usuário.</li>
  <li><strong>None:</strong> Intenção padrão acionada quando não é possível reconhecer nenhuma intenção específica.</li>
  <li><strong>PerfectTrip:</strong> Antecede e conduz o usuário para curiosidades específicas de destinos de viagem.</li>
  <li><strong>Register:</strong> Direciona os usuários para o processo de cadastro no bot.</li>
  <li><strong>User_Register:</strong> Específica para a coleta de informações pessoais como nome e e-mail durante o registro.</li>
</ul>

<p>Ao utilizar o LUIS nesse cenário, a experiência do usuário é otimizada, garantindo que suas intenções sejam compreendidas e atendidas de maneira eficiente, resultando em interações mais naturais e personalizadas.</p>

<img width="959" alt="luis" src="https://github.com/arthurmeirelessm/openaibot-dev/assets/78212769/37cf536f-21d6-4da5-8e02-c80898e1b0c8">

<h3>2 - Design e estrutura</h3>
<p>A estrutua do bot consiste em Arquitetura de Bot Modular e também de cascata, que é usuado em formulários e perguntas consequentes. O bot contém uma classe orquestradora que divide os modulos de entrada do usuário e redirecionam pra classe reconhecida pelo LUIS correlacionada: </p>

<img width="588" alt="menuprincipal" src="https://github.com/arthurmeirelessm/openaibot-dev/assets/78212769/ecf0f876-1e08-4b90-a216-21079dc0811e">

<p> Sendo assim, o usuário entra -> Dá o input -> LUIS reconhece e manda pras classes/bots correlacionados a Cadastro, Sua viagem perfeita, Desbravar o mundo.</p>


<h3>3 - Bot de cascata Purchase</h3>

<p>No ChatBot, a opção "Cadastro" aciona o bot de registro, um módulo cuidadosamente correlacionado por meio do Language Understanding Intelligent Service (LUIS). Aqui está uma explicação do fluxo de interações:</p>

<strong>Bot de Registro (LUIS - Register_User):</strong>
<ul>
  <li>O usuário escolhe a opção "Cadastro" no menu principal.</li>
  <li>O LUIS identifica a intenção "Register_User", encaminhando o usuário para o bot de registro.</li>
  <li>O bot de registro coleta informações como nome e e-mail do usuário, garantindo uma interação personalizada.</li>
  <li>Com base nas informações fornecidas, se bem-sucedido, o usuário é redirecionado para o próximo estágio.</li>
</ul>

<strong>Bot de Compra (PurchaseBot):</strong>
<ul>
  <li>O usuário, após o registro bem-sucedido, é encaminhado para o bot de compra.</li>
  <li>O bot de compra pergunta ao usuário sobre o destino desejado para a viagem.</li>
  <li>Em seguida, utiliza visão computacional OCR no arquivo PDF "tickets" para extrair informações de passagens disponíveis.</li>
  <li>Esses dados são integrados ao GPT para fornecer uma resposta contextualizada e inteligente ao usuário.</li>
  <li>O usuário tem a opção de realizar outra compra ou finalizar a interação.</li>
</ul>

<strong>Bot de FAQ (FAQBot):</strong>
<ul>
  <li>Caso o usuário opte por finalizar, é redirecionado para o bot de FAQ.</li>
  <li>O bot de FAQ avalia os comentários do usuário sobre o serviço de assistência da área.</li>
  <li>Proporciona respostas informativas e soluciona dúvidas frequentes.</li>
</ul>

<p>Esse fluxo estruturado garante uma experiência de usuário contínua, oferecendo desde o registro até a avaliação de serviços, tudo dentro de um ambiente amigável e eficiente.</p>


