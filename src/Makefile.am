## Process this file with automake to produce Makefile.in

AUTOMAKE_OPTIONS = 1.4 no-dependencies

bin_PROGRAMS = kakasi mkkanwa atoc_conv rdic_conv wx2_conv

kakasi_SOURCES= kakasi.c a2.c g2.c j2.c k2.c ee2.c hh2.c jj2.c kk2.c \
	dict.c itaiji.c kanjiio.c 78_83.c level.c
mkkanwa_SOURCES = mkkanwa.c dict.c itaiji.c getopt.c getopt1.c
atoc_conv_SOURCES = atoc-conv.c conv-util.c
rdic_conv_SOURCES = rdic-conv.c conv-util.c
wx2_conv_SOURCES = wx2-conv.c conv-util.c

noinst_HEADERS = conv-util.h kakasi.h getopt.h level.h

dictdir = $(pkgdatadir)
DEFS = -DHAVE_CONFIG_H \
       -DKANWADICT=\"$(dictdir)/kanwadict\" \
       -DITAIJIDICT=\"$(dictdir)/itaijidict\"
INCLUDES = -I..

