from rio import Api


class AdminLayout:
    def __init__(self, api: Api):
        self.api = api

    def render_dashboard(self):
        with self.api.layout() as layout:
            layout.title("Painel Administrativo PoT")
            layout.navigation([
                ("Carteira", "/wallet"),
                ("Inventário", "/inventory")
            ])

    def render_wallet(self, form):
        with self.api.layout() as layout:
            layout.title("Gerenciar Carteira")
            layout.navigation([
                ("Dashboard", "/"),
                ("Inventário", "/inventory")
            ])
            form.build()

    def render_inventory(self, form):
        with self.api.layout() as layout:
            layout.title("Gerenciar Inventário")
            layout.navigation([
                ("Dashboard", "/"),
                ("Carteira", "/wallet")
            ])
            form.build()
