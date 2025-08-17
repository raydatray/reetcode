import re
from collections import deque, defaultdict
from dataclasses import dataclass
from typing import Deque, Dict, List


class MaxLength:
    def solution(left: int, right: int) -> int:
        x, count = left, 1

        while x < 6 and x * 2 <= right:
            x *= 2
            count += 1

        count += (right - x) // 6
        return count


@dataclass
class Bead:
    color: str
    count: int


class Beads:
    def solution(actions: List[str]) -> str:
        beads: Deque[Bead] = deque()

        for action in actions:
            parts = action.split()
            if len(parts) not in [2, 3]:
                return "wrong command"

            side, count = parts[0], int(parts[1])
            if side not in ["L", "R"]:
                return "wrong command"

            is_right = side == "R"

            if len(parts) == 3:
                color = parts[2]
                target = beads[-1] if is_right else beads[0]

                if beads and target == color:
                    target.count += count
                else:
                    (beads.append if is_right else beads.appendleft)(Bead(color, count))
            else:
                remaining = count
                pop_fn = beads.pop if is_right else beads.popleft
                add_fn = beads.appendleft if is_right else beads.append
                target = beads[0] if is_right else beads[-1]

                while remaining > 0:
                    source = beads[-1] if is_right else beads[0]

                    if source.count > remaining:
                        source.count -= remaining
                        moved_bead = Bead(source.color, remaining)
                        remaining = 0
                    else:
                        moved_bead = pop_fn()
                        remaining -= moved_bead.count

                    if beads and target.color == moved_bead.color:
                        target.count += moved_bead.count
                    else:
                        add_fn(moved_bead)

        return " ".join([f"{bead.count}{bead.color}" for bead in reversed(beads)])


class EquationBalancer:
    def solution(self, s: str) -> bool:
        lhs, rhs = s.split("=")
        lhs = lhs.strip()
        rhs = rhs.strip()

        left_elements = self.parse_side(lhs)
        right_elements = self.parse_side(rhs)

        all_elements = set(left_elements.keys()).union(set(right_elements.keys()))

        for element in all_elements:
            if left_elements[element] != right_elements[element]:
                return False

        return True

    def parse_side(self, side: str) -> Dict[str, int]:
        total_element_count = defaultdict(int)

        compounds = [compound.strip() for compound in side.split("+")]

        for compound in compounds:
            compound_count = self.parse_compoud(compound)

            for element, count in compound_count.items():
                total_element_count[element] += count

        return total_element_count

    def parse_compoud(self, compound: str) -> Dict[str, int]:
        element_count = defaultdict(int)

        coeff_match = re.match(r"^(\d+)", compound)
        if coeff_match:
            coeff = int(coeff_match.group(1))
            compound = compound = compound[len(coeff_match.group(1)) :]
        else:
            coeff = 1

        elements = re.findall(r"([A-Z][a-z]?)(\d*)", compound)
        for element, count_str in elements:
            count = int(count_str) if count_str else 1
            element_count[element] += coeff * count

        return element_count
