[tox]
envlist = py39
skipsdist = True
 
[testenv]
deps =
    pytest
    pytest-cov
commands = pytest --cov=ISCODEVUTB_DSTeam_BLAHX3 --cov-report=xml --cov-config=tox.ini --cov-branch
 
