# Solução openaibot - OpenAI (gpt) com Serviços de IA da Azure 

<br> 

<div align="center">

![openai architecture](https://github.com/arthurmeirelessm/openaibot-dev/assets/78212769/afc52efd-98e5-4c15-8bf5-279b5916ba61)


</div>

<br> 

<br> 

**Quais recursos foram utilizados na solução e qual foi a razão pela qual foram escolhidos?**

Essa solução de Chatbot foi desenvolvida com diversas tecnologias avançadas para fornecer uma experiência aprimorada aos usuários. Nesse âmbito, foi utilizado um conjunto de soluções, incluindo SDKs da Microsoft Azure, a poderosa OpenAI e recursos de visão computacional (OCR) externos para alcançar um chatbot robusto e inteligente em Python.

<h3>Microsoft Azure - LUIS (Language Understanding Intelligent Service):</h3>
<p>O LUIS capacita o chatbot a compreender e interpretar comandos e intenções dos usuários, proporcionando uma análise profunda da linguagem natural.</p>
<p><strong>Por que foi usado::</strong></p>
<ul>
  <li>Melhora na compreensão de perguntas complexas.</li>
  <li>Fornecimento de respostas mais precisas.</li>
</ul>

<hr>

<h3>Microsoft Azure - Text Analytics:</h3>
<p>O Text Analytics realiza análise de sentimento em avaliações e interações dos usuários, proporcionando insights valiosos sobre a satisfação do usuário.</p>
<p><strong>Por que foi usado::</strong></p>
<ul>
  <li>Permite ajustes contínuos para melhorar a experiência geral.</li>
  <li>Oferece uma compreensão mais profunda das emoções dos usuários.</li>
</ul>

<hr>

<h3>Microsoft Azure - Azure Speech-to-Text:</h3>
<p>O Azure Speech-to-Text permite a transcrição precisa da entrada de voz dos usuários, convertendo-a em texto para processamento pelo chatbot.</p>
<p><strong>Por que foi usado::</strong></p>
<ul>
  <li>Amplia as opções de interação, permitindo aos usuários fornecerem comandos por voz.</li>
  <li>Facilita a entrada de dados sem depender apenas de texto.</li>
</ul>

<hr>

<h3>Microsoft Azure - Text-to-Speech:</h3>
<p>O Text-to-Speech converte as respostas do chatbot em fala, proporcionando uma experiência mais dinâmica e envolvente para os usuários.</p>
<p><strong>Por que foi usado::</strong></p>
<ul>
  <li>Torna as interações mais naturais ao oferecer respostas audíveis.</li>
  <li>Enriquece a experiência do usuário com feedback de áudio.</li>
</ul>

<hr>

<h3>OpenAI - GPT-3 e ChatBot Inteligente:</h3>
<p>A API GPT-3 da OpenAI proporciona ao chatbot capacidades avançadas de processamento de linguagem natural, gerando respostas mais contextuais e dinâmicas.</p>
<p><strong>Por que foi usado::</strong></p>
<ul>
  <li>Maior inteligência na interação com o usuário.</li>
  <li>Respostas mais naturalmente contextualizadas.</li>
</ul>

<hr>

<h3>Computer Vision com OCR (Optical Character Recognition) - PyPDF2:</h3>
<p>OCR com PyPDF2 extrai texto de PDFs, aprimorando a inteligência do chatbot ao lidar com consultas em bases de conhecimento presentes em documentos PDF.</p>
<p><strong>Por que foi usado::</strong></p>
<ul>
  <li>Enriquece a capacidade do chatbot de extrair informações de documentos.</li>
  <li>Aprimora a busca em bases de conhecimento.</li>
</ul>

<hr>

<h3>Envio de Mensagens (Notificações pro-ativas com smtplib):</h3>
<p>O uso do smtplib permite ao chatbot enviar e-mails, promovendo uma comunicação eficaz e transparente com os usuários.</p>
<p><strong>Por que foi usado::</strong></p>
<ul>
  <li>Transparência direta na comunicação.</li>
  <li>Notificações proativas e personalizadas.</li>
  <li>Confirmação de ações e engajamento contínuo.</li>
  <li>Comunicação assíncrona eficiente.</li>
</ul>



