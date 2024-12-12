.PHONY: push merge_master

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

merge_master:
	for /f "delims=" %%b in ('git rev-parse --abbrev-ref HEAD') do set current_branch=%%b ^ \
		&& git checkout master ^ \
		&& git merge --strategy=ours %%b ^ \
		&& git checkout %%b