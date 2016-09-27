Name     : jdk-scalatest-maven-plugin
Version  : 1.0
Release  : 1
URL      : http://repo2.maven.org/maven2/org/scalatest/scalatest-maven-plugin/1.0/scalatest-maven-plugin-1.0.jar
Source0  : http://repo2.maven.org/maven2/org/scalatest/scalatest-maven-plugin/1.0/scalatest-maven-plugin-1.0.jar
Source1  : http://repo2.maven.org/maven2/org/scalatest/scalatest-maven-plugin/1.0/scalatest-maven-plugin-1.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-scalatest-maven-plugin-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-scalatest-maven-plugin package.
Group: Data

%description data
data components for the jdk-scalatest-maven-plugin package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/scalatest-maven-plugin.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/scalatest-maven-plugin.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/scalatest-maven-plugin.xml \
%{buildroot}/usr/share/maven-poms/scalatest-maven-plugin.pom \
%{buildroot}/usr/share/java/scalatest-maven-plugin.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/scalatest-maven-plugin.jar
/usr/share/maven-metadata/scalatest-maven-plugin.xml
/usr/share/maven-poms/scalatest-maven-plugin.pom
