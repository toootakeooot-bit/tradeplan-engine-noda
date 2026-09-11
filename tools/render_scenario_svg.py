#!/usr/bin/env python3
"""Reference SVG renderer for NS7-B.

Renders supplied Scenario A/B/C data only. It does not infer market structure,
scenario meaning, Entry, SL, TP, or any NODA rule.
"""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any

W = 1440
PANEL_H = 760
OVERLAY_H = 900

STYLE = {
    "A": {"stroke": "#1565c0", "dash": ""},
    "B": {"stroke": "#c62828", "dash": "12 8"},
    "C": {"stroke": "#616161", "dash": "4 8"},
}


class RenderInputError(ValueError):
    pass


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def check_coord(value: Any, name: str) -> None:
    if not isinstance(value, (int, float)) or value < 0 or value > 1:
        raise RenderInputError(f"{name} must be in [0,1]")


def validate_critical(data: dict[str, Any]) -> None:
    for key in (
        "render_request_id", "source_chart_images", "environment_state_ref",
        "phase_state_ref", "setup_state_ref", "trigger_state_ref", "scenarios",
    ):
        if key not in data:
            raise RenderInputError(f"missing required field: {key}")

    scenarios = data["scenarios"]
    if not isinstance(scenarios, list) or len(scenarios) != 3:
        raise RenderInputError("scenarios must contain exactly three items")
    if [s.get("scenario_id") for s in scenarios] != ["A", "B", "C"]:
        raise RenderInputError("scenario order must be exactly A, B, C")

    required = (
        "scenario_label", "scenario_type", "premise", "direction",
        "activation_conditions", "invalidation_conditions", "next_action",
        "evidence_refs", "priority", "confidence", "current_status",
    )
    for s in scenarios:
        for key in required:
            if key not in s:
                raise RenderInputError(f"scenario {s.get('scenario_id')} missing: {key}")

    images = data["source_chart_images"]
    if not isinstance(images, list) or not images:
        raise RenderInputError("source_chart_images must contain at least one item")
    for img in images:
        if not img.get("chart_id") or not img.get("uri"):
            raise RenderInputError("each source chart requires chart_id and uri")

    ann = data.get("visual_annotations") or {}
    for m in ann.get("markers", []):
        check_coord(m.get("x"), f"marker {m.get('marker_id')} x")
        check_coord(m.get("y"), f"marker {m.get('marker_id')} y")
        if m.get("scenario_id") is not None and m.get("scenario_id") not in {"A", "B", "C"}:
            raise RenderInputError("marker scenario_id must be A/B/C")
    for line in ann.get("lines", []):
        for key in ("x1", "y1", "x2", "y2"):
            check_coord(line.get(key), f"line {line.get('line_id')} {key}")
    for zone in ann.get("zones", []):
        for key in ("x", "y", "width", "height"):
            check_coord(zone.get(key), f"zone {zone.get('zone_id')} {key}")
        if zone["x"] + zone["width"] > 1 or zone["y"] + zone["height"] > 1:
            raise RenderInputError(f"zone exceeds viewport: {zone.get('zone_id')}")
    for path in ann.get("paths", []):
        if path.get("scenario_id") not in {"A", "B", "C"}:
            raise RenderInputError("path scenario_id must be A/B/C")
        pts = path.get("points")
        if not isinstance(pts, list) or len(pts) < 2:
            raise RenderInputError("path requires at least two points")
        for i, p in enumerate(pts):
            check_coord(p.get("x"), f"path point {i} x")
            check_coord(p.get("y"), f"path point {i} y")


def load_input(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    validate_critical(data)
    return data


def header(width: int, height: int) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#fff"/>',
        '<style>text{font-family:Arial,"Noto Sans JP",sans-serif;fill:#111}.small{font-size:18px}.body{font-size:20px}.title{font-size:28px;font-weight:700}.muted{fill:#555}.box{fill:#fafafa;stroke:#bbb;stroke-width:2}</style>',
    ]


def wrap(text: str, width: int = 36) -> list[str]:
    text = str(text).strip()
    if not text:
        return ["—"]
    out, line = [], ""
    for token in text.replace("\n", " ").split(" "):
        candidate = token if not line else line + " " + token
        if len(candidate) > width and line:
            out.append(line)
            line = token
        else:
            line = candidate
    if line:
        out.append(line)
    return out


