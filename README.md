# Orbit Brand Launchpad

A lightweight, customizable Portacode template that deploys a polished shortcut launchpad.

## Deployment inputs

`portafile.yaml` declares these deployment-time inputs:

- `brand_name`
- `welcome_message`
- `accent_color`
- `background_color`
- `logo_data_url` (optional)

The deployment recipe applies those values to the generated page before starting the service. The app also includes browser-side customization and export tools for later changes.

## Files

- `portafile.yaml` — Portacode deployment recipe
- `index.html` — self-contained application

## Notes

This is a static visual application with no database, authentication, or backend persistence. It is intended as a quick template concept and uses the device's built-in Python HTTP server.

Deploy with Portacode by supplying the repository's `portafile.yaml`. Do not put private credentials or private logos in the repository.
