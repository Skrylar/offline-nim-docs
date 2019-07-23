from urllib.request import urlopen, Request
from tqdm import tqdm

docs = {
    "apis.html": "API naming design",
    "codeowners.html": "Code owners",
    "contributing.html": "Contributing",
    "estp.html": "Embedded Stack Trace Profiler (ESTP) User Guide",
    "intern.html": "Internals of the Nim Compiler",
    "backends.html": "Nim Backend Integration",
    "nimc.html": "Nim Compiler User Guide",
    "docgen.html": "Nim DocGen Tools Guide",
    "overview.html": "Nim Documentation Overview",
    "nep1.html": "Nim Enhancement Proposal #1 - Standard Library Style Guide",
    "manual_experimental.html": "Nim Experimental Features",
    "idetools.html": "Nim IDE Integration Guide",
    "nimsuggest.html": "Nim IDE Integration Guide",
    "koch.html": "Nim maintenance script",
    "manual.html": "Nim Manual",
    "lib.html": "Nim Standard Library",
    "tut1.html": "Nim Tutorial (Part I)",
    "tut2.html": "Nim Tutorial (Part II)",
    "tut3.html": "Nim Tutorial (Part III)",
    "gc.html": "Nim's Garbage Collector",
    "nimgrep.html": "nimgrep User's manual",
    "niminst.html": "niminst User's manual",
    "nims.html": "NimScript",
    "packaging.html": "Packaging Nim",
    "filters.html": "Source Code Filters",
    "tools.html": "Tools available with Nim",
}

base = "https://nim-lang.org/docs/"


for doc, title in tqdm(docs.items()):
    url = "{}{}".format(base, doc)
    req = Request(url, None, {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"})
    with urlopen(req) as u:
        with open(doc, "wb") as f:
            f.write(u.read())
