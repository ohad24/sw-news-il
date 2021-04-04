# Software News
This repo contains the source code for the site.

## Build
Main branch

![Github Workflow build on main](https://github.com/ohad24/sw-news-il/actions/workflows/ci.yaml/badge.svg?branch=main)


## Tech
 * Flask
 * JQuery
 * Bootstrap
 * Firebase

## Tests
Automatic CI using Github actions.

[![Coverage Status](https://coveralls.io/repos/github/ohad24/sw-news-il/badge.svg)](https://coveralls.io/github/ohad24/sw-news-il)
### Flask
Run locally on dev environment.
```bash
pytest --cov=src -v tests/
```

## Todo:
- [ ] Mailing list + email validation
- [x] Tests
- [ ] Full Tests
- [ ] CI
- [ ] CD
- [ ] Dynamic tags + caching
- [ ] Login
- [ ] New article/link page
- [ ] All article pages
- [ ] Favicon
- [ ] Logo
- [ ] Init DB ?
