from rio import Api, Application
from .services.wallet import WalletService
from .services.inventory import InventoryService
from .components import ResourceForm, InventoryForm, AdminLayout

app = Application("Admin Panel")
wallet_service = WalletService()
inventory_service = InventoryService()


@app.page("/")
def home(api: Api):
    layout = AdminLayout(api)
    layout.render_dashboard()


@app.page("/wallet")
def wallet(api: Api):
    layout = AdminLayout(api)
    form = ResourceForm(api, wallet_service)
    layout.render_wallet(form)


@app.page("/inventory")
def inventory(api: Api):
    layout = AdminLayout(api)
    form = InventoryForm(api, inventory_service)
    layout.render_inventory(form)


if __name__ == "__main__":
    app.run()
