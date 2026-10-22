# Development Roadmap

## Phase 1 — Source inventory
- [ ] Record archive checksum and keep the original APK/source archive unchanged.
- [ ] Inspect AndroidManifest.xml, package ID, min/target SDK, activities, services, receivers, providers and permissions.
- [ ] Inventory resource directories, launcher/adaptive icon assets, locales, fonts, native libraries and DEX/Smali package layout.
- [ ] Locate launch activity and high-level browser components from manifest and references.
- [ ] Review the applicable upstream license and redistribution terms.

**Exit criteria:** inventory report exists, entry points are identified, and major unknowns are listed.

## Phase 2 — Reproducible build pipeline
- [ ] Check available Java, Android SDK/build-tools, aapt/aapt2, apktool, smali/baksmali and zipalign/signing utilities.
- [ ] Determine whether the supplied decompiled tree is apktool output or another format.
- [ ] Recover/build resources and Smali without touching the immutable source archive.
- [ ] Record exact commands and tool versions in scripts/docs.
- [ ] Produce a debug APK and retain build logs.
- [ ] Verify package structure, alignment and signature.

**Exit criteria:** a repeatable build command produces a test APK; no success is claimed without output and logs.

## Phase 3 — Saifer branding
- [ ] Update application label in the correct resource(s) and all relevant locales.
- [ ] Replace launcher/adaptive icon assets with the user's supplied Saifer logo.
- [ ] Check monochrome icon treatment and legacy launcher compatibility.
- [ ] Inspect splash and other explicit brand assets without changing unrelated UI.
- [ ] Confirm web content strings and app identity do not show accidental mixed branding.

**Exit criteria:** resource checks pass and a built package presents the intended Saifer identity.

## Phase 4 — Functional validation
- [ ] Cold launch and restart.
- [ ] URL entry, search, load progress, reload, stop, back/forward.
- [ ] Tabs and tab restore behavior.
- [ ] Bookmarks, history and saved data.
- [ ] Downloads, file chooser and external intents.
- [ ] Reader/translation/print or PDF features where available.
- [ ] Permissions, privacy controls and data-clearing flows.
- [ ] Basic network loss, orientation, small-screen and light/dark checks.
- [ ] Review crash/logcat output and fix blocking defects.

**Exit criteria:** test results documented with device/API information; no unresolved release-blocking failures.

## Phase 5 — Release readiness
- [ ] Confirm package ID and version strategy.
- [ ] Keep signing keys private; do not commit them.
- [ ] Run a clean release build, zipalign and signature verification.
- [ ] Install and launch the release APK on a real device/emulator.
- [ ] Publish artifact checksum, release notes and known limitations.
- [ ] Deliver final APK only after the preceding gates are met.

## Working conventions
- Maintain an immutable copy of user-provided source inputs.
- Prefer small, reviewable commits.
- Do not overwrite the default branch until a change is reviewed.
- Treat reconstructed/decompiled code as distinct from original source code.
- Do not claim UI parity or feature parity without tests.
