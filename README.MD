# Boddys - Plataforma Social de Treinos

## Visão Geral

Boddys é uma aplicação web desenvolvida em Django que incentiva usuários a manterem uma rotina de exercícios físicos de forma interativa e social. A plataforma permite que os usuários cadastrem e acompanhem seus treinos, interajam com amigos em grupos, criem posts de final de treino, além de visualizar estatísticas de progresso.

## Funcionalidades Principais

- **Autenticação de Usuários:** Cadastro, login e logout de usuários.  
- **Gerenciamento de Grupos:** Criar grupos, entrar em grupos existentes através de um código de acesso, listar grupos que o usuário participa.  
- **Registro de Treinos:** Criar treinos, adicionar séries e exercícios a cada treino.  
- **Exercícios:** Integração com exercícios pré-cadastrados, tanto musculação quanto cardio.  
- **Posts Sociais:** Criar posts associados a grupos, compartilhar conquistas, interagir com outros membros do grupo.

## Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Framework:** Django 3+ (MTV)
- **Banco de Dados:** SQLite (padrão do Django, pode ser alterado)
- **Front-end:** HTML, CSS (personalizável e integrável com frameworks de estilo)
- **Template Engine:** Django Templates

## Estrutura do Projeto

```
boddys_project/
│
├─ boddys_project/
│  ├─ settings.py
│  ├─ urls.py
│  └─ ...
│
├─ core/
│  ├─ templates/core/
│  ├─ views.py
│  ├─ urls.py
│  └─ ...
│
├─ users/
│  ├─ models.py
│  ├─ forms.py
│  ├─ views.py
│  ├─ urls.py
│  ├─ templates/users/
│  └─ ...
│
├─ groups/
│  ├─ models.py
│  ├─ forms.py
│  ├─ views.py
│  ├─ urls.py
│  ├─ templates/groups/
│  └─ ...
│
├─ workouts/
│  ├─ models.py
│  ├─ forms.py
│  ├─ views.py
│  ├─ urls.py
│  ├─ templates/workouts/
│  └─ ...
│
└─ social/
   ├─ models.py
   ├─ forms.py
   ├─ views.py
   ├─ urls.py
   ├─ templates/social/
   └─ ...
```

## Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/boddys.git
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/MacOS
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realize as migrações do banco de dados:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário (opcional, para acessar o admin):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação no navegador:**
   ```
   http://127.0.0.1:8000/
   ```

## Uso

- **Cadastro e Login:** Acesse a página de signup para criar um novo usuário. Faça login para acessar as funcionalidades restritas.
- **Grupos:** Crie um grupo na página de "Meus Grupos" ou entre em um grupo já existente por meio do código de acesso.
- **Treinos:** Na página de treinos, crie novos treinos, edite-os e adicione séries e exercícios.
- **Posts:** Na área social, crie posts para compartilhar conquistas com os membros do seu grupo.

## Explicação dos Casos de Uso

### 1. Registrar Treino

- **Descrição**: Esse caso de uso permite que o usuário crie e registre um novo treino, associando-o à sua conta.
- **Responsável**: Integrante 1  
- **Arquivo**: `workouts/views.py`

```python
@login_required
def criar_treino_view(request):
    if request.method == 'POST':
        form = TreinoForm(request.POST)
        if form.is_valid():
            treino = form.save(commit=False)
            treino.usuario = request.user
            treino.save()
            return redirect('listar_treinos')
    else:
        form = TreinoForm()
    return render(request, 'workouts/criar_treino.html', {'form': form})
```

**Como funciona**:
1. Verifica se há um envio de formulário via `POST`.
2. Se o formulário (`TreinoForm`) for válido, cria um objeto `treino` associado ao usuário logado (`request.user`) e salva no banco de dados.
3. Em caso de sucesso, redireciona o usuário para a página de listagem de treinos.
4. Se o método não for `POST`, exibe o formulário vazio para preenchimento.

### 2. Cadastrar-se no Sistema

- **Descrição**: Este caso de uso possibilita o cadastro de novos usuários no sistema, realizando login automático após a conclusão do processo.
- **Responsável**: Integrante 2  
- **Arquivo**: `users/views.py`

```python
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automático após signup
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
```

**Como funciona**:
1. Se o método for `POST`, lê os dados do formulário (`SignUpForm`).
2. Se o formulário estiver válido, o usuário é criado e o login é feito automaticamente.
3. Em caso de sucesso, é exibida uma mensagem e o usuário é redirecionado para a página inicial.
4. Se houver erros, eles são mostrados para o usuário.
5. Se o método não for `POST`, carrega o formulário vazio para que o usuário possa se cadastrar.

## Dados de Teste e Exercícios Padrão

Ao iniciar o servidor, alguns exercícios padrão (como "Supino Reto", "Agachamento Livre" e "Corrida na Esteira") podem ser criados automaticamente, dependendo da configuração do `ready()` no app `workouts`.

## Licença

Este projeto está sob licença [MIT](LICENSE).