# Play Console worksheet

Answers for the forms under Play Console → Policy and programs → App content, and the release steps.

## Before going live

These block a public release (see CLAUDE.md, "Before going live"):

- [x] Written permission to distribute the papers (received 30 Oct 2026): Pariksha Niyamak Pradhikari,
      Uttar Pradesh, Prayagraj (updeled.gov.in) for UPTET and Super TET, and CBSE for CTET.
- [x] Tested on a device, and every question checked against the official final key (all `verified`).
- [x] Papers marked `distribution_cleared: true` and the pack `release_ready: true` (content 2026.10.30-release.1).
- [ ] Privacy policy hosted at a public URL (`privacy-policy.html`, with `CONTACT_EMAIL` filled in), e.g. on
      GitHub Pages or Google Sites.
- [ ] 2 to 8 phone screenshots (see `listing.md`).

An internal or closed testing track can go ahead earlier for the teacher pilot: only invited testers can
install it.

## App content forms

**Privacy policy**: the hosted URL of `privacy-policy.html`.

**App access**: All functionality is available without special access (no login).

**Ads**: No, the app does not contain ads.

**Content rating** (IARC questionnaire): category *Reference, News, or Educational*. Answer No to violence,
sexuality, language, controlled substances, gambling, user-generated content, user interaction and sharing
location. Expected rating: Everyone / 3+.

**Target audience and content**: 18 and over (teacher exam candidates). Not designed for children; the store
listing does not target children.

**News app**: No.

**Government apps**: No. The app is not developed by or for a government. The listing and the About screen
carry the "not affiliated" disclaimer and name the official sources, as Play's policy on apps that provide
government information asks.

**Financial features, health, VPN, etc.**: None.

**Data safety**:
- Does your app collect or share any of the required user data types? **No.**
- Everything the app stores stays on the device (SQLite) and is never transmitted. Feedback is given in a
  Google Form opened in the browser, and the banner opens WhatsApp; data typed there goes to those services,
  not through the app.
- Is all user data encrypted in transit? Not applicable (nothing is transmitted).
- Can users request data deletion? Users delete all data by uninstalling the app or clearing its storage.

**Permissions**: only `WRITE_EXTERNAL_STORAGE`, limited to Android 9 and older (saving a paper to Downloads).
No declaration form is needed.

## Store settings

- App category: **Education**
- Contact email: required, shown on the listing
- Countries: India
- Price: Free

## Building and uploading

```
flutter test
flutter analyze
dart run tool/validate_content.dart
flutter build appbundle --release
```

Add `--dart-define=FEEDBACK_FORM_URL=https://docs.google.com/forms/d/e/.../viewform` (and the field IDs, see
`lib/config.dart`) to show the feedback buttons.

Upload `build/app/outputs/bundle/release/app-release.aab`. It is signed with the upload key from
`android/key.properties`; enrol in Play App Signing when creating the app (the default), and keep the
keystore in `C:/Users/meher/.uptet-saathi-signing/` backed up: losing it means asking Google for an upload
key reset.

For every later upload, raise the build number in `pubspec.yaml` (`version: 1.0.1+2`, and so on); Play rejects
a version code it has seen before. Bump `content_version` in the pack whenever the content changes.
