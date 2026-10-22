# Saifer Browser

<p align="center">
  <img src="assets/saifer-browser-logo.svg" alt="Saifer Browser logo" width="220" />
</p>

<p align="center"><strong>Saifer Browser</strong> · Blue fox, glowing globe, and orange orbit.</p>

<p align="center"><a href="assets/saifer-browser-logo.svg">View the scalable transparent logo (SVG)</a></p>

Saifer Browser is an Android browser project being developed using the user-provided Via Browser 7.3.3 decompiled package as a technical reference.

## Current state

This repository is being organized as the canonical project workspace. The starting source package supplied in the project conversation is a decompiled archive containing Android manifest/resources/assets and Smali files; it is not yet confirmed to be a directly buildable Android Studio project.

## Development principles

- Keep the compact, straightforward browser interaction model that the reference app demonstrates.
- Apply Saifer branding (app name, app icon, logo and brand-specific strings) without introducing unrelated visual redesign.
- Preserve existing browser behavior wherever it can be lawfully and safely retained.
- Do not claim build or device-test success until the corresponding commands and tests have actually completed.
- Keep a record of source provenance, changes, build requirements and known limitations.

## Planned milestones

1. **Inventory** — inspect AndroidManifest, package/application identifiers, SDK targets, resources, assets and Smali entry points.
2. **Build reconstruction** — determine the compatible resource compiler, Smali assembler and packaging/signing toolchain; make the project reproducibly buildable.
3. **Branding** — replace user-facing branding assets/strings with the provided Saifer identity and validate launcher/adaptive icons.
4. **Functional validation** — build a debug package and verify launch, navigation, tabs, bookmarks, history, downloads and other available browser functions.
5. **Release readiness** — resolve blocking issues, document signing/versioning, perform release build and installation checks, and publish artifacts only after successful verification.

## Build status

**Not yet verified.** No installable APK is delivered by this README-only repository snapshot. APK compilation, signing and real-device testing must not be considered complete until logs and artifacts prove success.

## Project inputs

The user-provided archive `Via_7.3.3_src.zip` is the current decompiled-source input. The original APK was provided separately as `Via_7.3.3.apk`. Keep these inputs immutable as reference artifacts and document any output generated from them.

## Licensing and provenance

Before redistributing source-derived code or an APK, verify the upstream app's license and redistribution permissions. Avoid representing this project as official Via software.
