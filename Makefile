PKG_NAME := jdk-scalatest-maven-plugin
URL := http://repo2.maven.org/maven2/org/scalatest/scalatest-maven-plugin/1.0/scalatest-maven-plugin-1.0.jar
ARCHIVES := http://repo2.maven.org/maven2/org/scalatest/scalatest-maven-plugin/1.0/scalatest-maven-plugin-1.0.pom %{buildroot}

include ../common/Makefile.common
