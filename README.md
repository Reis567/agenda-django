# Django Project - Agenda
Versão em português no final (Portuguese version at the end)

This is a Django project developed by Reis567. The purpose of this project is to create a web application for managing contacts, allowing users to create, view, update, and delete contacts, as well as providing user registration and authentication features.

## Features

- User Registration: Users can register for the application by providing basic information such as name, last name, email, username, and password.
- User Authentication: Users can log in using their registered credentials.
- User Information Update: Users can update their personal information such as name, last name, and email.
- Contact Management: Users can create, view, update, and delete contacts. Each contact has fields such as name, last name, phone, email, description, and category.
- Contact Search: Users can search for contacts based on search criteria such as name, last name, phone, and email.
- Contact Pagination: Contacts are displayed in pages, with the option to navigate between pages.
- Access Restriction: Certain functionalities of the application, such as creating, updating, and deleting contacts, require user authentication.

## Technologies Used

- Django: Python web development framework.
- HTML: Markup language for structuring web pages.
- CSS: Styling language for defining the appearance of web pages.
- Bootstrap: CSS library for creating responsive and stylized web interfaces.
- SQLite Database: Lightweight and embedded database used by Django to store application data.

## Project Structure

The project is organized as follows:

- The main directory of the project is named `contacts`.
- The main application of the project is named `contact`.
- The `contact` application consists of the following components:
  - Models: `Category` and `Contact` to represent categories and contacts.
  - URLs: Configuration of the application's URLs.
  - Views: View functions to process user requests.
  - Forms: Definition of forms used in the views.
  - Admin: Configuration of the Django admin panel to manage the models.

## Installation and Execution

To run the project locally, follow these steps:

1. Make sure you have Python installed on your machine.
2. Clone the project repository: `git clone https://github.com/Reis567/agenda-django`.
3. Navigate to the project directory: `cd project`.
4. Create a virtual environment: `python -m venv venv`.
5. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`.
   - Linux/Mac: `source venv/bin/activate`.
6. Install project dependencies: `pip install -r requirements.txt`.
7. Run database migrations: `python manage.py migrate`.
8. Create a superuser: `python manage.py createsuperuser`.
9. Start the development server: `python manage.py runserver`.
10. Access the application in your browser: `http://localhost:8000`.

## Conclusion

This Django project developed by Reis567 is a web application for contact management. It provides comprehensive features for user registration, authentication, and contact management, allowing users to easily create, view, update, and delete contacts. The application utilizes Django and web technologies to deliver a user-friendly and responsive experience.

I hope this README.md is helpful in explaining your Django project. Feel free to customize it according to the specific characteristics of your project.





# PORTUGUÊS

# Projeto Django - Agenda

Este é um projeto Django desenvolvido por Reis567. O objetivo deste projeto é criar um aplicativo web para gerenciar contatos, permitindo ao usuário criar, visualizar, atualizar e excluir contatos, além de fornecer recursos de registro e autenticação de usuários.

## Funcionalidades

- Registro de usuário: os usuários podem se registrar no aplicativo fornecendo informações básicas, como nome, sobrenome, email, nome de usuário e senha.
- Autenticação de usuário: os usuários podem fazer login utilizando suas credenciais registradas.
- Atualização de informações do usuário: os usuários podem atualizar suas informações pessoais, como nome, sobrenome e email.
- Gerenciamento de contatos: os usuários podem criar, visualizar, atualizar e excluir contatos. Cada contato possui campos como nome, sobrenome, telefone, email, descrição e categoria.
- Pesquisa de contatos: os usuários podem pesquisar contatos com base em critérios de busca, como nome, sobrenome, telefone e email.
- Paginação de contatos: os contatos são exibidos em páginas, com a opção de navegar entre as páginas.
- Restrição de acesso: determinadas funcionalidades do aplicativo, como criação, atualização e exclusão de contatos, exigem que o usuário esteja autenticado.

## Tecnologias Utilizadas

- Django: framework de desenvolvimento web em Python.
- HTML: linguagem de marcação para estruturar as páginas web.
- CSS: linguagem de estilização para definir a aparência das páginas web.
- Bootstrap: biblioteca de CSS para criar interfaces web responsivas e estilizadas.
- Banco de Dados SQLite: banco de dados leve e incorporado ao Django para armazenar os dados do aplicativo.

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

- O diretório principal do projeto é chamado `contatos`.
- O aplicativo principal do projeto é chamado `contact`.
- O aplicativo `contact` possui os seguintes componentes:
  - Modelos: `Category` e `Contact` para representar as categorias e os contatos.
  - URLs: configuração das URLs do aplicativo.
  - Views: funções de visualização para processar as requisições do usuário.
  - Forms: definição dos formulários utilizados nas views.
  - Admin: configuração do painel de administração do Django para gerenciar os modelos.

## Instalação e Execução

Para executar o projeto localmente, siga estas etapas:

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone o repositório do projeto: `git clone https://github.com/Reis567/agenda-django`.
3. Acesse o diretório do projeto: `cd project`.
4. Crie um ambiente virtual: `python -m venv venv`.
5. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`.
   - Linux/Mac: `source venv/bin/activate`.
6. Instale as dependências do projeto: `pip install -r requirements.txt`.
7. Execute as migrações do banco de dados: `python manage.py migrate`.
8. Crie um superusuário: `python manage.py createsuperuser`.
9. Inicie o servidor de desenvolvimento: `python manage.py runserver`.
10. Acesse o aplicativo no navegador: `http://localhost:8000`.

## Conclusão

Este projeto Django desenvolvido por Reis567 é um aplicativo web de gerenciamento de contatos. Ele fornece recursos completos para registro, autenticação e gerenciamento de contatos, permitindo que os usuários criem, visualizem, atualizem e excluam contatos de forma fácil e eficiente. O aplicativo utiliza o Django e tecnologias web para fornecer uma experiência amigável e responsiva ao usuário.

Espero que este README.md seja útil para explicar o seu projeto Django. Sinta-se à vontade para personalizá-lo de acordo com as características específicas do seu projeto.
