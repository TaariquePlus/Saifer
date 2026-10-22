# Via 7.3.3 Decompiled Source Audit

Audit input: `Via_7.3.3_src.zip` supplied in the project workspace.

## Integrity
- Archive size: 8,174,436 bytes
- SHA-256: `fd73128eaaa68d4b4ab99f50d56a61496121596c5e035bfd5e0dbead85af2ac9`
- Archive entries: 9,273
- Smali files: 8,586
- Resource entries under `res/`: 547
- Asset entries under `assets/`: 8
- Package ID in decompiled manifest: `mark.via.gp`
- App version: `7.3.3`
- Version code: `20260823`
- apktool metadata version: `2.4.0-261014`
- Compile SDK metadata: 36 / Android 16

## Main manifest entry points
- Launcher/browser shell: `mark.via.Shell` (exported)
- Trampoline: `mark.via.Trampoline` (exported)
- Search: `mark.via.Search` (exported)
- Custom tab: `mark.via.CustomTab` (not exported)
- Download service: `mark.via.service.DownloadService`
- Read-aloud service: `mark.via.service.ReadAloudService`
- Custom Tabs connection: `mark.via.service.CustomTabsConnectionService`

The manifest also includes download/read-aloud receivers, search widget providers, a FileProvider and AndroidX/Firebase/Google service components.

## Build assessment
This is an apktool-style decompiled tree (manifest, `apktool.json`, `smali/`, `res/`, `assets/`, and `original/`), not a Gradle Android Studio project. It has no Gradle wrapper/build files in the archive root. A reproducible rebuild needs compatible apktool/resource framework tooling and Android signing utilities, or a separately engineered Gradle migration.

## Important constraint
The original package ID and Via application entry points must not be casually renamed or replaced before understanding code references, authorities, custom permissions, deep links and integrations. Branding should be applied in resources first. Any package ID change needs a separate, evidence-driven migration.

## Current repository state
The GitHub repository contains branding PNGs in `app/src/main/res/drawable-nodpi/`, but the complete decompiled source tree is not yet committed to the repository, and the Android app module is not yet a complete buildable project. Therefore this audit does not claim that the app is currently buildable or that the launcher icon has been changed in an installed APK.

## Next actions
1. Preserve the source archive and verify its checksum before each use.
2. Inventory the exact launcher/adaptive icon resource names and localized app-label resource keys.
3. Check available apktool/aapt/apksigner versions and build an untouched reference package first.
4. Apply the supplied PNG branding to the appropriate app-owned icon resources, retaining a clean rollback diff.
5. Rebuild, align, sign and install-test only after a reference rebuild succeeds.
