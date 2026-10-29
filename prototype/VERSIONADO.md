# Versionado del rediseño

## Primer punto de retorno

El 29 de octubre de 2026 se guarda el primer draft aceptado como base de trabajo en la rama local `redesign/homepage`, con la etiqueta `draft-01`.

Incluye la segunda propuesta visual, los cinco casos actualizados, los recursos originales de marca, el contenido editable y el generador del lector. El sitio original permanece en `src/`.

Este es el primer snapshot completo del rediseño en Git. `archive-v1/` conserva una copia parcial de los archivos de la primera propuesta; no representa una historia de commits anterior.

## Forma de trabajo

- Guardar cada cambio coherente en un commit descriptivo: contenido, diseño, navegación o funcionalidad.
- Crear etiquetas `draft-02`, `draft-03`, etc. cuando se quiera conservar una versión completa para revisión.
- Mantener los cambios en local hasta que el usuario indique un destino remoto. No hacer push ni desplegar por haber creado un commit o una etiqueta.
- Antes de volver a una versión anterior, conservar el trabajo pendiente. Preferir una nueva rama o un worktree de revisión antes que un reset destructivo.

## Inspección

```sh
git log --oneline --decorate redesign/homepage
git show --stat draft-01
git diff draft-01..HEAD -- prototype package.json
```

El remoto `origin` sigue apuntando al repositorio original y no se modifica. La rama del rediseño no tiene upstream configurado. Un repositorio privado independiente puede recibir este historial más adelante si el usuario lo solicita.

## Respaldo local

Se conserva un bundle con el historial y las referencias del primer draft en `outputs/versionado-website-20261029/cloudfianz-draft-01.bundle`, fuera del checkout del sitio. Se puede restaurar con `git clone` pasando la ruta del bundle y `--branch redesign/homepage` a una carpeta nueva.

El bundle conserva el primer draft, no los commits futuros. No es un respaldo remoto y no protege frente a la pérdida del disco.
