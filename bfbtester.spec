Summary:	Brute Force Binary Tester
Summary(pl):	"Brutalny" tester plików binarnych
Name:		bfbtester
Version:	2.0.1
Release:	1
License:	GPL v2
Group:		Development/Debuggers
Source0:	http://telia.dl.sourceforge.net/sourceforge/bfbtester/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
URL:		http://bfbtester.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BFBTester is good for doing quick, proactive security checks of binary
programs. BFBTester will perform checks of single and multiple
argument command line overflows and environment variable overflows. It
can also watch for tempfile creation activity to alert the user of any
programs using unsafe tempfile names.

%description -l pl

%prep
%setup -q

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
