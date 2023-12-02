test:
	@poetry run pytest -v --cov=src --cov-report=term-missing

new_day:
	@if [ -z "$(DAY)" ]; then \
        echo "DAY is not set"; \
        exit 1; \
    fi
	@mkdir -p src/day_$(DAY)
	@touch src/day_$(DAY)/__init__.py
	@touch src/day_$(DAY)/input.txt
	@echo "from typing import List\n\nfrom src.utils import get_input\n\n\ndef part_1(lines: List[str]):\n    pass\n\n\ndef part_2(lines: List[str]):\n    pass\n\n\nif __name__ == \"__main__\":\n    lines = get_input(\"day_$(DAY)/input.txt\")\n    part_1(lines)\n    part_2(lines)" > src/day_$(DAY)/solution.py
	@touch src/day_$(DAY)/instructions.txt
	@echo "from day_$(DAY).solution import part_1, part_2\n\n\ndef test_day_$(DAY)_part_1():\n    assert part_1([]) is not None\n\n\ndef test_day_$(DAY)_part_2():\n    assert part_2([]) is not None" > tests/test_day_$(DAY).py