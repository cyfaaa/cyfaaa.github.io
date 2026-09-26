# Local preview

The nine public pages are static HTML, generated from `_site_content/*.md` and `_site_content/papers.json`.

```sh
python3 -m pip install -r scripts/requirements.txt
python3 scripts/build_site.py
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/`. No push or deployment is needed.

The generated HTML pages have no Jekyll front matter, so GitHub Pages can copy them as static files. The existing Academic Pages theme and licence are retained for legacy pages. The page structure, typography, paper image rows, badges and overflow navigation use the public source of [Yige Yuan's website](https://github.com/yuanyige/yuanyige.github.io). The deployed reference CSS is retained as `assets/css/reference-main.css`; local content adaptations are in `assets/css/academic.css`. The upstream MIT notice is retained at `assets/reference-theme/LICENSE`. Source provenance was checked against the homepage and public repository on 26 September 2026. All biography, papers, photos and slides belong to Yinfeng Cao's records.

The homepage uses anchored sections. `/publications/` is a combined list with no year or venue-type divisions. Paper metadata and authentic figure paths are in `papers.json`; unavailable figures are omitted. Talks use verified presentation records, with actual slides under `files/talks/`.

Mail evidence and private audit files are kept outside this repository and are not part of the preview.

The CV is available at `/cv/` and `/files/Yinfeng_Cao_CV.pdf`. Its editable LaTeX source and original resume class are in `files/cv_source/`.

Projects lists the IEEE ComSoc project. Other systems are listed under `/demo/`.
