# Orbit Brand Launchpad

A lightweight, customizable Portacode template that deploys a polished shortcut launchpad.

<a href="https://portacode.com/dashboard/?portafile=https%3A%2F%2Fraw.githubusercontent.com%2Finsightifyr%2Fbrand-launchpad-template%2Fmain%2Fportafile.yaml" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Deploy%20with-Portacode-c95d2a?style=for-the-badge" alt="Deploy with Portacode">
</a>

## Deployment inputs

`portafile.yaml` declares these deployment-time inputs:

- `brand_name`
- `welcome_message`
- `accent_color`
- `background_color`
- `logo_url` (optional public HTTPS image URL)

The deployment recipe applies those values to the generated page before starting the service. The app also includes browser-side customization and export tools for later changes.

## Files

- `portafile.yaml` — Portacode deployment recipe
- `index.html` — self-contained application
- `configure.py` — applies deployment inputs
- `orbit.service` — service definition for port 8080

## Notes

This is a static visual application with no database, authentication, or backend persistence. It uses the device's built-in Python HTTP server.

You can also open the deployment directly:

https://portacode.com/dashboard/?portafile=https%3A%2F%2Fraw.githubusercontent.com%2Finsightifyr%2Fbrand-launchpad-template%2Fmain%2Fportafile.yaml

Do not put private credentials or private logos in the repository.
