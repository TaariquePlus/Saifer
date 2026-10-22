# Saifer Branding Patch 0.1.3-alpha

A patched decompiled-source archive was generated from the locally supplied `Via_7.3.3_src.zip` (source archive SHA-256: `fd73128eaaa68d4b4ab99f50d56a61496121596c5e035bfd5e0dbead85af2ac9`).

## Changes applied in the patch archive
- App display label: `res/values/strings.xml`, resource `ce`: `Via` → `Saifer Browser`.
- Adaptive launcher foreground: `res/drawable-xxxhdpi/cc.png` replaced with a resized, transparent user-provided PNG logo.
- Legacy launcher bitmap: `res/mipmap-xxhdpi/ic_launcher.png` replaced with a resized transparent version of the same PNG.
- Adaptive launcher XML continues to point to its existing foreground/background resources.
- The monochrome adaptive icon resource remains unchanged because a correct single-colour mask should be created and visually checked separately.
- Package ID, browser code, permissions and other resource strings were not mass-renamed.

## Artifact
- Local generated archive: `Saifer-Via-7.3.3-Branded-Source-0.1.3-alpha.zip`
- SHA-256: `d4dd9913df13a70ea646d7d9c956c74020789e8af2fbf81963a92c037871285c`
- Archive entries: 8,587
- The archive was structurally checked after writing; the two changed icon images are valid RGBA PNGs and the app label string is present.

## Build status / limits
This is a resource-level patch to the decompiled archive, not a verified APK. The environment used for this patch did not have `apktool`, `aapt/aapt2`, `apksigner`, or `zipalign` available, so no rebuild, signature, installation, or device test is claimed. The complete decompiled archive itself has not yet been uploaded into this GitHub repository; the patched archive must be added as a binary release/asset or uploaded through GitHub's binary upload workflow before it can serve as the repo's full source tree.
