#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile, CMake
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        if self.options["fftw"].precision == "single":
            cmake.definitions["ENABLE_SINGLE_PRECISION"] = "ON"
        elif self.options["fftw"].precision == "longdouble":
            cmake.definitions["ENABLE_LONG_DOUBLE_PRECISION"] = "ON"
        cmake.configure()
        cmake.build()

    def test(self):
        bin_path = os.path.join("bin", "test_package")
        self.run(bin_path, run_environment=True)
