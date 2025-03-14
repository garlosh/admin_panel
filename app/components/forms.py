from rio import Api


class ResourceForm:
    def __init__(self, api: Api, service):
        self.api = api
        self.service = service

    def build(self):
        with self.api.form() as form:
            player_id = form.text("ID do Jogador")
            cristais = form.number("Cristais", min=0)
            onix = form.number("Ônix", min=0)
            form.submit("Adicionar Recursos",
                        lambda: self.service.add_recursos(player_id, cristais, onix))


class InventoryForm:
    def __init__(self, api: Api, service):
        self.api = api
        self.service = service

    def build(self):
        with self.api.form() as form:
            player_id = form.text("ID do Jogador")
            item_id = form.number("ID do Item", min=1)
            quantidade = form.number("Quantidade", min=1, max=255)
            form.submit("Adicionar Item",
                        lambda: self.service.add_item(player_id, item_id, quantidade))