def text_block(lines: list[str], x: int, y: int, line_h: int = 22) -> list[str]:
    return [f'<text x="{x}" y="{y+i*line_h}" class="small">{esc(line)}</text>' for i, line in enumerate(lines)]


def render_panel(data: dict[str, Any], out_path: Path) -> None:
    svg = header(W, PANEL_H)
    svg += [
        '<text x="40" y="48" class="title">NODA Scenario A / B / C</text>',
        f'<text x="40" y="78" class="small muted">request: {esc(data["render_request_id"])}</text>',
    ]
    margin, gap = 35, 20
    col_w = (W - margin * 2 - gap * 2) // 3
    y0, h = 105, 620
    paths = {p["scenario_id"]: p for p in (data.get("visual_annotations") or {}).get("paths", [])}

    for idx, s in enumerate(data["scenarios"]):
        sid = s["scenario_id"]
        st = STYLE[sid]
        x0 = margin + idx * (col_w + gap)
        svg.append(f'<rect x="{x0}" y="{y0}" width="{col_w}" height="{h}" rx="16" class="box"/>')
        svg += [
            f'<text x="{x0+20}" y="{y0+38}" class="title">{esc(sid)} · {esc(s["scenario_label"])}</text>',
            f'<text x="{x0+20}" y="{y0+70}" class="small">{esc(s["scenario_type"])} | {esc(s["direction"])} | {esc(s["current_status"])}</text>',
            f'<line x1="{x0+20}" y1="{y0+86}" x2="{x0+col_w-20}" y2="{y0+86}" stroke="{st["stroke"]}" stroke-width="5" stroke-dasharray="{st["dash"]}"/>',
        ]
        rows = [
            ("Premise", s["premise"]),
            ("Activate", " / ".join(s["activation_conditions"]) or "—"),
            ("Invalidate", " / ".join(s["invalidation_conditions"]) or "—"),
            ("Next", s["next_action"]),
            ("Evidence", ", ".join(s["evidence_refs"]) or "—"),
        ]
        y = y0 + 120
        for label, value in rows:
            svg.append(f'<text x="{x0+20}" y="{y}" class="small" font-weight="700">{esc(label)}</text>')
            lines = wrap(value)[:3]
            svg += text_block(lines, x0 + 20, y + 25)
            y += 42 + 22 * len(lines)

        p = paths.get(sid)
        if p:
            bx, by, bw, bh = x0 + 20, y0 + h - 120, col_w - 40, 80
            pts = " ".join(f'{bx+pt["x"]*bw:.1f},{by+pt["y"]*bh:.1f}' for pt in p["points"])
            svg.append(f'<polyline points="{pts}" fill="none" stroke="{st["stroke"]}" stroke-width="4" stroke-dasharray="{st["dash"]}"/>')
            svg.append(f'<text x="{bx}" y="{by-8}" class="small muted">supplied path</text>')
        else:
            svg.append(f'<text x="{x0+20}" y="{y0+h-45}" class="small muted">No supplied visual path — not inferred.</text>')

    unresolved = data.get("unresolved") or []
    if unresolved:
        msg = " | ".join(f'{u["code"]}: {u["description"]}' for u in unresolved[:2])
        svg.append(f'<text x="40" y="748" class="small muted">{esc(msg)}</text>')
    svg.append("</svg>")
    out_path.write_text("\n".join(svg), encoding="utf-8")


def marker(x: float, y: float, role: str, sid: str | None = None) -> str:
    stroke = STYLE.get(sid or "C", STYLE["C"])["stroke"]
    if role == "INVALIDATION":
        return f'<g stroke="{stroke}" stroke-width="5"><line x1="{x-10}" y1="{y-10}" x2="{x+10}" y2="{y+10}"/><line x1="{x+10}" y1="{y-10}" x2="{x-10}" y2="{y+10}"/></g>'
    return f'<circle cx="{x}" cy="{y}" r="9" fill="#fff" stroke="{stroke}" stroke-width="5"/>'


