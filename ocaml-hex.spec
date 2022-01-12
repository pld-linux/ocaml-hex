#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		_enable_debug_packages	0

Summary:	Minimal library providing hexadecimal converters
Summary(pl.UTF-8):	Minimalna biblioteka zapewniająca konwertery szesnastkowe
Name:		ocaml-hex
Version:	1.4.0
Release:	1
License:	ISC
Group:		Libraries
#Source0Download: https://github.com/mirage/ocaml-hex/releases
Source0:	https://github.com/mirage/ocaml-hex/releases/download/v%{version}/hex-v%{version}.tbz
# Source0-md5:	57103ff33e70f14171c46d88f5452d11
URL:		https://github.com/mirage/ocaml-hex
BuildRequires:	ocaml >= 1:4.03.0
BuildRequires:	ocaml-bigarray-compat-devel >= 1.0.0
BuildRequires:	ocaml-cstruct-devel >= 1.7.0
BuildRequires:	ocaml-dune >= 1.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minimal library providing hexadecimal converters.

%description -l pl.UTF-8
Minimalna biblioteka zapewniająca konwertery szesnastkowe.

%package devel
Summary:	Minimal library providing hexadecimal converters - development part
Summary(pl.UTF-8):	Minimalna biblioteka zapewniająca konwertery szesnastkowe - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-bigarray-compat-devel >= 1.0.0
Requires:	ocaml-cstruct-devel >= 1.7.0

%description devel
This package contains libraries and signature files for developing
applications that use OCaml hex library.

%description devel -l pl.UTF-8
Ten pakiet zawiera biblioteki i pliki sygnatur do tworzenia aplikacji
wykorzystujących bibliotekę OCamla hex.

%prep
%setup -q -n hex-v%{version}

%build
dune build %{?_smp_mflags} --display=verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/hex/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/hex

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/hex
%{_libdir}/ocaml/hex/META
%{_libdir}/ocaml/hex/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/hex/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/hex/dune-package
%{_libdir}/ocaml/hex/opam
%{_libdir}/ocaml/hex/*.cmi
%{_libdir}/ocaml/hex/*.cmt
%{_libdir}/ocaml/hex/*.cmti
%{_libdir}/ocaml/hex/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/hex/hex.a
%{_libdir}/ocaml/hex/*.cmx
%{_libdir}/ocaml/hex/*.cmxa
%endif
