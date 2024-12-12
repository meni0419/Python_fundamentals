.PHONY: push
push:
	@if not defined c ( \
		echo Usage: make push c="<comment>"; \
		exit /b 1; \
	) else ( \
		for /f "delims=" %%b in ('git rev-parse --abbrev-ref HEAD') do set current_branch=%%b && \
		git add . && \
		git commit -m "$(c)" && \
		git push origin %%b \
	)