Summary:	Brute Force Binary Tester
Summary(pl.UTF-8):   "Brutalny" tester plików binarnych
Name:		bfbtester
Version:	2.0.1
Release:	1
License:	GPL v2
Group:		Development/Debuggers
Source0:	http://dl.sourceforge.net/bfbtester/%{name}-%{version}.tar.gz
# Source0-md5:	88b50a026c817e9cc391dddb71216a3e
URL:		http://bfbtester.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BFBTester is good for doing quick, proactive security checks of binary
programs. BFBTester will perform checks of single and multiple
argument command line overflows and environment variable overflows. It
can also watch for tempfile creation activity to alert the user of any
programs using unsafe tempfile names.

%description -l pl.UTF-8
BFBTester służy do szybkiego sprawdzania bezpieczeństwa programów
binarnych. BFBTester sprawdza występowanie przepełnienia bufora dla
jednego i wielu parametrów z linii poleceń oraz dla zmiennych
środowiskowych. Może także kontrolować tworzenie plików tymczasowych i
ostrzegać użytkownika o programach używających niebezpiecznych nazw
plików tymczasowych.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
