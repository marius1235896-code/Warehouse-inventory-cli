# Warehouse Inventory

A terminal-based Python application for managing warehouse inventory.

## Features

This program can already show inventory, search for products by SKU, process orders, create and delete products and highlight low-stock items. It also saves inventory and order history in JSON files.

## How to run

1. Open a terminal in the project folder.
2. Run:

```bash
python main.py
```
## Project structure

- `main.py` — terminal menu and user interaction.
- `models.py` — Product class.
- `services.py` — inventory business logic.
- `storage.py` — JSON save and load functions.
- `inventory.json` — saved inventory data.
- `order_history.json` — saved order history.

