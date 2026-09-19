# Orbit Brand Launchpad

A lightweight, customizable Portacode template that deploys a polished shortcut launchpad.

<a href="https://portacode.com/dashboard/?portafile=https%3A%2F%2Fraw.githubusercontent.com%2Finsightifyr%2Fbrand-launchpad-template%2Fmain%2Fportafile.yaml" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Deploy%20with-Portacode-c95d2a?style=for-the-badge" alt="Deploy with Portacode">
</a>

## Deployment inputs

`portafile.yaml` declares these deployment-time inputs:

- `brand_name`
- `welcome_message`
- `accent_color` (six-digit hex color)
- `background_color` (six-digit hex color)
- `logo_file` (optional PNG, JPEG, or WebP upload)

The deployment recipe copies the uploaded logo into the deployment's protected staging area, validates its type and size, converts it to an embedded data URL, and places it in the generated page before the service starts. The deployed app therefore uses the uploaded image without needing a public image URL.

## Files

- `portafile.yaml` — Portacode deployment recipe
- `index.html` — self-contained application
- `configure.py` — applies deployment inputs and embeds the uploaded logo
- `orbit.service` — service definition for port 8080

## Notes

This is a static visual application with no database, authentication, or backend persistence. It uses the device's built-in Python HTTP server.

Direct deployment:

https://portacode.com/dashboard/?portafile=https%3A%2F%2Fraw.githubusercontent.com%2Finsightifyr%2Fbrand-launchpad-template%2Fmain%2Fportafile.yaml

Do not put private credentials in the repository. Uploaded logos are used only during the deployment that receives them.
