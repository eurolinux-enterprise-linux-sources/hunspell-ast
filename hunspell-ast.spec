Name: hunspell-ast
Summary: Asturian hunspell dictionaries
Epoch: 1
Version: 0.02
Release: 6%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/e-files/3932/1/asturianu.oxt
URL: http://softastur.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv3+
BuildArch: noarch

Requires: hunspell

%description
Asturian hunspell dictionaries.

%prep
%setup -q -c

%build
chmod -x dictionaries/*

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/ast.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ast_ES.aff
cp -p dictionaries/ast.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ast_ES.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSES-en.txt LICENCES-ast.txt
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:0.02-6
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 01 2012 Caolán McNamara <caolanm@redhat.com> - 1:0.02-4
- initial version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 08 2011 Caolán McNamara <caolanm@redhat.com> - 1:0.02-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 16 2010 Caolán McNamara <caolanm@redhat.com> - 1:0.01-1
- latest version

* Mon Apr 12 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100331-1
- initial version
