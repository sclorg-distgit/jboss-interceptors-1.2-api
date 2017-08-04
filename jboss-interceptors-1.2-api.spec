%{?scl:%scl_package jboss-interceptors-1.2-api}
%{!?scl:%global pkg_name %{name}}

%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global oname jboss-interceptors-api_1.2_spec

Name:          %{?scl_prefix}jboss-interceptors-1.2-api
Version:       1.0.0
Release:       6.2%{?dist}
Summary:       Java EE Interceptors 1.2 API
License:       CDDL or GPLv2 with exceptions
URL:           https://github.com/jboss/jboss-interceptors-api_spec
Source0:       https://github.com/jboss/jboss-interceptors-api_spec/archive/jboss-interceptors-api_1.2_spec-%{namedversion}.tar.gz

BuildRequires: %{?scl_prefix}jboss-parent

BuildRequires: %{?scl_prefix}maven-local
BuildRequires: %{?scl_prefix}maven-enforcer-plugin
BuildRequires: %{?scl_prefix}maven-plugin-bundle
BuildRequires: %{?scl_prefix}maven-source-plugin

BuildArch:     noarch

%description
The Java EE  Interceptors 1.2 API classes from JSR 318.

%package javadoc
Summary:       Javadoc for %{pkg_name}

%description javadoc
This package contains javadoc for %{pkg_name}.

%prep
%setup -q -n jboss-interceptors-api_spec-jboss-interceptors-api_1.2_spec-%{namedversion}

# Fix incorrect-fsf-address
sed -i "s,59,51,;s,Temple Place,Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%mvn_file :%{oname} %{pkg_name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 1.0.0-6.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.0.0-6.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 22 2016 gil cattaneo <puntogil@libero.it> 1.0.0-5
- regenerate build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 06 2015 gil cattaneo <puntogil@libero.it> 1.0.0-2
- introduce license macro

* Wed Jan 14 2015 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-1
- Upstream release 1.0.0.Final

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.4.Alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.3.Alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 09 2013 gil cattaneo <puntogil@libero.it> 1.0.0-0.2.Alpha3
- switch to XMvn
- minor changes to adapt to current guideline

* Mon May 13 2013 gil cattaneo <puntogil@libero.it> 1.0.0-0.1.Alpha3
- initial rpm
