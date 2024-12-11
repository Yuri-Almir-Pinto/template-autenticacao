from abc import ABC, abstractmethod

class LoginTemplate(ABC):
    def realizar_login(self, email: str):
        self.validar_credenciais()
        self.salvar_resultado_validacao(email)
        self.carregar_preferencias()
        self.redirecionar()

    def validar_credenciais(self, *, print_info: bool = True, metodo_auth: str = "Email"):
        def show(*args, **kwargs):
            if print_info:
                print(*args, **kwargs)
        
        if metodo_auth == "Google":
            show("Validando com Google...")
        elif metodo_auth == "GitHub":
            show("Validando com GitHub...")
        elif metodo_auth == "Email":
            show("Validando com Email...")
        else:
            show("Método de autenticação desconhecido.")
            
        

    @abstractmethod
    def salvar_resultado_validacao(self, email: str):
        pass

    @abstractmethod
    def carregar_preferencias(self):
        pass

    @abstractmethod
    def redirecionar(self):
        pass


class LoginFuncionario(LoginTemplate):
    def validar_credenciais(self):
        print("Validando credenciais para funcionário...")
        super().validar_credenciais(metodo_auth="Email")

    def salvar_resultado_validacao(self, email: str):
        self.email = email
        print(f"Resultado da validação salvo para o funcionário: {self.email}")

    def carregar_preferencias(self):
        print("Carregando preferências do funcionário...")

    def redirecionar(self):
        print("Redirecionando para o Dashboard do funcionário.")


class LoginCliente(LoginTemplate):
    def validar_credenciais(self):
        print("Validando credenciais do cliente com Google...")
        super().validar_credenciais(print_info=False, metodo_auth="Google")

    def salvar_resultado_validacao(self, email: str):
        self.email = email
        print(f"Resultado da validação salvo para o cliente: {self.email}")

    def carregar_preferencias(self):
        print("Carregando preferências do cliente...")

    def redirecionar(self):
        print("Redirecionando para a página Home do cliente.")


if __name__ == "__main__":
    # Simulação de login
    usuario_funcionario = LoginFuncionario()
    usuario_funcionario.realizar_login("yuri@gmail.com")

    print("")

    usuario_cliente = LoginCliente()
    usuario_cliente.realizar_login("james@gmail.com")
