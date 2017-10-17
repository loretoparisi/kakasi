## Process this file with automake to produce Makefile.in

AUTOMAKE_OPTIONS = 1.4 no-dependencies

dictdir = $(pkgdatadir)
DEFS = -DLIBRARY -DHAVE_CONFIG_H \
       -DKANWADICT=\"$(dictdir)/kanwadict\" \
       -DITAIJIDICT=\"$(dictdir)/itaijidict\"
INCLUDES = -I.. -I../src

lib_LTLIBRARIES = libkakasi.la
libkakasi_la_SOURCES = libdict.c libkakasi.c libkanjiio.c \
	liba2.c libg2.c libj2.c libk2.c libee2.c libhh2.c libjj2.c libkk2.c \
	libitaiji.c lib78_83.c liblevel.c
libkakasi_la_LDFLAGS = \
	-version-info 3:0:1  -export-dynamic

include_HEADERS = libkakasi.h
DISTCLEANFILES = ${libkakasi_la_SOURCES}

EXTRA_DIST = kakasi.def makefile.msc.in


libdict.c: ../src/dict.c
	rm -f $@
	$(LN_S) ../src/dict.c $@

libkakasi.c: ../src/kakasi.c
	rm -f $@
	$(LN_S) ../src/kakasi.c $@

libkanjiio.c: ../src/kanjiio.c
	rm -f $@
	$(LN_S) ../src/kanjiio.c $@

liba2.c: ../src/a2.c
	rm -f $@
	$(LN_S) ../src/a2.c $@

libg2.c: ../src/g2.c
	rm -f $@
	$(LN_S) ../src/g2.c $@

libj2.c: ../src/j2.c
	rm -f $@
	$(LN_S) ../src/j2.c $@

libk2.c: ../src/k2.c
	rm -f $@
	$(LN_S) ../src/k2.c $@

libee2.c: ../src/ee2.c
	rm -f $@
	$(LN_S) ../src/ee2.c $@

libhh2.c: ../src/hh2.c
	rm -f $@
	$(LN_S) ../src/hh2.c $@

libjj2.c: ../src/jj2.c
	rm -f $@
	$(LN_S) ../src/jj2.c $@

libkk2.c: ../src/kk2.c
	rm -f $@
	$(LN_S) ../src/kk2.c $@

libitaiji.c: ../src/itaiji.c
	rm -f $@
	$(LN_S) ../src/itaiji.c $@

lib78_83.c: ../src/78_83.c
	rm -f $@
	$(LN_S) ../src/78_83.c $@

liblevel.c: ../src/level.c
	rm -f $@
	$(LN_S) ../src/level.c $@

