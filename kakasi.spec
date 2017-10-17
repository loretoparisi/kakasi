%define ver	2.3.6
%define  RELEASE 1
%define  rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}

Summary: KAKASI - kanji kana simple inverter
Name: kakasi
Version: %ver
Release: %rel
Source: http://kakasi.namazu.org/stable/kakasi-%{ver}.tar.gz
URL: http://kakasi.namazu.org/
Copyright: GPL
Group: Applications/Text
Buildroot: %{_tmppath}/%{name}-%{ver}-buildroot

%description
KAKASI is the language processing filter to convert Kanji characters 
to Hiragana, Katakana or Romaji(1) and may be helpful to read Japanese 
documents. Word-splitting patch has merged from version 2.3.0.

%description -l ja
KAKASI は漢字かなまじり文をひらがな文やローマ字文に変換することを
目的として作成したプログラムと辞書の総称です。さらに、バージョン 
2.3.0 からは、分かち書きパッチがマージされました。

%package devel
Summary: header file and libraries of KAKASI
Group: Development/Libraries
Requires: kakasi = %{version}

%description devel
Header file and Libraries of KAKASI. 

%description devel -l ja
KAKASIのヘッダファイル及びライブラリです。

%package dict
Summary: The base dictionary of KAKASI
Group: Applications/Text
Obsoletes: kakasidict

%description dict
The basic dictionary of KAKASI.

%description dict -l ja
KAKASIの基本辞書です。

%changelog
* Fri Mar 20 2001 Ryuji Abe <rug@namazu.org>
- more macros.
- fix %files.

* Mon Jan 22 2001 Ryuji Abe <rug@namazu.org>
- fix source.

* Thu Jan 04 2001 Ryuji Abe <rug@namazu.org>
- fix typo in %description.

* Thu Dec 27 2000 Ryuji Abe <rug@namazu.org>
- fix %files.

* Sat Mar 04 2000 Ryuji Abe <raeva@t3.rim.or.jp>
- fix summary.

* Wed Dec 08 1999 Motonobu Ichimura <famao@kondara.org>
- change Group ( Utilities/Text -> Applications/Text ) for Kondara

* Fri Oct 28 1999 Ryuji Abe <raeva@t3.rim.or.jp>
- added japanese manpage in packages.
- build dict packages.

* Sat Oct 16 1999 Ryuji Abe <raeva@t3.rim.or.jp>
- fixed including libkakasi.so* in non-devel packages.

%prep
%setup

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

gzip --best $RPM_BUILD_DIR/%{name}-%{ver}/doc/kakasi.1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/ja/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{ver}/doc/kakasi.1.gz \
	$RPM_BUILD_ROOT%{_mandir}/ja/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README README-ja
%{_bindir}/kakasi
%{_bindir}/mkkanwa
%{_bindir}/atoc_conv
%{_bindir}/rdic_conv
%{_bindir}/wx2_conv
%{_libdir}/libkakasi.so.*
%{_mandir}/ja/man1/kakasi.1.gz
%{_datadir}/kakasi/itaijidict

%files devel
%defattr(-, root, root)
%{_bindir}/kakasi-config
%{_libdir}/libkakasi.so
%{_libdir}/libkakasi.a
%{_libdir}/libkakasi.la
%{_includedir}/libkakasi.h

%files dict
%defattr(-, root, root)
%{_datadir}/kakasi/kanwadict
