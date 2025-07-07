# Software Workshop

Welcome to the Software Workshop documentation repository!

This repository contains the source files for building and hosting documentation for a hands-on software skills workshop.

## 📚 Contents

This site includes two main sections:

### 🔹 In-Workshop Resources
Materials used **during** the live sessions, including:
- Python Programming
- Python Plotting
- Unix Shell
- Git Version Control
- Python for Earth Science
- Workflows for Earth Science

### 🔹 Additional Resources
Further learning and references for **after** the workshop.

## 🛠️ Building the Docs Locally

To build the documentation locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Build the HTML docs
make html

# Open in browser
open docs/_build/html/index.html
```

## 🚀 Deployment

This project is set up to automatically build and deploy the documentation to GitHub Pages using a GitHub Actions workflow. The output is published to the `gh-pages` branch.

## 📂 File Structure

```
docs/
├── conf.py               # Sphinx configuration
├── index.rst             # Main table of contents
├── in_workshop/          # In-workshop resources and notebooks
├── additional_resources/ # Post-workshop learning materials
```

## 🧪 Notebooks

Example Jupyter notebooks are included under `docs/in_workshop/` for each topic area. These can be run locally or integrated into interactive environments like Binder.

---

Maintained by the Workshop Organizing Team.
