##
AUTOMAKE_OPTIONS = 1.4 no-dependencies

TESTS_ENVIRONMENT = top_srcdir=$(top_srcdir) top_builddir=$(top_builddir) \
                    pkgdatadir=$(top_srcdir)

TESTS = kakasi-1 kakasi-2 kakasi-3 kakasi-4 kakasi-5 kakasi-6 kakasi-7 \
	kakasi-8 kakasi-9

SUBDIRS = data

clean-local:
	rm -f test-log tmp

EXTRA_DIST = $(TESTS) env.sh
