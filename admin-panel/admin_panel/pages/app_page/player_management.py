from __future__ import annotations

import typing as t
from dataclasses import KW_ONLY, field

import rio
import sys
from pathlib import Path

# Add root directory to path to make services available
sys.path.insert(0, str(Path(__file__).absolute().parent.parent.parent.parent))

from services.inventory import InventoryService
from services.wallet import WalletService


@rio.page(
    name="Player Management",
    url_segment="player-management",

)
class PlayerManagementPage(rio.Component):
    """
    Page for managing player resources and inventory.
    """

    # Form fields for player and resources
    player_id: str = ""
    cristais_amount: str = "0"
    onix_amount: str = "0"
    item_id: str = ""
    item_quantity: str = "1"

    # Status messages
    wallet_status: str = ""
    inventory_status: str = ""

    # Services
    # _wallet_service: WalletService
    # _inventory_service: InventoryService

    def __post_init__(self,):
        # super().__init__(**kwargs)
        self._wallet_service = WalletService()
        self._inventory_service = InventoryService()

    def add_resources(self) -> None:
        """Add resources to a player's wallet"""
        try:
            # Validate inputs
            if not self.player_id:
                self.wallet_status = "Error: Player ID is required"
                return

            cristais = int(self.cristais_amount) if self.cristais_amount else 0
            onix = int(self.onix_amount) if self.onix_amount else 0

            if cristais == 0 and onix == 0:
                self.wallet_status = "Error: At least one resource must be specified"
                return

            # Call service
            result = self._wallet_service.add_recursos(
                player_id=self.player_id,
                cristais=cristais,
                onix=onix
            )

            if result:
                self.wallet_status = f"Success: Added {cristais} cristais and {onix} onix to player {self.player_id}"
            else:
                self.wallet_status = "Error: Failed to add resources"
        except ValueError:
            self.wallet_status = "Error: Invalid resource amount"
        except Exception as e:
            self.wallet_status = f"Error: {str(e)}"

    def add_inventory_item(self) -> None:
        """Add an item to a player's inventory"""
        try:
            # Validate inputs
            if not self.player_id:
                self.inventory_status = "Error: Player ID is required"
                return

            if not self.item_id:
                self.inventory_status = "Error: Item ID is required"
                return

            item_id = int(self.item_id)
            quantity = int(self.item_quantity)

            if quantity <= 0:
                self.inventory_status = "Error: Quantity must be greater than 0"
                return

            # Call service
            result = self._inventory_service.add_item(
                player_id=self.player_id,
                item_id=item_id,
                quantidade=quantity
            )

            if result:
                self.inventory_status = f"Success: Added {quantity} of item {item_id} to player {self.player_id}"
            else:
                self.inventory_status = "Error: Failed to add item to inventory"
        except ValueError:
            self.inventory_status = "Error: Invalid item ID or quantity"
        except Exception as e:
            self.inventory_status = f"Error: {str(e)}"

    def build(self) -> rio.Component:
        return rio.Column(
            rio.Text("Gerenciamento de jogadores", style="heading1"),

            # Wallet Management Section
            rio.Card(
                rio.Column(
                    rio.Text("Gerenciamento de Carteira", style="heading2"),
                    rio.Text(
                        "Adiciona recursos à carteira do jogador", style="dim"),
                    rio.TextInput(
                        text=self.bind().player_id,
                        label="Player ID",
                        # placeholder="Enter player's Alderon ID"
                    ),
                    rio.Row(
                        rio.TextInput(
                            text=self.bind().cristais_amount,
                            label="Cristais",
                            # placeholder="0",
                            # input_type="number"
                        ),
                        rio.TextInput(
                            text=self.bind().onix_amount,
                            label="Onix",
                            # placeholder="0",
                            # input_type="number"
                        ),
                        spacing=1
                    ),
                    rio.Button(
                        "Adicionar Recursos",
                        on_press=self.add_resources,
                    ),
                    rio.Banner(
                        text=self.wallet_status,
                        style="info",
                        margin_top=1,
                    ),
                    spacing=1,
                    margin=2,
                )
            ),

            # Inventory Management Section
            rio.Card(
                rio.Column(
                    rio.Text("Gerenciamento de inventario", style="heading2"),
                    rio.Text(
                        "Adiciona items ao inventário do jogador", style="dim"),
                    rio.TextInput(
                        text=self.bind().player_id,
                        label="Player ID",
                        # placeholder="Enter player's Alderon ID"
                    ),
                    rio.Row(
                        rio.TextInput(
                            text=self.bind().item_id,
                            label="Item ID",
                            # placeholder="Item ID",
                            # input_type="number"
                        ),
                        rio.TextInput(
                            text=self.bind().item_quantity,
                            label="Quantidade",
                            # placeholder="1",
                            # input_type="number"
                        ),
                        spacing=1
                    ),
                    rio.Button(
                        "Adicionar Item",
                        # on_press=self.add_inventory_item,
                    ),
                    rio.Banner(
                        text=self.inventory_status,
                        style="info",
                        margin_top=1,
                    ),
                    spacing=1,
                    margin=2,
                )
            ),

            spacing=2,
            min_width=60,
            margin_bottom=4,
            align_x=0.5,
            align_y=0,
        )
