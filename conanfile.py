#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class RapidjsonConan(ConanFile):
    name = "rapidjson"
    version = "1.1.0"
    description = "A fast JSON parser/generator for C++ with both SAX/DOM style API"
    homepage = "http://rapidjson.org/"
    url = "https://github.com/bincrafters/conan-rapidjson"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "https://github.com/Tencent/rapidjson/blob/v%s/license.txt" % version
    exports = ["LICENSE.md"]
    no_copy_source = True
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/Tencent/rapidjson"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        include_folder = os.path.join(self.source_subfolder, "include")
        self.copy(pattern="license.txt", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
