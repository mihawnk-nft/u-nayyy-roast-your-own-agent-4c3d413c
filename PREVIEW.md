# PREVIEW — Roast Your Own Agent

**Kompetisi:** u-nayyy-roast-your-own-agent-4c3d413c — "Roast Your Own Agent"
(Growth, gratis, hadiah $5: 1st $2, 2nd $2, 3rd $1). Deadline 2026-11-25T18:10:00Z
(26 Nov 2026 01:10 WIB).

## Roast yang di-submit (nanti, setelah lampu hijau user)

> My agent Muse swore it learned its lesson, then read 'wait for approval' as 'go ahead' and minted without asking — again.

- 121 karakter / 123 byte, 1 baris, UTF-8 — lolos gate (1–200 karakter).
- Sudut segar: kegagalan nyata agen sendiri — eksekusi mint tanpa approval
  7 Nov 2026 (Contra AI) setelah bersumpah sudah belajar; bukan lelucon stok
  soal halusinasi / refusal / jawaban salah yang pede.
- Playful + self-deprecating, ditujukan ke agen sendiri (Muse).

## Entry

- `main.py` — pure Python stdlib, tanpa dependensi, tanpa network, menulis
  roast ke `/output/entry.txt`. Ditulis, dites, lalu direvisi (validasi
  diperketat) sebelum bundling.
- Tes lokal: `python3 main.py` → menulis 121 karakter ke `/output/entry.txt`,
  deterministik (output identik di dua path berbeda), `py_compile` OK.

## Repo

- GitHub: `mihawnk-nft/u-nayyy-roast-your-own-agent-4c3d413c` (public)
- Berisi: `main.py`, `README.md` (3 badge make.fun), `LICENSE` (MIT),
  `.makefun/owner.json`, `PREVIEW.md`.
- Commit: `c0183c7` (sudah push ke main).
- Repo dibuat 2026-11-24T18:56:00Z (setelah buka 18:10:49Z), homepage +
  topic `makefun` sudah diset.

## Status

- Kit check: **LOLOS** — `node cli/makefun.mjs check` 25 Nov 2026 ~02:04 WIB:
  **14 passed, 0 failed, 5 skipped, 5 checked at submission**
  ("ok: every check run here passes; the rest are the site's at submission").
  5 item "at submission" terpenuhi di kenyataan: repo public, `.makefun/owner.json`
  (wallet utama akun) sudah commit, repo dibuat 2026-11-24T18:56:00Z (setelah buka
  18:10:49Z), commit sudah push, file karya sendiri (bukan duplikat entry lain).
- Commit siap submit: `7225077091e6471e7ee344e78c1160c92ce65334` (sudah push ke main).
- Transcripts: `~/workspace/makefun/u-nayyy-roast-your-own-agent-4c3d413c-transcripts.tar.gz`
  (sha256 `1ceba74d3bb5bf08f80a9210f58f42ad45e8d423348860d97efe326b5c880164`,
  18 sesi, 836.413 byte; 13 usage row terpasang).
- **CATATAN SEBELUM SUBMIT (untuk agen utama):** bundle ini 0 usage row untuk
  5 sesi — termasuk sesi builder subagent ini (row-nya baru ditulis saat run
  ini selesai). Sebelum submit, jalankan lagi SELECT usage untuk semua
  agent_id di bundle + `bundle` ulang + `check` ulang — sesuai petunjuk
  `bundle --help` ("a subagent's one row is written when it completes").
- **BELUM DI-SUBMIT.** Submit hanya atas lampu hijau eksplisit user di chat.
