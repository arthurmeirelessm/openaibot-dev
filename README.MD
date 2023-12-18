# Solução openaibot - OpenAI (gpt) com Serviços de IA da Azure 

<br> 

<div align="center">

![openai architecture](https://github.com/arthurmeirelessm/openaibot-dev/assets/78212769/afc52efd-98e5-4c15-8bf5-279b5916ba61)


</div>

<br> 

<br> 


**Quais recursos foram utilizados na solução e qual foi a razão pela qual foram escolhidos?**

Essa solução de Chatbot foi desenvolvida com diversas tecnologias avançadas para fornecer uma experiência aprimorada aos usuários. Nesse âmbito, foi utilizado um conjunto de soluções, incluindo SDKs da Microsoft Azure, a poderosa OpenAI e recursos de visão computacional (OCR) externos para alcançar um chatbot robusto e inteligente em Python.


**Microsoft Azure - LUIS (Language Understanding Intelligent Service)**:

O LUIS capacita o chatbot a compreender e interpretar comandos e intenções dos usuários, proporcionando uma análise profunda da linguagem natural.

Melhora na compreensão de perguntas complexas.
Fornecimento de respostas mais precisas.

**Microsoft Azure - Text Analytics**:

O Text Analytics realiza análise de sentimento em avaliações e interações dos usuários, proporcionando insights valiosos sobre a satisfação do usuário.

Permite ajustes contínuos para melhorar a experiência geral.
Oferece uma compreensão mais profunda das emoções dos usuários.

**Microsoft Azure - Azure Speech-to-Text**:

O Azure Speech-to-Text permite a transcrição precisa da entrada de voz dos usuários, convertendo-a em texto para processamento pelo chatbot.

Amplia as opções de interação, permitindo aos usuários fornecerem comandos por voz.
Facilita a entrada de dados sem depender apenas de texto.

**Microsoft Azure - Text-to-Speech**:

O Text-to-Speech converte as respostas do chatbot em fala, proporcionando uma experiência mais dinâmica e envolvente para os usuários.

Torna as interações mais naturais ao oferecer respostas audíveis.
Enriquece a experiência do usuário com feedback de áudio.

**OpenAI - GPT-3 e ChatBot Inteligente:**

A API GPT-3 da OpenAI proporciona ao chatbot capacidades avançadas de processamento de linguagem natural, gerando respostas mais contextuais e dinâmicas.

Maior inteligência na interação com o usuário.
Respostas mais naturalmente contextualizadas.

**Computer Vision com OCR (Optical Character Recognition) - PyPDF2**:

OCR com PyPDF2 extrai texto de PDFs, aprimorando a inteligência do chatbot ao lidar com consultas em bases de conhecimento presentes em documentos PDF.

Enriquece a capacidade do chatbot de extrair informações de documentos.
Aprimora a busca em bases de conhecimento.

**Envio de Mensagens (Notificações pro-ativas com smtplib**:

O uso do smtplib permite ao chatbot enviar e-mails, promovendo uma comunicação eficaz e transparente com os usuários.

Transparência direta na comunicação.
Notificações proativas e personalizadas.
Confirmação de ações e engajamento contínuo.
Comunicação assíncrona eficiente.

<br> 

* **1 - Active Wearables:** Devices or wristbands that continuously transmit patient information.

<br> 

* **2 - Data processing and shaping before being sent to AWS:** This involves extracting data from wearable devices using SDKs, libraries, or CSV files. In this solution, this step is exemplified by a mobile application, which integrates the methods for extracting data from devices and then employs the AWS SDK to transmit the data in a specified format.

<br> 

* **3 - Data Ingestion in AWS:** After the preliminary external data preprocessing, considering its architecture's capability to handle incoming data from numerous wearables simultaneously, AWS IoT Core is employed. In this context, AWS IoT Core serves as the focal point for the arrival and storage of real-time data, which is transmitted via MQTT or HTTP/HTTPS, with security ensured through x.509 certificates or KMS.
<br> 
  
* **4 - Post-Ingestion Processing and Storage:** It comprises a Lambda function triggered by an AWS IoT Core rule, thereby processing or structuring the ingested data and subsequently storing it in an AWS S3 bucket.

<br> 

* **5 - Provided Endpoint (API):** In this phase, a Lambda function is employed to extract and execute a secondary treatment, with the objective of presenting the data in a REST format.

<br> 

* **6 - API Manager Communicating with Lambda:** Step six involves utilizing the AWS API Gateway to oversee our GET endpoint, enabling the retrieval of data with specific parameters such as User ID and Wearable ID. Its security framework relies on AWS IAM, AWS Cognito, and ultimately, AWS WAF (Web Application Firewall).

<br> 

* **7 -Data Analysis:** In this step, services like AWS Glue are utilized to extract data from the S3 bucket containing wearable payloads and transform them into structured data models. Subsequently, AWS Athena is employed to execute SQL queries on data sourced directly from AWS S3 or AWS Glue, which constitutes the foundation of this architecture.
<br> 

* **8 - Dashboard:** The entity responsible for the dashboard is AWS QuickSight, which, in this scenario, can retrieve queried data from AWS Athena and convert it into dashboard insights. This process can incorporate the use of the AWS Cognito authorization and authentication mechanism to ensure restricted user access to your production URL. 

<br> 

* **9 - Machine Learning Recommendation Model:** Here lies the core of our solution. This Machine Learning model, powered by AWS SageMaker, assumes the role of constant data analysis from wearables. It's capable of detecting suspicious changes within this data, potentially identifying illnesses, risks, and patient monitoring. All of this is achieved through the analysis of various data points, including stress levels, heart rate, anomalies, sleep patterns, electrocardiograms, abnormal body temperatures, menstrual calendars, blood pressure, and more.

<br> 

* **10 - Notifier:** In this phase, AWS SNS comes into play, enabling the distribution of this data via topics and subsequently triggering AWS SQS queues. This process effectively organizes each type of recommendation based on user or wearable ID, as generated by the Machine Learning model.

<br> 

* **11 - Microservices (Queues):** Following the AWS SNS notifier, the AWS SQS queue system comes into action. It segregates these recommendation responses into distinct queues, ensuring that each Lambda can autonomously extract this information.

<br> 

* **12 - Notificar usuário:** AWS SES faz a ação de notificar usuários tanto por Email, SMS

<br> 

* **13 - Health Campaigns Section:** This section is designated for users to receive campaigns, such as health plan recommendations, alerts to schedule doctor appointments, health risk notifications, and more.     