def render_overlay(data: dict[str, Any], out_path: Path) -> None:
    img = data["source_chart_images"][0]
    if not img.get("uri"):
        raise RenderInputError("overlay requires chart uri")
    svg = header(W, OVERLAY_H)
    cx, cy, cw, ch = 40, 80, 1360, 760
    svg += [
        '<text x="40" y="48" class="title">NODA Scenario Overlay</text>',
        f'<image href="{esc(img["uri"])}" x="{cx}" y="{cy}" width="{cw}" height="{ch}" preserveAspectRatio="none"/>',
        f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" fill="none" stroke="#333" stroke-width="2"/>',
    ]
    ann = data.get("visual_annotations") or {}
    sx = lambda v: cx + v * cw
    sy = lambda v: cy + v * ch

    for z in ann.get("zones", []):
        svg.append(f'<rect x="{sx(z["x"]):.1f}" y="{sy(z["y"]):.1f}" width="{z["width"]*cw:.1f}" height="{z["height"]*ch:.1f}" fill="#777" fill-opacity="0.12" stroke="#555" stroke-width="2" stroke-dasharray="6 6"/>')
        if z.get("label"):
            svg.append(f'<text x="{sx(z["x"])+6:.1f}" y="{sy(z["y"])+22:.1f}" class="small">{esc(z["label"])}</text>')

    for line in ann.get("lines", []):
        svg.append(f'<line x1="{sx(line["x1"]):.1f}" y1="{sy(line["y1"]):.1f}" x2="{sx(line["x2"]):.1f}" y2="{sy(line["y2"]):.1f}" stroke="#222" stroke-width="3" stroke-dasharray="8 6"/>')
        if line.get("label"):
            svg.append(f'<text x="{sx(line["x2"])+5:.1f}" y="{sy(line["y2"])-5:.1f}" class="small">{esc(line["label"])}</text>')

    for p in ann.get("paths", []):
        st = STYLE[p["scenario_id"]]
        pts = " ".join(f'{sx(pt["x"]):.1f},{sy(pt["y"]):.1f}' for pt in p["points"])
        svg.append(f'<polyline points="{pts}" fill="none" stroke="{st["stroke"]}" stroke-width="6" stroke-dasharray="{st["dash"]}"/>')
        last = p["points"][-1]
        svg.append(f'<text x="{sx(last["x"])+8:.1f}" y="{sy(last["y"])-8:.1f}" class="title">{esc(p["scenario_id"])}</text>')

    for m in ann.get("markers", []):
        x, y = sx(m["x"]), sy(m["y"])
        svg.append(marker(x, y, m["role"], m.get("scenario_id")))
        if m.get("label"):
            svg.append(f'<text x="{x+12:.1f}" y="{y-12:.1f}" class="small">{esc(m["label"])}</text>')

    svg += [
        f'<text x="40" y="875" class="small muted">Chart: {esc(img["chart_id"])} {esc(img.get("timeframe") or "")} · geometry supplied upstream; NS7-B does not infer coordinates.</text>',
        "</svg>",
    ]
    out_path.write_text("\n".join(svg), encoding="utf-8")


def build_output(data: dict[str, Any], out_dir: Path) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    panel = out_dir / "scenario_panel.svg"
    overlay = out_dir / "scenario_overlay.svg"
    render_panel(data, panel)
    render_overlay(data, overlay)
    unresolved = [{"code": u["code"], "description": u["description"]} for u in data.get("unresolved", [])]
    return {
        "render_request_id": data["render_request_id"],
        "status": "PARTIAL" if unresolved else "RENDERED",
        "artifacts": [
            {"artifact_type": "scenario_panel_image", "format": "SVG", "path": str(panel), "chart_id": None, "notes": "A/B/C summary panel"},
            {"artifact_type": "scenario_overlay_image", "format": "SVG", "path": str(overlay), "chart_id": data["source_chart_images"][0]["chart_id"], "notes": "Overlay uses supplied geometry only"},
        ],
        "unresolved": unresolved,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input_json", type=Path)
    ap.add_argument("--out-dir", type=Path, default=Path("rendered"))
    args = ap.parse_args()
    try:
        data = load_input(args.input_json)
        result = build_output(data, args.out_dir)
    except (OSError, json.JSONDecodeError, RenderInputError) as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
