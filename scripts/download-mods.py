from urllib.request import urlopen, Request
from tqdm import tqdm

docs = {
'algorithm.html': 'algorithm',
'assertions.html': 'assertions',
'asyncdispatch.html': 'asyncdispatch',
'asyncfile.html': 'asyncfile',
'asyncftpclient.html': 'asyncftpclient',
'asyncfutures.html': 'asyncfutures',
'asynchttpserver.html': 'asynchttpserver',
'asyncjs.html': 'asyncjs',
'asyncnet.html': 'asyncnet',
'asyncstreams.html': 'asyncstreams',
'base64.html': 'base64',
'bitops.html': 'bitops',
'browsers.html': 'browsers',
'cgi.html': 'cgi',
'chains.html': 'chains',
'channels.html': 'channels',
'colors.html': 'colors',
'complex.html': 'complex',
'cookies.html': 'cookies',
'coro.html': 'coro',
'cpuinfo.html': 'cpuinfo',
'cpuload.html': 'cpuload',
'critbits.html': 'critbits',
'cstrutils.html': 'cstrutils',
'db_common.html': 'db_common',
'db_mysql.html': 'db_mysql',
'db_odbc.html': 'db_odbc',
'db_postgres.html': 'db_postgres',
'db_sqlite.html': 'db_sqlite',
'deques.html': 'deques',
'diff.html': 'diff',
'distros.html': 'distros',
'dollars.html': 'dollars',
'dom.html': 'dom',
'dynlib.html': 'dynlib',
'editdistance.html': 'editdistance',
'encodings.html': 'encodings',
'endians.html': 'endians',
'fenv.html': 'fenv',
'hashes.html': 'hashes',
'heapqueue.html': 'heapqueue',
'highlite.html': 'highlite',
'htmlgen.html': 'htmlgen',
'htmlparser.html': 'htmlparser',
'httpclient.html': 'httpclient',
'httpcore.html': 'httpcore',
'intsets.html': 'intsets',
'io.html': 'io',
'iterators.html': 'iterators',
'jsconsole.html': 'jsconsole',
'jsffi.html': 'jsffi',
'json.html': 'json',
'lenientops.html': 'lenientops',
'lexbase.html': 'lexbase',
'linenoise.html': 'linenoise',
'lists.html': 'lists',
'locks.html': 'locks',
'logging.html': 'logging',
'macros.html': 'macros',
'marshal.html': 'marshal',
'math.html': 'math',
'md5.html': 'md5',
'memfiles.html': 'memfiles',
'mersenne.html': 'mersenne',
'mimetypes.html': 'mimetypes',
'nativesockets.html': 'nativesockets',
'net.html': 'net',
'nimprof.html': 'nimprof',
'nimscript.html': 'nimscript',
'nre.html': 'nre',
'oids.html': 'oids',
'options.html': 'options',
'os.html': 'os',
'osproc.html': 'osproc',
'oswalkdir.html': 'oswalkdir',
'parsecfg.html': 'parsecfg',
'parsecsv.html': 'parsecsv',
'parsejson.html': 'parsejson',
'parseopt.html': 'parseopt',
'parsesql.html': 'parsesql',
'parseutils.html': 'parseutils',
'parsexml.html': 'parsexml',
'pegs.html': 'pegs',
'posix_utils.html': 'posix_utils',
'punycode.html': 'punycode',
'random.html': 'random',
'rationals.html': 'rationals',
'rdstdin.html': 'rdstdin',
're.html': 're',
'rlocks.html': 'rlocks',
'ropes.html': 'ropes',
'rst.html': 'rst',
'rstast.html': 'rstast',
'rstgen.html': 'rstgen',
'rtarrays.html': 'rtarrays',
'segfaults.html': 'segfaults',
'selectors.html': 'selectors',
'sequtils.html': 'sequtils',
'sets.html': 'sets',
'sexp.html': 'sexp',
'sha1.html': 'sha1',
'sharedlist.html': 'sharedlist',
'sharedtables.html': 'sharedtables',
'smtp.html': 'smtp',
'stats.html': 'stats',
'streams.html': 'streams',
'strformat.html': 'strformat',
'strmisc.html': 'strmisc',
'strscans.html': 'strscans',
'strtabs.html': 'strtabs',
'strutils.html': 'strutils',
'sugar.html': 'sugar',
'system.html': 'system',
'tables.html': 'tables',
'terminal.html': 'terminal',
'threadpool.html': 'threadpool',
'threads.html': 'threads',
'time_t.html': 'time_t',
'times.html': 'times',
'typeinfo.html': 'typeinfo',
'typetraits.html': 'typetraits',
'unicode.html': 'unicode',
'unidecode.html': 'unidecode',
'unittest.html': 'unittest',
'uri.html': 'uri',
'util.html': 'util',
'varints.html': 'varints',
'volatile.html': 'volatile',
'widestrs.html': 'widestrs',
'winlean.html': 'winlean',
'wordwrap.html': 'wordwrap',
'xmlparser.html': 'xmlparser',
'xmltree.html': 'xmltree',
}

base = 'https://nim-lang.org/docs/'

for doc, title in tqdm(docs.items()):
    url = "{}{}".format(base, doc)
    req = Request(url, None, {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})
    with urlopen(req) as u:
        with open(doc, "wb") as f:
            f.write(u.read())