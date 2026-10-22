# Rebuild Instructions

## Current limitation

The decompiled source archive is currently available in the ChatGPT project workspace as `Saifer-Via-7.3.3-Branded-Source-0.1.3-alpha.zip`, but binary archive upload to this repository has not been completed. The GitHub Actions workflow therefore requires a reachable HTTPS URL to that ZIP.

## Run the manual workflow

1. Upload the patched source ZIP to a private release, approved file host, or GitHub release asset that provides a direct HTTPS download URL.
2. Open **Actions → Build patched Via-derived source → Run workflow**.
3. Paste the direct URL in `source_archive_url`.
4. Inspect the workflow logs and download the `saifer-debug-unsigned` artifact if the rebuild succeeds.
5. Do not install an unsigned APK as a release build; signing and installation tests are separate steps.

## Local rebuild

Requirements: Java 17+, a compatible apktool release, and enough disk space for the unpacked source and output.

```bash
java -jar apktool.jar b source -o Saifer-debug-unsigned.apk
```

The input directory must be a valid apktool decompilation, including `AndroidManifest.xml`, `apktool.json`, `res/`, and Smali directories.

## What success means

A successful apktool build only proves resource/Smali packaging succeeded. It does not prove the APK installs, launches, is correctly signed, or works on a device. Those checks must be run and recorded separately.
