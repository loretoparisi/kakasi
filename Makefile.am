## Process this file with automake to produce Makefile.in

@SET_MAKE@
AUTOMAKE_OPTIONS = 1.4 no-dependencies

dictdir = $(pkgdatadir)
dict_DATA = kanwadict itaijidict

bin_SCRIPTS = kakasi-config

EXTRA_DIST = config.rpath INSTALL-ja README-ja ONEWS maintMakefile \
	     kakasi.spec.in kakasi.spec itaijidict magic-kakasi
EXTRA_DIRS = doc
SUBDIRS = src lib man tests

CLEANFILES = kanwadict

kanwadict:
	if test -f kakasidict; then \
	    ITAIJIDICT="itaijidict" src/mkkanwa$(EXEEXT) $@ kakasidict; \
	fi

dist-hook:
	for subdir in $(EXTRA_DIRS); do \
	    cp -rp $$subdir $(DESTDIR)$(distdir)/$$subdir; \
	done
	if test -f kakasidict; then \
	    cp -rp kakasidict $(DESTDIR)$(distdir)/kakasidict; \
	fi

##Bug in automake: Can't use `if MAINTAINER_MODE'
@MAINTAINER_MODE_TRUE@include $(srcdir)/maintMakefile
