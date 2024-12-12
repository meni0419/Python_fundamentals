.PHONY: push
push:
	@if not defined b ( \
		echo Usage: make push b=<branch> c=<comment>; \
		exit /b 1; \
	) else if not defined c ( \
		echo Usage: make push b=<branch> c=<comment>; \
		exit /b 1; \
	)
	git add .
	git commit -m "$(c)"
	git push origin $(b)