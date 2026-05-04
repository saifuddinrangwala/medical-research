# Public Release Checklist (De-Identification)

Use this checklist before pushing any profile/research updates to a public repository.

## 1) Remove direct identifiers

- [ ] Replace full name with neutral label (for example: `Candidate A`).
- [ ] Redact all unique identifiers (seat number, student ID, roll number, application ID, etc.).
- [ ] Remove personal contact details (phone, email, address, passport, Aadhaar, PAN, etc.).
- [ ] Replace local machine paths with placeholders like `[REDACTED_LOCAL_PATH]/...`.

## 2) Neutralize naming in paths and command files

- [ ] Ensure profile folder slug is non-identifying (for example: `profiles/candidate-a/`).
- [ ] Ensure command filenames are non-identifying (for example: `advice-candidate.md`).
- [ ] Ensure rule filenames are non-identifying.
- [ ] Update all internal links after any folder/file rename.

## 3) Clean contextual leaks

- [ ] Remove references that directly reveal identity through narrative text.
- [ ] Check changelog entries for old names/paths.
- [ ] Check examples/snippets for accidental PII.

## 4) Verify by search (must pass)

Run targeted repo-wide scans for known identifiers before commit:

- [ ] Full name fragments
- [ ] IDs/roll numbers
- [ ] Local path fragments (for example: `C:\Users\...`)
- [ ] Original source filenames that contain identity

## 5) Final validation

- [ ] Open root `README.md` and profile `README.md` and confirm they are de-identified.
- [ ] Open role/rule and command files and confirm no personal names remain.
- [ ] Confirm no raw personal source documents are added to git.
- [ ] Confirm advice quality is still intact after de-identification.

---

## Suggested quick scan pattern (ripgrep)

Use this template and adapt with known strings:

`rg -n -i "full_name_fragment|id_fragment|C:\\\\Users\\\\|passport|aadhaar|pan|phone|email" .`

If any match appears, redact before pushing.
