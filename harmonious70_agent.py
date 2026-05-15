"""
HÅRMONIOUS70 × STEAM SANS agent
A small Python companion for generating CSS variables, scene manifests, and design-review notes from the JSON token sheet.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import json

@dataclass(frozen=True)
class HarmonyState:
    scene: str = "night"
    clarity: float = 0.88
    warmth: float = 0.55
    depth: float = 0.92
    ease: float = 0.74

    @property
    def resonance_index(self) -> float:
        return round((self.clarity * 0.34) + (self.warmth * 0.21) + (self.depth * 0.21) + (self.ease * 0.24), 4)

    @property
    def pressure(self) -> float:
        return round(max(0.08, min(0.34, self.resonance_index * 0.13)), 4)

class Harmonious70Agent:
    def __init__(self, token_path: str | Path = "harmonious70.tokens.json"):
        self.token_path = Path(token_path)
        self.tokens = json.loads(self.token_path.read_text(encoding="utf-8"))

    def css_vars(self, state: HarmonyState) -> str:
        palette = self.tokens["color"][state.scene]
        lines = [f":root[data-h70-scene='{state.scene}'] {{"]
        for name, value in palette.items():
            lines.append(f"  --h70-{self._kebab(name)}: {value};")
        lines.append(f"  --h70-pressure: {state.pressure};")
        lines.append(f"  --h70-resonance-index: {state.resonance_index};")
        lines.append("}")
        return "\n".join(lines)

    def scene_manifest(self, state: HarmonyState) -> dict:
        return {
            "scene": state.scene,
            "resonanceIndex": state.resonance_index,
            "pressure": state.pressure,
            "muralInstruction": self.tokens["sceneShift"][state.scene],
            "typeInstruction": "STEAM SANS remains experiential: Harris clarifies, HBA breathes, Vapor transmits.",
            "vesselVerseMove": ["locate", "name", "deepen", "return"],
        }

    def review_note(self, state: HarmonyState) -> str:
        manifest = self.scene_manifest(state)
        return (
            f"The {manifest['scene']} scene carries a resonance index of {manifest['resonanceIndex']}. "
            f"The muralist interprets the environment as: {manifest['muralInstruction']} "
            "Every interface object earns its place through clarity, warmth, depth, and ease."
        )

    @staticmethod
    def _kebab(value: str) -> str:
        return ''.join(['-' + c.lower() if c.isupper() else c for c in value]).replace('_', '-').lstrip('-')

if __name__ == "__main__":
    agent = Harmonious70Agent(Path(__file__).with_name("harmonious70.tokens.json"))
    night = HarmonyState(scene="night")
    day = HarmonyState(scene="day", clarity=0.92, warmth=0.82, depth=0.63, ease=0.86)
    print(agent.css_vars(night))
    print()
    print(json.dumps(agent.scene_manifest(day), ensure_ascii=False, indent=2))
