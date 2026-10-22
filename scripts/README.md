# Saifer Browser branding patch

This script applies the first Saifer branding pass to an **apktool-decoded Via Browser source tree**. It edits the app label and two existing PNG launcher-icon resources; it does not create a Gradle project or build an APK.

## Run it

1. Decode the original APK with a compatible apktool version.
2. Install Pillow: `python -m pip install Pillow`.
3. Run:

```sh
python scripts/patch_branding.py /path/to/decoded-source /path/to/saifer-logo.png
```

Use the user-provided transparent PNG as the logo. The image is contained proportionally on a transparent square; it is not cropped. The script expects the resource layout found in the audited Via 7.3.3 source archive.

## Scope and limits

- Sets resource `ce` in `res/values/strings.xml` to `Saifer Browser`.
- Replaces `res/drawable-xxxhdpi/cc.png` and `res/mipmap-xxhdpi/ic_launcher.png`.
- Intentionally leaves the package ID, manifest, adaptive-icon XML, monochrome icon, and other resources alone.
- This is a source patch, not a build. Rebuild with apktool and test-install the resulting APK separately. A successful build, signing, or runtime test is not implied.
