# se-lab5

A small inventory management demo that was used to practice static analysis and fixing common issues reported by tools like Pylint, Flake8, and Bandit.

Overview
- Simple inventory operations are implemented in [`addItem`](inventory_system.py), [`removeItem`](inventory_system.py), [`getQty`](inventory_system.py), [`loadData`](inventory_system.py), [`saveData`](inventory_system.py), [`printData`](inventory_system.py), and [`checkLowItems`](inventory_system.py).
- Inventory is stored in [`inventory.json`](inventory.json).

Quick start
- Run the demo:
  ```sh
  python3 inventory_system.py

  Inspect or edit the inventory in inventory.json.
Notes from the static analysis work

A short write-up of the remediation process and lessons learned is available in reflection.md.
A concise list of issues found and how they were fixed is in issue_table.md.
Final static analysis outputs are included as reports:
pylint_report_fixed.txt
flake8_report_fixed.txt
bandit_report_fixed.txt
Repository files

inventory_system.py
inventory.json
reflection.md
issue_table.md
pylint_report.txt
pylint_report_fixed.txt
flake8_report.txt
flake8_report_fixed.txt
bandit_report.txt
bandit_report_fixed.txt