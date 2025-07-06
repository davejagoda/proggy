Instead of having a bunch of somewhat useful proggy directories
scattered all over the place, I am putting them all in one place.  In
addition, these I feel at least are good enough to show to someone
else . . .

python
------
Stop using `python2`, only use `python3`.

Stop using:
- `requirements.txt`
- `virtualenv` (directly)
- `pipenv`
- `Pipfile`
- `Pipfile.lock`

Only use:
- `uv`
- `uv.lock`
- `pyproject.toml`

Manually invoke formatting:

```
uv run black . && uv run isort .
```

javascript
----------
Manually invoke formatting:

```
npx prettier . --write && npx eslint .
```
