.PHONY: add push

push:
	@git add .
	@git commit -m "LeetCode"
	@git push -u origin main

format:
	@ruff format .

lint:
	@ruff check .
