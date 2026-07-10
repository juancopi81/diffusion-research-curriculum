---
name: lecture-notes
description: Turn a lecture video from a YouTube URL or local file into structured Markdown study notes using the Video Moment Finder MCP connector, its transcript, and blackboard frames. Use when requests ask for lecture notes, study notes, or enrichment notes from a video, or mention VMF with a lecture.
---

# Lecture Notes

Create source-grounded lecture notes through Video Moment Finder while
preserving this repository's note structure, naming, and source-fidelity rules.

## Canonical Workflow

Read [`../../../.claude/skills/lecture-notes/SKILL.md`](../../../.claude/skills/lecture-notes/SKILL.md)
completely before acting, then follow that workflow. It is the canonical recipe
for downloading, uploading, polling, transcript and frame inspection, note
naming, Markdown structure, validation, and cleanup.

## Codex and Other MCP Clients

- Map the canonical VMF tool names to the tools exposed by the connected MCP
  server: `upload_video`, `get_video_status`, `get_transcript`, and
  `get_frames`.
- Do not attempt to invoke the MCP `lecture_notes` prompt as a tool. Execute the
  canonical transcript-and-frames recipe directly.
- If VMF is unavailable, stop before downloading and tell the user that the
  Video Moment Finder MCP server must be connected and authenticated.
- Keep the user's explicit output path when provided. Otherwise follow the
  canonical curriculum-versus-enrichment naming rules.
