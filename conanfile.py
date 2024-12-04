from conan import ConanFile
from conan.tools.files import update_conandata, get, copy, replace_in_file, chdir, rmdir
from conan.tools.gnu import MakeDeps
from conan.tools.scm import Git
from conan.tools.scm import Version
from conan.tools.layout import basic_layout
from conan.tools.env import VirtualRunEnv
import os

class ARTTrackingConan(ConanFile):
    name = "arttracking"
    version = "2.9.0"
    url = "https://github.com/TUM-CONAN/conan_artracking_dtrack_sdk"
    homepage = "https://ar-tracking.com/"
    description = "DTrack SDK for ART"
    topics = ("video",)
    license = "MIT"
    package_type = "shared-library"

    settings = "os", "arch", "compiler", "build_type"

    exports = "CMakeLists.txt"
    generators = "CMakedeps", "CMakeToolchain"

    options = {
        # "shared": [True, False],
        # "fPIC": [True, False],
    }
    default_options = {
        # "shared": False,
        # "fPIC": True,
    }
    
    # def requirements(self):
    #     self.requires("gtest/1.14.0")

    # TODO use yml file for the tag version
    def source(self):
         get(self,
             "https://github.com/ar-tracking/DTrackSDK/archive/refs/tags/v2.9.0.zip",
             strip_root = True)

    def layout(self):
        basic_layout(self, src_folder="src")

    def generate(self):
        deps = MakeDeps(self)
        deps.generate()
    
    def build(self):
        # for now only on linux .. windows is built using msbuild
        copy(self, "Makefile", src=self.recipe_folder,
             dst=self.source_folder)
        with VirtualRunEnv(self).vars().apply():
                with chdir(self, self.source_folder):
                    self.run("make libDTrackSDK")
    
    def package(self):
        #libs
        copy(self, pattern="*.so", 
             dst=os.path.join(self.package_folder, "lib"),
             src=os.path.join(os.path.dirname(self.build_folder), "src", "lib"),
             keep_path=False)
        #headers
        copy(self, 
             pattern="*.hpp", 
             dst=os.path.join(self.package_folder, "include", "arttracking"), 
             src=os.path.join(self.source_folder, "include"))
    
    def package_info(self):
        self.cpp_info.components["arttracking"].includedirs = [os.path.join("include")]
        self.cpp_info.components["arttracking"].libs = ["DTrackSDK"]

