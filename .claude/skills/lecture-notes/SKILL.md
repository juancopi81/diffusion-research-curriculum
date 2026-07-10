---
name: lecture-notes
description: Turn a lecture video (YouTube URL or local file) into structured Markdown study notes using the Video Moment Finder (vmf) MCP connector — transcript plus blackboard frames. Use when the user asks for lecture notes, study notes, or enrichment notes from a video, or mentions "vmf" with a lecture.
---

# Lecture video → study notes (via Video Moment Finder)

End-to-end workflow: obtain the video locally, index it in Video Moment Finder,
then synthesize notes from its transcript and blackboard frames. The MCP
`lecture_notes` prompt is NOT agent-invocable (prompts are a user-side
primitive in supported clients) — this skill embeds the full recipe instead.
Do not attempt to invoke the prompt as an MCP tool.

## Inputs to collect (ask only for what's missing)

- YouTube URL **or** local video file path.
- Course context: course name, professor, lecture number and topic
  (e.g. "Stat 110 (Harvard), Prof. Joe Blitzstein, Lecture 31: Markov Chains").
- Output path. Honor an explicit path from the user. Otherwise inspect existing
  notes and use lowercase underscore-separated names:
  - Planned curriculum lecture: `notes/wNN_<course>_<topic>.md`, for example
    `notes/w08_stat110_lln_clt.md`.
  - Off-curriculum lecture: `notes/<course>_enrichment_lNN_<topic>.md`, for
    example `notes/stat110_enrichment_l31_markov_chains.md`.
  - If the source has no lecture number, omit the `lNN` component.
  Do not attach an enrichment lecture to the current or most recent week just
  because that is when it was watched.
- Optionally: the user's own handwritten notes (text or pasted photos).

## Preflight (before downloading anything)

1. Confirm the vmf MCP connector is available (its tools are named like
   `upload_video`, `get_video_status`, `get_transcript`, `get_frames`). If
   absent, stop and ask the user to connect it (`/mcp`).
2. `uvx yt-dlp --version` (preferred over a global install).
3. `ffmpeg -version` — required to merge video+audio streams. If broken or
   missing, tell the user before attempting any install.
4. Read one existing notes file (e.g. `notes/w08_stat110_chi_square_student_t_mvn.md`)
   to calibrate structure and voice, and follow the repo's
   "Markdown LaTeX Style (GitHub-safe)" rules in CLAUDE.md/AGENTS.md.

## Step 1 — Get the video locally (skip if a local file was provided)

```bash
uvx yt-dlp --no-playlist -f "bv*[height<=1080]+ba/b" --merge-output-format mp4 \
  -o "<temporary-directory>/<lecture>.mp4" "<url>"
```

Download to a dedicated temporary directory outside the repo. Direct upload is
required (not a YouTube URL submit): server-side YouTube import is unreliable
from cloud IPs AND doesn't retain a source video, which downgrades frames to
320px thumbnails — illegible for board math.

## Step 2 — Upload (two-step presigned flow, ~500 API units to index)

1. `upload_video(action="start", filename=<name>.mp4, content_type="video/mp4")`
   → returns `video_id` + `upload_url`.
2. `curl --fail --show-error -X PUT -H "Content-Type: video/mp4"
   --upload-file <file> "<upload_url>"` — do NOT send an Authorization header
   to the presigned URL.
3. `upload_video(action="complete", video_id=..., filename=...)`.

Videos up to 90 minutes and 8 GiB are accepted.

## Step 3 — Poll patiently

`get_video_status(video_id)` every 3–4 minutes (background sleep between
checks; never spin). Expect roughly 7–8 minutes of processing per 30 minutes
of video. If not `ready` after 40 minutes or status is `failed`, stop and
report the status/error verbatim.

## Step 4 — Synthesize the notes (the recipe)

1. `get_transcript(video_id)` once, no time filter — full transcript with
   per-segment timestamps.
2. Read it and identify (a) the lecture's natural sections and (b) **board
   moments** — places where the speaker references something visual without
   fully describing it ("let's draw…", "as you can see here…", "this
   diagram…").
3. For the 5–15 most important board moments: `get_frames(video_id,
   timestamps=[...])` (high resolution is the default; ≤8 timestamps per
   call). Board content accumulates while the speaker writes, so request a
   timestamp near the END of each explanation, a few seconds after the
   drawing is finished. If a frame is unclear, request 2–3 nearby timestamps
   and use the clearest. If the response says `fallback_used` (thumbnails),
   warn the user that board legibility may be reduced.
4. Transcribe every important visual into the notes as LaTeX or a faithful
   text description — never a "see figure" reference. For anything
   mathematical, trust the frames over the transcript: ASR renders spoken
   math as prose ("f prime of x") and mishears technical terms.
5. Write ONE Markdown document:
   - Title + lecture link + course metadata block at the top (match existing
     notes files exactly).
   - A **source-status line** disclosing the notes are AI-assisted,
     synthesized from the video's transcript and frames (and merged with the
     user's own notes if provided) — prose must paraphrase the lecture, never
     reproduce transcript passages verbatim.
   - Numbered `##` sections following the lecture's own structure.
   - Math per the repo's GitHub-safe LaTeX rules; key results in `\boxed{}`
     inside display blocks.
   - A final **Main Takeaways** bullet list.
6. If the user provided their own notes: treat them as the primary skeleton —
   verify, correct, complete, and enrich from the video, flagging any
   conflict explicitly.

## Guardrails and cleanup

- Do not modify `CURRICULUM.md` or `PROGRESS.md` unless the user explicitly
  requests it.
- On success or failure, delete the exact temporary directory created for this
  run. Never use a broad deletion pattern. Do NOT delete the indexed video from
  Video Moment Finder (re-runs of the notes step cost only ~6–16 units;
  re-indexing costs ~500).
